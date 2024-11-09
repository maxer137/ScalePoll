<script setup>
import Opinion from './components/Opinion.vue'
import { ref } from 'vue'
import Login from "@/components/Login.vue";
import {useLoginStore} from "@/stores/login.js";


let store = useLoginStore()
// evil debug to easily log in (don't tell evil hackers)
store.logged_in = true
</script>

<template>
  <header>
  </header>

  <main class="d-flex justify-content-between">
    <Login v-if="!store.logged_in"></Login>
    <Opinion v-if=store.logged_in title="Ronald is the best boomer"/>
  </main>
</template>

<style scoped>
</style>
