<template>
  <div
    class="nexus-profile-page"
    :class="{ 'nexus-collapsed-sidebar': isLeftSidebarCollapsed }"
  >
    <!-- Left Sidebar -->
    <div class="nexus-left-sidebar">
      <button @click="toggleLeftSidebar" class="nexus-collapse-button">
        <img
          :src="
            isLeftSidebarCollapsed
              ? 'https://api.iconify.design/lucide:chevrons-right.svg'
              : 'https://api.iconify.design/lucide:chevrons-left.svg'
          "
          :alt="isLeftSidebarCollapsed ? 'Expand' : 'Collapse'"
        />
      </button>
      <h1 class="nexus-worlds-title">WORLDS</h1>
      <nav class="nexus-nav">
        <ul class="nexus-nav-list">
          <li v-for="item in navItems" :key="item.id" class="nexus-nav-item">
            <a
              :href="item.href"
              class="nexus-nav-link"
              :class="{ 'nexus-active': item.id === activeNavItem }"
            >
              <img :src="item.icon" :alt="item.name" class="nexus-nav-icon" />
              <span class="nexus-nav-text">{{ item.name }}</span>
            </a>
          </li>
        </ul>
      </nav>
      <button class="nexus-create-world-button" @click="openCreateWorldModal">
        Create World
      </button>
      <div class="nexus-your-worlds">
        <h3 class="nexus-your-worlds-title">Your WORLDS:</h3>
        <ul class="nexus-your-worlds-list">
          <li
            v-for="world in yourWorlds"
            :key="world.id"
            class="nexus-your-world-item"
          >
            <img
              :src="world.icon"
              :alt="world.name"
              class="nexus-your-world-icon"
            />
            <span class="nexus-your-world-name">{{ world.name }}</span>
            <span class="nexus-your-world-members"
              >{{ world.members }} members</span
            >
          </li>
        </ul>
      </div>
    </div>

    <!-- Main Content -->
    <div class="nexus-main-content">
      <header class="nexus-profile-header">
        <div class="nexus-profile-cover">
          <img
            src="/placeholder.svg?height=200&width=1000"
            alt="Cover"
            class="nexus-cover-image"
          />
        </div>
        <div class="nexus-profile-info">
          <img
            src="https://i.pinimg.com/736x/9e/14/a8/9e14a82e1a9219374634c52a0a479334.jpg?height=120&width=120"
            alt="Avatar"
            class="nexus-profile-avatar"
          />
          <div class="nexus-profile-details">
            <h1 class="nexus-profile-name">John Doe</h1>
            <p class="nexus-profile-username">@johndoe</p>
            <p class="nexus-profile-bio">Exploring the digital frontier</p>
          </div>
          <button class="nexus-edit-profile-btn">Edit Profile</button>
        </div>
      </header>

      <div class="nexus-profile-content">
        <div class="nexus-profile-tabs">
          <button
            v-for="tab in tabs"
            :key="tab"
            @click="activeTab = tab"
            :class="{ 'nexus-active': activeTab === tab }"
            class="nexus-tab-button"
          >
            {{ tab }}
          </button>
        </div>

        <div class="nexus-tab-content">
          <div v-if="activeTab === 'Posts'" class="nexus-posts-section">
            <div v-for="post in posts" :key="post.id" class="nexus-post-card">
              <div class="nexus-post-header">
                <img
                  :src="post.authorAvatar"
                  :alt="post.author"
                  class="nexus-post-avatar"
                />
                <div class="nexus-post-meta">
                  <p class="nexus-post-author">{{ post.author }}</p>
                  <p class="nexus-post-date">{{ post.date }}</p>
                </div>
              </div>
              <p class="nexus-post-content">{{ post.content }}</p>
              <div class="nexus-post-actions">
                <button class="nexus-post-action">
                  <img
                    src="https://api.iconify.design/lucide:thumbs-up.svg"
                    alt="Like"
                    class="nexus-action-icon"
                  />
                  {{ post.likes }}
                </button>
                <button class="nexus-post-action">
                  <img
                    src="https://api.iconify.design/lucide:message-circle.svg"
                    alt="Comment"
                    class="nexus-action-icon"
                  />
                  {{ post.comments }}
                </button>
                <button class="nexus-post-action">
                  <img
                    src="https://api.iconify.design/lucide:share-2.svg"
                    alt="Share"
                    class="nexus-action-icon"
                  />
                  Share
                </button>
              </div>
            </div>
          </div>

          <div v-if="activeTab === 'Worlds'" class="nexus-worlds-section">
            <div
              v-for="world in worlds"
              :key="world.id"
              class="nexus-world-card"
            >
              <img
                :src="world.image"
                :alt="world.name"
                class="nexus-world-image"
              />
              <div class="nexus-world-info">
                <h3 class="nexus-world-name">{{ world.name }}</h3>
                <p class="nexus-world-members">{{ world.members }} members</p>
              </div>
            </div>
          </div>

          <div
            v-if="activeTab === 'Achievements'"
            class="nexus-achievements-section"
          >
            <div
              v-for="achievement in achievements"
              :key="achievement.id"
              class="nexus-achievement-card"
            >
              <img
                :src="achievement.icon"
                :alt="achievement.name"
                class="nexus-achievement-icon"
              />
              <div class="nexus-achievement-info">
                <h3 class="nexus-achievement-name">{{ achievement.name }}</h3>
                <p class="nexus-achievement-description">
                  {{ achievement.description }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const isLeftSidebarCollapsed = ref(false);
const activeNavItem = ref("worlds");
const activeTab = ref("Posts");

const tabs = ["Posts", "Worlds", "Achievements"];

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

const posts = ref([
  {
    id: 1,
    author: "John Doe",
    authorAvatar:
      "https://i.pinimg.com/736x/9e/14/a8/9e14a82e1a9219374634c52a0a479334.jpg?height=40&width=40",
    date: "2h ago",
    content:
      "Just discovered an amazing new virtual world! Can't wait to explore it further.",
    likes: 42,
    comments: 7,
  },
  {
    id: 2,
    author: "John Doe",
    authorAvatar: "/placeholder.svg?height=40&width=40",
    date: "1d ago",
    content:
      "Working on a new project that will revolutionize digital interactions. Stay tuned!",
    likes: 128,
    comments: 23,
  },
]);

const worlds = ref([
  {
    id: 1,
    name: "Cyberpunk City",
    members: 1500,
    image: "/placeholder.svg?height=100&width=100",
  },
  {
    id: 2,
    name: "Space Station Alpha",
    members: 800,
    image: "/placeholder.svg?height=100&width=100",
  },
  {
    id: 3,
    name: "Virtual Reality Hub",
    members: 2000,
    image: "/placeholder.svg?height=100&width=100",
  },
]);

const achievements = ref([
  {
    id: 1,
    name: "World Creator",
    description: "Created your first virtual world",
    icon: "/placeholder.svg?height=50&width=50",
  },
  {
    id: 2,
    name: "Social Butterfly",
    description: "Connected with 100 other users",
    icon: "/placeholder.svg?height=50&width=50",
  },
  {
    id: 3,
    name: "Explorer",
    description: "Visited 50 different virtual worlds",
    icon: "/placeholder.svg?height=50&width=50",
  },
]);

const toggleLeftSidebar = () => {
  isLeftSidebarCollapsed.value = !isLeftSidebarCollapsed.value;
};

const openCreateWorldModal = () => {
  // Implement the logic to open the create world modal
  console.log("Open create world modal");
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap");

.nexus-profile-page {
  display: grid;
  grid-template-columns: 240px 1fr;
  min-height: 100vh;
  font-family: "Orbitron", sans-serif;
  background-color: #0f1117;
  color: #8b9bb4;
}

.nexus-profile-page.nexus-collapsed-sidebar {
  grid-template-columns: 60px 1fr;
}

.nexus-left-sidebar {
  background-color: #0a0c10;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  border-right: 1px solid #1e2533;
  position: relative;
  transition: width 0.3s ease;
}

.nexus-collapse-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
}

.nexus-collapse-button img {
  width: 20px;
  height: 20px;
  filter: invert(0.7);
}

.nexus-worlds-title {
  color: #4169e1;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.nexus-nav-list {
  list-style-type: none;
  padding: 0;
}

.nexus-nav-link {
  display: flex;
  align-items: center;
  color: #8b9bb4;
  text-decoration: none;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  border-radius: 4px;
  transition: background-color 0.3s, color 0.3s;
}

.nexus-nav-link:hover,
.nexus-nav-link.nexus-active {
  background-color: #1e2533;
  color: #4169e1;
}

.nexus-nav-icon {
  width: 20px;
  height: 20px;
  margin-right: 0.5rem;
  filter: invert(0.7);
}

.nexus-create-world-button {
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

.nexus-create-world-button:hover {
  background-color: #9932cc;
}

.nexus-your-worlds {
  margin-top: 1rem;
  overflow-y: auto;
}

.nexus-your-worlds-title {
  font-size: 0.9rem;
  color: #8b9bb4;
  margin-bottom: 0.5rem;
}

.nexus-your-worlds-list {
  list-style-type: none;
  padding: 0;
}

.nexus-your-world-item {
  display: flex;
  align-items: center;
  padding: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.nexus-your-world-item:hover {
  background-color: #1e2533;
}

.nexus-your-world-icon {
  width: 32px;
  height: 32px;
  margin-right: 0.5rem;
  border-radius: 4px;
}

.nexus-your-world-name {
  flex-grow: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.nexus-your-world-members {
  font-size: 0.7rem;
  color: #4b5563;
  margin-left: auto;
}

.nexus-main-content {
  padding: 2rem;
  overflow-y: auto;
}

.nexus-profile-header {
  margin-bottom: 2rem;
}

.nexus-profile-cover {
  height: 200px;
  overflow: hidden;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.nexus-cover-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.nexus-profile-info {
  display: flex;
  align-items: flex-end;
  flex-wrap: wrap;
}

.nexus-profile-avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 4px solid #1a1e2e;
  margin-right: 1rem;
  margin-bottom: 1rem;
}

.nexus-profile-details {
  flex: 1;
  min-width: 200px;
}

.nexus-profile-name {
  font-size: 2rem;
  font-weight: bold;
  margin: 0;
  color: #ffffff;
}

.nexus-profile-username {
  font-size: 1rem;
  color: #4169e1;
  margin: 0.25rem 0;
}

.nexus-profile-bio {
  font-size: 0.9rem;
  margin: 0.5rem 0;
}

.nexus-edit-profile-btn {
  padding: 0.5rem 1rem;
  background-color: #4169e1;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 1rem;
}

.nexus-edit-profile-btn:hover {
  background-color: #3a5fcd;
}

.nexus-profile-tabs {
  display: flex;
  border-bottom: 1px solid #1e2533;
  margin-bottom: 1rem;
  overflow-x: auto;
  white-space: nowrap;
}

.nexus-tab-button {
  padding: 0.5rem 1rem;
  background: none;
  border: none;
  color: #8b9bb4;
  cursor: pointer;
  font-size: 1rem;
  transition: color 0.3s;
}

.nexus-tab-button.nexus-active {
  color: #4169e1;
  border-bottom: 2px solid #4169e1;
}

.nexus-tab-content {
  margin-top: 1rem;
}

.nexus-post-card,
.nexus-world-card,
.nexus-achievement-card {
  background-color: #1a1e2e;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1rem;
}

.nexus-post-header {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}

.nexus-post-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 0.5rem;
}

.nexus-post-meta {
  flex: 1;
}

.nexus-post-author {
  font-weight: bold;
  margin: 0;
  color: #ffffff;
}

.nexus-post-date {
  font-size: 0.8rem;
  color: #8b9bb4;
  margin: 0;
}

.nexus-post-content {
  margin-bottom: 1rem;
}

.nexus-post-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.nexus-post-action {
  display: flex;
  align-items: center;
  background: none;
  border: none;
  color: #8b9bb4;
  cursor: pointer;
  transition: color 0.3s;
}

.nexus-post-action:hover {
  color: #4169e1;
}

.nexus-action-icon {
  width: 16px;
  height: 16px;
  margin-right: 0.25rem;
  filter: invert(0.7);
}

.nexus-worlds-section,
.nexus-achievements-section {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.nexus-world-image,
.nexus-achievement-icon {
  width: 100%;
  height: 100px;
  object-fit: cover;
  border-radius: 4px;
  margin-bottom: 0.5rem;
}

.nexus-world-name,
.nexus-achievement-name {
  font-size: 1rem;
  margin: 0;
  color: #ffffff;
}

.nexus-world-members,
.nexus-achievement-description {
  font-size: 0.8rem;
  color: #8b9bb4;
  margin: 0.25rem 0 0;
}

.nexus-collapsed-sidebar .nexus-left-sidebar {
  width: 60px;
}

.nexus-collapsed-sidebar .nexus-worlds-title,
.nexus-collapsed-sidebar .nexus-nav-text,
.nexus-collapsed-sidebar .nexus-create-world-button,
.nexus-collapsed-sidebar .nexus-your-worlds-title,
.nexus-collapsed-sidebar .nexus-your-world-name,
.nexus-collapsed-sidebar .nexus-your-world-members {
  display: none;
}

.nexus-collapsed-sidebar .nexus-nav-link {
  justify-content: center;
}

.nexus-collapsed-sidebar .nexus-nav-icon {
  margin-right: 0;
}

.nexus-collapsed-sidebar .nexus-your-world-item {
  justify-content: center;
}

.nexus-collapsed-sidebar .nexus-your-world-icon {
  margin-right: 0;
}

@media (max-width: 768px) {
  .nexus-profile-page {
    grid-template-columns: 1fr;
  }

  .nexus-left-sidebar {
    display: none;
  }

  .nexus-profile-info {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .nexus-profile-avatar {
    margin-right: 0;
  }

  .nexus-profile-tabs {
    justify-content: space-between;
  }

  .nexus-tab-button {
    flex: 1;
    text-align: center;
  }

  .nexus-worlds-section,
  .nexus-achievements-section {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .nexus-main-content {
    padding: 1rem;
  }

  .nexus-profile-name {
    font-size: 1.5rem;
  }

  .nexus-profile-username,
  .nexus-profile-bio {
    font-size: 0.8rem;
  }

  .nexus-post-actions {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
