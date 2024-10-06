<template>
  <div class="app-container">
    <div class="left-sidebar">
      <h1 class="logo glitch" data-text="NEXUS">NEXUS</h1>
      <nav>
        <ul>
          <li>
            <a href="#" class="nav-item" @click="setActiveView('worlds')"
              ><img
                src="https://api.iconify.design/lucide:globe.svg"
                alt="Worlds"
              />
              WORLDS</a
            >
          </li>
          <li>
            <a href="#" class="nav-item" @click="setActiveView('friends')"
              ><img
                src="https://api.iconify.design/lucide:users.svg"
                alt="Friends"
              />
              FRIENDS</a
            >
          </li>
          <li>
            <a href="#" class="nav-item" @click="setActiveView('settings')"
              ><img
                src="https://api.iconify.design/lucide:settings.svg"
                alt="Settings"
              />
              SETTINGS</a
            >
          </li>
        </ul>
      </nav>
      <div class="create-world-button" @click="createWorld">
        <img
          src="https://api.iconify.design/lucide:plus-circle.svg"
          alt="Create World"
        />
        CREATE WORLD
      </div>
    </div>
    <div class="main-content">
      <div class="world-header">
        <h2 class="world-name">WORLD</h2>
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
      </div>
      <div class="chat-area">
        <div class="chat-header">
          <h2># {{ activeChannelName }}</h2>
          <div class="header-icons">
            <img
              src="https://api.iconify.design/lucide:bell.svg"
              alt="Notifications"
              @click="toggleNotifications"
            />
            <img
              src="https://api.iconify.design/lucide:users.svg"
              alt="Members"
              @click="toggleMembersList"
            />
            <img
              src="https://api.iconify.design/lucide:search.svg"
              alt="Search"
              @click="toggleSearch"
            />
            <img
              src="https://api.iconify.design/lucide:message-square.svg"
              alt="Messages"
              @click="setActiveView('messages')"
            />
          </div>
        </div>
        <div class="messages" ref="chatMessages">
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
    <div class="right-sidebar" :class="{ 'show-members': showMembers }">
      <div class="online-users">
        <h3>ONLINE - {{ onlineMembers.length }}</h3>
        <ul>
          <li v-for="member in onlineMembers" :key="member.id">
            <img :src="member.avatar" :alt="member.name" class="avatar" />
            <span class="member-name">{{ member.name }}</span>
            <span class="status-indicator online"></span>
          </li>
        </ul>
      </div>
      <div class="offline-users">
        <h3>OFFLINE - {{ offlineMembers.length }}</h3>
        <ul>
          <li v-for="member in offlineMembers" :key="member.id">
            <img :src="member.avatar" :alt="member.name" class="avatar" />
            <span class="member-name">{{ member.name }}</span>
            <span class="status-indicator offline"></span>
          </li>
        </ul>
      </div>
    </div>
    <div class="user-audio-controls">
      <img
        src="https://api.iconify.design/lucide:mic.svg"
        alt="Microphone"
        @click="toggleMic"
        :class="{ active: micActive }"
      />
      <img
        src="https://api.iconify.design/lucide:headphones.svg"
        alt="Headphones"
        @click="toggleHeadphones"
        :class="{ active: headphonesActive }"
      />
      <span class="user-name">Your Username</span>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from "vue";

const activeView = ref("worlds");
const activeChannel = ref("general");
const newMessage = ref("");
const chatMessages = ref(null);
const showMembers = ref(false);
const micActive = ref(false);
const headphonesActive = ref(false);

const textChannels = ref([
  { id: "general", name: "General" },
  { id: "tech-talk", name: "Tech Talk" },
  { id: "random", name: "Random" },
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

const members = ref([
  {
    id: 1,
    name: "CyberPunk2077",
    avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=CyberPunk2077",
    status: "online",
  },
  {
    id: 2,
    name: "NeonRider",
    avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=NeonRider",
    status: "online",
  },
  {
    id: 3,
    name: "SynthWave",
    avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=SynthWave",
    status: "offline",
  },
  {
    id: 4,
    name: "PixelDreamer",
    avatar: "https://api.dicebear.com/6.x/pixel-art/svg?seed=PixelDreamer",
    status: "offline",
  },
]);

const onlineMembers = computed(() =>
  members.value.filter((member) => member.status === "online")
);
const offlineMembers = computed(() =>
  members.value.filter((member) => member.status === "offline")
);

const activeChannelName = computed(() => {
  const channel = [...textChannels.value, ...voiceChannels.value].find(
    (c) => c.id === activeChannel.value
  );
  return channel ? channel.name : "";
});

const setActiveView = (view) => {
  activeView.value = view;
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
    if (chatMessages.value) {
      chatMessages.value.scrollTop = chatMessages.value.scrollHeight;
    }
  });
};

const toggleNotifications = () => {
  // Implement notification toggle logic
  console.log("Notifications toggled");
};

const toggleMembersList = () => {
  showMembers.value = !showMembers.value;
};

const toggleSearch = () => {
  // Implement search toggle logic
  console.log("Search toggled");
};

const createWorld = () => {
  // Implement world creation logic
  console.log("Creating a new world");
};

const toggleMic = () => {
  micActive.value = !micActive.value;
};

const toggleHeadphones = () => {
  headphonesActive.value = !headphonesActive.value;
};

onMounted(() => {
  scrollToBottom();
});
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap");

.app-container {
  display: grid;
  grid-template-columns: 200px 1fr 240px;
  grid-template-rows: 1fr auto;
  height: 100vh;
  font-family: "Orbitron", sans-serif;
  background-color: #1a1b26;
  color: #a9b1d6;
}

.left-sidebar,
.right-sidebar,
.world-header {
  background-color: #16161e;
  padding: 1rem;
}

.left-sidebar {
  grid-row: 1 / 3;
  border-right: 1px solid #2f3240;
  display: flex;
  flex-direction: column;
}

.logo {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  text-align: center;
  color: #7aa2f7;
}

.nav-item {
  display: flex;
  align-items: center;
  color: #a9b1d6;
  text-decoration: none;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-item:hover {
  background-color: #2f3240;
}

.nav-item img {
  width: 20px;
  height: 20px;
  margin-right: 0.5rem;
  filter: invert(0.7);
}

.create-world-button {
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #7aa2f7;
  color: #1a1b26;
  padding: 0.75rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.create-world-button:hover {
  background-color: #5d86e6;
}

.create-world-button img {
  width: 20px;
  height: 20px;
  margin-right: 0.5rem;
  filter: invert(1);
}

.main-content {
  display: grid;
  grid-template-rows: auto 1fr;
}

.world-header {
  border-bottom: 1px solid #2f3240;
}

.world-name {
  font-size: 1.2rem;
  margin-bottom: 1rem;
  color: #7aa2f7;
}

.channel-list h3 {
  font-size: 0.8rem;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
  color: #565f89;
}

.channel-list ul {
  list-style-type: none;
  padding: 0;
}

.channel-list li {
  padding: 0.25rem 0;
  cursor: pointer;
  transition: color 0.3s;
}

.channel-list li:hover,
.channel-list li.active {
  color: #7aa2f7;
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
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #1a1b26;
  border-bottom: 1px solid #2f3240;
}

.chat-header h2 {
  font-size: 1.2rem;
  color: #7aa2f7;
}

.header-icons {
  display: flex;
  gap: 1rem;
}

.header-icons img {
  width: 20px;
  height: 20px;
  filter: invert(0.7);
  cursor: pointer;
  transition: filter 0.3s;
}

.header-icons img:hover {
  filter: invert(0.9);
}

.messages {
  flex-grow: 1;
  overflow-y: auto;
  padding: 1rem;
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
  color: #7aa2f7;
}

.timestamp {
  font-size: 0.8rem;
  color: #565f89;
}

.message-input {
  display: flex;
  padding: 1rem;
  background-color: #1a1b26;
  border-top: 1px solid #2f3240;
}

.message-input input {
  flex-grow: 1;
  background-color: #24283b;
  border: none;
  padding: 0.5rem;
  border-radius: 4px;
  color: #a9b1d6;
  font-family: "Orbitron", sans-serif;
}

.message-input button {
  background-color: #7aa2f7;
  color: #1a1b26;
  border: none;
  padding: 0.5rem 1rem;
  margin-left: 0.5rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.message-input button:hover {
  background-color: #5d86e6;
}

.right-sidebar {
  grid-column: 3;
  grid-row: 1 / 3;
  border-left: 1px solid #2f3240;
  overflow-y: auto;
  transition: transform 0.3s ease-in-out;
}

.right-sidebar.show-members {
  transform: translateX(0);
}

.right-sidebar h3 {
  font-size: 0.8rem;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
  color: #565f89;
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

.member-name {
  margin-left: 0.5rem;
  flex-grow: 1;
}

.status-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.status-indicator.online {
  background-color: #9ece6a;
}

.status-indicator.offline {
  background-color: #565f89;
}

.user-audio-controls {
  grid-column: 1 / 4;
  display: flex;
  align-items: center;
  padding: 0.5rem 1rem;
  background-color: #16161e;
  border-top: 1px solid #2f3240;
}

.user-audio-controls img {
  width: 20px;
  height: 20px;
  margin-right: 1rem;
  filter: invert(0.7);
  cursor: pointer;
  transition: filter 0.3s;
}

.user-audio-controls img:hover,
.user-audio-controls img.active {
  filter: invert(0.9);
}

.user-name {
  margin-left: auto;
  color: #7aa2f7;
}

.glitch {
  position: relative;
  color: #7aa2f7;
  text-shadow: 0 0 10px #7aa2f7;
}

.glitch::before,
.glitch::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.glitch::before {
  left: 2px;
  text-shadow: -2px 0 #ff79c6;
  animation: glitch-animation 3s infinite linear alternate-reverse;
}

.glitch::after {
  left: -2px;
  text-shadow: 2px 0 #bd93f9;
  animation: glitch-animation 2s infinite linear alternate-reverse;
}

@keyframes glitch-animation {
  0% {
    clip-path: inset(71% 0 10% 0);
  }
  20% {
    clip-path: inset(29% 0 71% 0);
  }
  40% {
    clip-path: inset(57% 0 43% 0);
  }
  60% {
    clip-path: inset(14% 0 86% 0);
  }
  80% {
    clip-path: inset(100% 0 1% 0);
  }
  100% {
    clip-path: inset(43% 0 57% 0);
  }
}

@media (max-width: 768px) {
  .app-container {
    grid-template-columns: 1fr;
  }

  .left-sidebar,
  .right-sidebar {
    display: none;
  }

  .main-content {
    grid-column: 1;
  }

  .user-audio-controls {
    grid-column: 1;
  }
}
</style>
