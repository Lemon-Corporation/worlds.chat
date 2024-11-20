<template>
  <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950 flex flex-col justify-center items-center px-4 sm:px-6 lg:px-8">
    <div class="w-full max-w-md">
      <div class="text-center mb-10">
        <h2 class="text-4xl font-bold text-[#00ff9d] mb-2">Вход</h2>
        <p class="text-gray-300">Войдите в свой аккаунт Worlds</p>
      </div>
      <form @submit.prevent="handleSubmit" class="space-y-6">
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
        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember-me"
              v-model="rememberMe"
              type="checkbox"
              class="h-4 w-4 text-[#00ff9d] focus:ring-[#00ff9d] border-gray-300 rounded"
            />
            <label for="remember-me" class="ml-2 block text-sm text-gray-300">
              Запомнить меня
            </label>
          </div>
          <div class="text-sm">
            <a href="/auth/reset-password" class="font-medium text-[#00ff9d] hover:underline">
              Забыли пароль?
            </a>
          </div>
        </div>
        <div v-if="error" class="text-red-500 text-sm mt-2">
          {{ error }}
        </div>
        <div>
          <button
            type="submit"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-gray-900 bg-[#00ff9d] hover:bg-[#00cc7d] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#00ff9d]"
            :disabled="isLoading"
          >
            {{ isLoading ? 'Вход...' : 'Войти' }}
          </button>
        </div>
      </form>
      <div class="mt-6 text-center">
        <p class="text-sm text-gray-300">
          Нет аккаунта?
          <a href="/auth/sign-up" class="font-medium text-[#00ff9d] hover:underline">Зарегистрироваться</a>
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

const email = ref('');
const password = ref('');
const rememberMe = ref(false);
const error = ref('');
const isLoading = ref(false);

const handleSubmit = async () => {
  error.value = '';
  isLoading.value = true;

  try {
    const response = await store.dispatch('auth/login', {
      username: email.value,
      password: password.value
    });

    console.log('Вход выполнен успешно:', response);

    // Сохранение токена в localStorage, если выбрано "Запомнить меня"
    if (rememberMe.value) {
      localStorage.setItem('token', response.access_token);
    }
    router.push('/app');
    // Очистка формы после успешного входа
    email.value = '';
    password.value = '';
    rememberMe.value = false;

    // Перенаправление на главную страницу или панель управления
    router.push('/app');
  } catch (err) {
    console.error('Ошибка при входе:', err);
    error.value = err.message || 'Произошла ошибка при входе. Пожалуйста, попробуйте снова.';
  } finally {
    isLoading.value = false;
  }
};
</script>