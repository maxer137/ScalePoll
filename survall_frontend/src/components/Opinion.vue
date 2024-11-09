<script setup>

import {ref} from 'vue'

const props = defineProps({
  title: String,
})

const result = ref(false)
let question = ref(true)
let vote_value = ref(null)
let flewaway = ref(false)
// function change_vote(vote) {
//   vote_value.value = vote
// }

let relevance_value = ref(0)

let discussion_value = ref('')

let fore = ref(20)
let neutral = ref(30)
let against = ref(50)
let relevance = ref(3.4)

async function submit_vote() {
  let body = {
    question_uuid: 0,
    user_uuid: 0,
    answer_score: vote_value.value,
    relevance_score: parseInt(relevance_value.value),
    discussion_field: discussion_value.value,
  }
  result.value = !result.value
  console.log(body)
  // let response = await fetch(`${DOMAIN_NAME}/response`, {
  //   method: 'POST',
  //   body: JSON.stringify(body),
  // })
  // console.log(await response.text())
  // show_results(await response.json())
}

async function show_results(results) {
  // { for: 123, against: 2}
  //question uuid
  //fore, against, neutral
  //relevance
}

function flew() {
  flewaway.value = true
  console.log(flewaway)
}
</script>

<template>
  <div :class="{card: true, flyaway: vote_value!=null}" v-if="!flewaway" style="width: 100%;" @animationend="flew">
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
      <p class="card-text">Background information on topic</p>
    </div>
    <!--Buttons-->
    <div class="form card-footer d-flex flex-column">
      <div>
        <label class="form-label">Do you agree with the statement?</label>
        <div class="d-flex justify-content-between">
          <input type="radio" class="btn-check" name="options" id="agree" autocomplete="off" value="-1"
                 v-model="vote_value">
          <label class="btn btn-outline-danger" for="agree">Disagree</label>

          <input type="radio" class="btn-check" name="options" id="unsure" autocomplete="off" value="0"
                 v-model="vote_value">
          <label class="btn btn-outline-primary" for="unsure">Unsure</label>

          <input type="radio" class="btn-check" name="options" id="disagree" autocomplete="off" value="1"
                 v-model="vote_value">
          <label class="btn btn-outline-success" for="disagree">Agree</label>
        </div>
      </div>
    </div>
  </div>
  <div class="card fly-in" v-else>
    <div class="card-body">
      <h5 class="card-title">Feedback</h5>
      <div>
        <label class="form-label">How relevant is this question</label>
        <div  class="d-flex justify-content-between">
          <label class="form-text">Least relevant</label>
          <label class="form-text">Most relevant</label>
        </div>
        <input type="range" class="form-range" min="1" max="5" id="relevance" value="3"
               v-model="relevance_value"/>
      </div>
      <div>
        <label class="form-label">Add your discussion points</label>
        <input class="form-control" id="discussion" placeholder="Add extra inside on your choice"
               v-model="discussion_value">
      </div>
      <div>
        <label class="form-label">When ready</label>
      </div>
      <button type="button" class="btn btn-success" @click="submit_vote()">Submit</button>
    </div>

    <!--      Results-->
    <div class="card-footer">
      <h5>General opinion</h5>
      <div class="progress bg-danger" role="progressbar" aria-label="Basic example" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
        <div class="progress-bar bg-success" :style="{'width': fore + '%'}" id="progress_fore">{{fore}}%</div>
        <div class="progress-bar bg-secondary" :style="{'width': neutral + '%'}">{{neutral}}%</div>
        <div class="progress-bar bg-danger" :style="{'width': against + '%'}">{{against}}%</div>
      </div>
      <div class="d-flex flex-row">
        <h5 class="text-success">Yes</h5>
        <h5 class="text-secondary translate-middle-x position-absolute start-50">Neutral</h5>
        <h5 class="text-danger translate-middle-x position-absolute end-0">No</h5>
      </div>
      <h5>General relevance</h5>
      <input type="range" class="form-range" min="1" max="5" step="0.1" v-model=relevance disabled/>
    </div>
  </div>
</template>

<style scoped>
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
  40% {
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