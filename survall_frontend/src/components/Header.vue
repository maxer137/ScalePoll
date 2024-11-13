<script setup>

</script>

<template>

  <header class="d-flex w-100 justify-content-between border-bottom">
  <h1 class="m-2 d-flex">
    <RouterLink to="/" class="d-flex">
      <img src="/src/assets/logo.png" style="height: 3rem" alt="logo"/>
      Survall
    </RouterLink>
  </h1>

  <div class="d-flex w-100 justify-content-end align-items-center">
    <RouterLink to="/closed_questions">Closed Questions</RouterLink>
    <RouterLink to="/answered_questions">Your history</RouterLink>
  </div>
  </header>
</template>

<style scoped>

</style>