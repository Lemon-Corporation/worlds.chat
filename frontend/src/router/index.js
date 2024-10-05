import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import WorldsView from "../views/WorldsView.vue";
import ProfileView from "../views/ProfileView.vue";
import MessagesView from "../views/MessagesView.vue";
import WorldRoomView from "../views/WorldRoomView.vue";
import LoginView from "../views/LoginView.vue";
const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/worlds",
    name: "Worlds",
    component: WorldsView,
  },
  {
    path: "/profile",
    name: "Profile",
    component: ProfileView,
  },
  {
    path: "/messages",
    name: "Messages",
    component: MessagesView,
  },
  {
    path: "/worldroom",
    name: "WorldRoom",
    component: WorldRoomView,
  },
  {
    path: "/auth/sign-in",
    name: "Sign-In",
    component: LoginView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
