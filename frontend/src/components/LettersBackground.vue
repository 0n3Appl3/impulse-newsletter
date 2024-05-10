<script setup lang="ts">
</script>

<template>
	<Transition name="portrait-fade-top" appear>
		<img class="preview-one" src="/images/newsletter-preview.png" alt="Newsletter Preview"/>
	</Transition>
	<Transition name="portrait-fade" appear>
		<img class="preview-two" src="/images/newsletter-preview.png" alt="Newsletter Preview"/>
	</Transition>
</template>

<style scoped>
.preview-one, .preview-two {
    position: absolute;
    filter: drop-shadow(0.5rem 0.5rem 0.75rem #00000063);
	z-index: -1;
}
.preview-one {
	height: 80%;
	top: -40%;
	left: 5%;
}
.preview-two {
	height: 80%;
	bottom: -40%;
	right: 5%;
}
.orb__container, .orb__container-two {
    position: absolute;
    background: rgb(219,43,57);
	background: linear-gradient(54deg, rgba(219,43,57,1) 0%, rgba(173,42,159,1) 61%, rgba(142,50,255,1) 100%);
    z-index: -1;
}
.orb__container {
	position: absolute;
	top: 0;
	right: 0;
	border-radius: 33% 67% 72% 28% / 74% 26% 74% 26%;
	width: 1050px;
	height: 100%;
}
.orb__container-two {
	top: 5%;
	right: 35%;
	border-radius: 17% 83% 48% 52% / 45% 37% 63% 55%;
	width: 500px;
	height: 50%;
}
.portrait-fade-enter-active, .portrait-fade-leave-active  {
  transition: all 1.6s cubic-bezier(0.215, 0.610, 0.355, 1);
}
.portrait-fade-enter-from, .portrait-fade-leave-to {
  opacity: 0;
  transform: translateY(300px);
}
.portrait-fade-top-enter-active, .portrait-fade-top-leave-active  {
  transition: all 1s cubic-bezier(0.215, 0.610, 0.355, 1);
}
.portrait-fade-top-enter-from, .portrait-fade-top-leave-to {
  opacity: 0;
  transform: translateY(-300px);
}
@media screen and (max-width: 1000px) {
	.preview-one {
		height: 50%;
		top: -30%;
	}
	.preview-two {
		height: 50%;
		bottom: -30%;
	}
}
@media screen and (max-width: 700px) {
	.portrait {
		right: 0%;
		height: 60%;
	}
}
</style>