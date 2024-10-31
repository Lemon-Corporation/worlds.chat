<template>
  <nav
    class="fixed top-0 w-full bg-white/80 backdrop-blur-md z-50 border-b border-lime-200 transition-all duration-300"
    :class="{ 'shadow-lg': scrolled }"
  >
    <div class="container mx-auto px-4 py-4">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-8">
          <a
            href="#"
            class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-lime-500 via-green-500 to-emerald-500 hover:from-lime-600 hover:via-green-600 hover:to-emerald-600 transition-colors"
          >
            WORLDS
          </a>
          <div class="hidden lg:flex space-x-6">
            <a
              v-for="link in navLinks"
              :key="link.href"
              :href="link.href"
              class="text-gray-600 hover:text-lime-700 transition-colors relative group"
            >
              {{ link.text }}
              <span
                class="absolute left-0 bottom-0 w-full h-0.5 bg-lime-500 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300"
              ></span>
            </a>
          </div>
        </div>
        <div class="flex items-center space-x-4">
          <button
            @click="clcktest()"
            class="px-4 py-2 border border-lime-300 rounded-md hover:bg-lime-100 transition-colors text-lime-700 hover:text-lime-800"
          >
            Войти
          </button>
          <button
            @click="toggleMobileMenu"
            class="lg:hidden p-2 rounded-md hover:bg-lime-100 transition-colors"
          >
            <Menu v-if="!isMobileMenuOpen" class="w-6 h-6 text-lime-600" />
            <X v-else class="w-6 h-6 text-lime-600" />
          </button>
        </div>
      </div>
    </div>
    <transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="transform -translate-y-full opacity-0"
      enter-to-class="transform translate-y-0 opacity-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="transform translate-y-0 opacity-100"
      leave-to-class="transform -translate-y-full opacity-0"
    >
      <div
        v-if="isMobileMenuOpen"
        class="lg:hidden bg-white border-t border-lime-200"
      >
        <div class="container mx-auto px-4 py-4">
          <a
            v-for="link in navLinks"
            :key="link.href"
            :href="link.href"
            class="block py-2 text-gray-600 hover:text-lime-700 transition-colors"
            @click="toggleMobileMenu"
          >
            {{ link.text }}
          </a>
        </div>
      </div>
    </transition>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { Menu, X } from "lucide-vue-next";
import { useRouter } from "vue-router";

const router = useRouter();
const isMobileMenuOpen = ref(false);
const scrolled = ref(false);

const navLinks = [
  { href: "/worlds", text: "Миры" },
  { href: "/support-center", text: "Центр поддрежки" },
  { href: "#technology", text: "Технологии" },
  { href: "https://lemon-coporation.com/ru", text: "О нас" },
];

const clcktest = () => {
  router.push("/auth/sign-in");
};

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};

const handleScroll = () => {
  scrolled.value = window.scrollY > 20;
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>

<style scoped>
/* Add any additional styles here */
</style>
