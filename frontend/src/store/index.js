import { createStore } from 'vuex';
import auth from './modules/auth';
import { encrypt, decrypt } from './utils/encryption';

export default createStore({
  modules: {
    auth
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