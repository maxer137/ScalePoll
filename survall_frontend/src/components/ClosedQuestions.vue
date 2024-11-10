<script setup>
import SmallQuestion from "@/components/SmallQuestion.vue";
import {useApiStore} from "@/stores/login.js";
import {ref} from "vue";

const store = useApiStore()
let questions = ref()
//Get a list of all closed questions.
//We only get the questions that can't be answered on anymore,
// This way the user won't be biased by the amount of people that feel a certain way
async function init() {
  questions.value = await store.get_closed_questions()
  console.log(questions.value)
}
init()
</script>

<template>
  <div class="d-flex flex-column">
    <div v-for="question in questions" >
      <SmallQuestion :question="question"></SmallQuestion>
    </div>
  </div>
</template>

<style scoped>

</style>