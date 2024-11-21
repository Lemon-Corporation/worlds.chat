// store/modules/auth.js
import axios from 'axios';

export const auth = {
  namespaced: true,
  state: () => ({
    accessToken: null,
    refreshToken: null,
    user: null,
  }),
  mutations: {
    SET_TOKENS(state, { accessToken, refreshToken }) {
      state.accessToken = accessToken;
      state.refreshToken = refreshToken;
    },
    SET_USER(state, user) {
      state.user = user;
    },
    CLEAR_AUTH(state) {
      state.accessToken = null;
      state.refreshToken = null;
      state.user = null;
    },
  },
  actions: {
    async login({ commit }, { email, password }) {
      try {
        const response = await axios.post('/auth/login', 
          new URLSearchParams({
            'username': email,
            'password': password,
          }),
          {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
            }
          }
        );
        const { access_token, refresh_token } = response.data;
        commit('SET_TOKENS', { accessToken: access_token, refreshToken: refresh_token });
        return response.data;
      } catch (error) {
        if (error.response && error.response.data && error.response.data.detail) {
          throw new Error(error.response.data.detail);
        } else {
          throw new Error('Произошла ошибка при входе в систему');
        }
      }
    },
    async register({ commit }, { username, email, password }) {
      try {
        const response = await axios.post('/auth/register', {
          username,
          email,
          password
        });
        return response.data;
      } catch (error) {
        if (error.response && error.response.data && error.response.data.detail) {
          throw new Error(error.response.data.detail);
        } else {
          throw new Error('Произошла ошибка при регистрации');
        }
      }
    },
    logout({ commit }) {
      commit('CLEAR_AUTH');
      // Здесь можно добавить логику для удаления токенов на сервере
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.accessToken,
    getAccessToken: (state) => state.accessToken,
    getRefreshToken: (state) => state.refreshToken,
    getUser: (state) => state.user,
  },
};

export default auth;