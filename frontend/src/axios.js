import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://107.172.10.250:5000',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

// Добавляем перехватчик для отладки
instance.interceptors.request.use(request => {
  console.log('Starting Request:', request);
  return request;
});

instance.interceptors.response.use(
  response => {
    console.log('Response:', response);
    return response;
  },
  error => {
    console.error('Response Error:', error);
    return Promise.reject(error);
  }
);

export default instance;