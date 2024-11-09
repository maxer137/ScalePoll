<script setup>

import SmallQuestion from "@/components/SmallQuestion.vue";
import {useLoginStore} from "@/stores/login.js";
import {ref} from "vue";

const store = useLoginStore()
let questions = ref()
async function init() {
  questions.value = await store.get_my_questions()
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