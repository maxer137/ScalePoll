<script setup>
import Opinion from './components/Opinion.vue'
import { ref } from 'vue'
import Login from "@/components/Login.vue";
import {useLoginStore} from "@/stores/login.js";


let store = useLoginStore()
let questions = ref([])

async function get_question() {
  questions.value = await store.get_question
  console.log(questions.value)
}

store.$subscribe((mutation, state) => {
  if (state.logged_in) {
    get_question()
  }
})
console.log(questions.value)
// evil debug to easily log in (don't tell evil hackers)
// store.logged_in = true
</script>

<template>
  <header>
  </header>

  <main class="d-flex justify-content-between">
    <Login v-if="!store.logged_in" ></Login>
    <div v-for="question in questions" >
      <Opinion :question="question"/>
    </div>
  </main>
</template>

<style scoped>
</style>
