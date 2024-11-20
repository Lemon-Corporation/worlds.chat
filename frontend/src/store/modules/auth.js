import axios from 'axios';

const state = {
  user: null,
  token: null,
};

const mutations = {
  SET_USER(state, user) {
    state.user = user;
  },
  SET_TOKEN(state, token) {
    state.token = token;
  },
};

const actions = {
  async register({ commit }, userData) {
    try {
      const response = await axios.post('/auth/register', userData);
      console.log('Ответ от сервера при регистрации:', response.data);
      
      // Здесь мы не устанавливаем токен, так как сервер не возвращает его при регистрации
      // Вместо этого мы можем установить данные пользователя
      commit('SET_USER', {
        id: response.data.user_id,
        email: response.data.email,
        username: response.data.username
      });
      
      return response.data;
    } catch (error) {
      console.error('Ошибка при регистрации:', error.response?.data || error.message);
      throw new Error(error.response?.data?.detail || 'Ошибка регистрации');
    }
  },

  const login = async ({ commit }, { email, password }) => {
    try {
      const response = await axios.post('/auth/login', { email, password });
      commit('SET_USER', response.data);
      return response.data;
    } catch (error) {
      if (error.response && error.response.data && error.response.data.detail) {
        // Обработка структурированной ошибки от FastAPI
        const errorDetails = error.response.data.detail;
        let errorMessage = '';
        if (Array.isArray(errorDetails)) {
          errorMessage = errorDetails.map(err => err.msg).join(', ');
        } else {
          errorMessage = errorDetails;
        }
        throw new Error(errorMessage);
      } else {
        throw new Error('Произошла ошибка при входе в систему');
      }
    }
  },
  async logout({ commit }) {
    try {
      const token = state.token;
      if (token) {
        await axios.post('/auth/logout', null, {
          headers: { Authorization: `Bearer ${token}` }
        });
      }
      
      // Очищаем данные пользователя и токен
      commit('SET_USER', null);
      commit('SET_TOKEN', null);
      localStorage.removeItem('refresh_token');
      
      // Удаляем заголовок Authorization
      delete axios.defaults.headers.common['Authorization'];
    } catch (error) {
      console.error('Ошибка при выходе:', error);
    }
  },

  async refreshToken({ commit }) {
    try {
      const refreshToken = localStorage.getItem('refresh_token');
      if (!refreshToken) {
        throw new Error('Refresh token not found');
      }

      const response = await axios.post('/auth/refresh', { refresh_token: refreshToken });
      const { access_token } = response.data;

      commit('SET_TOKEN', access_token);
      axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;

      return access_token;
    } catch (error) {
      console.error('Ошибка при обновлении токена:', error);
      commit('SET_USER', null);
      commit('SET_TOKEN', null);
      localStorage.removeItem('refresh_token');
      throw error;
    }
  },
};

const getters = {
  isAuthenticated: (state) => !!state.token,
  currentUser: (state) => state.user,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};