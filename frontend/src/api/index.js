import axios from 'axios'

const api = axios.create({
  baseURL: 'http://107.172.10.250:5000',
  withCredentials: true
})

// Перехватчик для добавления токена к каждому запросу
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Перехватчик для обработки ошибок
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/auth/sign-in'
    }
    return Promise.reject(error)
  }
)

export default api