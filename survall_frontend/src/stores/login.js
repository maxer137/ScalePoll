import { defineStore } from 'pinia'

export const useLoginStore = defineStore('login', {
    state: () => ({
        token: null,
        logged_in: false,
    }),
    getters: {
        async get_question() {
            let response = await fetch(`${import.meta.env.VITE_API_DOMAIN}/get_question`,{
                headers: {'Authorization': `${this.token}`},
            })
            if (!response.ok) {
                console.log("login success")
            }
            return [await response.json()]
        }
    },
    actions: {
        async login(username) {
            console.log(username)
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
            await this.test_authentication()
        },

        async test_authentication() {
            let response = fetch(`${import.meta.env.VITE_API_DOMAIN}/authentication_example`,{
                headers: {'Authorization': `${this.token}`},
                method: 'POST',
            })
            if (!response.ok) {
                console.log("login success")
            }
        },

        async submit_vote(question_uiid, user_hash, answer_score, relevance_score, discussion_field) {
            let response = await fetch(`${import.meta.env.VITE_API_DOMAIN}/get_question`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: {
                    question_uuid: question_uiid,
                    user_hash: user_hash,
                    answer_score: answer_score,
                    relevance_score: relevance_score,
                    discussion_field: discussion_field,
                },
            })

            if (!response.ok) {
                console.log("login success")
            }
            return await response.json()
        }
    }
})