<script setup>
import {ref} from 'vue'
import {useApiStore} from "@/stores/login.js";
import * as Bootstrap from "bootstrap";

const store = useApiStore()

let title = ref('')
let description = ref('')


</script>

<template>
  <div class="card" style="width: 100%;" @animationend="flew">
    <div class="card-body">
      <h5 class="card-title">Create a new question</h5>
      <label class="form-label">Question title</label>
      <input type="text" class="form-control" v-model="title">
      <label class="form-label">Question description</label>
      <input type="text" class="form-control" v-model="description">
    </div>
    <div class="card-footer">
      <button class="form-control btn">Save</button>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>