<script setup>

import {ref} from 'vue'

const props = defineProps({
  title: String,
  description: String,
  result: Array(3),
  relevance: Number
})


const { title, description, result, relevance} = toRefs(props);

let vote_value = ref(null)
let relevance_value = ref(3)

let discussion_value = ref('')
let fore = ref(20)
let neutral = ref(30)
let against = ref(50)

let output = result.reduce((accumulator, currentValue) => {
  return accumulator + currentValue
},0)


</script>

<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
      <p class="card-text">{{ description }}</p>
    </div>
    <!--Buttons-->
    <div class="card-footer">
      <div>
        <h5>General opinion</h5>
        <div class="progress bg-danger" role="progressbar" aria-label="Basic example" aria-valuemin="0"
             aria-valuemax="100">
          <div class="progress-bar bg-danger" :style="{'width': against/output*100 + '%'}">{{ result[2] }}%</div>
          <div class="progress-bar bg-secondary" :style="{'width': neutral/output*100 + '%'}">{{ result[1] }}%</div>
          <div class="progress-bar bg-success" :style="{'width': fore/output*100 + '%'}" id="progress_fore">{{ result[0] }}%</div>
        </div>
        <div class="d-flex flex-row">
          <h5 class="text-danger translate-middle-x position-absolute end-0">Disagree</h5>
          <h5 class="text-secondary translate-middle-x position-absolute start-50">Neutral</h5>
          <h5 class="text-success">Agree</h5>
        </div>
        <h5>General relevance</h5>
        <input type="range" class="form-range" min="1" max="5" step="0.1" v-model=relevance disabled/>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">

/* Styling for the div */
.flyaway {
  animation: flyaway 1.5s ease-in-out forwards;
}

.fly-in {
  animation: fly-in 1.2s ease-in-out forwards;
}

/* Flyaway animation */
@keyframes flyaway {
  0% {
    transform: translate(0, 0) scale(1);
  }
  10% {
    transform: translate(0, 0) scale(1.2);
  }
  20% {
    transform: translate(0, 0) scale(1);
  }
  40% {
    transform: translate(0, 0) scale(1);
    opacity: 1;
  }
  100% {
    transform: translate(100vw, -100vh) scale(1.2) rotate(45deg);
    opacity: 0.8;
  }
}

@keyframes fly-in {
  0% {
    transform: translate(-100vw, -100vh) scale(1.2) rotate(65deg);
    opacity: 0.8;
  }
  100% {
    transform: translate(0, 0) scale(1);
    opacity: 1;
  }
}
</style>