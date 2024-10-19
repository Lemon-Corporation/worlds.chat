<template>
  <div class="app-container">
    <div class="sidebar">
      <div
        v-for="item in sidebarItems"
        :key="item.text"
        :class="['sidebar-item', { active: item.active }]"
      >
        <img :src="item.icon" :alt="item.text" />
        {{ item.text }}
      </div>
      <button class="create-world-btn">Create World</button>
    </div>
    <div class="main-content">
      <div class="header">
        <h1>WORLDS</h1>
        <div class="header-icons">
          <img
            v-for="icon in headerIcons"
            :key="icon.alt"
            :src="icon.src"
            :alt="icon.alt"
          />
        </div>
      </div>
      <div class="search-bar">
        <img src="https://api.iconify.design/lucide:search.svg" alt="Search" />
        <input type="text" placeholder="Search Worlds" />
      </div>
      <h2 class="section-title">Featured</h2>
      <div class="worlds-grid">
        <div
          v-for="world in featuredWorlds"
          :key="world.title"
          class="world-card"
        >
          <img :src="world.image" :alt="world.title" />
          <div class="world-title">{{ world.title }}</div>
        </div>
      </div>
      <h2 class="section-title">Trending</h2>
      <div class="worlds-grid">
        <div
          v-for="world in trendingWorlds"
          :key="world.title"
          class="world-card"
        >
          <img :src="world.image" :alt="world.title" />
          <div class="world-title">{{ world.title }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const sidebarItems = ref([
  {
    text: "Messages",
    icon: "https://api.iconify.design/lucide:message-circle.svg",
    active: false,
  },
  {
    text: "Worlds",
    icon: "https://api.iconify.design/lucide:users.svg",
    active: true,
  },
  {
    text: "Inner",
    icon: "https://api.iconify.design/lucide:hash.svg",
    active: false,
  },
  {
    text: "Notifications",
    icon: "https://api.iconify.design/lucide:bell.svg",
    active: false,
  },
]);

const headerIcons = ref([
  { src: "https://api.iconify.design/lucide:bell.svg", alt: "Notifications" },
  { src: "https://api.iconify.design/lucide:hash.svg", alt: "Hash" },
  { src: "https://api.iconify.design/lucide:user.svg", alt: "User Profile" },
]);

const featuredWorlds = ref([
  {
    title: "Cyberpunk 2077",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
  {
    title: "Neon Tokyo",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
  {
    title: "Synthwave Dreams",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
]);

const trendingWorlds = ref([
  {
    title: "Vaporwave Lounge",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
  {
    title: "Dystopian Future",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
  {
    title: "Arcade Retrofest",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
]);
</script>

<style>
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

.search-bar {
  background-color: var(--bg-sidebar);
  border-radius: 25px;
  padding: 10px 20px;
  display: flex;
  align-items: center;
  margin-bottom: 30px;
  transition: var(--transition);
}

.search-bar:focus-within {
  box-shadow: 0 0 0 2px var(--accent-purple);
}

.search-bar img {
  filter: invert(0.7);
}

.search-bar input {
  background-color: transparent;
  border: none;
  color: var(--text-primary);
  width: 100%;
  margin-left: 10px;
  font-size: 1rem;
  outline: none;
}

.search-bar input::placeholder {
  color: var(--text-secondary);
}

.section-title {
  font-size: 1.5rem;
  margin-bottom: 20px;
  color: var(--text-primary);
  font-weight: 600;
}

.worlds-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.world-card {
  position: relative;
  border-radius: 10px;
  overflow: hidden;
  background-color: var(--bg-card);
  transition: var(--transition);
  cursor: pointer;
}

.world-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.world-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  transition: var(--transition);
}

.world-card:hover img {
  transform: scale(1.05);
}

.world-title {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
  padding: 15px;
  color: var(--text-primary);
  font-weight: 600;
  transition: var(--transition);
}

.world-card:hover .world-title {
  padding-bottom: 20px;
}

@media (max-width: 768px) {
  .app-container {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
    padding: 10px;
  }

  .sidebar-item {
    padding: 8px;
  }

  .main-content {
    padding: 10px;
  }

  .header {
    flex-direction: column;
    align-items: flex-start;
  }

  .header-icons {
    margin-top: 10px;
  }

  .worlds-grid {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  }
}
</style>
