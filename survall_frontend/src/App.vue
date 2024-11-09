<script setup>
import Opinion from './components/Opinion.vue'
import { ref } from 'vue'
import Login from "@/components/Login.vue";
import {useLoginStore} from "@/stores/login.js";
import AnsweredQuestions from "@/components/AnsweredQuestions.vue";
import OutOfQuestions from "@/components/OutOfQuestions.vue";
import ClosedQuestions from "@/components/ClosedQuestions.vue";


let store = useLoginStore()
let question = ref(null)
let state = ref(0);

async function get_question() {
  question.value = null
  question.value = await store.get_question()
}

store.$subscribe((mutation, state) => {
  if (state.logged_in) {
    get_question()
  }
})

// evil debug to easily log in (don't tell evil hackers)
// store.logged_in = true
</script>

<template>
  <header class="d-flex w-100 justify-content-between border-bottom">
    <h1 class="m-2 d-flex"><img src="./assets/logo.png" style="height: 3rem" alt="logo"/>Survall</h1>
    <div class="d-flex w-100 justify-content-end align-items-center border-bottom">
      <button type="button" class="btn btn-primary m-2" @click="state=0">Vote</button>
      <button type="button" class="btn btn-primary m-2" @click="state=1">Your History</button>
      <button type="button" class="btn btn-primary m-2" @click="state=2">Overview</button>
    </div>
  </header>

  <main class="d-flex flex-grow justify-content-between align-items-center h-100">
    <Login v-if="!store.logged_in" ></Login>
    <div v-else>
      <div v-if="state===0" >
        <Opinion v-if="question !== null" :question="question" :key="question['uuid']" @nextquestion="get_question"/>
        <OutOfQuestions v-else/>
      </div>
      <div v-if="state===1">
        <AnsweredQuestions></AnsweredQuestions>
      </div>
      <div v-if="state===2">
        <ClosedQuestions></ClosedQuestions>
      </div>
    </div>
  </main>
</template>

<style scoped>
</style>
