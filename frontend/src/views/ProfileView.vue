<template>
  <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950">
    <!-- Верхняя навигация -->
    <NavBar/>
    <!-- Основной контент -->
    <div class="container mx-auto px-4 py-8">
      <div v-if="!user" class="flex justify-center items-center h-64">
        <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-[#00ff9d]"></div>
      </div>
      <div v-else-if="error" class="bg-red-500/20 text-red-100 p-4 rounded-lg">
        {{ error }}
      </div>
      <div v-else class="bg-gray-800 rounded-lg shadow-xl overflow-hidden">
        <!-- Баннер профиля -->
        <div class="h-48 bg-gradient-to-r from-purple-600 to-blue-600 relative">
          <img
            :src="user.banner_url || 'https://via.placeholder.com/1200x400'"
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
                :src="user.profile_pic_url || 'https://via.placeholder.com/150'"
                :alt="user.username"
                class="w-full h-full object-cover"
              />
            </div>

            <!-- Информация о пользователе -->
            <div class="mt-4 md:mt-0 flex-grow">
              <h1 class="text-3xl font-bold text-[#00ff9d]">{{ user.username }}</h1>
              <p class="text-gray-400">{{ user.email }}</p>
            </div>

            <!-- Кнопки действий -->
            <div class="mt-4 md:mt-0 flex space-x-2">
              <button @click="openEditProfileModal" class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-bold py-2 px-4 rounded transition-colors duration-200">
                Редактировать профиль
              </button>
            </div>
          </div>

          <!-- Биография -->
          <div class="mt-6">
            <h2 class="text-xl font-bold text-[#00ff9d] mb-2">О себе</h2>
            <p class="text-gray-300">{{ user.bio || 'Биография пользователя не заполнена' }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Модальное окно редактирования профиля -->
    <div v-if="showEditProfileModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-gray-800 p-6 rounded-lg w-full max-w-md">
        <h2 class="text-2xl font-bold text-[#00ff9d] mb-4">Редактировать профиль</h2>
        <form @submit.prevent="updateProfile">
          <div class="mb-4">
            <label for="username" class="block text-gray-300 mb-2">Имя пользователя</label>
            <input v-model="editForm.username" id="username" type="text" class="w-full bg-gray-700 text-white rounded px-3 py-2">
          </div>
          <div class="mb-4">
            <label for="bio" class="block text-gray-300 mb-2">О себе</label>
            <textarea v-model="editForm.bio" id="bio" class="w-full bg-gray-700 text-white rounded px-3 py-2" rows="4"></textarea>
          </div>
          <div class="mb-4">
            <label for="banner_url" class="block text-gray-300 mb-2">URL баннера</label>
            <input v-model="editForm.banner_url" id="banner_url" type="text" class="w-full bg-gray-700 text-white rounded px-3 py-2">
          </div>
          <div class="mb-4">
            <label for="profile_pic_url" class="block text-gray-300 mb-2">URL аватарки</label>
            <input v-model="editForm.profile_pic_url" id="profile_pic_url" type="text" class="w-full bg-gray-700 text-white rounded px-3 py-2">
          </div>
          <div class="flex justify-end">
            <button type="button" @click="closeEditProfileModal" class="mr-2 px-4 py-2 bg-gray-600 text-white rounded">Отмена</button>
            <button type="submit" class="px-4 py-2 bg-[#00ff9d] text-gray-900 rounded">Сохранить</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import NavBar from '@/components/NavBar.vue';
import axios from 'axios';

const store = useStore();
const error = ref(null);

const user = computed(() => store.getters['auth/getUser']);
const accessToken = store.getters['auth/getAccessToken'];

const showEditProfileModal = ref(false);

const editForm = ref({
  username: '',
  bio: '',
  profile_pic_url: '',
});

const getProfile = async () => {
  try {
    const response = await axios.get('http://localhost:8000/user/me', {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });
    store.commit('auth/SET_USER', response.data);
  } catch (err) {
    console.error('Error fetching profile:', err);
    error.value = 'Произошла ошибка при получении профиля. Пожалуйста, попробуйте позже.';
  }
};

const openEditProfileModal = () => {
  editForm.value.username = user.value.username;
  editForm.value.profile_pic_url = user.value.profile_pic_url || ''
  editForm.value.banner_url = user.value.banner_url || ''
  editForm.value.bio = user.value.bio || '';
  showEditProfileModal.value = true;
};

const closeEditProfileModal = () => {
  showEditProfileModal.value = false;
};

const updateProfile = async () => {
  try {
    const response = await axios.patch('http://localhost:8000/user/', editForm.value, {
      headers: {
        Authorization: `Bearer ${accessToken.value}`,
      },
    });
    store.commit('auth/SET_USER', { ...user.value, ...response.data });
    closeEditProfileModal();
  } catch (err) {
    console.error('Error updating profile:', err);
    error.value = 'Произошла ошибка при обновлении профиля. Пожалуйста, попробуйте позже.';
  }
};

onMounted(async () => {
  await getProfile();
});
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
