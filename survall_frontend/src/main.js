import './assets/main.css'

// Import our custom CSS
import './scss/styles.scss'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'


const DOMAIN_NAME = "http://127.0.0.1:1337/"

import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
