<template>
  <footer
    class="bg-gradient-to-b from-lime-100 via-green-100 to-emerald-100 py-12"
  >
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div>
          <h3
            class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-lime-600 via-green-600 to-emerald-600 mb-4"
          >
            WORLDS
          </h3>
          <p class="text-gray-600 mb-4">
            Создавая будущее виртуального взаимодействия.
          </p>
        </div>
        <div>
          <h4 class="text-lg font-semibold text-gray-800 mb-4">
            Быстрые ссылки
          </h4>
          <ul class="space-y-2">
            <li v-for="link in quickLinks" :key="link.href">
              <a
                :href="link.href"
                class="text-gray-600 hover:text-lime-600 transition-colors"
                >{{ link.text }}</a
              >
            </li>
          </ul>
        </div>
        <div>
          <h4 class="text-lg font-semibold text-gray-800 mb-4">Поддержка</h4>
          <ul class="space-y-2">
            <li v-for="link in supportLinks" :key="link.href">
              <a
                :href="link.href"
                class="text-gray-600 hover:text-lime-600 transition-colors"
                >{{ link.text }}</a
              >
            </li>
          </ul>
        </div>
        <div>
          <h4 class="text-lg font-semibold text-gray-800 mb-4">
            Подпишитесь на новости
          </h4>
          <p class="text-gray-600 mb-4">
            Будьте в курсе последних обновлений и новостей WORLDS.
          </p>
          <form @submit.prevent="subscribeToNewsletter" class="flex">
            <input
              type="email"
              placeholder="Ваш email"
              class="flex-grow px-4 py-2 rounded-l-md border-t border-b border-l border-gray-300 focus:outline-none focus:ring-2 focus:ring-lime-500"
              required
            />
            <button
              type="submit"
              class="px-4 py-2 bg-gradient-to-r from-lime-500 to-green-500 text-white rounded-r-md hover:from-lime-600 hover:to-green-600 transition-colors"
            >
              Подписаться
            </button>
          </form>
        </div>
      </div>
      <div class="mt-8 pt-8 border-t border-gray-200">
        <div class="flex flex-wrap justify-between items-center">
          <p class="text-gray-600 text-sm">
            © {{ new Date().getFullYear() }} WORLDS. Все права защищены.
          </p>
          <div class="flex space-x-4 mt-4 sm:mt-0"></div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
const quickLinks = [
  { href: "https://lemon-corporation.com/ru", text: "Lemon Corporation" },
  { href: "https://sk.ru", text: "Сколково" },
  { href: "/worlds", text: "Миры" },
];

const supportLinks = [
  { href: "/support-center", text: "Центр поддержки" },
  { href: "https://t.me/lemoncorphelp", text: "Связаться с нами" },
];

const subscribeToNewsletter = () => {
  // Implement newsletter subscription logic here
  console.log("Subscribed to newsletter");
};
</script>

<style scoped>
/* Add any additional styles here */
</style>
