<template>
  <div
    class="nexus-chat"
    :class="{ 'collapsed-sidebar': isLeftSidebarCollapsed }"
  >
    <!-- Left Sidebar -->
    <div class="left-sidebar" :class="{ collapsed: isLeftSidebarCollapsed }">
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
      <!-- World Banner -->
      <div class="world-banner">
        <img
          src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/_b125fe34-4499-4159-b13f-ffa887ae619c-ui4a4GVkfm80f4pF5DTAmEh1pjY0o3.jpeg"
          alt="World Banner"
          class="banner-image"
        />
        <div class="banner-overlay">
          <h1>WORLD</h1>
        </div>
      </div>

      <!-- World Header -->
      <div class="world-header">
        <img
          src="https://api.iconify.design/game-icons:fire-dash.svg"
          alt="World Icon"
          class="world-icon"
        />
        <h2>WORLD</h2>
        <div class="world-settings">
          <button @click="openWorldSettings" class="settings-button">
            <img
              src="https://api.iconify.design/lucide:settings.svg"
              alt="Settings"
            />
          </button>
          <button @click="openInviteModal" class="invite-button">
            <img
              src="https://api.iconify.design/lucide:user-plus.svg"
              alt="Invite"
            />
          </button>
        </div>
      </div>

      <!-- Channel List -->
      <div class="channel-list" :class="{ show: showChannelList }">
        <button @click="toggleChannelList" class="toggle-channel-list">
          {{ showChannelList ? "Hide Channels" : "Show Channels" }}
        </button>
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
    <div class="right-sidebar" :class="{ show: showRightSidebar }">
      <button @click="toggleRightSidebar" class="toggle-right-sidebar">
        {{ showRightSidebar ? "Hide Users" : "Show Users" }}
      </button>
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

    <!-- World Settings Modal -->
    <div v-if="showWorldSettings" class="modal">
      <div class="modal-content">
        <h2>World Settings</h2>
        <button @click="closeWorldSettings" class="close-button">×</button>
        <div class="settings-form">
          <label for="worldName">World Name:</label>
          <input type="text" id="worldName" v-model="worldSettings.name" />
          <label for="worldDescription">Description:</label>
          <textarea
            id="worldDescription"
            v-model="worldSettings.description"
          ></textarea>
          <button @click="saveWorldSettings" class="save-button">
            Save Changes
          </button>
        </div>
      </div>
    </div>

    <!-- Invite Modal -->
    <div v-if="showInviteModal" class="modal">
      <div class="modal-content">
        <h2>Invite Users</h2>
        <button @click="closeInviteModal" class="close-button">×</button>
        <div class="invite-form">
          <input type="text" v-model="inviteLink" readonly />
          <button @click="copyInviteLink" class="copy-button">Copy Link</button>
        </div>
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
const showWorldSettings = ref(false);
const showInviteModal = ref(false);
const inviteLink = ref("https://worlds.chat/invite/WORLD123");
const showChannelList = ref(false);
const showRightSidebar = ref(false);

const worldSettings = ref({
  name: "WORLD",
  description: "Welcome to our amazing world!",
});

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

const openWorldSettings = () => {
  showWorldSettings.value = true;
};

const closeWorldSettings = () => {
  showWorldSettings.value = false;
};

const saveWorldSettings = () => {
  console.log("Saving world settings:", worldSettings.value);
  closeWorldSettings();
};

const openInviteModal = () => {
  showInviteModal.value = true;
};

const closeInviteModal = () => {
  showInviteModal.value = false;
};

const copyInviteLink = () => {
  navigator.clipboard.writeText(inviteLink.value).then(() => {
    alert("Invite link copied to clipboard!");
  });
};

const toggleChannelList = () => {
  showChannelList.value = !showChannelList.value;
};

const toggleRightSidebar = () => {
  showRightSidebar.value = !showRightSidebar.value;
};

onMounted(() => {
  scrollToBottom();
});
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap");

.nexus-chat {
  display: grid;
  grid-template-columns: auto 1fr auto;
  height: 100vh;
  font-family: "Orbitron", sans-serif;
  background-color: #0f1117;
  color: #8b9bb4;
  overflow: hidden;
}

.left-sidebar {
  background-color: #0a0c10;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  border-right: 1px solid #1e2533;
  position: relative;
  transition: all 0.3s ease;
  width: 240px;
}

.left-sidebar.collapsed {
  width: 60px;
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
  grid-template-columns: auto 1fr;
  grid-template-rows: auto auto 1fr;
  overflow: hidden;
}

.world-banner {
  grid-column: 1 / -1;
  position: relative;
  width: 100%;
  height: 120px;
  overflow: hidden;
}

.banner-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.banner-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.banner-overlay h1 {
  color: #ffffff;
  font-size: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.world-header {
  grid-column: 1 / -1;
  display: flex;
  align-items: center;
  padding: 0.5rem 1rem;
  background-color: rgba(13, 16, 22, 0.8);
  border-bottom: 1px solid #1e2533;
}

.world-icon {
  width: 32px;
  height: 32px;
  margin-right: 0.5rem;
  filter: invert(0.7);
}

.world-header h2 {
  color: #4169e1;
  font-size: 1rem;
  flex-grow: 1;
}

.world-settings {
  display: flex;
  gap: 0.5rem;
}

.settings-button,
.invite-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
}

.settings-button img,
.invite-button img {
  width: 20px;
  height: 20px;
  filter: invert(0.7);
}

.channel-list {
  background-color: #0d1016;
  padding: 1rem;
  border-right: 1px solid #1e2533;
  overflow-y: auto;
  transition: all 0.3s ease;
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
  height: calc(95vh - 160px);
}

.chat-header {
  padding: 0.5rem 1rem;
  background-color: #0d1016;
  border-bottom: 1px solid #1e2533;
}

.chat-header h2 {
  color: #4169e1;
  font-size: 1rem;
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
  transition: all 0.3s ease;
  width: 240px;
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

.modal {
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #1e2533;
  padding: 2rem;
  border-radius: 8px;
  width: 80%;
  max-width: 500px;
  position: relative;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 1.5rem;
  background: none;
  border: none;
  color: #8b9bb4;
  cursor: pointer;
}

.settings-form,
.invite-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.settings-form label {
  color: #8b9bb4;
}

.settings-form input,
.settings-form textarea,
.invite-form input {
  background-color: #0d1016;
  border: 1px solid #1e2533;
  color: #ffffff;
  padding: 0.5rem;
  border-radius: 4px;
  font-family: "Orbitron", sans-serif;
}

.save-button,
.copy-button {
  background-color: #4169e1;
  color: #ffffff;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-family: "Orbitron", sans-serif;
  transition: background-color 0.3s;
}

.save-button:hover,
.copy-button:hover {
  background-color: #3a5fcd;
}

.toggle-channel-list,
.toggle-right-sidebar {
  display: none;
  width: 100%;
  padding: 0.5rem;
  background-color: #4169e1;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family: "Orbitron", sans-serif;
  margin-bottom: 1rem;
}

@media (max-width: 1024px) {
  .nexus-chat {
    grid-template-columns: 1fr;
  }

  .left-sidebar {
    position: fixed;
    left: -240px;
    top: 0;
    bottom: 0;
    z-index: 1000;
  }

  .left-sidebar.collapsed {
    left: 0;
  }

  .main-content {
    grid-template-columns: 1fr;
  }

  .channel-list {
    position: fixed;
    left: -240px;
    top: 0;
    bottom: 0;
    z-index: 999;
    width: 240px;
  }

  .channel-list.show {
    left: 0;
  }

  .right-sidebar {
    position: fixed;
    right: -240px;
    top: 0;
    bottom: 0;
    z-index: 998;
  }

  .right-sidebar.show {
    right: 0;
  }

  .toggle-channel-list,
  .toggle-right-sidebar {
    display: block;
  }

  .world-banner {
    height: 100px;
  }

  .banner-overlay h1 {
    font-size: 1.5rem;
  }
}

@media (min-width: 1025px) and (max-width: 1440px) {
  .nexus-chat {
    grid-template-columns: auto 1fr auto;
  }

  .left-sidebar,
  .right-sidebar {
    width: 200px;
  }
}

@media (min-width: 1441px) {
  .nexus-chat {
    grid-template-columns: auto 1fr auto;
  }

  .left-sidebar,
  .right-sidebar {
    width: 280px;
  }
}

@media (min-width: 2560px) {
  .nexus-chat {
    max-width: 2560px;
    margin: 0 auto;
  }

  .left-sidebar,
  .right-sidebar {
    width: 320px;
  }

  .world-banner {
    height: 180px;
  }

  .banner-overlay h1 {
    font-size: 3rem;
  }
}
</style>
