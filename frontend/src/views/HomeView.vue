<template>
  <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950">
    <nav class="border-b border-purple-500/20 backdrop-blur-md bg-gray-900/50 w-full fixed top-0 z-50">
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
            <button
              @click="$router.push('/auth/sign-in')"
              class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium py-2 px-4 rounded-md transition-colors duration-200 flex items-center gap-2"
            >
              <span class="hidden sm:inline">Войти</span>
            </button>
          </div>
        </div>
      </div>
    </nav>

    <section class="pt-32 pb-16 md:pt-40 md:pb-20 container mx-auto px-4 relative overflow-hidden">
      <div class="max-w-4xl mx-auto text-center relative z-10">
        <h1 class="text-4xl md:text-6xl font-bold leading-tight mb-6 text-white">
          Создавайте свои
          <span class="bg-clip-text text-transparent bg-gradient-to-r from-[#00ff9d] via-[#00cc7d] to-[#009f62]">
            Миры
          </span>
          в Безграничной Песочнице!
        </h1>
        <p class="text-xl text-gray-300 mb-8">
          WORLDS - это революционная платформа-песочница, где вы можете создавать полноценные миры для общения, работы и творчества. Голосовые каналы, видеовстречи, управление задачами - все это и многое другое с максимальной настраиваемостью!
        </p>
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <button @click="$router.push('/auth/sign-in')" class="px-6 py-3 text-lg  bg-[#00cc7d] hover:bg-[#00cc7d] text-gray-900 font-medium rounded-md transition-colors shadow-lg  transform">
            Создать свой Мир
          </button>
          <button @click="scrollToFeatures" class="px-6 py-3 text-lg border border-[#00ff9d] text-[#00ff9d] hover:bg-[#00ff9d]/10 font-medium rounded-md transition-colors">
            Узнать больше
          </button>
        </div>
      </div>

      <div class="mt-16 relative">
        <div class="relative mx-auto max-w-5xl bg-gray-900/80 rounded-xl shadow-2xl overflow-hidden border border-purple-500/20">
          <div class="p-8">
            <div class="flex flex-col md:flex-row justify-between items-center mb-8">
              <div class="flex items-center space-x-4 mb-4 md:mb-0">
                <div class="w-12 h-12 bg-gradient-to-br from-[#00ff9d] to-[#00cc7d] rounded-full flex items-center justify-center">
                  <Globe2 class="w-6 h-6 text-gray-900" />
                </div>
                <div>
                  <h3 class="text-xl font-semibold text-[#00ff9d]">
                    Мир: Творческая Мастерская
                  </h3>
                  <p class="text-gray-400">
                    500 участников • Безграничные возможности
                  </p>
                </div>
              </div>
              <button @click="$router.push('/auth/sign-in')" class="px-4 py-2 border border-[#00ff9d] text-[#00ff9d] rounded-md hover:bg-[#00ff9d]/10 transition-colors flex items-center">
                Присоединиться <ArrowRight class="ml-2 w-4 h-4" />
              </button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div class="md:col-span-2 bg-gray-800/60 rounded-lg p-4">
                <h4 class="font-semibold mb-2 text-[#00ff9d]">Совместной Работа</h4>
                <div class="aspect-video bg-gray-700/60 rounded-lg flex items-center justify-center relative">
                  <video
                    v-if="isVideoPlaying"
                    ref="videoRef"
                    class="w-full h-full object-cover rounded-lg"
                    autoplay
                    loop
                    muted
                  >
                    <source src="/placeholder.mp4" type="video/mp4" />
                    Ваш браузер не поддерживает видео тег.
                  </video>
                  <Video v-else class="w-12 h-12 text-[#00ff9d]" />
                </div>
              </div>
              <div class="space-y-4">
                <div class="bg-gray-800/60 rounded-lg p-4">
                  <h4 class="font-semibold mb-2 text-[#00ff9d]">Чат и Задачи</h4>
                  <div class="space-y-2">
                    <div class="flex items-center space-x-2">
                      <div class="w-8 h-8 bg-[#00ff9d] rounded-full"></div>
                      <p class="text-sm text-gray-300">Новая идея для проекта!</p>
                    </div>
                    <div class="flex items-center space-x-2">
                      <div class="w-8 h-8 bg-[#00cc7d] rounded-full"></div>
                      <p class="text-sm text-gray-300">Задача: Создать макет</p>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-800/60 rounded-lg p-4">
                  <h4 class="font-semibold mb-2 text-[#00ff9d]">Активные каналы</h4>
                  <ul class="space-y-2 text-sm">
                    <li
                      v-for="channel in activeChannels"
                      :key="channel.name"
                      class="flex items-center space-x-2"
                    >
                      <component
                        :is="channel.icon"
                        class="w-4 h-4"
                        :class="channel.iconColor"
                      />
                      <span class="text-gray-300">{{ channel.name }}</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="absolute bottom-4 left-4 right-4 bg-gradient-to-r from-[#00ff9d] via-[#00cc7d] to-[#009f62] text-gray-900 p-4 rounded-lg">
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-4">
                <Mic class="w-6 h-6" />
                <Video class="w-6 h-6" />
                <Layers class="w-6 h-6" />
              </div>
              <p class="text-sm font-medium">
                Голосовой чат, Видеовстреча
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="features" class="py-20 bg-gray-900/60">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-16 bg-clip-text text-transparent bg-gradient-to-r from-[#00ff9d] via-[#00cc7d] to-[#009f62]">
          Безграничные возможности Песочницы WORLDS
        </h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
            v-for="(feature, index) in features"
            :key="index"
            class="p-6 rounded-xl border border-purple-500/20 bg-gray-800/60 hover:shadow-lg transition-all duration-300 group"
          >
            <div class="w-12 h-12 rounded-full bg-gradient-to-br from-[#00ff9d] via-[#00cc7d] to-[#009f62] flex items-center justify-center mb-4 group-hover:from-[#00cc7d] group-hover:via-[#009f62] group-hover:to-[#007248] transition-colors duration-300">
              <component :is="feature.icon" class="w-8 h-8 text-gray-900" />
            </div>
            <h3 class="text-xl font-semibold mb-2 text-[#00ff9d] group-hover:text-[#00cc7d] transition-colors duration-300">
              {{ feature.title }}
            </h3>
            <p class="text-gray-300">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <section id="worlds" class="py-20 bg-gray-900/40">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-16 bg-clip-text text-transparent bg-gradient-to-r from-[#00ff9d] via-[#00cc7d] to-[#009f62]">
          Исследуйте уникальные Миры
        </h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
            v-for="(world, index) in worlds"
            :key="index"
            class="p-6 rounded-xl border border-purple-500/20 bg-gray-800/60 hover:shadow-lg transition-all duration-300 group"
          >
            <div class="flex items-center justify-between mb-4">
              <div class="w-12 h-12 rounded-full bg-gradient-to-br from-[#00ff9d]/20 to-[#00cc7d]/20 flex items-center justify-center">
                <component
                  :is="world.icon"
                  class="w-8 h-8"
                  :class="world.iconColor"
                />
              </div>
              <div class="text-sm text-gray-400">
                <span class="font-semibold text-[#00ff9d]">{{
                  world.members.toLocaleString()
                }}</span>
                участников
              </div>
            </div>
            <h3 class="text-xl font-semibold mb-2 text-[#00ff9d] group-hover:text-[#00cc7d] transition-colors duration-300">
              {{ world.name }}
            </h3>
            <p class="text-gray-300 mb-4">{{ world.description }}</p>
            <div class="flex justify-between items-center">
              <span class="text-sm text-gray-400">{{ world.channels }} каналов</span>
              <button @click="$router.push('/auth/sign-in')" class="px-3 py-1 text-sm text-[#00ff9d] border border-[#00ff9d] rounded-md hover:bg-[#00ff9d]/10 transition-colors">
                Исследовать
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer class="bg-gray-900 py-12 border-t border-purple-500/20">
      <div class="container mx-auto px-4">
        <div class="grid md:grid-cols-4 gap-8">
          <div>
            <h3 class="text-xl font-bold text-[#00ff9d] mb-4">WORLDS</h3>
            <p class="text-gray-400">Создавайте уникальные миры для общения, работы и творчества.</p>
          </div>
          <div>
            <h4 class="text-lg font-semibold text-[#00ff9d] mb-4">Навигация</h4>
            <ul class="space-y-2">
              <li><a href="/" class="text-gray-400 hover:text-[#00ff9d] transition-colors">Главная</a></li>
              <li><a href="/app" class="text-gray-400 hover:text-[#00ff9d] transition-colors">Запуск</a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-lg font-semibold text-[#00ff9d] mb-4">Ресурсы</h4>
            <ul class="space-y-2">
              <li><a href="lemon-corporation.com" class="text-gray-400 hover:text-[#00ff9d] transition-colors">Lemon Corporation</a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-lg font-semibold text-[#00ff9d] mb-4">Подписаться на новости</h4>
            <form @submit.prevent="subscribeNewsletter" class="flex">
              <input
                type="email"
                v-model="newsletterEmail"
                placeholder="Ваш email"
                class="bg-gray-800 text-white px-4 py-2 rounded-l-md focus:outline-none focus:ring-2 focus:ring-[#00ff9d]"
              />
              <button
                type="submit"
                class="bg-[#00ff9d] text-gray-900 px-4 py-2 rounded-r-md hover:bg-[#00cc7d] transition-colors"
              >
                Подписаться
              </button>
            </form>
          </div>
        </div>
        <div class="mt-8 pt-8 border-t border-gray-800 text-center">
          <p class="text-gray-400">&copy; 2024 WORLDS. Все права защищены.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from "vue";
import {
  Globe2,
  ArrowRight,
  Video,
  Hash,
  Mic,
  Layers,
  Palette,
  Bot,
  Cpu,
  Music,
  Share2,
  User,
} from "lucide-vue-next";

const navigation = [
  { name: "Исследуйте миры... Они ведут к нужному пути!", href: "/", current: true },
];

const isVideoPlaying = ref(false);
const newsletterEmail = ref("");

const activeChannels = [
  { name: "Мозговой штурм", icon: Hash, iconColor: "text-[#00ff9d]" },
  { name: "Дизайн-студия", icon: Video, iconColor: "text-[#00cc7d]" },
  { name: "Проектный чат", icon: Hash, iconColor: "text-[#009f62]" },
];

const features = [
  {
    icon: Layers,
    title: "Многоуровневая структура",
    description:
      "Создавайте сложные иерархии каналов, ролей и разрешений для идеальной организации вашего Мира.",
  },
  {
    icon: Palette,
    title: "Полная кастомизация",
    description:
      "Настраивайте внешний вид, функциональность и поведение каждого элемента вашего Мира.",
  },
  {
    icon: Bot,
    title: "AI-ассистенты",
    description:
      "Создавайте умных помощников для модерации, обучения и развлечения участников вашего Мира.",
  },
  {
    icon: Cpu,
    title: "Встроенные приложения",
    description:
      "Разрабатывайте и интегрируйте собственные приложения прямо внутри вашего Мира.",
  },
  {
    icon: Music,
    title: "ИИ перевод аудио",
    description:
      "Общайтесь и переводите свою речь на все языки мира для снятия барьеров!",
  },
  {
    icon: Share2,
    title: "Децентрализациия",
    description:
      "Компании могут децентрализованно запускать нашу платформу и работать в ней!",
  },
];

const worlds = [
  {
    icon: Cpu,
    iconColor: "text-[#00ff9d]",
    name: "Тестовый мир",
    description:
      "Мир созданный разработчиками для тестирования платформы",
    members: 10,
    channels: 12,
  },
  {
    icon: Palette,
    iconColor: "text-[#00cc7d]",
    name: "Творческая мастерская",
    description:
      "Пространство для художников, дизайнеров и креативщиков",
    members: 500,
    channels: 25,
  },
  {
    icon: Bot,
    iconColor: "text-[#009f62]",
    name: "AI Лаборатория",
    description:
      "Исследуйте и разрабатывайте AI вместе с единомышленниками",
    members: 250,
    channels: 18,
  },
];

const testimonials = [
  {
    name: "Анна С.",
    role: "Дизайнер",
    comment: "WORLDS открыл для меня новые возможности в совместной работе над проектами. Это намного больше, чем просто платформа для общения!",
  },
  {
    name: "Михаил Р.",
    role: "Разработчик",
    comment: "Возможность создавать собственные приложения внутри платформы - это просто фантастика. WORLDS действительно безграничен в своих возможностях.",
  },
  {
    name: "Елена К.",
    role: "Менеджер проектов",
    comment: "Благодаря WORLDS наша команда стала работать эффективнее. Удобные инструменты для управления задачами и коммуникации в одном месте - это именно то, что нам было нужно.",
  },
];

const scrollToFeatures = () => {
  const featuresSection = document.getElementById('features');
  if (featuresSection) {
    featuresSection.scrollIntoView({ behavior: 'smooth' });
  }
};

const subscribeNewsletter = () => {
  // Здесь будет логика подписки на рассылку
  console.log('Подписка на рассылку:', newsletterEmail.value);
  newsletterEmail.value = '';
};
</script>

<style scoped>
@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
  }
}

@media (min-width: 1536px) {
  .container {
    max-width: 1400px;
  }
}
</style>