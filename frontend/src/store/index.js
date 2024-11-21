import { createStore } from 'vuex';
import auth from './modules/auth';
import axios from 'axios';
import { encrypt, decrypt } from './utils/encryption';


export default createStore({
  state: {
    worlds: [],
    activeChannels: [],
    currentUser: null,
  },
  mutations: {
    SET_WORLDS(state, worlds) {
      state.worlds = worlds
    },
    SET_ACTIVE_CHANNELS(state, channels) {
      state.activeChannels = channels
    },
    SET_CURRENT_USER(state, user) {
      state.currentUser = user
    },
  },
  actions: {
    async fetchWorlds({ commit }) {
      try {
        const response = await axios.get('/api/user/worlds')
        commit('SET_WORLDS', response.data.worlds)
      } catch (error) {
        console.error('Error fetching worlds:', error)
      }
    },
    async createWorld({ dispatch }, worldData) {
      try {
        await axios.post('/api/worlds/create', worldData)
        dispatch('fetchWorlds')
      } catch (error) {
        console.error('Error creating world:', error)
      }
    },
    async fetchCurrentUser({ commit }) {
      try {
        const response = await axios.get('/api/user/me')
        commit('SET_CURRENT_USER', response.data)
      } catch (error) {
        console.error('Error fetching current user:', error)
      }
    },
  },
  async createChannel({ dispatch }, channelData) {
    try {
      await axios.post('/api/channels/create', channelData);
      // Assuming you have an action to fetch channels for a specific world
      dispatch('fetchChannels', channelData.world_id);
    } catch (error) {
      console.error('Error creating channel:', error);
    }
  },
  modules: {
    auth,
  },
  plugins: [
    (store) => {
      // Загрузка состояния из куки при инициализации
      const encryptedState = localStorage.getItem('appState');
      if (encryptedState) {
        const decryptedState = JSON.parse(decrypt(encryptedState));
        store.replaceState(decryptedState);
      }

      // Сохранение состояния в куки при изменении
      store.subscribe((mutation, state) => {
        const encryptedState = encrypt(JSON.stringify(state));
        localStorage.setItem('appState', encryptedState);
      });
    }
  ]
});