<template>
  <nav class="border-b border-purple-500/20 backdrop-blur-md bg-gray-900/50 w-full">
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <span class="text-[#00ff9d] text-xl sm:text-2xl font-bold font-mono"><a href="/app">WORLDS</a></span>
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
              @click="$router.push(item.href)"
              @click.prevent="setCurrentNavItem(item.name)"
            >
              {{ item.name }}
            </a>
          </div>
        </div>
        <div class="flex items-center gap-2 sm:gap-4">
          <button v-if="isAuthenticated" @click="openMentionsModal" class="text-gray-300 hover:text-[#00ff9d] transition-colors duration-200 hidden sm:block">
            <AtSign class="w-5 h-5 sm:w-6 sm:h-6" />
          </button>
          <button v-if="isAuthenticated" @click="openNotificationModal" class="text-gray-300 hover:text-[#00ff9d] transition-colors duration-200 hidden sm:block">
            <Bell class="w-5 h-5 sm:w-6 sm:h-6" />
          </button>
          <div v-if="isAuthenticated" class="relative">
            <a href="/profile">
              <img
                class="h-8 w-8 rounded-full bg-purple-500/20"
                :src="userAvatar"
                alt="Аватар пользователя"
              />
            </a>
            <span
              class="absolute bottom-0 right-0 block h-2 w-2 rounded-full bg-[#00ff9d] ring-2 ring-gray-900"
            ></span>
          </div>
          <a
            v-else
            href="/auth/sign-in"
            class="text-gray-300 hover:text-[#00ff9d] transition-colors duration-200 px-3 py-2 rounded-md text-sm font-medium"
            @click="$router.push(item.href)"
            @click.prevent="$router.push('/auth/sign-in')"
          >
            Войти
          </a>
          <button @click="toggleMobileMenu" class="text-gray-300 hover:text-[#00ff9d] transition-colors duration-200 md:hidden">
            <Menu class="w-6 h-6" />
          </button>
        </div>
      </div>
    </div>
  </nav>

  <teleport to="body">
    <transition name="fade">
      <div v-if="mobileMenuOpen" class="fixed inset-0 bg-gray-900/50 backdrop-blur-sm z-50">
        <div class="flex justify-end p-4">
          <button @click="toggleMobileMenu" class="text-gray-300 hover:text-[#00ff9d] transition-colors duration-200">
            <X class="w-6 h-6" />
          </button>
        </div>
        <div class="flex flex-col items-center space-y-4 p-4">
          <a
            v-for="item in navigation"
            :key="item.name"
            :href="item.href"
            :class="[
              item.current
                ? 'bg-purple-500/20 text-[#00ff9d]'
                : 'text-gray-300 hover:bg-purple-500/10 hover:text-[#00ff9d]',
              'px-3 py-2 rounded-md text-lg font-medium transition-colors duration-200 w-full text-center',
            ]"
            @click="$router.push(item.href)"
            @click.prevent="setCurrentNavItem(item.name)"
          >
            {{ item.name }}
          </a>
          <div v-if="isAuthenticated" class="flex space-x-4 mt-4">
            <button @click="openMentionsModal" class="text-gray-300 hover:text-[#00ff9d] transition-colors duration-200">
              <AtSign class="w-6 h-6" />
            </button>
            <button @click="openNotificationModal" class="text-gray-300 hover:text-[#00ff9d] transition-colors duration-200">
              <Bell class="w-6 h-6" />
            </button>
          </div>
          <a
            v-else
            href="/auth/sign-in"
            class="text-gray-300 hover:text-[#00ff9d] transition-colors duration-200 px-3 py-2 rounded-md text-lg font-medium w-full text-center"
            @click.prevent="$router.push('/auth/sign-in')"
          >
            Войти
          </a>
        </div>
      </div>
    </transition>
  </teleport>

  <NotificationModal :show="showNotificationModal" @close="closeNotificationModal" />
  <MentionsModal :show="showMentionsModal" @close="closeMentionsModal" />
</template>

<script setup>
import { ref, computed } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import {
  AtSign,
  Bell,
  Menu,
  X
} from "lucide-vue-next";
import NotificationModal from './NotificationModal.vue';
import MentionsModal from './MentionsModal.vue';

const store = useStore();
const router = useRouter();

const navigation = ref([
  { name: "Миры", href: "/app", current: true },
  { name: "Сообщения", href: "/messages", current: false },
  { name: "Обзор", href: "/top/worlds", current: false },
  { name: "Боты", href: "/worlds/bots", current: false },
]);

const mobileMenuOpen = ref(false);
const showNotificationModal = ref(false);
const showMentionsModal = ref(false);

const isAuthenticated = computed(() => store.getters['auth/isAuthenticated']);
const userAvatar = computed(() => store.getters['auth/getUser']?.avatar || 'https://i.pinimg.com/736x/26/71/0c/26710c62610833284e41ac25ad166700.jpg');

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value;
};

const openNotificationModal = () => {
  showNotificationModal.value = true;
};

const closeNotificationModal = () => {
  showNotificationModal.value = false;
};

const openMentionsModal = () => {
  showMentionsModal.value = true;
};

const closeMentionsModal = () => {
  showMentionsModal.value = false;
};

const setCurrentNavItem = (name) => {
  navigation.value.forEach(item => {
    item.current = item.name === name;
  });
  if (mobileMenuOpen.value) {
    toggleMobileMenu();
  }
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-active {
  opacity: 0;
}
</style>