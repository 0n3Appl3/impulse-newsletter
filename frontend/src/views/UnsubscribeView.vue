<script setup lang="ts">
import { onMounted } from 'vue'

const query = window.location.hash.replace('#/unsubscribe', '')
const params = new URLSearchParams(query)
const email = params.get('email')

onMounted(async () => {
	console.log(query)
	await fetch("https://appl3pvp.com:3001/api/v1/email/" + email, {
			method: 'POST',
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json'
			},
	})
})
</script>

<template>
	<h1>unsubscribed</h1>
	<p>That's really sad.</p>
</template>

<style scoped>
</style>
