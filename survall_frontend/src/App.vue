<script setup>
import Opinion from './components/Opinion.vue'
import { ref } from 'vue'
import Login from "@/components/Login.vue";
import {useLoginStore} from "@/stores/login.js";


let store = useLoginStore()
</script>

<template>
  <header>
  </header>

  <main class="d-flex justify-content-between">
    <Login v-if="!store.logged_in"></Login>
    <Opinion v-if=store.logged_in title="tests"/>
  </main>
</template>

<style scoped>
</style>
