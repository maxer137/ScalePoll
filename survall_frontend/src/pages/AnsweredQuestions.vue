<script setup>

import SmallQuestion from "@/components/SmallQuestion.vue";
import {useApiStore} from "@/stores/login.js";
import {ref} from "vue";

const store = useApiStore()
let questions = ref()

//Get a list of all questions answered by a user.
//We only get the questions that the user answered,
//We aren't able to display what we voted on. Because the server doesn't know that.
//This way the user won't be biased by the amount of people that feel a certain way
async function init() {
  questions.value = await store.get_my_questions()
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