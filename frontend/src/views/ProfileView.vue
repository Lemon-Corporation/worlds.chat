<template>
  <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950">
    <!-- Верхняя навигация -->
    <NavBar/>
    <!-- Основной контент -->
    <div class="container mx-auto px-4 py-8">
      <div class="bg-gray-800 rounded-lg shadow-xl overflow-hidden">
        <!-- Баннер профиля -->
        <div class="h-48 bg-gradient-to-r from-purple-600 to-blue-600 relative">
          <img
            :src="user.banner"
            alt="Баннер профиля"
            class="w-full h-full object-cover"
          />
          <div class="absolute bottom-0 left-0 w-full h-1/2 bg-gradient-to-t from-gray-800 to-transparent"></div>
        </div>

        <div class="p-6">
          <div class="flex flex-col md:flex-row md:items-end md:space-x-6">
            <!-- Аватар -->
            <div class="w-32 h-32 rounded-full border-4 border-gray-800 overflow-hidden -mt-16 md:-mt-20 z-10 relative bg-gray-700">
              <img
                :src="user.avatar"
                :alt="user.username"
                class="w-full h-full object-cover"
              />
            </div>

            <!-- Информация о пользователе -->
            <div class="mt-4 md:mt-0 flex-grow">
              <h1 class="text-3xl font-bold text-[#00ff9d]">{{ user.username }}</h1>
              <p class="text-gray-400">{{ user.tag }}</p>
              <div class="mt-2 flex items-center space-x-2">
                <span class="bg-purple-500/20 text-[#00ff9d] px-2 py-1 rounded text-sm">{{ user.level }} уровень</span>
                <span class="text-gray-400 text-sm">{{ user.xp }} XP</span>
              </div>
            </div>

            <!-- Кнопки действий -->
            <div class="mt-4 md:mt-0 flex space-x-2">
              <button class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-bold py-2 px-4 rounded transition-colors duration-200">
                Редактировать профиль
              </button>
              <button class="bg-purple-500/20 hover:bg-purple-500/30 text-[#00ff9d] font-bold py-2 px-4 rounded transition-colors duration-200">
                Настройки
              </button>
            </div>
          </div>

          <!-- Статистика -->
          <div class="mt-6 grid grid-cols-2 md:grid-cols-4 gap-4">
            <div class="bg-gray-700 rounded-lg p-4 text-center">
              <h3 class="text-[#00ff9d] font-bold text-xl">{{ user.worldsCount }}</h3>
              <p class="text-gray-400">Миров</p>
            </div>
            <div class="bg-gray-700 rounded-lg p-4 text-center">
              <h3 class="text-[#00ff9d] font-bold text-xl">{{ user.friendsCount }}</h3>
              <p class="text-gray-400">Друзей</p>
            </div>
            <div class="bg-gray-700 rounded-lg p-4 text-center">
              <h3 class="text-[#00ff9d] font-bold text-xl">{{ user.postsCount }}</h3>
              <p class="text-gray-400">Постов</p>
            </div>
            <div class="bg-gray-700 rounded-lg p-4 text-center">
              <h3 class="text-[#00ff9d] font-bold text-xl">{{ user.achievementsCount }}</h3>
              <p class="text-gray-400">Достижений</p>
            </div>
          </div>

          <!-- Биография -->
          <div class="mt-6">
            <h2 class="text-xl font-bold text-[#00ff9d] mb-2">О себе</h2>
            <p class="text-gray-300">{{ user.bio }}</p>
          </div>

          <!-- Миры пользователя -->
          <div class="mt-6">
            <h2 class="text-xl font-bold text-[#00ff9d] mb-4">Миры пользователя</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
              <div v-for="world in user.worlds" :key="world.id" class="bg-gray-700 rounded-lg p-4 flex items-center space-x-4">
                <img :src="world.icon" :alt="world.name" class="w-12 h-12 rounded-full">
                <div>
                  <h3 class="text-[#00ff9d] font-bold">{{ world.name }}</h3>
                  <p class="text-gray-400 text-sm">{{ world.membersCount }} участников</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Достижения -->
          <div class="mt-6">
            <h2 class="text-xl font-bold text-[#00ff9d] mb-4">Последние достижения</h2>
            <div class="flex flex-wrap gap-4">
              <div v-for="achievement in user.recentAchievements" :key="achievement.id" class="bg-gray-700 rounded-lg p-4 flex items-center space-x-4">
                <img :src="achievement.icon" :alt="achievement.name" class="w-12 h-12">
                <div>
                  <h3 class="text-[#00ff9d] font-bold">{{ achievement.name }}</h3>
                  <p class="text-gray-400 text-sm">{{ achievement.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { AtSign, Bell } from 'lucide-vue-next';
import NavBar from '@/components/NavBar.vue';

const navigation = [
  { name: "Обзор", href: "#", current: false },
  { name: "Популярное", href: "#", current: false },
  { name: "Категории", href: "#", current: false },
  { name: "Мои Миры", href: "#", current: false },
  { name: "Профиль", href: "#", current: true },
];

const user = ref({
  username: 'User',
  tag: '@user',
  avatar: 'https://i.pinimg.com/736x/26/71/0c/26710c62610833284e41ac25ad166700.jpg',
  banner: 'https://i.imgur.com/dlFRtHv.png',
  level: 0,
  xp: 0,
  worldsCount: 1,
  friendsCount: 0,
  postsCount: 0,
  achievementsCount: 1,
  bio: 'Исследователь цифровых миров и создатель уникальных виртуальных пространств. Люблю погружаться в новые реальности и делиться своими открытиями с сообществом.',
  worlds: [
    { id: 1, name: 'Тестовый мир', icon: 'https://i.imgur.com/dlFRtHv.png', membersCount: 1 },
  ],
  recentAchievements: [
    { id: 1, name: 'Первооткрыватель', icon: 'https://i.imgur.com/dlFRtHv.png', description: 'Создал свой первый мир' },
  ]
});
</script>