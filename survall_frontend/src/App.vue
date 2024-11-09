<script setup>
import Opinion from './components/Opinion.vue'
import { ref } from 'vue'
import Login from "@/components/Login.vue";
import {useLoginStore} from "@/stores/login.js";
import AnsweredQuestions from "@/components/AnsweredQuestions.vue";


let store = useLoginStore()
let questions = ref([])
let state = ref(0);

async function get_question() {
  console.log("getting question")
  questions.value = await store.get_question()
  console.log(questions.value)
}

store.$subscribe((mutation, state) => {
  if (state.logged_in) {
    get_question()
  }
})

async function next_question() {
  console.log("what")
  await get_question()
}
console.log(questions.value)
// evil debug to easily log in (don't tell evil hackers)
// store.logged_in = true
</script>

<template>
  <header class="d-flex w-100 justify-content-end align-items-center border-bottom">
    <button type="button" class="btn btn-primary m-2" @click="state=0">Vote</button>
    <button type="button" class="btn btn-primary m-2" @click="state=1">Your History</button>
    <button type="button" class="btn btn-primary m-2" @click="state=0">Overview</button>
  </header>

  <main class="d-flex flex-grow justify-content-between align-items-center h-100">
    <Login v-if="!store.logged_in" ></Login>
    <div v-else-if="state===0" v-for="question in questions" >
      <Opinion :question="question" :key="question['uuid']" @nextquestion="next_question"/>
    </div>
    <div v-if="state===1">
      <AnsweredQuestions></AnsweredQuestions>
    </div>
  </main>
</template>

<style scoped>
</style>
