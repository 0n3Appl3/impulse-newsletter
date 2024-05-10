<script setup lang="ts">
import { ref } from 'vue'

const email = ref('')
const status = ref('')

const emailFormat: RegExp = new RegExp(/([a-zA-Z0-9_.+-]+)@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]/)

const attemptSubmit = (event: Event) => {
    status.value = ''
    if (emailFormat.test(email.value) === false) {
        event.preventDefault()
        status.value = 'Enter your email address in the correct format. e.g. name@email.com'
        return
    }
}
</script>

<template>
    <div class="subscribe__container">
        <div class="subscribe__form">
            <form>
                <input v-model="email" type="text" id="email" name="email" placeholder="Enter your email" required />
                <button @click="attemptSubmit" type="button">Subscribe</button>
                <p>{{ status }}</p>
            </form>
        </div>
        <div class="border"></div>
    </div>
</template>

<style scoped>
form {
    display: inline;
    margin: 0 auto;
}
form input {
    outline: none;
    border: none;
    color: var(--color-text);
    background-color: #eeeeee;
    padding: 8px 15px;
    margin-right: 0.5rem;
}
form button {
    text-decoration: none;
    padding: 8px 15px;
    border: none;
    background-color: var(--color-button);
    color: var(--color-background);
    transition: all 0.15s ease-in-out;
}
form button:hover, button:hover {
    background-color: var(--color-button-hover);
    cursor: pointer;
}
p {
    color: var(--color-button-hover);
    margin-top: 0.7rem;
}
.subscribe__container {
    display: block;
    filter: drop-shadow(0.5rem 0.5rem 0.75rem #00000063);
    margin-top: 2rem;
}
.subscribe__form {
    background-color: white;
    padding: 1rem;
    text-align: center;
}
.border {
    width: 100%;
    height: 7px;
    background: rgb(131,58,180);
    background: linear-gradient(90deg, rgba(131,58,180,1) 0%, rgba(253,29,29,1) 50%, rgba(252,176,69,1) 100%);
    overflow: hidden;
}
</style>
