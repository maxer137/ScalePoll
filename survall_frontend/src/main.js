import './assets/main.css'

// Import our custom CSS
import './scss/styles.scss'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'


import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'


const pinia = createPinia()
const app = createApp(App)


app.use(pinia)
app.mount('#app')
