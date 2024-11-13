import { defineStore } from 'pinia'

//The Pinia store we use to contact the API and authentication server.
export const useApiStore = defineStore('login', {
    state: () => ({
        token: null,
        logged_in: false,
    }),
    actions: {
        async get_question() {
            let response = await fetch(`${import.meta.env.VITE_API_DOMAIN}/get_question`,{
                headers: {'Authorization': `${this.token}`},
            })
            if (!response.ok) {
                console.log("something went wrong")
            }
            if (response.status === 204) {
                return null
            }
            return await response.json()
        },
        async get_my_questions() {
            let response = await fetch(`${import.meta.env.VITE_API_DOMAIN}/previous_questions`,{
                headers: {'Authorization': `${this.token}`},
            })
            if (!response.ok) {
                console.log()
            }
            return await response.json()
        },

        async get_closed_questions() {
            let response = await fetch(`${import.meta.env.VITE_API_DOMAIN}/closed_questions`,{
                headers: {'Authorization': `${this.token}`},
            })
            if (!response.ok) {
                console.log()
            }
            return await response.json()
        },

        async login(username) {
            let response = await fetch(`${import.meta.env.VITE_AUTH_DOMAIN}/login`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    user: username
                })
            })
            if (!response.ok) {
                return
            }

            this.token = (await response.json())['token']
            this.logged_in = true
            return true
        },

        async submit_vote(question_uiid, user_hash, answer_score, relevance_score, discussion_field) {
            let response = await fetch(`${import.meta.env.VITE_API_DOMAIN}/post_answer`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json', 'Authorization': `${this.token}`},
                body: JSON.stringify({
                    question_uuid: question_uiid,
                    answer_score: answer_score,
                    relevance_score: relevance_score,
                    discussion: discussion_field,
                }),
            })

            if (!response.ok) {
                console.log("login success")
            }
            return await response.json()
        }
    }
})