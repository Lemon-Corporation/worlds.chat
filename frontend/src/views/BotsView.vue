<template>
  <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950">
    <!-- Верхняя навигация -->
    <NavBar/>
    <!-- Основной контент -->
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-4xl font-bold text-[#00ff9d] mb-8">Боты</h1>
      
      <div class="bg-gray-800 rounded-lg p-8 text-center">
        <Bot class="w-24 h-24 text-[#00ff9d] mx-auto mb-6" />
        <h2 class="text-2xl font-bold text-[#00ff9d] mb-4">Функция в бета-тестировании</h2>
        <p class="text-gray-300 mb-8">
          Мы работаем над улучшением функциональности ботов. Следите за обновлениями!
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Bot } from 'lucide-vue-next';
import NavBar from '@/components/NavBar.vue';

const navigation = [
  { name: "Обзор", href: "#", current: false },
  { name: "Популярное", href: "#", current: false },
  { name: "Категории", href: "#", current: false },
  { name: "Мои Миры", href: "#", current: false },
  { name: "Боты", href: "#", current: true },
];

</script>

<style scoped>
.bot-container {
  width: 100%;
  height: 100%;
  perspective: 1000px;
  overflow: hidden;
  border-radius: 50%;
  box-shadow: 0 0 20px rgba(0, 255, 157, 0.3);
}

.bot {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  border-radius: 50%;
  position: relative;
  animation: float 6s ease-in-out infinite;
  transform-style: preserve-3d;
}

.bot-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.1) 0%, rgba(0, 0, 0, 0.4) 100%);
  border-radius: 50%;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

.bot-container:hover .bot {
  animation-play-state: paused;
}

.bot-container:hover .bot-overlay {
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.2) 0%, rgba(0, 0, 0, 0.3) 100%);
}
</style>