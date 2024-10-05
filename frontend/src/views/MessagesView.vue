<template>
  <div class="app-container">
    <div class="sidebar">
      <div
        v-for="item in sidebarItems"
        :key="item.text"
        :class="['sidebar-item', { active: item.text === 'Messages' }]"
      >
        <img :src="item.icon" :alt="item.text" />
        {{ item.text }}
      </div>
      <button class="create-world-btn">Create World</button>
    </div>
    <div class="main-content">
      <div class="header">
        <h1>Messages</h1>
        <div class="header-icons">
          <img
            v-for="icon in headerIcons"
            :key="icon.alt"
            :src="icon.src"
            :alt="icon.alt"
          />
        </div>
      </div>
      <div class="message-container">
        <div class="conversation-list">
          <div class="search-bar">
            <img
              src="https://api.iconify.design/lucide:search.svg"
              alt="Search"
            />
            <input
              type="text"
              placeholder="Search conversations"
              v-model="searchQuery"
            />
          </div>
          <div
            v-for="conversation in filteredConversations"
            :key="conversation.id"
            :class="[
              'conversation-item',
              { active: conversation.id === activeConversation.id },
            ]"
            @click="setActiveConversation(conversation)"
          >
            <img
              :src="conversation.avatar"
              :alt="conversation.name"
              class="avatar"
            />
            <div class="conversation-info">
              <h3>{{ conversation.name }}</h3>
              <p>{{ conversation.lastMessage }}</p>
            </div>
            <span class="time">{{ conversation.time }}</span>
          </div>
        </div>
        <div class="chat-window">
          <div v-if="activeConversation" class="chat-header">
            <img
              :src="activeConversation.avatar"
              :alt="activeConversation.name"
              class="avatar"
            />
            <h2>{{ activeConversation.name }}</h2>
          </div>
          <div class="message-list" ref="messageList">
            <div
              v-for="message in activeConversation.messages"
              :key="message.id"
              :class="['message', { sent: message.sent }]"
            >
              <p>{{ message.content }}</p>
              <span class="message-time">{{ message.time }}</span>
            </div>
          </div>
          <div class="message-input">
            <input
              type="text"
              placeholder="Type a message..."
              v-model="newMessage"
              @keyup.enter="sendMessage"
            />
            <button @click="sendMessage">
              <img
                src="https://api.iconify.design/lucide:send.svg"
                alt="Send"
              />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from "vue";

const sidebarItems = ref([
  { text: "Home", icon: "https://api.iconify.design/lucide:home.svg" },
  { text: "Profile", icon: "https://api.iconify.design/lucide:user.svg" },
  { text: "Worlds", icon: "https://api.iconify.design/lucide:globe.svg" },
  {
    text: "Messages",
    icon: "https://api.iconify.design/lucide:message-circle.svg",
  },
  { text: "Notifications", icon: "https://api.iconify.design/lucide:bell.svg" },
]);

const headerIcons = ref([
  { src: "https://api.iconify.design/lucide:bell.svg", alt: "Notifications" },
  { src: "https://api.iconify.design/lucide:settings.svg", alt: "Settings" },
  { src: "https://api.iconify.design/lucide:log-out.svg", alt: "Logout" },
]);

const conversations = ref([
  {
    id: 1,
    name: "Alice Cooper",
    avatar:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
    lastMessage: "Hey, how's the new world coming along?",
    time: "2m ago",
    messages: [
      {
        id: 1,
        content: "Hey, how's the new world coming along?",
        time: "2:30 PM",
        sent: false,
      },
      {
        id: 2,
        content: "It's going great! Just adding some final touches.",
        time: "2:31 PM",
        sent: true,
      },
      { id: 3, content: "Can't wait to see it!", time: "2:32 PM", sent: false },
    ],
  },
  {
    id: 2,
    name: "Bob Cyber",
    avatar:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
    lastMessage: "The neon lights in your world are amazing!",
    time: "1h ago",
    messages: [
      {
        id: 1,
        content: "I just visited your Neon City. It's incredible!",
        time: "1:15 PM",
        sent: false,
      },
      {
        id: 2,
        content: "Thanks! I spent a lot of time on the lighting.",
        time: "1:20 PM",
        sent: true,
      },
      {
        id: 3,
        content: "The neon lights in your world are amazing!",
        time: "1:22 PM",
        sent: false,
      },
    ],
  },
  {
    id: 3,
    name: "Charlie Pixel",
    avatar:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
    lastMessage: "Want to collaborate on a new world?",
    time: "1d ago",
    messages: [
      {
        id: 1,
        content: "Hey, I have an idea for a new world.",
        time: "11:00 AM",
        sent: false,
      },
      {
        id: 2,
        content: "Sounds interesting! What's the concept?",
        time: "11:05 AM",
        sent: true,
      },
      {
        id: 3,
        content: "It's a retro-futuristic space station. Want to collaborate?",
        time: "11:10 AM",
        sent: false,
      },
      {
        id: 4,
        content: "That sounds awesome! I'd love to collaborate.",
        time: "11:15 AM",
        sent: true,
      },
      {
        id: 5,
        content: "Great! Let's set up a meeting to discuss details.",
        time: "11:20 AM",
        sent: false,
      },
      {
        id: 6,
        content: "Perfect. How about tomorrow at 2 PM?",
        time: "11:25 AM",
        sent: true,
      },
      {
        id: 7,
        content: "Works for me. See you then!",
        time: "11:30 AM",
        sent: false,
      },
    ],
  },
]);

const activeConversation = ref(conversations.value[0]);
const searchQuery = ref("");
const newMessage = ref("");
const messageList = ref(null);

const filteredConversations = computed(() => {
  return conversations.value.filter(
    (conv) =>
      conv.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      conv.lastMessage.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const setActiveConversation = (conversation) => {
  activeConversation.value = conversation;
  nextTick(() => {
    scrollToBottom();
  });
};

const sendMessage = () => {
  if (newMessage.value.trim()) {
    activeConversation.value.messages.push({
      id: activeConversation.value.messages.length + 1,
      content: newMessage.value,
      time: new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
      sent: true,
    });
    activeConversation.value.lastMessage = newMessage.value;
    activeConversation.value.time = "Just now";
    newMessage.value = "";
    nextTick(() => {
      scrollToBottom();
    });
  }
};

const scrollToBottom = () => {
  if (messageList.value) {
    messageList.value.scrollTop = messageList.value.scrollHeight;
  }
};

onMounted(() => {
  scrollToBottom();
});
</script>

<style scoped>
:root {
  --bg-main: #1e1e2e;
  --bg-sidebar: #2a2a3a;
  --bg-card: #2f2f3f;
  --text-primary: #ffffff;
  --text-secondary: #a0a0b0;
  --accent-purple: #6c5ce7;
  --accent-hover: #5a4bd1;
  --transition: all 0.3s ease;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app-container {
  font-family: "Poppins", sans-serif;
  background-color: var(--bg-main);
  color: var(--text-primary);
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: 250px;
  background-color: var(--bg-sidebar);
  padding: 20px;
  transition: var(--transition);
}

.sidebar-item {
  display: flex;
  align-items: center;
  padding: 10px;
  margin-bottom: 10px;
  cursor: pointer;
  color: var(--text-secondary);
  transition: var(--transition);
  border-radius: 5px;
}

.sidebar-item:hover,
.sidebar-item.active {
  background-color: var(--bg-card);
  color: var(--text-primary);
  transform: translateX(5px);
}

.sidebar-item img {
  width: 24px;
  height: 24px;
  margin-right: 10px;
  filter: invert(0.7);
  transition: var(--transition);
}

.sidebar-item:hover img,
.sidebar-item.active img {
  filter: invert(1);
}

.create-world-btn {
  background-color: var(--accent-purple);
  color: var(--text-primary);
  border: none;
  padding: 12px;
  width: 100%;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
  transition: var(--transition);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.create-world-btn:hover {
  background-color: var(--accent-hover);
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(108, 92, 231, 0.2);
}

.main-content {
  flex-grow: 1;
  padding: 20px;
  overflow-y: auto;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--bg-sidebar);
}

.header h1 {
  font-size: 2.5rem;
  font-weight: 600;
  letter-spacing: 1px;
}

.header-icons {
  display: flex;
  align-items: center;
}

.header-icons img {
  width: 24px;
  height: 24px;
  margin-left: 20px;
  filter: invert(1);
  transition: var(--transition);
  cursor: pointer;
}

.header-icons img:hover {
  transform: scale(1.1);
}

.message-container {
  display: flex;
  height: calc(100vh - 140px);
  background-color: var(--bg-card);
  border-radius: 10px;
  overflow: hidden;
}

.conversation-list {
  width: 300px;
  background-color: var(--bg-sidebar);
  overflow-y: auto;
}

.search-bar {
  display: flex;
  align-items: center;
  padding: 10px;
  background-color: var(--bg-card);
}

.search-bar img {
  width: 20px;
  height: 20px;
  margin-right: 10px;
  filter: invert(0.7);
}

.search-bar input {
  width: 100%;
  background-color: transparent;
  border: none;
  color: var(--text-primary);
  font-size: 14px;
}

.search-bar input::placeholder {
  color: var(--text-secondary);
}

.conversation-item {
  display: flex;
  align-items: center;
  padding: 15px;
  cursor: pointer;
  transition: var(--transition);
}

.conversation-item:hover,
.conversation-item.active {
  background-color: var(--bg-card);
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.conversation-info {
  flex-grow: 1;
}

.conversation-info h3 {
  font-size: 16px;
  margin-bottom: 5px;
}

.conversation-info p {
  font-size: 14px;
  color: var(--text-secondary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.time {
  font-size: 12px;
  color: var(--text-secondary);
}

.chat-window {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.chat-header {
  display: flex;
  align-items: center;
  padding: 15px;
  background-color: var(--bg-card);
  border-bottom: 1px solid var(--bg-sidebar);
}

.chat-header h2 {
  margin-left: 10px;
  font-size: 18px;
}

.message-list {
  flex-grow: 1;
  padding: 20px;
  overflow-y: auto;
}

.message {
  max-width: 70%;
  margin-bottom: 15px;
  padding: 10px 15px;
  border-radius: 20px;
  background-color: var(--bg-sidebar);
  align-self: flex-start;
}

.message.sent {
  background-color: var(--accent-purple);
  align-self: flex-end;
}

.message p {
  margin-bottom: 5px;
}

.message-time {
  font-size: 12px;
  color: var(--text-secondary);
}

.message-input {
  display: flex;
  align-items: center;
  padding: 15px;
  background-color: var(--bg-card);
}

.message-input input {
  flex-grow: 1;
  padding: 10px;
  border: none;
  border-radius: 20px;
  background-color: var(--bg-sidebar);
  color: var(--text-primary);
  font-size: 14px;
}

.message-input button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  margin-left: 10px;
}

.message-input button img {
  width: 24px;
  height: 24px;
  filter: invert(1);
}

@media (max-width: 768px) {
  .app-container {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
    padding: 10px;
  }

  .main-content {
    padding: 10px;
  }

  .message-container {
    flex-direction: column;
    height: calc(100vh - 200px);
  }

  .conversation-list {
    width: 100%;
    height: 200px;
  }

  .chat-window {
    height: calc(100% - 200px);
  }
}
</style>
