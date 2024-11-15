import os
import uuid

from datetime import datetime, timezone
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from objects.answer import Answer
from objects.user_question import UserQuestionPair
from objects.question import Question
from objects.authentication import Authentication

from database.sql_base import Base


class SQLDatabase():
    def __init__(self, DATABASE_NAME='survall.db', inject_mock_data=True):
        # Setup the SQLite engine
        self.db_url = f'sqlite:///{DATABASE_NAME}?check_same_thread=False'
        self.engine = create_engine(self.db_url, echo=True)

        # Create all the tables (Question, Answer, UserQuestionAnswer)
        Base.metadata.create_all(self.engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        if inject_mock_data:
            self.inject_mock_data() 

    def register_authentication(self, authentication:Authentication):
        registration_exists = self.session.query(Authentication).filter(
            Authentication.session_token == authentication.session_token and Authentication.user_hash == authentication.user_hash).first()
        if registration_exists:
            return False # No new session registration has been made
        else:
            self.session.add(authentication)
            self.session.commit()
            return True

    def check_authentication(self, session_token):
        return self.session.query(Authentication).filter(Authentication.session_token == session_token).first()

    def get_previous_questions(self, authentication:Authentication):
        question_uuids = self.session.query(UserQuestionPair.question_uuid).filter_by(user_uuid=authentication.user_hash)
        unique_question_uuids = [uuid[0] for uuid in question_uuids]
        questions = self.session.query(Question).filter(Question.uuid.in_(unique_question_uuids)).order_by(Question.creation_time).all()

        return questions
    
    # Get all closed questions in general
    def get_closed_questions(self):
        questions = self.session.query(Question).order_by(Question.creation_time).all()

        print("CHECKING FOR CLOSED QUESTIONS")
        closed_questions = []
        for question in questions:
            if question.closed == True: # or question.close_time <= datetime.now(timezone.utc):
                closed_questions.append(question)
        
        print(closed_questions)

        return closed_questions
    
    # Get closed questions related to a specific question
    def get_related_questions(self, question:Question):
        questions = self.session.query(Question).filter(
            Question.root_question_uuid == question.root_question_uuid and
            (Question.closed == True or 
            Question.close_time <= datetime.now(timezone.utc))
            ).order_by(Question.creation_time).all()

        return questions

    def get_iterated_question(self, iteration, user_uuid):
        questions = self.session.query(Question).order_by(Question.creation_time).filter(
            Question.closed == False and Question.close_time >= datetime.now(timezone.utc)).all()
       
        # Exclude questions that the user has already answered
        answered_question_uuids = self.session.query(UserQuestionPair.question_uuid).filter(
            UserQuestionPair.user_uuid == user_uuid
        ).all()
        answered_question_uuids = {q[0] for q in answered_question_uuids}  # Convert to set for faster lookup

        print("USER ANSWERED ALL THE FOLLOWING QUESTIONS:")
        print(answered_question_uuids)

        # Filter questions to exclude ones already answered by the user
        unanswered_questions = [q for q in questions if q.get_uuid() not in answered_question_uuids]

        # Get the question based on the iteration and modulus of the total number of questions
        question_index = iteration % len(unanswered_questions) if unanswered_questions else None

        print(f"Current open questions: {len(questions)}")
        print(f"Current questions index: {question_index}")
        print(iteration)

        # Return the question if available
        return unanswered_questions[question_index] if question_index is not None else None

    def get_random_question(self, iteration, user_uuid):
        questions = self.session.query(Question).filter(
            Question.closed == False and Question.close_time >= datetime.now(timezone.utc)).order_by(func.random()).all()

        # Exclude questions that the user has already answered
        answered_question_uuids = self.session.query(UserQuestionPair.question_uuid).filter(
            UserQuestionPair.user_uuid == user_uuid
        ).all()
        answered_question_uuids = {q[0] for q in answered_question_uuids}  # Convert to set for faster lookup

        print("USER ANSWERED ALL THE FOLLOWING QUESTIONS:")
        print(answered_question_uuids)

        # Filter questions to exclude ones already answered by the user
        unanswered_questions = [q for q in questions if q.get_uuid() not in answered_question_uuids]
        
        if len(unanswered_questions) > 0:
            return unanswered_questions[0] # Can just chose the first in the list as it is randomized when querying
        else:
            return None

    def check_if_user_answered_question(self, user_question_pair:UserQuestionPair):
        existing_answer = self.session.query(UserQuestionPair).filter_by(
            user_uuid=user_question_pair.user_uuid, 
            question_uuid=user_question_pair.question_uuid).first()
        
        print("CHECK IF THE USER ALREADY ANSWERED THE QUESTION:")
        print(existing_answer)

        if existing_answer is None:
            return False
        
        print("Answer already exists, skipping submitting")
        return True
    
    def save_question(self, question:Question):
        if question.root_question_uuid is None:
            question.root_question_uuid = question.uuid

        print("SAVING QUESTION")
        print(question)

        self.session.add(question)
        self.session.commit()
    
    def save_answer(self, answer:Answer, user_question_pair:UserQuestionPair):
        print("LOOKING FOR QUESTION:")
        print(answer.question_uuid)
        question = self.get_question_by_uuid(answer.question_uuid)
        print("FOUND THE FOLLOWING QUESTION:")
        print(question)

        question.answers_count += 1
        if int(answer.answer_score) == -1:
            question.amount_negative += 1
        elif int(answer.answer_score) == 0:
            question.amount_neutral += 1
        elif int(answer.answer_score) == 1:
            question.amount_positive += 1
        else:
            print("ERROR: invalid vote, ignoring")


        if answer.discussion != '' and answer.discussion is not None:
            question.discussion_count += 1

        question.relevance_sum += int(answer.relevance_score)
        question.threshold_sum += int(answer.relevance_score)

        self.session.add(question)
        self.session.add(answer)
        self.session.add(user_question_pair)
        self.session.commit()

        print("Persisting Answer")
        print(answer)

    def get_answers_of_question(self, question):
        return self.session.query(Answer).filter(Answer.question_uuid == question.uuid).all()

    def get_answer_by_uuid(self, answer_uuid):
        return self.session.query(Answer).filter(Answer.uuid == answer_uuid).first()
    
    def get_question_by_uuid(self, question_uuid):
        return self.session.query(Question).filter(Question.uuid == question_uuid).first()
    
    # Mock data for debugging
    def inject_mock_data(self):
        mock_user = Authentication(user_hash="mock_user_hash")
        mock_user.session_token = str(uuid.UUID('12345678-1234-5678-1234-567812345678'))
        continue_injection = self.register_authentication(authentication=mock_user)

        if continue_injection == False:
            return

        mock_question = Question("Do you agree with raising the minimum wage?", "The minimum wage is the lowest pay that a worker may receive. Due to costs of living, some believe it is too low to sustain a healthy lifestyle.") # This is a root question so no parent or root uuid is set
        mock_answer = Answer(
            question_uuid=mock_question.get_uuid(),
            answer_score=-1, # Options: -1,0,1
            relevance_score=5, # Range: 1-5
            discussion="As a small business owner, I worry that raising the minimum wage will stretch my budget to the breaking point. I can’t afford to pay my employees more without having to cut staff or even close up shop."
            )
        mock_user_question_pair = UserQuestionPair(
            user_uuid=mock_user.user_hash,
            question_uuid=mock_question.get_uuid()
        )

        self.save_question(question=mock_question)
        self.save_answer(answer=mock_answer, user_question_pair=mock_user_question_pair)

        mock_answer = Answer(
            question_uuid=mock_question.get_uuid(),
            answer_score=1, # Options: -1,0,1
            relevance_score=5, # Range: 1-5
            discussion="I believe raising the minimum wage is essential to reducing poverty and bridging the income gap. A fair wage would give people the financial security they need to live with dignity."
            )

        mock_user_question_pair = UserQuestionPair(
            user_uuid=str(uuid.uuid4()),
            question_uuid=mock_question.get_uuid()
        )

        self.save_answer(answer=mock_answer, user_question_pair=mock_user_question_pair)

        mock_answer = Answer(
            question_uuid=mock_question.get_uuid(),
            answer_score=1, # Options: -1,0,1
            relevance_score=5, # Range: 1-5
            discussion="A higher minimum wage would help close the wage gap, especially for women and minorities who are overrepresented in low-wage industries. This change would promote a more equitable society."
            )

        mock_user_question_pair = UserQuestionPair(
            user_uuid=str(uuid.uuid4()),
            question_uuid=mock_question.get_uuid()
        )

        self.save_answer(answer=mock_answer, user_question_pair=mock_user_question_pair)

        mock_answer = Answer(
            question_uuid=mock_question.get_uuid(),
            answer_score=-1, # Options: -1,0,1
            relevance_score=5, # Range: 1-5
            discussion="There are better ways to fight poverty than raising the minimum wage. Tax credits, for instance, provide targeted relief without putting pressure on businesses to cover the costs."
            )

        mock_user_question_pair = UserQuestionPair(
            user_uuid=str(uuid.uuid4()),
            question_uuid=mock_question.get_uuid()
        )

        self.save_answer(answer=mock_answer, user_question_pair=mock_user_question_pair)

        mock_question_2 = Question("Do you support the legalization of recreational cannabis?","Some believe cannabis should be legal for adults to use recreationally, while others are concerned about potential health and social impacts.")
        self.save_question(question=mock_question_2)

        mock_question_3 = Question("Do you believe governments should limit immigration?","Supporters of immigration limits argue it can protect jobs and resources, while opponents believe it reduces cultural diversity and compassion.")
        self.save_question(question=mock_question_3)

        mock_question_4 = Question("Should school uniforms be mandatory in public schools?","Proponents argue uniforms promote equality and reduce bullying, while opponents feel they restrict individual expression.")
        self.save_question(question=mock_question_4)

        mock_question_5 = Question("Do you support raising taxes on the wealthy to reduce income inequality?","Some see taxing the wealthy more as a fair way to address income gaps, while others worry it discourages economic growth and investment.")
        self.save_question(question=mock_question_5)

        mock_question_6 = Question("Is climate change a result of human activity?","Scientists have linked human actions to climate change, but some believe natural factors are more significant.")
        self.save_question(question=mock_question_6)

        mock_question_7 = Question("Should there be a universal basic income for all citizens?"," Advocates believe a universal income could reduce poverty, while critics worry about the cost and its effects on work motivation.")
        self.save_question(question=mock_question_7)

        mock_question_8 = Question("Should social media companies regulate misinformation on their platforms?","Some feel it’s essential to prevent the spread of false information, while others argue it restricts free speech.")
        self.save_question(question=mock_question_8)

        mock_question_9 = Question("Is animal testing for scientific research justified?","Proponents believe it’s crucial for medical advances, while critics feel it’s unethical to subject animals to testing.")
        self.save_question(question=mock_question_9)

        mock_question_10 = Question("Do you believe artificial intelligence (AI) is a threat to human jobs?","Some believe AI will replace many jobs, while others think it will create new opportunities.")
        self.save_question(question=mock_question_10)

        mock_question_11 = Question("Should there be stricter regulations on gun ownership?","Advocates argue that stricter gun laws could reduce violence, while opponents believe it infringes on personal freedoms.")
        self.save_question(question=mock_question_11)

        mock_question_12 = Question("Do you think violent video games increase aggressive behavior in young people?","Critics of violent games argue they can influence real-life aggression, while others say there’s no proven link.")
        mock_question_12.closed = True
        self.save_question(question=mock_question_12)

        mock_question_13 = Question("Should all citizens have free access to healthcare?","Proponents of free healthcare argue it’s a basic right, while critics are concerned about high government costs.")
        mock_question_13.closed = True
        self.save_question(question=mock_question_13)