<template>
  <div
    class="min-h-screen bg-gradient-to-b from-lime-50 via-green-50 to-emerald-50"
  >
    <NavBar />
    <!-- Hero Section -->
    <HelloWorld />
    <section
      class="pt-32 pb-16 md:pt-40 md:pb-20 container mx-auto px-4 relative overflow-hidden"
    >
      <div class="max-w-4xl mx-auto text-center relative z-10">
        <h1 class="text-4xl md:text-6xl font-bold leading-tight mb-6">
          Создавайте свои
          <span
            class="bg-clip-text text-transparent bg-gradient-to-r from-lime-500 via-green-500 to-emerald-500"
          >
            Миры </span
          >!
        </h1>
        <p class="text-xl text-gray-700 mb-8">
          WORLDS - это революционная платформа, где каждый Мир подобен серверу
          Discord, но с безграничными возможностями настройки, расширений и
          инноваций. Создавайте уникальные пространства для общения, работы и
          творчества без языковых барьеров.
        </p>
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <button
            class="px-6 py-3 text-lg bg-gradient-to-r from-lime-500 via-green-500 to-emerald-500 text-white rounded-md hover:from-lime-600 hover:via-green-600 hover:to-emerald-600 transition-colors shadow-lg hover:shadow-xl transform hover:-translate-y-1"
          >
            Создать свой Мир
          </button>
        </div>
      </div>

      <!-- Animated Preview -->
      <div class="mt-16 relative">
        <div
          class="relative mx-auto max-w-5xl bg-white rounded-xl shadow-2xl overflow-hidden border border-lime-200"
        >
          <div class="p-8">
            <div
              class="flex flex-col md:flex-row justify-between items-center mb-8"
            >
              <div class="flex items-center space-x-4 mb-4 md:mb-0">
                <div
                  class="w-12 h-12 bg-gradient-to-br from-lime-500 to-green-500 rounded-full flex items-center justify-center"
                >
                  <Globe2 class="w-6 h-6 text-white" />
                </div>
                <div>
                  <h3 class="text-xl font-semibold">
                    Мир: Глобальная Конференция
                  </h3>
                  <p class="text-gray-500">
                    250 участников • 5 языков • 3 измерения
                  </p>
                </div>
              </div>
              <button
                class="px-4 py-2 border border-lime-300 rounded-md hover:bg-lime-100 transition-colors flex items-center"
              >
                Присоединиться <ArrowRight class="ml-2 w-4 h-4" />
              </button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div class="md:col-span-2 bg-lime-50 rounded-lg p-4">
                <h4 class="font-semibold mb-2">3D Конференц-зал</h4>
                <div
                  class="aspect-video bg-lime-100 rounded-lg flex items-center justify-center relative"
                >
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
                  <Video v-else class="w-12 h-12 text-lime-400" />
                </div>
              </div>
              <div class="space-y-4">
                <div class="bg-lime-50 rounded-lg p-4">
                  <h4 class="font-semibold mb-2">Чат</h4>
                  <div class="space-y-2">
                    <div class="flex items-center space-x-2">
                      <div class="w-8 h-8 bg-green-500 rounded-full"></div>
                      <p class="text-sm">Привет всем!</p>
                    </div>
                    <div class="flex items-center space-x-2">
                      <div class="w-8 h-8 bg-emerald-500 rounded-full"></div>
                      <p class="text-sm">Рад быть здесь</p>
                    </div>
                  </div>
                </div>
                <div class="bg-lime-50 rounded-lg p-4">
                  <h4 class="font-semibold mb-2">Активные каналы</h4>
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
                      <span>{{ channel.name }}</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div
            class="absolute bottom-4 left-4 right-4 bg-gradient-to-r from-lime-500 via-green-500 to-emerald-500 text-white p-4 rounded-lg"
          >
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-4">
                <Mic class="w-6 h-6" />
                <Languages class="w-6 h-6" />
                <Layers class="w-6 h-6" />
              </div>
              <p class="text-sm font-medium">
                Мгновенный перевод и 3D-аудио активированы
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section
      id="features"
      class="py-20 bg-gradient-to-b from-lime-100 via-green-100 to-emerald-100"
    >
      <div class="container mx-auto px-4">
        <h2
          class="text-3xl md:text-4xl font-bold text-center mb-16 bg-clip-text text-transparent bg-gradient-to-r from-lime-600 via-green-600 to-emerald-600"
        >
          Безграничные возможности Миров
        </h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
            v-for="(feature, index) in features"
            :key="index"
            class="p-6 rounded-xl border border-lime-200 bg-white hover:shadow-lg transition-all duration-300 group"
          >
            <div
              class="w-12 h-12 rounded-full bg-gradient-to-br from-lime-400 via-green-400 to-emerald-400 flex items-center justify-center mb-4 group-hover:from-lime-500 group-hover:via-green-500 group-hover:to-emerald-500 transition-colors duration-300"
            >
              <component :is="feature.icon" class="w-8 h-8 text-white" />
            </div>
            <h3
              class="text-xl font-semibold mb-2 group-hover:text-lime-600 transition-colors duration-300"
            >
              {{ feature.title }}
            </h3>
            <p class="text-gray-600">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Worlds Section -->
    <section
      id="worlds"
      class="py-20 bg-gradient-to-b from-lime-50 via-green-50 to-emerald-50"
    >
      <div class="container mx-auto px-4">
        <h2
          class="text-3xl md:text-4xl font-bold text-center mb-16 bg-clip-text text-transparent bg-gradient-to-r from-lime-600 via-green-600 to-emerald-600"
        >
          Исследуйте уникальные Миры
        </h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
            v-for="(world, index) in worlds"
            :key="index"
            class="p-6 rounded-xl border border-lime-200 bg-white hover:shadow-lg transition-all duration-300 group"
          >
            <div class="flex items-center justify-between mb-4">
              <div
                class="w-12 h-12 rounded-full bg-gradient-to-br from-lime-100 to-green-100 flex items-center justify-center"
              >
                <component
                  :is="world.icon"
                  class="w-8 h-8"
                  :class="world.iconColor"
                />
              </div>
              <div class="text-sm text-gray-500">
                <span class="font-semibold text-lime-600">{{
                  world.members.toLocaleString()
                }}</span>
                участников
              </div>
            </div>
            <h3
              class="text-xl font-semibold mb-2 group-hover:text-lime-600 transition-colors duration-300"
            >
              {{ world.name }}
            </h3>
            <p class="text-gray-600 mb-4">{{ world.description }}</p>
            <div class="flex justify-between items-center">
              <span class="text-sm text-gray-500"
                >{{ world.channels }} каналов</span
              >
              <button
                class="px-3 py-1 text-sm text-lime-600 border border-lime-600 rounded-md hover:bg-lime-50 transition-colors"
              >
                Исследовать
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Technology Section -->
    <section
      id="technology"
      class="py-20 bg-gradient-to-b from-lime-100 via-green-100 to-emerald-100"
    >
      <div class="container mx-auto px-4">
        <h2
          class="text-3xl md:text-4xl font-bold text-center mb-16 bg-clip-text text-transparent bg-gradient-to-r from-lime-600 via-green-600 to-emerald-600"
        >
          Передовые технологии WORLDS
        </h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
            v-for="(tech, index) in technologies"
            :key="index"
            class="p-6 rounded-xl border border-lime-200 bg-white hover:shadow-lg transition-all duration-300 group"
          >
            <div
              class="w-12 h-12 rounded-full bg-gradient-to-br from-lime-400 via-green-400 to-emerald-400 flex items-center justify-center mb-4 group-hover:from-lime-500 group-hover:via-green-500 group-hover:to-emerald-500 transition-colors duration-300"
            >
              <component :is="tech.icon" class="w-8 h-8 text-white" />
            </div>
            <h3
              class="text-xl font-semibold mb-2 group-hover:text-lime-600 transition-colors duration-300"
            >
              {{ tech.title }}
            </h3>
            <p class="text-gray-600">{{ tech.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section
      id="project-stages"
      class="py-20 bg-gradient-to-b from-lime-100 via-green-100 to-emerald-100"
    >
      <div class="container mx-auto px-4">
        <h2
          class="text-3xl md:text-4xl font-bold text-center mb-16 bg-clip-text text-transparent bg-gradient-to-r from-lime-600 via-green-600 to-emerald-600"
        >
          Этапы развития проекта WORLDS
        </h2>
        <div class="max-w-4xl mx-auto">
          <div class="relative">
            <div
              class="absolute left-1/2 transform -translate-x-1/2 h-full w-1 bg-gradient-to-b from-lime-400 via-green-400 to-emerald-400"
            ></div>
            <div
              v-for="(stage, index) in projectStages"
              :key="index"
              class="relative mb-12"
            >
              <div class="flex items-center mb-4">
                <div
                  class="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-8 h-8 bg-white rounded-full border-4 border-lime-500 z-10"
                ></div>
                <div
                  :class="index % 2 === 0 ? 'pr-8 text-right' : 'pl-8 ml-auto'"
                  class="w-1/2"
                >
                  <h3 class="text-xl font-semibold text-lime-700">
                    {{ stage.title }}
                  </h3>
                  <p class="text-gray-600">{{ stage.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Call to Action Section -->
    <section
      class="py-20 bg-gradient-to-b from-lime-50 via-green-50 to-emerald-50 relative overflow-hidden"
    >
      <div class="container mx-auto px-4 text-center relative z-10">
        <div class="max-w-2xl mx-auto">
          <h2
            class="text-3xl md:text-4xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-lime-600 via-green-600 to-emerald-600"
          >
            Готовы создать свой уникальный Мир?
          </h2>
          <p class="text-xl text-gray-600 mb-8">
            Присоединяйтесь к WORLDS сегодня и станьте частью революции в сфере
            виртуального общения и сотрудничества.
          </p>
          <button
            class="px-6 py-3 text-lg bg-gradient-to-r from-lime-500 via-green-500 to-emerald-500 text-white rounded-md hover:from-lime-600 hover:via-green-600 hover:to-emerald-600 transition-colors shadow-lg hover:shadow-xl transform hover:-translate-y-1"
          >
            Создать свой Мир прямо сейчас
          </button>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <FooterBar />
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
  Languages,
  Layers,
  Palette,
  Bot,
  Compass,
  Cpu,
  Music,
  Share2,
  Sparkles,
  Zap,
  Lock,
  Headphones,
  Gamepad,
  Flask,
} from "lucide-vue-next";
import NavBar from "@/components/NavBar.vue";
import FooterBar from "@/components/FooterBar.vue";
import HelloWorld from "@/components/HelloWorld.vue";

const isVideoPlaying = ref(false);
const activeChannels = [
  { name: "Главная сцена", icon: Hash, iconColor: "text-lime-600" },
  { name: "Нетворкинг", icon: Hash, iconColor: "text-green-600" },
  { name: "Q&A", icon: Hash, iconColor: "text-emerald-600" },
];

const projectStages = [
  {
    title: "Альфа-версия",
    description:
      "Разработка основного функционала и тестирование с ограниченной группой пользователей.",
  },
  {
    title: "Бета-тестирование",
    description:
      "Открытое тестирование для более широкой аудитории, сбор обратной связи и улучшение платформы.",
  },
  {
    title: "Официальный запуск",
    description:
      "Полноценный запуск платформы с основными функциями и поддержкой нескольких языков.",
  },
  {
    title: "Расширение возможностей",
    description:
      "Добавление новых функций, таких как AR-интеграция и расширенные инструменты для совместной работы.",
  },
  {
    title: "Глобальное масштабирование",
    description:
      "Оптимизация инфраструктуры для поддержки миллионов пользователей по всему миру.",
  },
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
    icon: Compass,
    title: "3D-навигация",
    description:
      "Перемещайтесь между каналами и комнатами в трехмерном пространстве вашего Мира.",
  },
  {
    icon: Cpu,
    title: "Встроенные приложения",
    description:
      "Разрабатывайте и интегрируйте собственные приложения прямо внутри вашего Мира.",
  },
  {
    icon: Languages,
    title: "Мгновенный перевод",
    description: "Общайтесь с участниками со всего мира без языковых барьеров.",
  },
  {
    icon: Music,
    title: "Иммерсивное аудио",
    description:
      "Создавайте объемное звуковое пространство с 3D-аудио и синхронизированными плейлистами.",
  },
  {
    icon: Share2,
    title: "Расширенное сотрудничество",
    description:
      "Используйте инструменты для совместной работы, от досок для брейнштормов до кодовых редакторов.",
  },
  {
    icon: Sparkles,
    title: "Дополненная реальность",
    description:
      "Интегрируйте элементы AR для создания смешанных виртуально-реальных пространств.",
  },
];

const worlds = [
  {
    icon: Cpu,
    iconColor: "text-lime-600",
    name: "Технологический Хаб",
    description:
      "Мир для разработчиков и технических энтузиастов с каналами для обсуждения последних технологий, совместного кодирования и технических презентаций.",
    members: 15000,
    channels: 50,
  },
  {
    icon: Flask,
    iconColor: "text-green-600",
    name: "Глобальный Кампус",
    description:
      "Образовательный Мир с виртуальными классами, библиотеками и зонами для групповых проектов. Идеально для дистанционного обучения и международных образовательных программ.",
    members: 50000,
    channels: 200,
  },
  {
    icon: Palette,
    iconColor: "text-emerald-600",
    name: "Креативная Студия",
    description:
      "Мир для художников, дизайнеров и креативщиков. Включает галереи, мастерские и зоны для совместного творчества с использованием AR-инструментов.",
    members: 10000,
    channels: 30,
  },
  {
    icon: Share2,
    iconColor: "text-lime-600",
    name: "Бизнес Альянс",
    description:
      "Профессиональный Мир для нетворкинга, проведения виртуальных конференций и бизнес-встреч с расширенными инструментами для презентаций и аналитики.",
    members: 20000,
    channels: 100,
  },
  {
    icon: Gamepad,
    iconColor: "text-green-600",
    name: "Игровая Вселенная",
    description:
      "Развлекательный Мир для геймеров с каналами для различных игр, турнирными зонами и возможностью интеграции стримов прямо в интерфейс Мира.",
    members: 100000,
    channels: 500,
  },
  {
    icon: Flask,
    iconColor: "text-emerald-600",
    name: "Научный Коллаборатор",
    description:
      "Мир для ученых и исследователей с виртуальными лабораториями, конференц-залами для презентации исследований и инструментами для совместного анализа данных.",
    members: 5000,
    channels: 40,
  },
];

const technologies = [
  {
    icon: Zap,
    title: "Квантовые нейросети",
    description:
      "Использование квантовых вычислений для непревзойденной скорости и точности.",
  },
  {
    icon: Lock,
    title: "Квантовое шифрование",
    description:
      "Абсолютная безопасность коммуникаций, основанная на принципах квантовой механики.",
  },
  {
    icon: Headphones,
    title: "Нейро-3D аудио",
    description: "Создание полностью иммерсивного звукового ландшафта.",
  },
  {
    icon: Globe2,
    title: "Распределенные вычисления",
    description:
      "Использование мощности устройств пользователей для создания децентрализованной сети с минимальной задержкой.",
  },
  {
    icon: Cpu,
    title: "AI-оркестрация",
    description:
      "Интеллектуальное управление ресурсами и оптимизация производительности каждого Мира в реальном времени.",
  },
  {
    icon: Layers,
    title: "Многомерное пространство",
    description:
      "Технология создания и навигации по многомерным виртуальным пространствам для более глубокого погружения.",
  },
];
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

/* Add any additional styles here */
</style>
