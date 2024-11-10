<script setup>
import {ref} from 'vue'
import {useApiStore} from "@/stores/login.js";
import Opinion from './components/Opinion.vue'
import Login from "@/components/Login.vue";
import AnsweredQuestions from "@/components/AnsweredQuestions.vue";
import OutOfQuestions from "@/components/OutOfQuestions.vue";
import ClosedQuestions from "@/components/ClosedQuestions.vue";

// Setup store to connect to api
let store = useApiStore()
// Setup the current question
let question = ref(null)
// Set up the page navigator
let page = ref(0);

//Request a new question from the API.
//We set the question to null first, otherwise the animations don't reload/re-render
async function get_question() {
  question.value = null
  question.value = await store.get_question()
}

// After we log in, we get a question to ask the user.
store.$subscribe((mutation, state) => {
  if (state.logged_in) {
    get_question()
  }
})

</script>

<template>
  <header class="d-flex w-100 justify-content-between border-bottom">
    <h1 class="m-2 d-flex"><img src="./assets/logo.png" style="height: 3rem" alt="logo"/>Survall</h1>
    <div class="d-flex w-100 justify-content-end align-items-center border-bottom">
      <button type="button" class="btn btn-primary m-2" @click="page=0">Vote</button>
      <button type="button" class="btn btn-primary m-2" @click="page=1">Your History</button>
      <button type="button" class="btn btn-primary m-2" @click="page=2">Overview</button>
    </div>
  </header>

  <main class="d-flex flex-grow justify-content-between align-items-center h-100">
    <Login v-if="!store.logged_in"/>
    <div v-else>
      <div v-if="page===0">
        <Opinion v-if="question !== null" :question="question" :key="question['uuid']" @nextquestion="get_question"/>
        <OutOfQuestions v-else/>
      </div>
      <div v-if="page===1">
        <AnsweredQuestions/>
      </div>
      <div v-if="page===2">
        <ClosedQuestions/>
      </div>
    </div>
  </main>
</template>

<style scoped>
</style>
