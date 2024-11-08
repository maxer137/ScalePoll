<script setup>
import {ref} from 'vue'
import {useLoginStore} from "@/stores/counter.js";

const store = useLoginStore()

let username = ref('')

async function login(event) {
  event.preventDefault()
  store.login(username.value)
}
</script>

<template>
  <form>
    <div class="mb-3">
      <label for="exampleInputEmail1" class="form-label">Unique super secure login that only you have (Use your junction
        ID)</label>
      <input type="number" class="form-control" id="user_id" aria-describedby="numberHelp" v-model="username">
      <div id="emailHelp" class="form-text">Your junction ID is the number at the bottom of your event ID <br>
        <a href="https://eu.junctionplatform.com/dashboard/event/junction-2024/event-id">https://eu.junctionplatform.com/dashboard/event/junction-2024/event-id</a>
      </div>
    </div>
    <button class="btn btn-primary" @click="login($event)">Submit</button>
  </form>
</template>

<style scoped>

</style>