<template>
  <div
    class="min-h-screen bg-gradient-to-b from-lime-50 via-green-50 to-emerald-50"
  >
    <NavBar />

    <main class="container mx-auto px-4 py-8">
      <h1
        class="text-4xl font-bold text-center mb-8 bg-clip-text text-transparent bg-gradient-to-r from-lime-600 via-green-600 to-emerald-600"
      >
        Центр поддержки WORLDS
      </h1>

      <!-- Search Section -->
      <div class="max-w-2xl mx-auto mb-12">
        <div class="relative">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Поиск по базе знаний..."
            class="w-full px-4 py-2 rounded-full border-2 border-lime-300 focus:outline-none focus:border-lime-500 transition-colors"
          />
          <button
            @click="performSearch"
            class="absolute right-2 top-1/2 transform -translate-y-1/2 bg-lime-500 text-white p-2 rounded-full hover:bg-lime-600 transition-colors"
          >
            <Search class="w-5 h-5" />
          </button>
        </div>
      </div>

      <!-- Quick Links -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
        <div
          v-for="(category, index) in supportCategories"
          :key="index"
          class="bg-white p-6 rounded-xl shadow-md hover:shadow-lg transition-shadow duration-300"
        >
          <component :is="category.icon" class="w-12 h-12 text-lime-500 mb-4" />
          <h2 class="text-xl font-semibold mb-2">{{ category.title }}</h2>
          <p class="text-gray-600 mb-4">{{ category.description }}</p>
          <a
            href="#"
            class="text-lime-600 hover:text-lime-700 font-medium transition-colors"
          >
            Узнать больше <ArrowRight class="inline w-4 h-4 ml-1" />
          </a>
        </div>
      </div>

      <!-- FAQ Section -->
      <div class="mb-12">
        <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">
          Часто задаваемые вопросы
        </h2>
        <div class="max-w-3xl mx-auto">
          <div v-for="(faq, index) in faqs" :key="index" class="mb-4">
            <button
              @click="toggleFaq(index)"
              class="flex justify-between items-center w-full text-left p-4 rounded-lg bg-white shadow-md hover:shadow-lg transition-shadow duration-300"
            >
              <span class="text-lg font-medium text-gray-800">{{
                faq.question
              }}</span>
              <ChevronDown
                :class="{ 'transform rotate-180': faq.isOpen }"
                class="w-5 h-5 text-lime-600 transition-transform duration-300"
              />
            </button>
            <div
              v-show="faq.isOpen"
              class="mt-2 p-4 bg-lime-50 rounded-lg text-gray-700"
            >
              {{ faq.answer }}
            </div>
          </div>
        </div>
      </div>

      <!-- Contact Form -->
      <div class="max-w-2xl mx-auto">
        <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">
          Свяжитесь с нами
        </h2>
        <form
          @submit.prevent="submitForm"
          class="bg-white p-6 rounded-xl shadow-md"
        >
          <div class="mb-4">
            <label for="name" class="block text-gray-700 font-medium mb-2"
              >Имя</label
            >
            <input
              v-model="contactForm.name"
              type="text"
              id="name"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-lime-500"
            />
          </div>
          <div class="mb-4">
            <label for="email" class="block text-gray-700 font-medium mb-2"
              >Email</label
            >
            <input
              v-model="contactForm.email"
              type="email"
              id="email"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-lime-500"
            />
          </div>
          <div class="mb-4">
            <label for="subject" class="block text-gray-700 font-medium mb-2"
              >Тема</label
            >
            <select
              v-model="contactForm.subject"
              id="subject"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-lime-500"
            >
              <option value="">Выберите тему</option>
              <option value="technical">Техническая поддержка</option>
              <option value="billing">Вопросы по оплате</option>
              <option value="feature">Предложение функции</option>
              <option value="other">Другое</option>
            </select>
          </div>
          <div class="mb-4">
            <label for="message" class="block text-gray-700 font-medium mb-2"
              >Сообщение</label
            >
            <textarea
              v-model="contactForm.message"
              id="message"
              rows="4"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-lime-500"
            ></textarea>
          </div>
          <button
            type="submit"
            class="w-full bg-gradient-to-r from-lime-500 to-green-500 text-white font-bold py-2 px-4 rounded-md hover:from-lime-600 hover:to-green-600 transition-colors"
          >
            Отправить
          </button>
        </form>
      </div>
    </main>

    <FooterBar />
  </div>
</template>

<script setup>
import { ref } from "vue";
import NavBar from "@/components/NavBar.vue";
import FooterBar from "@/components/FooterBar.vue";
import {
  Search,
  ArrowRight,
  ChevronDown,
  BookOpen,
  MessageCircle,
  Settings,
  HelpCircle,
  FileText,
  Users,
} from "lucide-vue-next";

const searchQuery = ref("");
const performSearch = () => {
  // Implement search functionality
  console.log("Searching for:", searchQuery.value);
};

const supportCategories = [
  {
    icon: BookOpen,
    title: "Руководства",
    description: "Пошаговые инструкции по использованию WORLDS",
  },
  {
    icon: MessageCircle,
    title: "Сообщество",
    description:
      "Присоединяйтесь к обсуждениям и получайте помощь от других пользователей",
  },
  {
    icon: Settings,
    title: "Настройка аккаунта",
    description: "Управление настройками профиля и безопасности",
  },
  {
    icon: HelpCircle,
    title: "Часто задаваемые вопросы",
    description: "Ответы на популярные вопросы о WORLDS",
  },
  {
    icon: FileText,
    title: "Документация API",
    description: "Техническая документация для разработчиков",
  },
  {
    icon: Users,
    title: "Управление Мирами",
    description: "Советы по созданию и администрированию Миров",
  },
];

const faqs = ref([
  {
    question: "Как создать свой первый Мир?",
    answer:
      'Чтобы создать свой первый Мир, войдите в аккаунт и нажмите кнопку "Создать Мир" на главной странице. Следуйте инструкциям мастера создания, выберите шаблон и настройте основные параметры.',
    isOpen: false,
  },
  {
    question: "Как работает система мгновенного перевода?",
    answer:
      "Система мгновенного перевода использует передовые AI-технологии для автоматического перевода сообщений в реальном времени. Вы можете выбрать свой родной язык в настройках, и все сообщения будут автоматически переводиться.",
    isOpen: false,
  },
  {
    question: "Какие ограничения есть в бесплатной версии?",
    answer:
      "Бесплатная версия WORLDS позволяет создать до 3 Миров с ограничением в 100 участников каждый. Также доступны базовые инструменты для коммуникации и совместной работы. Для расширенных возможностей рекомендуем ознакомиться с нашими платными планами.",
    isOpen: false,
  },
  {
    question: "Как обеспечивается безопасность данных в WORLDS?",
    answer:
      "Мы используем передовые технологии шифрования для защиты всех данных пользователей. Все коммуникации защищены протоколом SSL/TLS, а хранимые данные зашифрованы. Мы также регулярно проводим аудиты безопасности и следуем лучшим практикам в области защиты данных.",
    isOpen: false,
  },
]);

const toggleFaq = (index) => {
  faqs.value[index].isOpen = !faqs.value[index].isOpen;
};

const contactForm = ref({
  name: "",
  email: "",
  subject: "",
  message: "",
});

const submitForm = () => {
  // Implement form submission logic here
  console.log("Form submitted:", contactForm.value);
  // Reset form after submission
  contactForm.value = {
    name: "",
    email: "",
    subject: "",
    message: "",
  };
  // Show success message (you can implement this using a modal or toast notification)
  alert("Ваше сообщение отправлено. Мы свяжемся с вами в ближайшее время.");
};
</script>

<style scoped>
/* Add any additional styles here */
</style>
