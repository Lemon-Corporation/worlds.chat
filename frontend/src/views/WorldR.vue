<template>
  <div
    class="nexus-chat"
    :class="{ 'collapsed-sidebar': isLeftSidebarCollapsed }"
  >
    <!-- Left Sidebar -->
    <div class="left-sidebar">
      <button @click="toggleLeftSidebar" class="collapse-button">
        <img
          :src="
            isLeftSidebarCollapsed
              ? 'https://api.iconify.design/lucide:chevrons-right.svg'
              : 'https://api.iconify.design/lucide:chevrons-left.svg'
          "
          :alt="isLeftSidebarCollapsed ? 'Expand' : 'Collapse'"
        />
      </button>
      <h1 class="worlds-title">WORLDS</h1>
      <nav>
        <ul>
          <li v-for="item in navItems" :key="item.id">
            <a
              :href="item.href"
              class="nav-item"
              :class="{ active: item.id === activeNavItem }"
            >
              <img :src="item.icon" :alt="item.name" />
              <span>{{ item.name }}</span>
            </a>
          </li>
        </ul>
      </nav>
      <button class="create-world-button">Create World</button>
      <div class="your-worlds">
        <h3>Your WORLDS:</h3>
        <ul>
          <li v-for="world in yourWorlds" :key="world.id">
            <img :src="world.icon" :alt="world.name" />
            <span class="world-name">{{ world.name }}</span>
            <span class="member-count">{{ world.members }} members</span>
          </li>
        </ul>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- World Header -->
      <div class="world-header">
        <img
          src="https://api.iconify.design/game-icons:fire-dash.svg"
          alt="World Icon"
          class="world-icon"
        />
        <h2>WORLD</h2>
      </div>

      <!-- Channel List -->
      <div class="channel-list">
        <h3>TEXT CHANNELS</h3>
        <ul>
          <li
            v-for="channel in textChannels"
            :key="channel.id"
            :class="{ active: channel.id === activeChannel }"
            @click="setActiveChannel(channel.id)"
          >
            # {{ channel.name }}
          </li>
        </ul>
        <h3>VOICE CHANNELS</h3>
        <ul>
          <li
            v-for="channel in voiceChannels"
            :key="channel.id"
            :class="{ active: channel.id === activeChannel }"
            @click="setActiveChannel(channel.id)"
          >
            <img
              src="https://api.iconify.design/lucide:mic.svg"
              alt="Voice Channel"
            />
            {{ channel.name }}
          </li>
        </ul>
      </div>

      <!-- Chat Area -->
      <div class="chat-area">
        <div class="chat-header">
          <h2># {{ activeChannelName }}</h2>
        </div>
        <div class="messages" ref="messagesContainer">
          <div v-for="message in messages" :key="message.id" class="message">
            <img :src="message.avatar" :alt="message.author" class="avatar" />
            <div class="message-content">
              <div class="message-header">
                <span class="author">{{ message.author }}</span>
                <span class="timestamp">{{ message.timestamp }}</span>
              </div>
              <div class="message-text">{{ message.text }}</div>
            </div>
          </div>
        </div>
        <div class="message-input">
          <input
            v-model="newMessage"
            @keyup.enter="sendMessage"
            :placeholder="`Message #${activeChannelName}`"
          />
          <button @click="sendMessage">Send</button>
        </div>
      </div>
    </div>

    <!-- Right Sidebar -->
    <div class="right-sidebar">
      <div class="online-users">
        <h3>ONLINE - {{ onlineUsers.length }}</h3>
        <ul>
          <li v-for="user in onlineUsers" :key="user.id">
            <img :src="user.avatar" :alt="user.name" class="avatar" />
            <span class="user-name">{{ user.name }}</span>
            <span class="status-indicator online"></span>
          </li>
        </ul>
      </div>
      <div class="offline-users">
        <h3>OFFLINE - {{ offlineUsers.length }}</h3>
        <ul>
          <li v-for="user in offlineUsers" :key="user.id">
            <img :src="user.avatar" :alt="user.name" class="avatar" />
            <span class="user-name">{{ user.name }}</span>
            <span class="status-indicator offline"></span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from "vue";

const isLeftSidebarCollapsed = ref(false);
const activeChannel = ref("general");
const newMessage = ref("");
const messagesContainer = ref(null);
const activeNavItem = ref("worlds");

const navItems = [
  {
    id: "messages",
    name: "Messages",
    icon: "https://api.iconify.design/lucide:message-square.svg",
    href: "#",
  },
  {
    id: "worlds",
    name: "Worlds",
    icon: "https://api.iconify.design/lucide:globe.svg",
    href: "#",
  },
  {
    id: "inner",
    name: "Inner",
    icon: "https://api.iconify.design/lucide:circle.svg",
    href: "#",
  },
  {
    id: "notifications",
    name: "Notifications",
    icon: "https://api.iconify.design/lucide:bell.svg",
    href: "#",
  },
];

const yourWorlds = ref([
  {
    id: 1,
    name: "Solstice",
    icon: "https://api.dicebear.com/6.x/pixel-art/svg?seed=Solstice",
    members: 5000,
  },
  {
    id: 2,
    name: "Neon City",
    icon: "https://api.dicebear.com/6.x/pixel-art/svg?seed=NeonCity",
    members: 3000,
  },
  {
    id: 3,
    name: "Space Odyssey",
    icon: "https://api.dicebear.com/6.x/pixel-art/svg?seed=SpaceOdyssey",
    members: 10000,
  },
  {
    id: 4,
    name: "Tech Talk",
    icon: "https://api.dicebear.com/6.x/pixel-art/svg?seed=TechTalk",
    members: 1000,
  },
]);

const textChannels = ref([
  { id: "general", name: "General" },
  { id: "tech-talk", name: "Tech Talk" },
]);

const voiceChannels = ref([
  { id: "lounge", name: "Lounge" },
  { id: "gaming", name: "Gaming" },
]);

const messages = ref([
  {
    id: 1,
    author: "CyberPunk2077",
    avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=CyberPunk2077",
    text: "Welcome to the Cyber Nexus!",
    timestamp: "2023-05-10 14:30",
  },
  {
    id: 2,
    author: "NeonRider",
    avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=NeonRider",
    text: "Hey everyone, just joined this world. Looks awesome!",
    timestamp: "2023-05-10 14:35",
  },
]);

const onlineUsers = ref([
  {
    id: 1,
    name: "CyberPunk2077",
    avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=CyberPunk2077",
  },
  {
    id: 2,
    name: "NeonRider",
    avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=NeonRider",
  },
]);

const offlineUsers = ref([
  {
    id: 3,
    name: "SynthWave",
    avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=SynthWave",
  },
  {
    id: 4,
    name: "PixelDreamer",
    avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=PixelDreamer",
  },
]);

const activeChannelName = computed(() => {
  const channel = [...textChannels.value, ...voiceChannels.value].find(
    (c) => c.id === activeChannel.value
  );
  return channel ? channel.name : "";
});

const toggleLeftSidebar = () => {
  isLeftSidebarCollapsed.value = !isLeftSidebarCollapsed.value;
};

const setActiveChannel = (channelId) => {
  activeChannel.value = channelId;
};

const sendMessage = () => {
  if (newMessage.value.trim()) {
    messages.value.push({
      id: messages.value.length + 1,
      author: "You",
      avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=You",
      text: newMessage.value,
      timestamp: new Date().toLocaleString(),
    });
    newMessage.value = "";
    scrollToBottom();
  }
};

const scrollToBottom = () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
    }
  });
};

onMounted(() => {
  scrollToBottom();
});
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap");

.nexus-chat {
  display: grid;
  grid-template-columns: 240px 1fr 240px;
  height: 100vh;
  font-family: "Orbitron", sans-serif;
  background-color: #0f1117;
  color: #8b9bb4;
  overflow: hidden;
}

.nexus-chat.collapsed-sidebar {
  grid-template-columns: 60px 1fr 240px;
}

.left-sidebar {
  background-color: #0a0c10;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  border-right: 1px solid #1e2533;
  position: relative;
  transition: width 0.3s ease;
}

.collapse-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
}

.collapse-button img {
  width: 20px;
  height: 20px;
  filter: invert(0.7);
}

.worlds-title {
  color: #4169e1;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

nav ul {
  list-style-type: none;
  padding: 0;
}

.nav-item {
  display: flex;
  align-items: center;
  color: #8b9bb4;
  text-decoration: none;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  border-radius: 4px;
  transition: background-color 0.3s, color 0.3s;
}

.nav-item:hover,
.nav-item.active {
  background-color: #1e2533;
  color: #4169e1;
}

.nav-item img {
  width: 20px;
  height: 20px;
  margin-right: 0.5rem;
  filter: invert(0.7);
}

.create-world-button {
  background-color: #8a2be2;
  color: #ffffff;
  border: none;
  padding: 0.75rem;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  margin-top: 1rem;
  transition: background-color 0.3s;
}

.create-world-button:hover {
  background-color: #9932cc;
}

.your-worlds {
  margin-top: 1rem;
  overflow-y: auto;
}

.your-worlds h3 {
  font-size: 0.9rem;
  color: #8b9bb4;
  margin-bottom: 0.5rem;
}

.your-worlds ul {
  list-style-type: none;
  padding: 0;
}

.your-worlds li {
  display: flex;
  align-items: center;
  padding: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.your-worlds li:hover {
  background-color: #1e2533;
}

.your-worlds li img {
  width: 32px;
  height: 32px;
  margin-right: 0.5rem;
  border-radius: 4px;
}

.world-name {
  flex-grow: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.member-count {
  font-size: 0.7rem;
  color: #4b5563;
  margin-left: auto;
}

.main-content {
  display: grid;
  grid-template-columns: 240px 1fr;
  overflow: hidden;
}

.world-header {
  grid-column: 1 / -1;
  display: flex;
  align-items: center;
  padding: 1rem;
  background-color: #0d1016;
  border-bottom: 1px solid #1e2533;
}

.world-icon {
  width: 48px;
  height: 48px;
  margin-right: 1rem;
  filter: invert(0.7);
}

.world-header h2 {
  color: #4169e1;
  font-size: 1.2rem;
}

.channel-list {
  background-color: #0d1016;
  padding: 1rem;
  border-right: 1px solid #1e2533;
  overflow-y: auto;
}

.channel-list h3 {
  font-size: 0.8rem;
  color: #8b9bb4;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
}

.channel-list ul {
  list-style-type: none;
  padding: 0;
}

.channel-list li {
  padding: 0.25rem 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  transition: color 0.3s;
}

.channel-list li:hover,
.channel-list li.active {
  color: #4169e1;
}

.channel-list li img {
  width: 16px;
  height: 16px;
  margin-right: 0.5rem;
  filter: invert(0.7);
}

.chat-area {
  display: flex;
  flex-direction: column;
}

.chat-header {
  padding: 1rem;
  background-color: #0d1016;
  border-bottom: 1px solid #1e2533;
}

.chat-header h2 {
  color: #4169e1;
  font-size: 1.2rem;
}

.messages {
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
}

.message {
  display: flex;
  margin-bottom: 1rem;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 1rem;
}

.message-content {
  flex-grow: 1;
}

.message-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.25rem;
}

.author {
  font-weight: bold;
  color: #4169e1;
}

.timestamp {
  font-size: 0.8rem;
  color: #4b5563;
}

.message-input {
  display: flex;
  padding: 1rem;
  background-color: #0d1016;
  border-top: 1px solid #1e2533;
}

.message-input input {
  flex-grow: 1;
  background-color: #1e2533;
  border: none;
  padding: 0.5rem;
  border-radius: 4px;
  color: #ffffff;
  font-family: "Orbitron", sans-serif;
}

.message-input button {
  background-color: #4169e1;
  color: #ffffff;
  border: none;
  padding: 0.5rem 1rem;
  margin-left: 0.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-family: "Orbitron", sans-serif;
  transition: background-color 0.3s;
}

.message-input button:hover {
  background-color: #3a5fcd;
}

.right-sidebar {
  background-color: #0a0c10;
  padding: 1rem;
  overflow-y: auto;
  border-left: 1px solid #1e2533;
}

.right-sidebar h3 {
  font-size: 0.8rem;
  color: #8b9bb4;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
}

.right-sidebar ul {
  list-style-type: none;
  padding: 0;
}

.right-sidebar li {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}

.user-name {
  margin-left: 0.5rem;
  flex-grow: 1;
}

.status-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.status-indicator.online {
  background-color: #10b981;
}

.status-indicator.offline {
  background-color: #4b5563;
}

.collapsed-sidebar .left-sidebar {
  width: 60px;
}

.collapsed-sidebar .worlds-title,
.collapsed-sidebar .nav-item span,
.collapsed-sidebar .create-world-button,
.collapsed-sidebar .your-worlds h3,
.collapsed-sidebar .world-name,
.collapsed-sidebar .member-count {
  display: none;
}

.collapsed-sidebar .nav-item {
  justify-content: center;
}

.collapsed-sidebar .nav-item img {
  margin-right: 0;
}

.collapsed-sidebar .your-worlds li {
  justify-content: center;
}

.collapsed-sidebar .your-worlds li img {
  margin-right: 0;
}

@media (max-width: 1024px) {
  .nexus-chat {
    grid-template-columns: 1fr;
  }

  .left-sidebar,
  .right-sidebar {
    display: none;
  }

  .main-content {
    grid-template-columns: 1fr;
  }

  .channel-list {
    display: none;
  }
}
</style>
