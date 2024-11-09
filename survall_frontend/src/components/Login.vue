<script setup>
import {ref} from 'vue'
import {useLoginStore} from "@/stores/login.js";

const store = useLoginStore()

let random = Math.floor(Math.random() * 99999999);
let username = ref(random.toString())

async function login(event) {
  event.preventDefault()
  console.log(username.value)
  await store.login(username.value)
}
</script>

<template>
  <form>
    <div class="mb-3">
      <h1>Login</h1>
      <label for="exampleInputEmail1" class="form-label">Unique super secure login that only you have (This number
        should be unique to you. Remember it if you want to join the same account)</label>
      <input type="number" class="form-control" id="user_id" aria-describedby="numberHelp" v-model="username">
      <p>
        This login is designed to be interchangeable with a third party ID system. Such as government ID systems. <br>
        For our demo, we simply let you choose a number.</p>
    </div>
    <button class="btn btn-primary" @click="login($event)">Submit</button>
  </form>
</template>

<style scoped>

</style>