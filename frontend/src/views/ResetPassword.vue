<template>
    <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950 flex flex-col justify-center items-center px-4 sm:px-6 lg:px-8">
      <div class="w-full max-w-md">
        <div class="text-center mb-10">
          <h2 class="text-4xl font-bold text-[#00ff9d] mb-2">Восстановление пароля</h2>
          <p class="text-gray-300">Введите ваш email для сброса пароля</p>
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
              placeholder="Введите ваш email"
            />
          </div>
          <div>
            <button
              type="submit"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-gray-900 bg-[#00ff9d] hover:bg-[#00cc7d] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#00ff9d]"
            >
              Отправить инструкции
            </button>
          </div>
        </form>
        <div class="mt-6 text-center">
          <p class="text-sm text-gray-300">
            Вспомнили пароль?
            <a href="/auth/sign-in" class="font-medium text-[#00ff9d] hover:underline">Вернуться ко входу</a>
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const email = ref('');
  
  const handleSubmit = () => {
    // Здесь будет логика отправки запроса на сброс пароля
    console.log('Запрос на сброс пароля:', { email: email.value });
    
    // Очистка формы после отправки
    email.value = '';
  
    alert('Инструкции по сбросу пароля отправлены на ваш email!');
  };
  </script>