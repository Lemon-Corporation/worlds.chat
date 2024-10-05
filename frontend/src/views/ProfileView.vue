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
        <h1>Profile</h1>
        <div class="header-icons">
          <img
            v-for="icon in headerIcons"
            :key="icon.alt"
            :src="icon.src"
            :alt="icon.alt"
          />
        </div>
      </div>
      <div class="profile-info">
        <img :src="user.avatar" :alt="user.name" class="profile-avatar" />
        <div class="profile-details">
          <h2>{{ user.name }}</h2>
          <p class="username">@{{ user.username }}</p>
          <p class="description">{{ user.description }}</p>
          <div class="profile-stats">
            <span
              ><strong>{{ user.following }}</strong> Following</span
            >
            <span
              ><strong>{{ user.followers }}</strong> Followers</span
            >
            <span
              ><strong>{{ user.worlds }}</strong> Worlds</span
            >
          </div>
        </div>
      </div>

      <h2 class="section-title">Recent Posts</h2>
      <div class="posts-grid">
        <div v-for="post in posts" :key="post.id" class="post-card">
          <p>{{ post.content }}</p>
          <span class="post-time">{{ post.time }}</span>
        </div>
      </div>

      <h2 class="section-title">My Worlds</h2>
      <div class="worlds-grid">
        <div v-for="world in ownWorlds" :key="world.id" class="world-card">
          <img :src="world.image" :alt="world.title" />
          <div class="world-title">{{ world.title }}</div>
        </div>
      </div>

      <h2 class="section-title">Subscribed Worlds</h2>
      <div class="worlds-grid">
        <div
          v-for="world in subscribedWorlds"
          :key="world.id"
          class="world-card"
        >
          <img :src="world.image" :alt="world.title" />
          <div class="world-title">{{ world.title }}</div>
        </div>
      </div>

      <h2 class="section-title">Achievements</h2>
      <div class="achievements-grid">
        <div
          v-for="achievement in achievements"
          :key="achievement.id"
          class="achievement-card"
        >
          <img
            :src="achievement.icon"
            :alt="achievement.title"
            class="achievement-icon"
          />
          <div class="achievement-details">
            <h3>{{ achievement.title }}</h3>
            <p>{{ achievement.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const sidebarItems = ref([
  {
    text: "Home",
    icon: "https://api.iconify.design/lucide:home.svg",
    active: false,
  },
  {
    text: "Profile",
    icon: "https://api.iconify.design/lucide:user.svg",
    active: true,
  },
  {
    text: "Worlds",
    icon: "https://api.iconify.design/lucide:globe.svg",
    active: false,
  },
  {
    text: "Messages",
    icon: "https://api.iconify.design/lucide:message-circle.svg",
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
  { src: "https://api.iconify.design/lucide:settings.svg", alt: "Settings" },
  { src: "https://api.iconify.design/lucide:log-out.svg", alt: "Logout" },
]);

const user = ref({
  name: "Alex Johnson",
  username: "alexj",
  avatar:
    "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  description:
    "Cyberpunk enthusiast and digital world creator. Exploring the boundaries of virtual reality and pushing the limits of imagination.",
  following: 250,
  followers: 10500,
  worlds: 15,
});

const posts = ref([
  {
    id: 1,
    content:
      'Just launched my new cyberpunk world "Neon Nights"! Come check it out and let me know what you think. #cyberpunk #virtualworlds',
    time: "2 hours ago",
  },
  {
    id: 2,
    content:
      "Working on a new AI-powered NPC system for more immersive world interactions. The future of virtual worlds is here! #AI #gamedev",
    time: "1 day ago",
  },
  {
    id: 3,
    content:
      "Excited to announce my collaboration with @technovision on an upcoming VR project. Stay tuned for more details! #VR #collaboration",
    time: "3 days ago",
  },
]);

const ownWorlds = ref([
  {
    id: 1,
    title: "Neon Nights",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
  {
    id: 2,
    title: "Quantum Realm",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
  {
    id: 3,
    title: "Steampunk City",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
]);

const subscribedWorlds = ref([
  {
    id: 4,
    title: "Dystopian Future",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
  {
    id: 5,
    title: "Enchanted Forest",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
  {
    id: 6,
    title: "Space Odyssey",
    image:
      "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-hs4qEC8Fk3y3NMWLOM7TLOqKLQivYk.png",
  },
]);

const achievements = ref([
  {
    id: 1,
    title: "World Creator",
    icon: "https://api.iconify.design/lucide:trophy.svg",
    description: "Created 10 unique worlds",
  },
  {
    id: 2,
    title: "Social Butterfly",
    icon: "https://api.iconify.design/lucide:users.svg",
    description: "Reached 10,000 followers",
  },
  {
    id: 3,
    title: "Trendsetter",
    icon: "https://api.iconify.design/lucide:trending-up.svg",
    description: "Had a world featured on the trending page",
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

.profile-info {
  display: flex;
  align-items: flex-start;
  margin-bottom: 30px;
}

.profile-avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 20px;
}

.profile-details h2 {
  font-size: 2rem;
  margin-bottom: 5px;
}

.username {
  color: var(--text-secondary);
  margin-bottom: 10px;
}

.description {
  margin-bottom: 15px;
  line-height: 1.5;
}

.profile-stats {
  display: flex;
  gap: 20px;
}

.profile-stats span {
  color: var(--text-secondary);
}

.profile-stats strong {
  color: var(--text-primary);
}

.section-title {
  font-size: 1.5rem;
  margin: 30px 0 20px;
  color: var(--text-primary);
  font-weight: 600;
}

.posts-grid {
  display: grid;
  gap: 20px;
  margin-bottom: 30px;
}

.post-card {
  background-color: var(--bg-card);
  padding: 20px;
  border-radius: 10px;
  transition: var(--transition);
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.post-time {
  display: block;
  margin-top: 10px;
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.worlds-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
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

.achievements-grid {
  display: grid;
  gap: 20px;
}

.achievement-card {
  display: flex;
  align-items: center;
  background-color: var(--bg-card);
  padding: 15px;
  border-radius: 10px;
  transition: var(--transition);
}

.achievement-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.achievement-icon {
  width: 40px;
  height: 40px;
  margin-right: 15px;
  filter: invert(1);
}

.achievement-details h3 {
  font-size: 1.1rem;
  margin-bottom: 5px;
}

.achievement-details p {
  color: var(--text-secondary);
  font-size: 0.9rem;
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

  .profile-info {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .profile-avatar {
    margin-right: 0;
    margin-bottom: 20px;
  }

  .profile-stats {
    justify-content: center;
  }

  .worlds-grid {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  }
}
</style>
