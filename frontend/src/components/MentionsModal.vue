<template>
    <transition name="fade">
      <div v-if="show" class="fixed inset-0 bg-black bg-opacity-50 backdrop-blur-sm flex justify-center items-center z-50">
        <div class="bg-gray-900 border border-purple-500/20 rounded-lg p-6 w-full max-w-md">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-[#00ff9d] text-xl font-bold">Упоминания</h2>
            <button @click="$emit('close')" class="text-gray-400 hover:text-[#00ff9d] transition-colors duration-200">
              <X class="w-5 h-5" />
            </button>
          </div>
          <p class="text-gray-300 text-center">Вас пока никто не упоминал в мирах... Как только произойдет, мы вас оповестим!</p>
        </div>
      </div>
    </transition>
  </template>
  
  <script setup>
  import { X } from 'lucide-vue-next';
  
  defineProps({
    show: Boolean
  });
  
  defineEmits(['close']);
  </script>
  
  <style scoped>
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.3s ease;
  }
  
  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
  </style>