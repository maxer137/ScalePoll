<script setup>
import {ref} from 'vue'
import {useApiStore} from "@/stores/login.js";
import Opinion from './components/Opinion.vue'
import Login from "@/pages/Login.vue";
import AnsweredQuestions from "@/pages/AnsweredQuestions.vue";
import OutOfQuestions from "@/components/OutOfQuestions.vue";
import ClosedQuestions from "@/pages/ClosedQuestions.vue";
import NewQuestion from "@/components/NewQuestion.vue";
import Header from "@/components/Header.vue";

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
    <Header/>
    <main class="d-flex flex-grow justify-content-between align-items-center h-100 m-4">
      <RouterView />
    </main>
</template>

<style scoped>
</style>
