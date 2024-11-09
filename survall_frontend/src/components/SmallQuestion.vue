<script setup>


const props = defineProps(['question'])
</script>

<template>
  <div class="card mb-3" style="width: 100%;">
    <div class="card-body">
      <h5 class="card-title">{{ question['question'] }}</h5>
      <p class="card-text">{{ question['description'] }}</p>
    </div>
    <div class="card-footer">
      <div class="progress bg-danger" role="progressbar" aria-label="Basic example" aria-valuenow="75"
           aria-valuemin="0" aria-valuemax="100">
        <div class="progress-bar bg-danger"
             :style="{'width': question['negative']/question['answers_count']*100 + '%'}">{{
            question['negative']
          }}
        </div>
        <div class="progress-bar bg-secondary"
             :style="{'width': (question['neutral'])/question['answers_count']*100 + '%'}">{{
            question['neutral']
          }}
        </div>
        <div class="progress-bar bg-success"
             :style="{'width': question['positive']/question['answers_count']*100 + '%'}" id="progress_fore">
          {{ question['positive'] }}
        </div>
      </div>
      <div class="d-flex flex-row">
        <p class="text-danger ">No</p>
        <p class="text-secondary translate-middle-x position-absolute start-50">Neutral</p>
        <p class="text-success translate-middle-x position-absolute end-0">Yes</p>
      </div>
      <h5>General relevance</h5>
      <input type="range" class="form-range" min="1" max="5" step="0.1"
             :value="question['relevance_sum'] / question['answers_count']" disabled/>
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