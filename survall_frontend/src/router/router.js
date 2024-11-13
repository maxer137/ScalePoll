import { createMemoryHistory, createRouter } from 'vue-router'

import VoteView from '/src/pages/Vote.vue'
import ClosedQuestionsView from '/src/pages/ClosedQuestions.vue'
import AnsweredQuestionsView from '/src/pages/AnsweredQuestions.vue'
import LoginView from '/src/pages/Login.vue'

import {useApiStore} from "@/stores/login.js";


const routes = [
    { path: '/', component: VoteView,
        meta: {
            requiresAuth: true
        } },
    { path: '/closed_questions', component: ClosedQuestionsView,
        meta: {
            requiresAuth: true
        } },
    { path: '/answered_questions', component: AnsweredQuestionsView,
        meta: {
            requiresAuth: true
        } },
    { name: 'login', path: '/login', component: LoginView },
]

const router = createRouter({
    history: createMemoryHistory(),
    routes,
})


router.beforeEach((to) => {
    // ✅ This will work because the router starts its navigation after
    // the router is installed and pinia will be installed too
    const store = useApiStore()

    if (to.meta.requiresAuth && !store.logged_in) return '/login'
})

export default router