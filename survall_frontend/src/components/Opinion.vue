<script setup>

import { ref } from 'vue'
const props = defineProps({
  title: String,
})

const result = ref(false)

async function vote(opinion) {
  let body = {
    vote: opinion,
  }
  result.value = !result.value
  // let response = await fetch(`${DOMAIN}/response`, {
  //   method: 'POST',
  //   body: JSON.stringify(body),
  // })
  // console.log(await response.text())
  // show_results(await response.json())
}

async function show_results(results) {
  // { for: 123, against: 2}
}
</script>

<template>
  <div class="card" style="width: 25rem;">
    <div >
      <div class="card-body">
        <h5 class="card-title">{{ title }}</h5>
        <p class="card-text">Background information on topic</p>
      </div>
<!--      Buttons-->
      <div v-if="!result" class="card-footer d-flex justify-content-between">
        <button type="button" class="btn btn-danger" @click="vote(-1)">disagree</button>
        <button type="button" class="btn btn-primary" @click="vote(0)">unsure</button>
        <button type="button" class="btn btn-success" @click="vote(1)">agree</button>
      </div>
<!--      Results-->
      <div v-else class="card-footer">
        <div class="progress bg-success" role="progressbar" aria-label="Basic example" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
          <div class="progress-bar bg-danger" style="width: 25%"></div>
          <div class="progress-bar bg-gray" style="width: 50%"></div>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>

</style>