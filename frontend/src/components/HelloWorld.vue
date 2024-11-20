<template>
  <TransitionRoot :show="isOpen" as="template">
    <div
      class="fixed inset-0 z-50 overflow-y-auto"
      aria-labelledby="modal-title"
      role="dialog"
      aria-modal="true"
    >
      <div
        class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
      >
        <TransitionChild
          as="template"
          enter="ease-out duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in duration-200"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div
            class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity backdrop-blur-sm"
            aria-hidden="true"
            @click="closeModal"
          ></div>
        </TransitionChild>

        <span
          class="hidden sm:inline-block sm:align-middle sm:h-screen"
          aria-hidden="true"
          >&#8203;</span
        >

        <TransitionChild
          as="template"
          enter="ease-out duration-300"
          enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          enter-to="opacity-100 translate-y-0 sm:scale-100"
          leave="ease-in duration-200"
          leave-from="opacity-100 translate-y-0 sm:scale-100"
          leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
        >
          <div
            class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
          >
            <div
              class="bg-white px-6 py-4 sm:px-8 sm:py-6 flex justify-center items-center space-x-6"
            >
              <img
                src="https://i.imgur.com/zL7Ig1z.png"
                alt="Lemon Corporation"
                class="h-20 sm:h-24"
              />
              <span class="text-gray-800 text-3xl sm:text-4xl font-bold"
                >x</span
              >
              <img
                src="https://i.imgur.com/yYDteYf.png"
                alt="Логотип компании 2"
                class="h-20 sm:h-24"
              />
            </div>
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
              <div class="sm:flex sm:items-start">
                <div
                  class="mx-auto flex-shrink-0 flex items-center justify-center h-14 w-14 rounded-full bg-green-100 sm:mx-0 sm:h-16 sm:w-16"
                >
                  <Sparkles class="h-8 w-8 text-green-600" />
                </div>
                <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                  <h3
                    class="text-xl sm:text-2xl leading-6 font-bold text-gray-900 mb-2"
                    id="modal-title"
                  >
                    Проект WORLDS в разработке
                  </h3>
                  <div class="mt-2">
                    <p class="text-base text-gray-500 leading-relaxed">
                      Мы усердно работаем над созданием революционной платформы
                      WORLDS. Скоро вы сможете создавать свои уникальные
                      виртуальные пространства и погружаться в новый мир общения
                      и сотрудничества.
                    </p>
                  </div>
                  <div class="mt-4">
                    <h4 class="text-lg font-semibold text-green-600 mb-2">
                      Что вас ждет:
                    </h4>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                      <li>Безграничные возможности кастомизации</li>
                      <li>Мгновенный перевод для общения без барьеров</li>
                      <li>Интеграция с передовыми AI-технологиями</li>
                      <li>Иммерсивные 3D-пространства для встреч и событий</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse"
            >
              <button
                type="button"
                @click="closeModal"
                class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-6 py-3 bg-green-600 text-base font-medium text-white hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 sm:ml-3 sm:w-auto sm:text-sm transition duration-150 ease-in-out"
              >
                Жду с нетерпением!
              </button>
              <button
                type="button"
                @click="closeModal"
                class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm transition duration-150 ease-in-out"
              >
                Напомнить позже
              </button>
            </div>
          </div>
        </TransitionChild>
      </div>
    </div>
  </TransitionRoot>
</template>

<script setup>
import { ref } from "vue";
import { Sparkles } from "lucide-vue-next";
import { TransitionChild, TransitionRoot } from "@headlessui/vue";

const isOpen = ref(true);

const closeModal = () => {
  isOpen.value = false;
};
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: all 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
  transform: scale(0.9);
}
</style>
