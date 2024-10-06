<template>
    <div class="nexus-chat">
      <div class="left-sidebar">
        <h1 class="logo glitch" data-text="NEXUS">NEXUS</h1>
        <nav>
          <ul>
            <li><a href="#" class="nav-item active"><img src="https://api.iconify.design/lucide:globe.svg" alt="Worlds" /> WORLDS</a></li>
            <li><a href="#" class="nav-item"><img src="https://api.iconify.design/lucide:users.svg" alt="Friends" /> FRIENDS</a></li>
            <li><a href="#" class="nav-item"><img src="https://api.iconify.design/lucide:settings.svg" alt="Settings" /> SETTINGS</a></li>
          </ul>
        </nav>
        <button class="create-world-button">
          <img src="https://api.iconify.design/lucide:plus-circle.svg" alt="Create World" />
          CREATE WORLD
        </button>
        <button class="private-message-button" @click="togglePrivateMessages">
          <img src="https://api.iconify.design/lucide:message-square.svg" alt="Private Messages" />
          MESSAGES
        </button>
      </div>
      <div class="main-content">
        <div class="world-header">
          <h2>WORLD</h2>
          <div class="channel-list">
            <h3>TEXT CHANNELS</h3>
            <ul>
              <li v-for="channel in textChannels" :key="channel.id" 
                  :class="{ active: channel.id === activeChannel }"
                  @click="setActiveChannel(channel.id)">
                # {{ channel.name }}
              </li>
            </ul>
            <h3>VOICE CHANNELS</h3>
            <ul>
              <li v-for="channel in voiceChannels" :key="channel.id" 
                  :class="{ active: channel.id === activeChannel }"
                  @click="setActiveChannel(channel.id)">
                <img src="https://api.iconify.design/lucide:mic.svg" alt="Voice Channel" /> {{ channel.name }}
              </li>
            </ul>
          </div>
        </div>
        <div class="chat-area">
          <div class="chat-header">
            <h2># {{ activeChannelName }}</h2>
            <div class="header-icons">
              <img src="https://api.iconify.design/lucide:bell.svg" alt="Notifications" @click="toggleNotifications" />
              <img src="https://api.iconify.design/lucide:users.svg" alt="Members" @click="toggleMembersList" />
              <img src="https://api.iconify.design/lucide:search.svg" alt="Search" @click="toggleSearch" />
              <img src="https://api.iconify.design/lucide:message-square.svg" alt="Threads" @click="toggleThreads" />
            </div>
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
            <input v-model="newMessage" @keyup.enter="sendMessage" :placeholder="`Message #${activeChannelName}`" />
            <button @click="sendMessage">Send</button>
          </div>
        </div>
      </div>
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
      <transition name="modal">
        <div v-if="showPrivateMessages" class="modal private-messages-modal">
          <h2>Private Messages</h2>
          <ul class="private-message-list">
            <li v-for="conversation in privateConversations" :key="conversation.id" @click="openPrivateChat(conversation.id)">
              <img :src="conversation.avatar" :alt="conversation.name" class="avatar" />
              <div class="conversation-info">
                <span class="conversation-name">{{ conversation.name }}</span>
                <span class="last-message">{{ conversation.lastMessage }}</span>
              </div>
            </li>
          </ul>
          <button @click="togglePrivateMessages" class="close-button">Close</button>
        </div>
      </transition>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted, nextTick } from 'vue';
  
  const activeChannel = ref('general');
  const newMessage = ref('');
  const messagesContainer = ref(null);
  const showPrivateMessages = ref(false);
  
  const textChannels = ref([
    { id: 'general', name: 'General' },
    { id: 'tech-talk', name: 'Tech Talk' },
    { id: 'random', name: 'Random' },
  ]);
  
  const voiceChannels = ref([
    { id: 'lounge', name: 'Lounge' },
    { id: 'gaming', name: 'Gaming' },
  ]);
  
  const messages = ref([
    {
      id: 1,
      author: 'CyberPunk2077',
      avatar: 'https://api.dicebear.com/6.x/pixel-art/svg?seed=CyberPunk2077',
      text: 'Welcome to the Cyber Nexus!',
      timestamp: '2023-05-10 14:30',
    },
    {
      id: 2,
      author: 'NeonRider',
      avatar: 'https://api.dicebear.com/6.x/pixel-art/svg?seed=NeonRider',
      text: 'Hey everyone, just joined this world. Looks awesome!',
      timestamp: '2023-05-10 14:35',
    },
  ]);
  
  const onlineUsers = ref([
    { id: 1, name: 'CyberPunk2077', avatar: 'https://api.dicebear.com/6.x/pixel-art/svg?seed=CyberPunk2077' },
    { id: 2, name: 'NeonRider', avatar: 'https://api.dicebear.com/6.x/pixel-art/svg?seed=NeonRider' },
  ]);
  
  const offlineUsers = ref([
    { id: 3, name: 'SynthWave', avatar: 'https://api.dicebear.com/6.x/pixel-art/svg?seed=SynthWave' },
    { id: 4, name: 'PixelDreamer', avatar: 'https://api.dicebear.com/6.x/pixel-art/svg?seed=PixelDreamer' },
  ]);
  
  const privateConversations = ref([
    { id: 1, name: 'NeonRider', avatar: 'https://api.dicebear.com/6.x/pixel-art/svg?seed=NeonRider', lastMessage: 'Hey, how are you?' },
    { id: 2, name: 'SynthWave', avatar: 'https://api.dicebear.com/6.x/pixel-art/svg?seed=SynthWave', lastMessage: 'Did you see the new world?' },
  ]);
  
  const activeChannelName = computed(() => {
    const channel = [...textChannels.value, ...voiceChannels.value].find(c => c.id === activeChannel.value);
    return channel ? channel.name : '';
  });
  
  const setActiveChannel = (channelId) => {
    activeChannel.value = channelId;
  };
  
  const sendMessage = () => {
    if (newMessage.value.trim()) {
      messages.value.push({
        id: messages.value.length + 1,
        author: 'You',
        avatar: 'https://api.dicebear.com/6.x/pixel-art/svg?seed=You',
        text: newMessage.value,
        timestamp: new Date().toLocaleString(),
      });
      newMessage.value = '';
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
  
  const togglePrivateMessages = () => {
    showPrivateMessages.value = !showPrivateMessages.value;
  };
  
  const openPrivateChat = (conversationId) => {
    console.log(`Opening private chat: ${conversationId}`);
    // Implement private chat logic here
  };
  
  const toggleNotifications = () => {
    console.log('Toggling notifications');
    // Implement notification toggle logic here
  };
  
  const toggleMembersList = () => {
    console.log('Toggling members list');
    // Implement members list toggle logic here
  };
  
  const toggleSearch = () => {
    console.log('Toggling search');
    // Implement search toggle logic here
  };
  
  const toggleThreads = () => {
    console.log('Toggling threads');
    // Implement threads toggle logic here
  };
  
  onMounted(() => {
    scrollToBottom();
  });
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap');
  
  .nexus-chat {
    display: grid;
    grid-template-columns: 240px 1fr 240px;
    height: 100vh;
    font-family: 'Orbitron', sans-serif;
    background-color: #0f1117;
    color: #8b9bb4;
    overflow: hidden;
  }
  
  .nexus-chat::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: 
      linear-gradient(0deg, transparent 24%, rgba(32, 67, 98, 0.05) 25%, rgba(32, 67, 98, 0.05) 26%, transparent 27%, transparent 74%, rgba(32, 67, 98, 0.05) 75%, rgba(32, 67, 98, 0.05) 76%, transparent 77%, transparent),
      linear-gradient(90deg, transparent 24%, rgba(32, 67, 98, 0.05) 25%, rgba(32, 67, 98, 0.05) 26%, transparent 27%, transparent 74%, rgba(32, 67, 98, 0.05) 75%, rgba(32, 67, 98, 0.05) 76%, transparent 77%, transparent);
    background-size: 50px 50px;
    z-index: -1;
  }
  
  .left-sidebar {
    background-color: #0a0c10;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    border-right: 1px solid #1e2533;
  }
  
  .logo {
    font-size: 2rem;
    color: #3b82f6;
    margin-bottom: 2rem;
    text-align: center;
    position: relative;
  }
  
  .glitch {
    position: relative;
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
    text-shadow: -2px 0 #ff00ff;
    clip: rect(44px, 450px, 56px, 0);
    animation: glitch-anim 5s infinite linear alternate-reverse;
  }
  
  .glitch::after {
    left: -2px;
    text-shadow: 2px 0 #00ffff;
    clip: rect(44px, 450px, 56px, 0);
    animation: glitch-anim 5s infinite linear alternate-reverse;
  }
  
  @keyframes glitch-anim {
    0% {
      clip: rect(31px, 9999px, 94px, 0);
    }
    4.166666667% {
      clip: rect(91px, 9999px, 43px, 0);
    }
    8.333333333% {
      clip: rect(85px, 9999px, 30px, 0);
    }
    12.5% {
      clip: rect(57px, 9999px, 67px, 0);
    }
    16.66666667% {
      clip: rect(100px, 9999px, 98px, 0);
    }
    20.83333333% {
      clip: rect(29px, 9999px, 97px, 0);
    }
    25% {
      clip: rect(4px, 9999px, 58px, 0);
    }
    29.16666667% {
      clip: rect(57px, 9999px, 30px, 0);
    }
    33.33333333% {
      clip: rect(86px, 9999px, 82px, 0);
    }
    37.5% {
      clip: rect(80px, 9999px, 3px, 0);
    }
    41.66666667% {
      clip: rect(4px, 9999px, 8px, 0);
    }
    45.83333333% {
      clip: rect(77px, 9999px, 64px, 0);
    }
    50% {
      clip: rect(89px, 9999px, 98px, 0);
    }
    54.16666667% {
      clip: rect(65px, 9999px, 71px, 0);
    }
    58.33333333% {
      clip: rect(93px, 9999px, 77px, 0);
    }
    62.5% {
      clip: rect(14px, 9999px, 13px, 0);
    }
    66.66666667% {
      clip: rect(46px, 9999px, 50px, 0);
    }
    70.83333333% {
      clip: rect(71px, 9999px, 57px, 0);
    }
    75% {
      clip: rect(73px, 9999px, 90px, 0);
    }
    79.16666667% {
      clip: rect(60px, 9999px, 89px, 0);
    }
    83.33333333% {
      clip: rect(72px, 9999px, 87px, 0);
    }
    87.5% {
      clip: rect(35px, 9999px, 54px, 0);
    }
    91.66666667% {
      clip: rect(51px, 9999px, 21px, 0);
    }
    95.83333333% {
      clip: rect(89px, 9999px, 99px, 0);
    }
    100% {
      clip: rect(54px, 9999px, 78px, 0);
    }
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
  
  .nav-item:hover, .nav-item.active {
    background-color: #1e2533;
    color: #3b82f6;
  }
  
  .nav-item img {
    width: 20px;
    height: 20px;
    margin-right: 0.5rem;
    filter: invert(0.7);
  }
  
  .create-world-button, .private-message-button {
    background-color: #1e2533;
    color: #3b82f6;
    border: none;
    padding: 0.75rem;
    border-radius: 4px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-top: 1rem;
    transition: background-color 0.3s, transform 0.3s;
  }
  
  .create-world-button:hover, .private-message-button:hover {
    background-color: #2a3649;
    transform: translateY(-2px);
  }
  
  .create-world-button img, .private-message-button img {
    width: 20px;
    height: 20px;
    margin-right: 0.5rem;
    filter: invert(0.7);
  }
  
  .main-content {
    display: flex;
  }
  
  .world-header {
    width: 240px;
    background-color: #0d1016;
    padding: 1rem;
    border-right: 1px solid #1e2533;
  }
  
  .world-header h2 {
    color: #3b82f6;
    margin-bottom: 1rem;
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
  
  .channel-list li:hover, .channel-list li.active {
    color: #3b82f6;
  }
  
  .channel-list li img {
    width: 16px;
    height: 16px;
    margin-right: 0.5rem;
    filter: invert(0.7);
  }
  
  .chat-area {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }
  
  .chat-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background-color: #0d1016;
    border-bottom: 1px solid #1e2533;
  }
  
  .chat-header h2 {
    color: #3b82f6;
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
    padding: 1rem;
    overflow-y: auto;
  }
  
  .message {
    display: flex;
    margin-bottom: 1rem;
    animation: fadeIn 0.3s ease;
  }
  
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
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
    color: #3b82f6;
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
    font-family: 'Orbitron', sans-serif;
  }
  
  .message-input button {
    background-color: #3b82f6;
    color: #ffffff;
    border: none;
    padding: 0.5rem 1rem;
    margin-left: 0.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-family: 'Orbitron', sans-serif;
    transition: background-color 0.3s;
  }
  
  .message-input button:hover {
    background-color: #2563eb;
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
  
  .modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #0d1016;
    border: 1px solid #1e2533;
    border-radius: 8px;
    padding: 2rem;
    z-index: 1000;
    max-width: 80%;
    max-height: 80%;
    overflow-y: auto;
  }
  
  .modal h2 {
    color: #3b82f6;
    margin-bottom: 1rem;
  }
  
  .private-message-list {
    list-style-type: none;
    padding: 0;
  }
  
  .private-message-list li {
    display: flex;
    align-items: center;
    padding: 0.5rem;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .private-message-list li:hover {
    background-color: #1e2533;
  }
  
  .conversation-info {
    margin-left: 1rem;
  }
  
  .conversation-name {
    font-weight: bold;
    color: #3b82f6;
  }
  
  .last-message {
    font-size: 0.8rem;
    color: #8b9bb4;
  }
  
  .close-button {
    background-color: #3b82f6;
    color: #ffffff;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    font-family: 'Orbitron', sans-serif;
    margin-top: 1rem;
    transition: background-color 0.3s;
  }
  
  .close-button:hover {
    background-color: #2563eb;
  }
  
  .modal-enter-active, .modal-leave-active {
    transition: opacity 0.3s, transform 0.3s;
  }
  
  .modal-enter-from, .modal-leave-to {
    opacity: 0;
    transform: translate(-50%, -50%) scale(0.9);
  }
  
  @media (max-width: 768px) {
    .nexus-chat {
      grid-template-columns: 1fr;
    }
  
    .left-sidebar, .right-sidebar {
      display: none;
    }
  
    .world-header {
      width: 100%;
    }
  
    .main-content {
      flex-direction: column;
    }
  }
  </style>