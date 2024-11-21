import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import HubView from "@/views/HubView.vue";
import AboutView from "@/views/AboutView.vue";
import BotsView from "@/views/BotsView.vue";
import ResetPassword from "@/views/ResetPassword.vue";
import ProfileView from "@/views/ProfileView.vue";
import MessagesView from "@/views/MessagesView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/top/worlds",
    name: "Popular",
    component: AboutView,
  },
  {
    path: "/messages",
    name: "Messages",
    component: MessagesView,
  },
  {
    path: "/worlds/bots",
    name: "Bots",
    component: BotsView,
  },
  {
    path: "/app",
    name: "hub",
    component: HubView,
  },
  {
    path: "/auth/sign-in",
    name: "Sign-In",
    component: LoginView,
  },
  {
    path: "/auth/reset-password",
    name: "reset",
    component: ResetPassword,
  },
  {
    path: "/auth/sign-up",
    name: "Sign-Up",
    component: RegisterView,
  },
  {
    path: "/profile",
    name: "Profile",
    component: ProfileView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
