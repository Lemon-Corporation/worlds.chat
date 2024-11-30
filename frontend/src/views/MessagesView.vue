<template>
  <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950 flex flex-col">
    <!-- Верхняя навигация -->
    <NavBar/>
    <div class="flex flex-grow h-[calc(100vh-4rem)]">
      <!-- Левый бар (сайдбар) -->
      <div class="w-64 bg-gray-900/80 backdrop-blur-sm border-r border-purple-500/20 overflow-y-auto flex flex-col">
        <div class="p-4">
          <input
            v-model="friendSearch"
            type="text"
            placeholder="Поиск друзей..."
            class="w-full bg-gray-800/60 border border-purple-500/20 rounded-lg px-3 py-2 text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] mb-4"
          />
          <button
            @click="showNewMessageModal = true"
            class="w-full bg-purple-500/20 hover:bg-purple-500/30 text-[#00ff9d] hover:text-[#00ff9d] py-2 rounded-lg flex items-center justify-center gap-2 transition-colors duration-200"
          >
            <Plus class="w-4 h-4" />
            Новое сообщение
          </button>
        </div>

        <div class="space-y-2 px-4 flex-grow overflow-y-auto">
          <div v-for="chat in filteredChats" :key="chat.id" class="space-y-1">
            <div
              @click="selectChat(chat)"
              class="flex items-center justify-between p-2 rounded-lg cursor-pointer hover:bg-purple-500/20 transition-colors duration-200"
              :class="{ 'bg-purple-500/20': chat.id === selectedChat?.id }"
            >
              <div class="flex items-center gap-2 min-w-0">
                <img 
                  :src="chat.avatar" 
                  :alt="chat.name"
                  class="w-10 h-10 rounded-full ring-1 ring-purple-500/50 flex-shrink-0"
                />
                <div class="min-w-0">
                  <span class="text-gray-300 font-medium truncate block">{{ chat.name }}</span>
                  <p class="text-gray-400 text-sm truncate">{{ chat.lastMessage }}</p>
                </div>
              </div>
              <div class="flex flex-col items-end ml-2">
                <span class="text-gray-400 text-xs">{{ chat.lastMessageTime }}</span>
                <span
                  v-if="chat.unreadCount"
                  class="bg-[#00ff9d] text-gray-900 text-xs font-bold px-2 py-1 rounded-full mt-1"
                >{{ chat.unreadCount }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Add Friend button -->
        <div class="p-4 border-t border-purple-500/20">
          <button
            @click="showAddFriendModal = true"
            class="w-full bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 py-2 rounded-lg flex items-center justify-center gap-2 transition-colors duration-200"
          >
            <UserPlus class="w-4 h-4" />
            Добавить друга
          </button>
        </div>
      </div>

      <!-- Основной контент -->
      <div class="flex-grow flex flex-col bg-gray-900/60 backdrop-blur-sm">
        <template v-if="selectedChat">
          <!-- Заголовок чата -->
          <div class="h-14 border-b border-purple-500/20 px-4 flex justify-between items-center bg-gray-900/40">
            <div class="flex items-center gap-2">
              <img 
                :src="selectedChat.avatar" 
                :alt="selectedChat.name"
                class="w-10 h-10 rounded-full ring-1 ring-purple-500/50"
              />
              <h1 class="font-semibold text-[#00ff9d]">{{ selectedChat.name }}</h1>
            </div>
            <div class="relative">
              <button @click="toggleChatOptions" class="text-gray-400 hover:text-[#00ff9d] transition-colors duration-200 focus:outline-none">
                <MoreVertical class="w-5 h-5" />
              </button>
              <div v-if="showChatOptions" ref="chatOptionsRef" class="absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-gray-800 ring-1 ring-black ring-opacity-5">
                <div class="py-1" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
                  <a href="#" class="block px-4 py-2 text-sm text-gray-300 hover:bg-gray-700 hover:text-[#00ff9d]" role="menuitem">Информация о чате</a>
                  <a href="#" class="block px-4 py-2 text-sm text-gray-300 hover:bg-gray-700 hover:text-[#00ff9d]" role="menuitem">Очистить историю</a>
                  <a href="#" class="block px-4 py-2 text-sm text-gray-300 hover:bg-gray-700 hover:text-[#00ff9d]" role="menuitem">Заблокировать пользователя</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Сообщения -->
          <div class="flex-grow p-4 overflow-y-auto space-y-4" ref="messagesContainer">
            <div
              v-for="message in selectedChat.messages"
              :key="message.id"
              :class="[
                'max-w-[70%] rounded-lg p-3',
                message.sent ? 'bg-[#00ff9d] text-gray-900 self-end ml-auto' : 'bg-gray-700 text-white self-start'
              ]"
            >
              <p>{{ message.content }}</p>
              <span class="text-xs opacity-70 mt-1 block text-right">{{ message.time }}</span>
            </div>
          </div>

          <!-- Ввод сообщения -->
          <div class="p-4 border-t border-purple-500/20 bg-gray-900/40">
            <form @submit.prevent="sendMessage" class="flex items-center gap-2">
              <button
                type="button"
                @click="toggleEmojiPicker"
                class="text-gray-400 hover:text-[#00ff9d] focus:outline-none"
              >
                <Smile class="w-5 h-5" />
              </button>
              <input
                v-model="newMessage"
                type="text"
                placeholder="Напишите сообщение..."
                class="flex-grow bg-gray-800/60 border border-purple-500/20 rounded-lg px-3 py-2 text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d]"
              />
              <button
                type="button"
                @click="openFilePicker"
                class="text-gray-400 hover:text-[#00ff9d] focus:outline-none"
              >
                <Paperclip class="w-5 h-5" />
              </button>
              <button
                type="submit"
                class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 p-2 rounded-lg transition-colors duration-200 focus:outline-none"
              >
                <Send class="w-5 h-5" />
              </button>
            </form>
          </div>

          <!-- Эмодзи пикер -->
          <div v-if="showEmojiPicker" class="absolute bottom-20 left-4 bg-gray-800 border border-purple-500/20 rounded-lg p-2 shadow-lg">
            <div class="grid grid-cols-8 gap-1">
              <button
                v-for="emoji in emojis"
                :key="emoji"
                @click="addEmoji(emoji)"
                class="text-2xl hover:bg-gray-700 rounded p-1 transition-colors duration-200"
              >
                {{ emoji }}
              </button>
            </div>
          </div>
        </template>
        <template v-else>
          <div class="flex-grow flex items-center justify-center p-4">
            <div class="text-center">
              <MessageSquare class="w-16 h-16 text-[#00ff9d] mx-auto mb-4" />
              <h2 class="text-2xl font-bold text-[#00ff9d] mb-2">Личные сообщения</h2>
              <p class="text-gray-400 mb-6">Выберите чат или создайте новый, чтобы начать общение.</p>
              <button
                @click="showNewMessageModal = true"
                class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium py-2 px-4 rounded-lg transition-colors duration-200 flex items-center gap-2 mx-auto focus:outline-none"
              >
                <Plus class="w-4 h-4" />
                Новое сообщение
              </button>
            </div>
          </div>
        </template>
      </div>
    </div>

    <!-- Модальное окно нового сообщения -->
    <div v-if="showNewMessageModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gray-900 border border-purple-500/20 rounded-lg w-full max-w-md p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-[#00ff9d] text-xl font-bold">Новый диалог</h2>
          <button @click="closeNewMessageModal" class="text-gray-400 hover:text-[#00ff9d] transition-colors duration-200 focus:outline-none">
            <X class="w-5 h-5" />
          </button>
        </div>
        <div class="space-y-4">
          <div>
            <label for="recipient" class="block text-gray-300 text-sm font-medium mb-2">Выберите собеседника</label>
            <div class="relative">
              <input
                id="recipient"
                v-model="newDialogRecipient"
                type="text"
                class="w-full bg-gray-800 border border-purple-500/20 rounded-lg px-3 py-2 text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d]"
                placeholder="Поиск друзей или @тег"
                @input="searchUsers"
              />
              <div v-if="searchResults.length > 0" class="absolute z-10 w-full mt-1 bg-gray-800 border border-purple-500/20 rounded-lg shadow-lg">
                <div
                  v-for="user in searchResults"
                  :key="user.id"
                  @click="selectUser(user)"
                  class="flex items-center p-2 hover:bg-gray-700 cursor-pointer rounded-lg"
                >
                  <img :src="user.avatar" :alt="user.name" class="w-10 h-10 rounded-full mr-3" />
                  <span class="text-gray-300">{{ user.name }}</span>
                </div>
              </div>
            </div>
          </div>
          <div class="flex justify-end gap-3 mt-6">
            <button
              type="button"
              @click="closeNewMessageModal"
              class="px-4 py-2 text-gray-400 hover:text-gray-300 transition-colors duration-200 focus:outline-none"
            >
              Отмена
            </button>
            <button
              @click="createNewDialog"
              class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium px-4 py-2 rounded-lg transition-colors duration-200 focus:outline-none"
            >
              Создать диалог
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Add Friend Modal -->
    <div v-if="showAddFriendModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gray-900 border border-purple-500/20 rounded-lg w-full max-w-md p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-[#00ff9d] text-xl font-bold">Добавить друга</h2>
          <button @click="closeAddFriendModal" class="text-gray-400 hover:text-[#00ff9d] transition-colors duration-200 focus:outline-none">
            <X class="w-5 h-5" />
          </button>
        </div>
        <div class="space-y-4">
          <div>
            <label for="friendUsername" class="block text-gray-300 text-sm font-medium mb-2">Имя пользователя или email</label>
            <input
              id="friendUsername"
              v-model="newFriendUsername"
              type="text"
              class="w-full bg-gray-800 border border-purple-500/20 rounded-lg px-3 py-2 text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d]"
              placeholder="Введите имя пользователя или email"
            />
          </div>
          <div class="flex justify-end gap-3 mt-6">
            <button
              type="button"
              @click="closeAddFriendModal"
              class="px-4 py-2 text-gray-400 hover:text-gray-300 transition-colors duration-200 focus:outline-none"
            >
              Отмена
            </button>
            <button
              @click="addFriend"
              class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium px-4 py-2 rounded-lg transition-colors duration-200 focus:outline-none"
            >
              Добавить
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, nextTick, onMounted, onUnmounted } from 'vue';
import { Plus, MoreVertical, Send, MessageSquare, X, Smile, Paperclip, UserPlus } from 'lucide-vue-next';
import NavBar from '@/components/NavBar.vue';

const chats = ref([
  {
    id: 1,
    name: 'Алиса',
    avatar: 'https://i.pinimg.com/736x/76/c9/22/76c9223d76249e8a2f9b9fea0667ac83.jpg',
    lastMessage: 'Привет! Как дела?',
    lastMessageTime: '12:30',
    unreadCount: 2,
    messages: [
      { id: 1, content: 'Привет! Как дела?', time: '12:30', sent: false },
      { id: 2, content: 'У меня все отлично! Как твои проекты?', time: '12:35', sent: true },
    ]
  },
  {
    id: 2,
    name: 'Борис',
    avatar: 'https://i.pinimg.com/736x/88/ab/62/88ab62333f5db8854790294fdff41b4e.jpg',
    lastMessage: 'Увидимся завтра на встрече',
    lastMessageTime: '15:45',
    unreadCount: 0,
    messages: [
      { id: 1, content: 'Привет, не забудь про завтрашнюю встречу', time: '15:40', sent: false },
      { id: 2, content: 'Увидимся завтра на встрече', time: '15:45', sent: false },
    ]
  },
]);

const selectedChat = ref(null);
const newMessage = ref('');
const messagesContainer = ref(null);

const showNewMessageModal = ref(false);
const newDialogRecipient = ref('');
const showEmojiPicker = ref(false);
const showChatOptions = ref(false);
const searchResults = ref([]);
const selectedUser = ref(null);

const showAddFriendModal = ref(false);
const newFriendUsername = ref('');
const friendSearch = ref('');

const emojis = ['😀', '😂', '😍', '🤔', '😎', '👍', '🎉', '🔥', '❤️', '🙌', '🤝', '🌟', '💡', '🎈', '🎁', '🏆'];

const filteredChats = computed(() => {
  if (!friendSearch.value) return chats.value;
  return chats.value.filter(chat => 
    chat.name.toLowerCase().includes(friendSearch.value.toLowerCase())
  );
});

const selectChat = (chat) => {
  selectedChat.value = chat;
  chat.unreadCount = 0;
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
    }
  });
};

const sendMessage = () => {
  if (newMessage.value.trim() === '') return;

  const message = {
    id: Date.now(),
    content: newMessage.value,
    time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    sent: true
  };

  selectedChat.value.messages.push(message);
  selectedChat.value.lastMessage = message.content;
  selectedChat.value.lastMessageTime = message.time;

  newMessage.value = '';

  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
    }
  });
};

const createNewDialog = () => {
  if (!selectedUser.value) return;

  const newChat = {
    id: Date.now(),
    name: selectedUser.value.name,
    avatar: selectedUser.value.avatar,
    lastMessage: '',
    lastMessageTime: '',
    unreadCount: 0,
    messages: []
  };

  chats.value.unshift(newChat);
  selectChat(newChat);
  closeNewMessageModal();
};

const closeNewMessageModal = () => {
  showNewMessageModal.value = false;
  newDialogRecipient.value = '';
  selectedUser.value = null;
  searchResults.value = [];
};

const toggleEmojiPicker = () => {
  showEmojiPicker.value = !showEmojiPicker.value;
};

const addEmoji = (emoji) => {
  newMessage.value += emoji;
};

const openFilePicker = () => {
  // Implement file picker functionality
  console.log('Opening file picker');
};

const toggleChatOptions = () => {
  showChatOptions.value = !showChatOptions.value;
};

const searchUsers = () => {
  // Имитация поиска пользователей
  searchResults.value = [
    { id: 1, name: 'Алиса', avatar: 'https://i.pravatar.cc/150?img=1' },
    { id: 2, name: 'Борис', avatar: 'https://i.pravatar.cc/150?img=2' },
    { id: 3, name: 'Виктория', avatar: 'https://i.pravatar.cc/150?img=3' },
  ].filter(user => user.name.toLowerCase().includes(newDialogRecipient.value.toLowerCase()));
};

const selectUser = (user) => {
  selectedUser.value = user;
  newDialogRecipient.value = user.name;
};

const closeAddFriendModal = () => {
  showAddFriendModal.value = false;
  newFriendUsername.value = '';
};

const addFriend = () => {
  if (newFriendUsername.value.trim() === '') return;
  
  // Here you would typically make an API call to add the friend
  console.log(`Adding friend: ${newFriendUsername.value}`);
  
  // For demonstration, let's add a new chat
  const newFriend = {
    id: Date.now(),
    name: newFriendUsername.value,
    avatar: `https://i.pravatar.cc/150?u=${newFriendUsername.value}`,
    lastMessage: '',
    lastMessageTime: '',
    unreadCount: 0,
    messages: []
  };
  
  chats.value.unshift(newFriend);
  closeAddFriendModal();
};

const chatOptionsRef = ref(null);

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});

const handleClickOutside = (event) => {
  if (chatOptionsRef.value && !chatOptionsRef.value.contains(event.target)) {
    showChatOptions.value = false;
  }
};

// Закрывать выпадающие меню при клике вне их области
watch(() => [showEmojiPicker.value, showChatOptions.value], () => {
  const closeDropdowns = (event) => {
    if (!event.target.closest('.emoji-picker') && !event.target.closest('.chat-options')) {
      showEmojiPicker.value = false;
      showChatOptions.value = false;
    }
  };

  if (showEmojiPicker.value || showChatOptions.value) {
    document.addEventListener('click', closeDropdowns);
  } else {
    document.removeEventListener('click', closeDropdowns);
  }
});
</script>

<style scoped>
/* Добавьте здесь любые дополнительные стили, если необходимо */
</style>