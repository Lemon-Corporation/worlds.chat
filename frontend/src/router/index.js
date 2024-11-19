import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Worlds from "../views/WorldsView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import Support from "../views/SupportCenterView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/support-center",
    name: "Support",
    component: Support,
  },
  {
    path: "/worlds",
    name: "Worlds",
    component: Worlds,
  },
  {
    path: "/auth/sign-in",
    name: "Sign-In",
    component: LoginView,
  },
  {
    path: "/auth/sign-up",
    name: "Sign-Up",
    component: RegisterView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
