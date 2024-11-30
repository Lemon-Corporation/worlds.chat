import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/tailwind.css";
import store from './store'
import axios from 'axios';
axios.defaults.baseURL = 'http://127.0.0.1:8000';

axios.interceptors.request.use(
  (config) => {
    const token = store.getters['auth/getAccessToken'];
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response && error.response.status === 401) {
      router.push('/auth/sign-in');
    }
    return Promise.reject(error);
  }
);

createApp(App).use(store).use(router).mount("#app");
