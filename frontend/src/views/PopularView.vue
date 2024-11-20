<template>
  <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950">
    <!-- Верхняя навигация -->
    <nav class="border-b border-purple-500/20 backdrop-blur-md bg-gray-900/50 w-full">
      <div class="px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center">
            <span class="text-[#00ff9d] text-2xl font-bold font-mono">WORLDS</span>
          </div>
          <div class="hidden md:block">
            <div class="flex items-center space-x-4">
              <a
                v-for="item in navigation"
                :key="item.name"
                :href="item.href"
                :class="[
                  item.current
                    ? 'bg-purple-500/20 text-[#00ff9d]'
                    : 'text-gray-300 hover:bg-purple-500/10 hover:text-[#00ff9d]',
                  'px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200',
                ]"
              >
                {{ item.name }}
              </a>
            </div>
          </div>
          <div class="flex items-center gap-4">
            <button class="text-gray-300 hover:text-[#00ff9d] transition-colors duration-200">
              <AtSign class="w-6 h-6" />
            </button>
            <button class="text-gray-300 hover:text-[#00ff9d] transition-colors duration-200">
              <Bell class="w-6 h-6" />
            </button>
            <div class="relative">
              <img
                class="h-8 w-8 rounded-full bg-purple-500/20"
                src="https://i.pinimg.com/736x/26/71/0c/26710c62610833284e41ac25ad166700.jpg"
                alt="Аватар пользователя"
              />
              <span
                class="absolute bottom-0 right-0 block h-2 w-2 rounded-full bg-[#00ff9d] ring-2 ring-gray-900"
              ></span>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- Основной контент -->
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-4xl font-bold text-[#00ff9d] mb-8">Популярные Миры</h1>
      
      <!-- Фильтры и сортировка -->
      <div class="flex flex-wrap items-center justify-between mb-8 gap-4">
        <div class="flex items-center space-x-4">
          <button
            v-for="filter in filters"
            :key="filter"
            @click="activeFilter = filter"
            :class="[
              'px-4 py-2 rounded-full text-sm font-medium transition-colors duration-200',
              activeFilter === filter
                ? 'bg-[#00ff9d] text-gray-900'
                : 'bg-gray-800 text-gray-300 hover:bg-purple-500/20 hover:text-[#00ff9d]'
            ]"
          >
            {{ filter }}
          </button>
        </div>
        <div class="relative">
          <select
            v-model="sortBy"
            class="appearance-none bg-gray-800 text-gray-300 py-2 pl-4 pr-8 rounded-full focus:outline-none focus:ring-2 focus:ring-[#00ff9d]"
          >
            <option value="popular">По популярности</option>
            <option value="new">Новые</option>
            <option value="members">По количеству участников</option>
          </select>
          <ChevronDown class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 pointer-events-none" />
        </div>
      </div>
      
      <!-- Сетка миров -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        <div v-for="world in filteredWorlds" :key="world.id" class="flex flex-col items-center">
          <div class="relative w-48 h-48 mb-4 group">
            <div class="planet-container">
              <div class="planet" :style="{ backgroundImage: `url(${world.image})` }">
                <div class="planet-overlay"></div>
              </div>
            </div>
            <div class="absolute inset-0 bg-black bg-opacity-40 rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
              <button @click="joinWorld(world.id)" class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium px-4 py-2 rounded-full transition-colors duration-200">
                Присоединиться
              </button>
            </div>
          </div>
          <div class="bg-gray-800 rounded-lg p-4 w-full text-center">
            <h2 class="text-xl font-bold text-[#00ff9d] mb-2">{{ world.name }}</h2>
            <p class="text-gray-300 mb-2 h-12 overflow-hidden">{{ world.description }}</p>
            <div class="flex items-center justify-center space-x-2">
              <Users class="w-5 h-5 text-[#00ff9d]" />
              <span class="text-gray-300">{{ world.members }} участников</span>
            </div>
            <span class="inline-block mt-2 bg-purple-500/20 text-[#00ff9d] px-2 py-1 rounded-full text-sm">
              {{ world.category }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { AtSign, Bell, ChevronDown, Users } from 'lucide-vue-next';

const navigation = [
  { name: "Обзор", href: "#", current: false },
  { name: "Популярное", href: "#", current: true },
  { name: "Категории", href: "#", current: false },
  { name: "Мои Миры", href: "#", current: false },
];

const filters = ["Все", "Фэнтези", "Sci-Fi", "Постапокалипсис", "Исторические"];
const activeFilter = ref("Все");
const sortBy = ref("popular");

const worlds = ref([
  {
    id: 1,
    name: "Эльдория",
    image: "https://i.imgur.com/dlFRtHv.png",
    category: "Фэнтези",
    description: "Магический мир, полный эльфов, драконов и древних тайн.",
    members: 15000
  },
  {
    id: 2,
    name: "Нео-Токио",
    image: "https://i.imgur.com/oPPTj4b.png",
    category: "Sci-Fi",
    description: "Футуристический мегаполис с передовыми технологиями и киберпанк-атмосферой.",
    members: 12000
  },
  {
    id: 3,
    name: "Пустошь",
    image: "https://i.imgur.com/w2LCHjF.png",
    category: "Постапокалипсис",
    description: "Мир после глобальной катастрофы, где выживание - главная цель.",
    members: 9000
  },
  {
    id: 4,
    name: "Древний Рим",
    image: "https://i.imgur.com/dlFRtHv.png",
    category: "Исторические",
    description: "Погрузитесь в эпоху Римской империи, интриг и гладиаторских боев.",
    members: 7500
  },
  {
    id: 5,
    name: "Атлантида",
    image: "https://i.imgur.com/oPPTj4b.png",
    category: "Фэнтези",
    description: "Исследуйте подводное королевство с древними технологиями и мифическими существами.",
    members: 11000
  },
  {
    id: 6,
    name: "Марсианская колония",
    image: "https://i.imgur.com/w2LCHjF.png",
    category: "Sci-Fi",
    description: "Станьте частью первого поселения людей на Красной планете.",
    members: 8500
  },
]);

const filteredWorlds = computed(() => {
  let result = worlds.value;
  
  if (activeFilter.value !== "Все") {
    result = result.filter(world => world.category === activeFilter.value);
  }
  
  if (sortBy.value === "popular") {
    result = result.sort((a, b) => b.members - a.members);
  } else if (sortBy.value === "new") {
    result = result.sort((a, b) => b.id - a.id);
  } else if (sortBy.value === "members") {
    result = result.sort((a, b) => b.members - a.members);
  }
  
  return result;
});

const joinWorld = (worldId) => {
  // Здесь будет логика для присоединения к выбранному миру
  console.log(`Присоединяемся к миру с ID: ${worldId}`);
};
</script>

<style scoped>
.planet-container {
  width: 100%;
  height: 100%;
  perspective: 1000px;
  overflow: hidden;
  border-radius: 50%;
  box-shadow: 0 0 20px rgba(0, 255, 157, 0.3);
}

.planet {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  border-radius: 50%;
  position: relative;
  animation: rotate 20s linear infinite;
  transform-style: preserve-3d;
}

.planet-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.1) 0%, rgba(0, 0, 0, 0.4) 100%);
  border-radius: 50%;
}

@keyframes rotate {
  0% {
    transform: rotateY(0deg);
  }
}

.planet-container:hover .planet {
  animation-play-state: paused;
}

.planet-container:hover .planet-overlay {
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.2) 0%, rgba(0, 0, 0, 0.3) 100%);
}
</style>