import { defineStore } from 'pinia'

export const useLoginStore = defineStore('login', {
    state: () => ({
        token: null,
        logged_in: false,
    }),
    actions: {
        async login(username) {
            let response = await fetch(`${import.meta.env.VITE_AUTH_DOMAIN}/login`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    user: username.value
                })
            })
            this.token = await response.json()
            this.logged_in = true
        },
    }
})