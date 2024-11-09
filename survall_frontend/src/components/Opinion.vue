<script setup>
import {ref} from 'vue'
import {useLoginStore} from "@/stores/login.js";
import * as Bootstrap from "bootstrap";


const store = useLoginStore()

const skipping = import.meta.env.VITE_PUBLIC_RUN === 'true'

const props = defineProps(['question'])
const emit = defineEmits(['nextquestion'])

const result = ref(false)
let vote_value = ref(null)
let flewaway = ref(false)
let relevance_value = ref(3)
let discussion_value = ref('')

function next_question() {
  emit('nextquestion')
  response_done.value = true

}

let response_done = ref(false)
console.log(props.question.uuid)
let vote_stats = ref({})

async function submit_vote() {
  result.value = !result.value

  const collapseElementList = document.querySelectorAll('#results-collapse')
  const collapseList = [...collapseElementList].map(collapseEl => new Bootstrap.Collapse(collapseEl))
  console.log(collapseList)

  vote_stats.value = await store.submit_vote(props.question.uuid,
      store.token,
      vote_value.value,
      parseInt(relevance_value.value),
      discussion_value.value,)
  console.log(await vote_stats)
}

function flew(e) {
  console.log(e.animationName)
  console.log(e.animationName)
  if (e.animationName.startsWith('flyaway')) {
    if (skipping) {
      next_question()
    } else {
      flewaway.value = true
    }
    console.log(flewaway)
  }
}

onkeydown = (event) => {
  if (event.key === 'a') {
    vote_value.value = 1
  } else if (event.key === 'd') {
    vote_value.value = -1
  } else if (event.key === 'u') {
    vote_value.value = 0
  }
};

</script>

<template>
  <div :class="{card: true, flyaway: vote_value!=null, 'fly-in': vote_value==null}" v-if="!flewaway"
       style="width: 100%;" @animationend="flew">
    <div class="card-body">
      <h5 class="card-title">{{ question.question }}</h5>
      <p class="card-text">{{ question.description }}</p>
    </div>
    <!--Buttons-->
    <div class="form card-footer d-flex flex-column">
      <div>
        <label class="form-label">Do you agree with the statement?</label>
        <div class="d-flex justify-content-between">
          <input type="radio" class="btn-check" name="options" id="disagree" autocomplete="off" value="-1"
                 v-model="vote_value">
          <label class="btn btn-outline-danger" for="disagree">Disagree</label>

          <input type="radio" class="btn-check" name="options" id="unsure" autocomplete="off" value="0"
                 v-model="vote_value">
          <label class="btn btn-outline-primary" for="unsure">Unsure</label>

          <input type="radio" class="btn-check" name="options" id="agree" autocomplete="off" value="1"
                 v-model="vote_value">
          <label class="btn btn-outline-success" for="agree">Agree</label>
        </div>
      </div>
    </div>
  </div>
  <div class="card" :class="{flyaway: response_done, 'fly-in': !response_done}" v-else>
    <div class="card-body">
      <h5 class="card-title">Feedback</h5>
      <div>
        <label class="form-label">How relevant is this question</label>
        <div class="d-flex justify-content-between">
          <label class="form-text">Least relevant</label>
          <label class="form-text">Most relevant</label>
        </div>
        <input type="range" class="form-range" min="1" max="5" id="relevance" value="3"
               v-model="relevance_value"/>
      </div>
      <div>
        <label class="form-label">Add your discussion points</label>
        <input class="form-control" id="discussion" placeholder="(Optional)"
               v-model="discussion_value">
      </div>
      <div class="center">
        <button type="button" class="btn btn-success" :disabled="result" @click="submit_vote()">Submit</button>
      </div>
    </div>

    <!--      Results-->
    <div class="card-footer collapse" id="results-collapse">
      <div class="progress bg-danger" role="progressbar" aria-label="Basic example" aria-valuenow="75"
           aria-valuemin="0" aria-valuemax="100">
        <div class="progress-bar bg-danger"
             :style="{'width': vote_stats['negative']/vote_stats['answers_count']*100 + '%'}">{{
            vote_stats['negative']
          }}
        </div>
        <div class="progress-bar bg-secondary"
             :style="{'width': (vote_stats['neutral'])/vote_stats['answers_count']*100 + '%'}">{{
            vote_stats['neutral']
          }}
        </div>
        <div class="progress-bar bg-success"
             :style="{'width': vote_stats['positive']/vote_stats['answers_count']*100 + '%'}" id="progress_fore">
          {{ vote_stats['positive'] }}
        </div>
      </div>
      <div class="d-flex flex-row">
        <p class="text-danger ">No</p>
        <p class="text-secondary translate-middle-x position-absolute start-50">Neutral</p>
        <p class="text-success translate-middle-x position-absolute end-0">Yes</p>
      </div>
      <h5>General relevance</h5>
      <input type="range" class="form-range" min="1" max="5" step="0.1"
             :value="vote_stats['relevance_sum'] / vote_stats['answers_count']" disabled/>
      <div class="center">
        <button type="button" class="btn btn-success" @click="next_question()">Next</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">

.btn-success {
  margin-top: 10px;
}

.center {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Styling for the div */
.flyaway {
  animation: flyaway 1.5s ease-in-out forwards;
}

.fly-in {
  animation: fly-in 1.2s ease-in-out forwards;
}

/* Flyaway animation */
@keyframes flyaway {
  0% {
    transform: translate(0, 0) scale(1);
  }
  10% {
    transform: translate(0, 0) scale(1.2);
  }
  20% {
    transform: translate(0, 0) scale(1);
  }
  60% {
    transform: translate(0, 0) scale(1);
    opacity: 1;
  }
  100% {
    transform: translate(100vw, -100vh) scale(1.2) rotate(45deg);
    opacity: 0.8;
  }
}

@keyframes fly-in {
  0% {
    transform: translate(-100vw, -100vh) scale(1.2) rotate(65deg);
    opacity: 0.8;
  }
  100% {
    transform: translate(0, 0) scale(1);
    opacity: 1;
  }
}
</style>