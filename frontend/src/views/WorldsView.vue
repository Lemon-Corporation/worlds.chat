<template>
  <div
    class="min-h-screen bg-gradient-to-b from-lime-50 via-green-50 to-emerald-50"
  >
    <NavBar />

    <main class="container mx-auto px-4 py-2">
      <h1>s</h1>
      <h1>ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss</h1>
      <h1>ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss</h1>
      <h1
        class="text-3xl md:text-4xl font-bold text-center mb-8 bg-clip-text text-transparent bg-gradient-to-r from-lime-600 via-green-600 to-emerald-600"
      >
        Миры WORLDS
      </h1>

      <!-- Introduction Section -->
      <section class="mb-16">
        <div
          class="max-w-3xl mx-auto bg-white rounded-xl shadow-lg overflow-hidden"
        >
          <div class="p-4 md:p-8">
            <h2 class="text-xl md:text-2xl font-semibold mb-4 text-gray-800">
              Что такое Мир в WORLDS?
            </h2>
            <p class="text-gray-600 mb-4">
              Мир в WORLDS - это уникальное виртуальное пространство, которое вы
              можете создать и настроить под свои нужды. Это больше, чем просто
              чат или форум - это полноценная цифровая экосистема для общения,
              работы и творчества.
            </p>
            <p class="text-gray-600 mb-4">Каждый Мир может включать в себя:</p>
            <ul class="list-disc list-inside text-gray-600 mb-4">
              <li>Многоуровневую структуру каналов и комнат</li>
              <li>3D-навигацию между различными зонами</li>
              <li>Встроенные инструменты для совместной работы</li>
              <li>Систему ролей и разрешений</li>
              <li>Интеграцию с внешними сервисами и приложениями</li>
            </ul>
            <p class="text-gray-600">
              Миры в WORLDS - это новый способ создавать онлайн-сообщества,
              виртуальные офисы, образовательные платформы и многое другое.
              Возможности ограничены только вашим воображением!
            </p>
          </div>
        </div>
      </section>

      <!-- Create Your Own World Section -->
      <section class="mb-16">
        <div
          class="max-w-3xl mx-auto bg-white rounded-xl shadow-lg overflow-hidden"
        >
          <div class="p-4 md:p-8">
            <h2 class="text-xl md:text-2xl font-semibold mb-4 text-gray-800">
              Создайте свой собственный Мир
            </h2>
            <p class="text-gray-600 mb-4">
              В WORLDS вы не ограничены предустановленными шаблонами. Вы можете
              создать свой уникальный Мир, который отражает ваше видение и
              отвечает вашим конкретным потребностям.
            </p>
            <p class="text-gray-600 mb-4">
              Независимо от того, хотите ли вы создать:
            </p>
            <ul class="list-disc list-inside text-gray-600 mb-4">
              <li>Инновационное образовательное пространство</li>
              <li>Виртуальный офис для удаленной команды</li>
              <li>Творческую студию для совместных проектов</li>
              <li>Социальный хаб для вашего сообщества</li>
              <li>Или что-то совершенно новое и уникальное</li>
            </ul>
            <p class="text-gray-600">
              WORLDS предоставит вам инструменты и возможности для воплощения
              вашей идеи в жизнь. Готовьтесь творить и создавать без границ!
            </p>
          </div>
        </div>
      </section>

      <!-- Featured Worlds Concept -->
      <section>
        <h2
          class="text-2xl md:text-3xl font-bold text-center mb-8 text-gray-800"
        >
          Концепции будущих Миров
        </h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-8">
          <div
            v-for="world in conceptWorlds"
            :key="world.name"
            class="bg-white rounded-xl shadow-lg overflow-hidden"
          >
            <div class="p-4 md:p-6">
              <component
                :is="world.icon"
                class="w-10 h-10 md:w-12 md:h-12 text-lime-500 mb-4"
              />
              <h3 class="text-lg md:text-xl font-semibold mb-2 text-gray-800">
                {{ world.name }}
              </h3>
              <p class="text-sm md:text-base text-gray-600">
                {{ world.description }}
              </p>
            </div>
          </div>
        </div>
      </section>
    </main>

    <FooterBar />

    <!-- Subscribe Modal -->
    <teleport to="body">
      <div
        v-if="showSubscribeModal"
        class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4"
      >
        <div class="bg-white rounded-lg p-6 md:p-8 max-w-md w-full">
          <h2 class="text-xl md:text-2xl font-bold mb-4 text-gray-800">
            Подписаться на обновления
          </h2>
          <form @submit.prevent="submitSubscription">
            <div class="mb-4">
              <label for="email" class="block text-gray-700 font-medium mb-2"
                >Email</label
              >
              <input
                v-model="subscriptionEmail"
                type="email"
                id="email"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-lime-500"
                placeholder="your@email.com"
              />
            </div>
            <button
              type="submit"
              class="w-full bg-gradient-to-r from-lime-500 to-green-500 text-white font-bold py-2 px-4 rounded-md hover:from-lime-600 hover:to-green-600 transition-colors"
            >
              Подписаться
            </button>
          </form>
          <button
            @click="showSubscribeModal = false"
            class="mt-4 text-sm text-gray-600 hover:text-lime-600 transition-colors"
          >
            Закрыть
          </button>
        </div>
      </div>
    </teleport>
  </div>
</template>

<script setup>
import { ref } from "vue";
import NavBar from "@/components/NavBar.vue";
import FooterBar from "@/components/FooterBar.vue";
import {
  Rocket,
  Globe,
  Users,
  Briefcase,
  GraduationCap,
  Gamepad,
} from "lucide-vue-next";

const showSubscribeModal = ref(false);
const subscriptionEmail = ref("");

const submitSubscription = () => {
  // Implement subscription logic here
  console.log("Subscribed email:", subscriptionEmail.value);
  // Reset form and close modal
  subscriptionEmail.value = "";
  showSubscribeModal.value = false;
  // Show success message (you can implement this using a modal or toast notification)
  alert(
    "Спасибо за подписку! Мы будем держать вас в курсе последних новостей о WORLDS."
  );
};

const conceptWorlds = [
  {
    name: "Глобальный Кампус",
    description:
      "Образовательная платформа с виртуальными аудиториями, библиотеками и пространствами для совместных проектов.",
    icon: GraduationCap,
  },
  {
    name: "Бизнес Хаб",
    description:
      "Виртуальный офис с конференц-залами, досками для брейнштормов и инструментами для управления проектами.",
    icon: Briefcase,
  },
  {
    name: "Творческая Студия",
    description:
      "Пространство для художников и дизайнеров с галереями, мастерскими и инструментами для совместного творчества.",
    icon: Users,
  },
  {
    name: "Игровая Вселенная",
    description:
      "Мир для геймеров с турнирными аренами, стриминговыми зонами и пространствами для обсуждения игр.",
    icon: Gamepad,
  },
  {
    name: "Глобальный Форум",
    description:
      "Платформа для международных конференций и дискуссий с мгновенным переводом и виртуальными выставочными залами.",
    icon: Globe,
  },
  {
    name: "Научный Коллаборатор",
    description:
      "Виртуальные лаборатории и конференц-залы для ученых, с инструментами для совместных исследований и анализа данных.",
    icon: Rocket,
  },
];
</script>

<style scoped>
/* Add any additional styles here */
</style>
