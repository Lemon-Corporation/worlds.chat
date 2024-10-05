<template>
  <div class="world-room">
    <div class="cyber-lines"></div>
    <div class="sidebar">
      <h1 class="world-name glitch" data-text="CYBER NEXUS">WORLD</h1>
      <div class="channels">
        <h2 class="channel-category">Text Channels</h2>
        <div
          v-for="channel in textChannels"
          :key="channel.id"
          :class="['channel-item', { active: channel.id === activeChannel }]"
          @click="setActiveChannel(channel.id)"
        >
          <img
            src="https://api.iconify.design/lucide:hash.svg"
            alt="Text Channel"
          />
          {{ channel.name }}
        </div>
        <h2 class="channel-category">Voice Channels</h2>
        <div
          v-for="channel in voiceChannels"
          :key="channel.id"
          :class="['channel-item', { active: channel.id === activeChannel }]"
          @click="setActiveChannel(channel.id)"
        >
          <img
            src="https://api.iconify.design/lucide:mic.svg"
            alt="Voice Channel"
          />
          {{ channel.name }}
        </div>
      </div>
    </div>
    <div class="main-content">
      <div class="chat-header">
        <h2># {{ activeChannelName }}</h2>
        <div class="header-icons">
          <img
            v-for="icon in headerIcons"
            :key="icon.alt"
            :src="icon.src"
            :alt="icon.alt"
          />
        </div>
      </div>
      <div class="chat-messages" ref="chatMessages">
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
          type="text"
          :placeholder="`Message #${activeChannelName}`"
        />
        <button @click="sendMessage" class="send-btn">Send</button>
      </div>
    </div>
    <div class="member-list">
      <h2 class="member-category">Online - {{ onlineMembers.length }}</h2>
      <div v-for="member in onlineMembers" :key="member.id" class="member-item">
        <img :src="member.avatar" :alt="member.name" class="avatar" />
        <span class="member-name">{{ member.name }}</span>
        <span class="status-indicator online"></span>
      </div>
      <h2 class="member-category">Offline - {{ offlineMembers.length }}</h2>
      <div
        v-for="member in offlineMembers"
        :key="member.id"
        class="member-item"
      >
        <img :src="member.avatar" :alt="member.name" class="avatar" />
        <span class="member-name">{{ member.name }}</span>
        <span class="status-indicator offline"></span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from "vue";

const activeChannel = ref("general");
const newMessage = ref("");
const chatMessages = ref(null);

const textChannels = ref([
  { id: "general", name: "General" },
  { id: "tech-talk", name: "Tech Talk" },
  { id: "random", name: "Random" },
]);

const voiceChannels = ref([
  { id: "lounge", name: "Lounge" },
  { id: "gaming", name: "Gaming" },
]);

const headerIcons = ref([
  { src: "https://api.iconify.design/lucide:bell.svg", alt: "Notifications" },
  { src: "https://api.iconify.design/lucide:users.svg", alt: "Members" },
  { src: "https://api.iconify.design/lucide:search.svg", alt: "Search" },
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

onMounted(() => {
  scrollToBottom();
});
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap");

.world-room {
  font-family: "Orbitron", sans-serif;
  display: flex;
  height: 100vh;
  background-color: var(--bg-main);
  color: var(--text-primary);
  position: relative;
  overflow: hidden;
}

.cyber-lines {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 0;
}

.cyber-lines::before,
.cyber-lines::after {
  content: "";
  position: absolute;
  width: 200vw;
  height: 200vh;
  top: -50%;
  left: -50%;
  background-image: linear-gradient(
      0deg,
      transparent 24%,
      rgba(108, 92, 231, 0.05) 25%,
      rgba(108, 92, 231, 0.05) 26%,
      transparent 27%,
      transparent 74%,
      rgba(108, 92, 231, 0.05) 75%,
      rgba(108, 92, 231, 0.05) 76%,
      transparent 77%,
      transparent
    ),
    linear-gradient(
      90deg,
      transparent 24%,
      rgba(108, 92, 231, 0.05) 25%,
      rgba(108, 92, 231, 0.05) 26%,
      transparent 27%,
      transparent 74%,
      rgba(108, 92, 231, 0.05) 75%,
      rgba(108, 92, 231, 0.05) 76%,
      transparent 77%,
      transparent
    );
  background-size: 50px 50px;
}

.cyber-lines::after {
  background-position: 25px 25px;
}

.sidebar {
  width: 240px;
  background-color: var(--bg-sidebar);
  padding: 20px;
  overflow-y: auto;
  z-index: 1;
}

.world-name {
  font-size: 1.5rem;
  margin-bottom: 20px;
  text-align: center;
}

.glitch {
  position: relative;
  color: var(--text-primary);
  text-shadow: 0 0 10px var(--accent-purple);
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
  text-shadow: -2px 0 var(--accent-cyan);
  animation: glitch-animation 3s infinite linear alternate-reverse;
}

.glitch::after {
  left: -2px;
  text-shadow: 2px 0 var(--accent-purple);
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

.channel-category {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin-top: 20px;
  margin-bottom: 10px;
  text-transform: uppercase;
}

.channel-item {
  display: flex;
  align-items: center;
  padding: 8px;
  margin-bottom: 5px;
  cursor: pointer;
  border-radius: 4px;
  transition: var(--transition);
}

.channel-item:hover,
.channel-item.active {
  background-color: var(--bg-card);
  color: var(--text-primary);
}

.channel-item img {
  width: 16px;
  height: 16px;
  margin-right: 8px;
  filter: invert(0.7);
}

.main-content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  z-index: 1;
}

.chat-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background-color: var(--bg-sidebar);
  border-bottom: 1px solid var(--accent-purple);
}

.header-icons {
  display: flex;
  gap: 15px;
}

.header-icons img {
  width: 20px;
  height: 20px;
  filter: invert(1);
  cursor: pointer;
  transition: var(--transition);
}

.header-icons img:hover {
  transform: scale(1.1);
}

.chat-messages {
  flex-grow: 1;
  padding: 20px;
  overflow-y: auto;
}

.message {
  display: flex;
  margin-bottom: 20px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.message-content {
  flex-grow: 1;
}

.message-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.author {
  font-weight: bold;
  color: var(--accent-cyan);
}

.timestamp {
  font-size: 0.8rem;
  color: var(--text-secondary);
}

.message-input {
  display: flex;
  padding: 15px;
  background-color: var(--bg-sidebar);
}

.message-input input {
  flex-grow: 1;
  background-color: var(--bg-card);
  border: none;
  padding: 10px;
  border-radius: 4px;
  color: var(--text-primary);
  font-family: "Orbitron", sans-serif;
}

.send-btn {
  background-color: var(--accent-purple);
  color: var(--text-primary);
  border: none;
  padding: 10px 20px;
  margin-left: 10px;
  border-radius: 4px;
  cursor: pointer;
  transition: var(--transition);
}

.send-btn:hover {
  background-color: var(--accent-hover);
}

.member-list {
  width: 240px;
  background-color: var(--bg-sidebar);
  padding: 20px;
  overflow-y: auto;
  z-index: 1;
}

.member-category {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin-top: 20px;
  margin-bottom: 10px;
  text-transform: uppercase;
}

.member-item {
  display: flex;
  align-items: center;
  padding: 8px;
  margin-bottom: 5px;
}

.member-name {
  margin-left: 10px;
  flex-grow: 1;
}

.status-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.status-indicator.online {
  background-color: #2ecc71;
}

.status-indicator.offline {
  background-color: #95a5a6;
}

@media (max-width: 768px) {
  .world-room {
    flex-direction: column;
  }

  .sidebar,
  .member-list {
    width: 100%;
    max-height: 200px;
  }

  .main-content {
    flex-grow: 1;
  }
}
</style>
