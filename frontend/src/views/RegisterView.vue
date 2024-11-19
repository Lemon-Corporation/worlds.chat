<template>
  <div
    class="min-h-screen flex items-center justify-center px-4 sm:px-6 lg:px-8 relative overflow-hidden"
  >
    <div
      class="absolute inset-0 bg-gradient-to-br from-green-600 via-green-500 to-green-300 opacity-50"
    ></div>
    <div
      class="absolute inset-0 particles-container"
      ref="particlesContainer"
    ></div>

    <div
      class="max-w-md w-full space-y-8 bg-white bg-opacity-90 backdrop-blur-lg p-10 rounded-xl shadow-2xl relative z-10 transform transition-all duration-500 ease-in-out"
      :class="{
        'translate-y-0 opacity-100': showMessage,
        'translate-y-10 opacity-0': !showMessage,
      }"
    >
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Регистрация временно закрыта
        </h2>
      </div>

      <div class="mt-8 text-center">
        <p class="text-lg text-gray-600 mb-6">
          Мы временно приостановили регистрацию новых пользователей. Приносим
          извинения за неудобства.
        </p>
        <p class="text-md text-gray-500 mb-8">
          Пожалуйста, попробуйте зарегистрироваться позже.
        </p>
        <router-link
          to="/"
          class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 transition-all duration-300 ease-in-out"
        >
          <ArrowLeft class="mr-2 h-5 w-5" />
          Вернуться на главную
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { ArrowLeft } from "lucide-vue-next";

const showMessage = ref(false);
const particlesContainer = ref(null);

onMounted(() => {
  showMessage.value = true;
  initParticles();
});

onUnmounted(() => {
  if (particlesContainer.value) {
    particlesContainer.value.innerHTML = "";
  }
});

const initParticles = () => {
  const particlesCount = 50;
  const colors = ["#8B5CF6", "#EC4899", "#6366F1"];
  const particles = [];

  for (let i = 0; i < particlesCount; i++) {
    particles.push(createParticle());
  }

  function createParticle() {
    const particle = document.createElement("div");
    particle.style.position = "absolute";
    particle.style.width = "6px";
    particle.style.height = "6px";
    particle.style.background =
      colors[Math.floor(Math.random() * colors.length)];
    particle.style.borderRadius = "50%";
    particle.style.top = Math.random() * 100 + "%";
    particle.style.left = Math.random() * 100 + "%";
    particle.style.transform = "scale(0)";
    particle.style.transition = "transform 1s ease-out, opacity 1s ease-out";
    particle.style.opacity = "0";
    particlesContainer.value.appendChild(particle);

    setTimeout(() => {
      particle.style.transform = "scale(1)";
      particle.style.opacity = "0.7";
    }, 100);

    setTimeout(() => {
      particle.style.transform = "scale(1.5)";
      particle.style.opacity = "0";
    }, 1000 + Math.random() * 3000);

    setTimeout(() => {
      particle.remove();
      particles.splice(particles.indexOf(particle), 1);
      particles.push(createParticle());
    }, 4000 + Math.random() * 3000);

    return particle;
  }
};
</script>

<style scoped>
.particles-container {
  pointer-events: none;
}
</style>
