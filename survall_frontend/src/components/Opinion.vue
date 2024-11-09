<script setup>

import {ref} from 'vue'
import * as Bootstrap from "bootstrap";
import {useLoginStore} from "@/stores/login.js";

const store = useLoginStore()

const result = ref(false)
let vote_value = ref(null)
let flewaway = ref(false)

let relevance_value = ref(3)

let discussion_value = ref('')

function next_question() {
  //request_question()
  response_done.value = true
  request_question()
  // result.value = false
  // vote_value = ref(null)
  // flewaway = ref(false)
  // relevance_value = ref(3)
  // discussion_value = ref('')
}

let question = ref('')
let description = ref('')

async function request_question() {
  let body = {
    user_hash: store.token,
  }
  console.log(body)
  let response = await fetch(`http://127.0.0.1:1337/get_question`, {
    method: 'POST',
    body: JSON.stringify(body),
  })
  console.log(await response.text())
  show_question(await response)
}

async function show_question(received) {
  //question uuid
  //question
  //desription
  console.log(received)
  question = received['question']
  description = received['description']

  // question = 'Ronald is the best boomer'
  // description = 'He is old'
}

let fore = ref(0)
let neutral = ref(0)
let against = ref(0)
let relevance = ref(3)
let response_done = ref(false)


async function submit_vote() {
  let body = {
    question_uuid: 0,
    user_hash: 0,
    answer_score: vote_value.value,
    relevance_score: parseInt(relevance_value.value),
    discussion_field: discussion_value.value,
  }
  result.value = !result.value
  show_results(0)
  console.log(body)
  const collapseElementList = document.querySelectorAll('#results-collapse')
  const collapseList = [...collapseElementList].map(collapseEl => new Bootstrap.Collapse(collapseEl))
  console.log(collapseList)
  let response = await fetch(`http://127.0.0.1:1337/post_answer`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json', 'Authorization': 'TODO '},// + store.token},
    body: JSON.stringify(body),
  })
  console.log(await response.text())
  show_results(await response.json())
}

async function show_results(results) {
  // { for: 123, against: 2}
  //question uuid
  //fore, against, neutral
  //relevance
  console.log(results)
  fore = results['fore']
  against = results['against']
  neutral = results['neutral']
  relevance = results['relevance']

  // fore = ref(30)
  // neutral = ref(30)
  // against = ref(40)
  // relevance = ref(3.4)
}

function flew() {
  flewaway.value = true
  console.log(flewaway)
}

request_question()
</script>

<template>
  <div :class="{card: true, flyaway: vote_value!=null}" v-if="!flewaway" style="width: 100%;" @animationend="flew">
    <div class="card-body">
      <h5 class="card-title">{{ question }}</h5>
      <p class="card-text">{{ description }}</p>
    </div>
    <!--Buttons-->
    <div class="form card-footer d-flex flex-column">
      <div>
        <label class="form-label">Do you agree with the statement?</label>
        <div class="d-flex justify-content-between">
          <input type="radio" class="btn-check" name="options" id="agree" autocomplete="off" value="1"
                 v-model="vote_value">
          <label class="btn btn-outline-danger" for="agree">Disagree</label>

          <input type="radio" class="btn-check" name="options" id="unsure" autocomplete="off" value="0"
                 v-model="vote_value">
          <label class="btn btn-outline-primary" for="unsure">Unsure</label>

          <input type="radio" class="btn-check" name="options" id="disagree" autocomplete="off" value="-1"
                 v-model="vote_value">
          <label class="btn btn-outline-success" for="disagree">Agree</label>
        </div>
      </div>
    </div>
  </div>
  <div class="card" :class="{flyaway: response_done, 'fly-in': !response_done}" v-else>
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
        <input class="form-control" id="discussion" placeholder="(Optional)"
               v-model="discussion_value">
      </div>
      <div class="center">
      <button type="button" class="btn btn-success" :disabled="result" @click="submit_vote()">Submit</button>
      </div>
    </div>

    <!--      Results-->
    <div class="card-footer collapse" id="results-collapse">
      <div>
        <h5>General opinion</h5>
        <p>{{ question }}</p>
        <div class="progress bg-danger" role="progressbar" aria-label="Basic example" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
          <div class="progress-bar bg-danger" :style="{'width': against + '%'}">{{against}}%</div>
          <div class="progress-bar bg-secondary" :style="{'width': neutral + '%'}">{{neutral}}%</div>
          <div class="progress-bar bg-success" :style="{'width': fore + '%'}" id="progress_fore">{{fore}}%</div>
        </div>
        <div class="d-flex flex-row">
          <p class="text-danger ">No</p>
          <p class="text-secondary translate-middle-x position-absolute start-50">Neutral</p>
          <p class="text-success translate-middle-x position-absolute end-0">Yes</p>
        </div>
        <h5>General relevance</h5>
        <input type="range" class="form-range" min="1" max="5" step="0.1" v-model=relevance disabled/>
        <div class="center">
          <button type="button" class="btn btn-success" @click="next_question()">Next</button>
        </div>
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