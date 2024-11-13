<script setup>
import {useApiStore} from "@/stores/login.js";
import {ref} from "vue";
import OutOfQuestions from "@/components/OutOfQuestions.vue";
import Opinion from "@/components/Opinion.vue";

const store = useApiStore()
let question = ref(null)
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

get_question()

</script>

<template>
  <div class="d-flex flex-column">
    <Opinion v-if="question !== null" :question="question" :key="question['uuid']" @nextquestion="get_question"/>
    <OutOfQuestions v-else/>
  </div>
</template>

<style scoped>

</style>