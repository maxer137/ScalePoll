# Setup

### (Optional) Setup Environment
`conda create --name survall_backend python=3.10.0`

`conda activate survall_backend`

### Install packages
`pip install -r requirements.txt`

### Running the code
`python main.py`

### Query local backend
#### Get a question
In cmd: `curl http://127.0.0.1:1337/get_question`

In browser: `http://127.0.0.1:1337/get_question`

#### Give a response
In cmd: `curl --header "Content-Type: application/json" --data "{\"question_uuid\": \"f843ba02-d1ab-4f10-8a70-503c72989c9d\", \"user_uuid\": \"a9b59649-e30f-4a87-b4cf-0e2730d9df5a\", \"answer_score\": 1, \"relevance_score\": 1, \"discussion\": \"Why is this a question?\"}" http://127.0.0.1:1337/post_answer`


#### Test authentication
`curl --header "Content-Type: application/json" --data "{\"hash\": \"f843ba02-d1ab-4f10-8a70-503c72989c9d\"}" http://127.0.0.1:1337/login`

`curl --request POST --header "Content-Type: application/json" --header "Authorization: [INSERT TOKEN HERE]" --data "[INSERT DATA HERE]" http://127.0.0.1:1337/authentication_example`

`curl --request POST --header "Content-Type: application/json" --header "Authorization: 12345678-1234-5678-1234-567812345678" --data "[INSERT DATA HERE]" http://127.0.0.1:1337/authentication_example`