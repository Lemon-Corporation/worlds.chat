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
        'translate-y-0 opacity-100': showForm,
        'translate-y-10 opacity-0': !showForm,
      }"
    >
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Войти в WORLDS
        </h2>
      </div>
      <div class="mt-8 space-y-6">
        <div class="flex justify-center space-x-4 mb-4">
          <button
            @click="loginMethod = 'email'"
            :class="{
              'bg-green-600 text-white': loginMethod === 'email',
              'bg-gray-200 text-gray-700': loginMethod !== 'email',
            }"
            class="px-4 py-2 rounded-md transition-colors duration-300 ease-in-out"
          >
            <Mail class="inline-block mr-2" size="18" />
            Email
          </button>
          <button
            @click="loginMethod = 'phone'"
            :class="{
              'bg-green-600 text-white': loginMethod === 'phone',
              'bg-gray-200 text-gray-700': loginMethod !== 'phone',
            }"
            class="px-4 py-2 rounded-md transition-colors duration-300 ease-in-out"
          >
            <Phone class="inline-block mr-2" size="18" />
            Телефон
          </button>
        </div>

        <form @submit.prevent="handleLogin" class="mt-8 space-y-6">
          <a
            href="/"
            class="font-medium text-green-600 hover:text-green-500 transition-colors duration-300 ease-in-out"
            >На главную</a
          >
          <div class="rounded-md shadow-sm -space-y-px">
            <div>
              <label :for="loginMethod" class="sr-only">{{
                loginMethod === "email" ? "Email" : "Телефон"
              }}</label>
              <input
                :id="loginMethod"
                :name="loginMethod"
                :type="loginMethod === 'email' ? 'email' : 'tel'"
                :autocomplete="loginMethod === 'email' ? 'email' : 'tel'"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm transition-all duration-300 ease-in-out"
                :placeholder="
                  loginMethod === 'email' ? 'Email адрес' : 'Номер телефона'
                "
                v-model="loginData.identifier"
              />
            </div>
            <div>
              <label for="password" class="sr-only">Пароль</label>
              <input
                id="password"
                name="password"
                type="password"
                autocomplete="current-password"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm transition-all duration-300 ease-in-out"
                placeholder="Пароль"
                v-model="loginData.password"
              />
            </div>
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input
                id="remember-me"
                name="remember-me"
                type="checkbox"
                class="h-4 w-4 text-green-600 focus:ring-green-500 border-gray-300 rounded transition-all duration-300 ease-in-out"
              />
              <label for="remember-me" class="ml-2 block text-sm text-gray-900">
                Запомнить меня
              </label>
            </div>

            <div class="text-sm">
              <a
                href="#"
                class="font-medium text-green-600 hover:text-green-500 transition-colors duration-300 ease-in-out"
              >
                Забыли пароль?
              </a>
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 transition-all duration-300 ease-in-out"
            >
              <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                <LockClosed
                  class="h-5 w-5 text-green-500 group-hover:text-green-400 transition-colors duration-300 ease-in-out"
                  aria-hidden="true"
                />
              </span>
              Войти
            </button>
          </div>
        </form>
      </div>
      <div class="mt-6 text-center">
        <p class="text-sm text-gray-600">
          Нет аккаунта?
          <a
            href="/auth/sign-up"
            class="font-medium text-green-600 hover:text-green-500 transition-colors duration-300 ease-in-out"
          >
            Зарегистрироваться
          </a>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { Mail, Phone, LockClosed } from "lucide-vue-next";

const loginMethod = ref("email");
const loginData = ref({
  identifier: "",
  password: "",
});
const showForm = ref(false);
const particlesContainer = ref(null);

const handleLogin = () => {
  // Здесь будет логика входа
  console.log("Попытка входа с:", loginData.value);
};

onMounted(() => {
  showForm.value = true;
  initParticles();
});

onUnmounted(() => {
  // Очистка частиц при размонтировании компонента
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
