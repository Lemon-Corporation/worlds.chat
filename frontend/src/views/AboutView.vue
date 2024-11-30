<template>
  <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950">
    <!-- Верхняя навигация -->
    <NavBar/>

    <!-- Основной контент -->
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-4xl font-bold text-[#00ff9d] mb-8">Мои Миры</h1>

      <!-- Сетка миров -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        <div v-for="world in worlds" :key="world.id" class="flex flex-col items-center">
          <div class="relative w-48 h-48 mb-4 group">
            <div class="absolute inset-0 rounded-full overflow-hidden shadow-lg transition-transform duration-300 group-hover:transform group-hover:scale-110">
              <img :src="world.icon" :alt="world.name" class="w-full h-full object-cover" />
            </div>
            <div class="absolute inset-0 bg-black bg-opacity-40 rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
              <button @click="openWorld(world.id)" class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium px-4 py-2 rounded-full transition-colors duration-200">
                Открыть
              </button>
            </div>
          </div>
          <div class="bg-gray-800 rounded-lg p-4 w-full text-center">
            <h2 class="text-xl font-bold text-[#00ff9d] mb-2">{{ world.name }}</h2>
            <p class="text-gray-300 mb-2 h-12 overflow-hidden">{{ world.description }}</p>
            <span class="text-sm text-[#00ff9d]">{{ world.members }} участников</span>
          </div>
        </div>

        <!-- Карточка для создания нового мира -->
        <div @click="showCreateWorldModal = true" class="flex flex-col items-center cursor-pointer">
          <div class="relative w-48 h-48 mb-4 group">
            <div class="absolute inset-0 rounded-full overflow-hidden bg-purple-500/20 flex items-center justify-center transition-transform duration-300 group-hover:transform group-hover:scale-110">
              <Plus class="w-16 h-16 text-[#00ff9d]" />
            </div>
          </div>
          <div class="bg-gray-800 rounded-lg p-4 w-full text-center">
            <h2 class="text-xl font-bold text-[#00ff9d] mb-2">Создать новый мир</h2>
            <p class="text-gray-300 mb-2 h-12">Начните свое новое приключение</p>
            <span class="text-sm text-[#00ff9d]">Нажмите, чтобы создать</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Модальное окно создания мира -->
    <div v-if="showCreateWorldModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gray-900 border border-purple-500/20 rounded-lg w-full max-w-md p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-[#00ff9d] text-xl font-bold">Создать Новый Мир</h2>
          <button @click="showCreateWorldModal = false" class="text-gray-400 hover:text-[#00ff9d] transition-colors duration-200">
            <X class="w-5 h-5" />
          </button>
        </div>
        <form @submit.prevent="createWorld" class="space-y-4">
          <div>
            <label for="worldName" class="block text-gray-300 text-sm font-medium mb-2">Название Мира</label>
            <input
              id="worldName"
              v-model="newWorld.name"
              type="text"
              class="w-full bg-gray-800 border border-purple-500/20 rounded-md px-3 py-2 text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] transition-colors duration-200"
              placeholder="Введите название мира"
            />
          </div>
          <div>
            <label for="worldDescription" class="block text-gray-300 text-sm font-medium mb-2">Описание</label>
            <textarea
              id="worldDescription"
              v-model="newWorld.description"
              rows="3"
              class="w-full bg-gray-800 border border-purple-500/20 rounded-md px-3 py-2 text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] transition-colors duration-200"
              placeholder="Опишите ваш мир"
            ></textarea>
          </div>
          <div>
            <label class="block text-gray-300 text-sm font-medium mb-2">Иконка Мира</label>
            <div class="grid grid-cols-3 gap-4">
              <button
                v-for="(icon, index) in worldIcons"
                :key="index"
                type="button"
                @click="newWorld.icon = icon"
                :class="[
                  'p-2 rounded-full transition-all duration-200',
                  newWorld.icon === icon ? 'border-2 border-[#00ff9d]' : 'border-2 border-transparent'
                ]"
              >
                <img :src="icon" :alt="'Иконка мира ' + (index + 1)" class="w-12 h-12 rounded-full" />
              </button>
            </div>
          </div>
          <div class="flex justify-end gap-3 mt-6">
            <button
              type="button"
              @click="showCreateWorldModal = false"
              class="px-4 py-2 text-gray-400 hover:text-gray-300 transition-colors duration-200"
            >
              Отмена
            </button>
            <button
              type="submit"
              class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium px-4 py-2 rounded-md transition-colors duration-200"
            >
              Создать Мир
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';
import { AtSign, Bell, Plus, X } from 'lucide-vue-next';
import { useRouter } from 'vue-router';
import NavBar from '@/components/NavBar.vue';

const router = useRouter();
const store = useStore();

const worldIcons = [
  "https://i.imgur.com/dlFRtHv.png",
  "https://i.imgur.com/oPPTj4b.png",
  "https://i.imgur.com/w2LCHjF.png"
];

const worlds = ref([]);

const fetchAvailableWorlds = async () => {
  const accessToken = store.getters['auth/getAccessToken'];

  try {
    // Fetch user worlds
    const worldsResponse = await axios.get('http://localhost:8000/user/worlds', {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'accept': 'application/json'
      }
    });

    const allWorlds = worldsResponse.data.worlds;
   

    // Ensure unique IDs and correct categorization
    const mainWorlds = allWorlds.filter(world => world.partner_id === null);
    const categoryWorlds = allWorlds.filter(world => world.partner_id !== null);

    // Fetch all channels
    const channelsResponse = await axios.get('http://localhost:8000/channels/all?page=1&per_page=40', {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'accept': 'application/json'
      }
    });

    const allChannels = channelsResponse.data.channels;

    // Create a map to easily find parent worlds by id
    const worldMap = new Map();
    mainWorlds.forEach(world => {
      worldMap.set(world.id, {
        id: world.id,
        name: world.name,
        icon: world.icon_url,
        expanded: false,
        notifications: false,
        categories: [],
        channels: [], // Initialize channels array
      });
    });

    // Convert map back to an array for worlds ref
    worlds.value = Array.from(worldMap.values());
  } catch (error) {
    console.error('Failed to fetch available worlds and channels:', error);
  }
};


fetchAvailableWorlds();

const showCreateWorldModal = ref(false);
const newWorld = ref({
  name: '',
  description: '',
  icon: worldIcons[0]
});

const createWorld = () => {
  const worldId = Math.max(...worlds.value.map(w => w.id)) + 1;
  worlds.value.push({
    id: worldId,
    name: newWorld.value.name,
    description: newWorld.value.description,
    icon: newWorld.value.icon,
    members: 1 // Начинаем с создателя мира
  });
  showCreateWorldModal.value = false;
  newWorld.value = { name: '', description: '', icon: worldIcons[0] };
};

const openWorld = (worldId) => {
  // Здесь будет логика для открытия выбранного мира
  router.push("/app");
  console.log(`Открываем мир с ID: ${worldId}`);
};
</script>
