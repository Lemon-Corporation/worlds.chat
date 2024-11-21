<template>
  <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950 flex flex-col justify-center items-center px-4 sm:px-6 lg:px-8">
    <div class="w-full max-w-md">
      <div class="text-center mb-10">
        <h2 class="text-4xl font-bold text-[#00ff9d] mb-2">Регистрация</h2>
        <p class="text-gray-300">Создайте свой аккаунт в Worlds</p>
      </div>
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <div>
          <label for="username" class="block text-sm font-medium text-gray-300 mb-1">Имя пользователя</label>
          <input
            id="username"
            v-model="username"
            type="text"
            required
            class="w-full px-3 py-2 bg-gray-800 border border-purple-500/20 rounded-md text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] focus:border-transparent"
            placeholder="Введите имя пользователя"
          />
        </div>
        <div>
          <label for="email" class="block text-sm font-medium text-gray-300 mb-1">Email</label>
          <input
            id="email"
            v-model="email"
            type="email"
            required
            class="w-full px-3 py-2 bg-gray-800 border border-purple-500/20 rounded-md text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] focus:border-transparent"
            placeholder="Введите email"
          />
        </div>
        <div>
          <label for="password" class="block text-sm font-medium text-gray-300 mb-1">Пароль</label>
          <input
            id="password"
            v-model="password"
            type="password"
            required
            class="w-full px-3 py-2 bg-gray-800 border border-purple-500/20 rounded-md text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] focus:border-transparent"
            placeholder="Введите пароль"
          />
        </div>
        <div>
          <label for="confirmPassword" class="block text-sm font-medium text-gray-300 mb-1">Подтвердите пароль</label>
          <input
            id="confirmPassword"
            v-model="confirmPassword"
            type="password"
            required
            class="w-full px-3 py-2 bg-gray-800 border border-purple-500/20 rounded-md text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] focus:border-transparent"
            placeholder="Подтвердите пароль"
          />
        </div>
        <div>
          <button
            type="submit"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-gray-900 bg-[#00ff9d] hover:bg-[#00cc7d] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#00ff9d]"
          >
            Зарегистрироваться
          </button>
        </div>
      </form>
      <div class="mt-6 text-center">
        <p class="text-sm text-gray-300">
          Уже есть аккаунт?
          <a href="/auth/sign-in" class="font-medium text-[#00ff9d] hover:underline">Войти</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const store = useStore();
const router = useRouter();

const username = ref('');
const email = ref('');
const password = ref('');
const error = ref('');
const successMessage = ref('');
const isLoading = ref(false);

const handleSubmit = async () => {
  if (!username.value || !email.value || !password.value) {
    error.value = 'Пожалуйста, заполните все поля';
    return;
  }

  isLoading.value = true;
  error.value = '';
  successMessage.value = '';

  try {
    const result = await store.dispatch('auth/register', {
      username: username.value,
      email: email.value,
      password: password.value
    });
    successMessage.value = result.message;
    setTimeout(() => {
      router.push('/login');
    }, 2000);
  } catch (err) {
    error.value = err.message;
  } finally {
    isLoading.value = false;
  }
};
</script>