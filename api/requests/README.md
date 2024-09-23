### 1. Пользовательские запросы

- **Регистрация пользователя**
  - **POST** `/api/users/register`
  - **Тело запроса:** `{ "username": "string", "email": "string", "password": "string" }`
  
- **Авторизация пользователя**
  - **POST** `/api/users/login`
  - **Тело запроса:** `{ "email": "string", "password": "string" }`
  
- **Получение профиля пользователя**
  - **GET** `/api/users/{userId}`
  
- **Обновление профиля пользователя**
  - **PUT** `/api/users/{userId}`
  - **Тело запроса:** `{ "username": "string", "profilePicture": "string", "bio": "string" }`

### 2. Запросы для ботов

- **Создание бота**
  - **POST** `/api/bots`
  - **Тело запроса:** `{ "name": "string", "description": "string", "commands": "array" }`
  
- **Получение списка ботов**
  - **GET** `/api/bots`
  
- **Обновление информации о боте**
  - **PUT** `/api/bots/{botId}`
  - **Тело запроса:** `{ "name": "string", "description": "string", "commands": "array" }`
  
- **Удаление бота**
  - **DELETE** `/api/bots/{botId}`

### 3. Игровые лобби

- **Создание игрового лобби**
  - **POST** `/api/lobbies`
  - **Тело запроса:** `{ "name": "string", "gameType": "string", "settings": "object" }`
  
- **Получение информации о лобби**
  - **GET** `/api/lobbies/{lobbyId}`
  
- **Вступление в лобби**
  - **POST** `/api/lobbies/{lobbyId}/join`
  
- **Покидание лобби**
  - **POST** `/api/lobbies/{lobbyId}/leave`

### 4. Социальные взаимодействия

- **Создание поста**
  - **POST** `/api/posts`
  - **Тело запроса:** `{ "content": "string", "userId": "string" }`
  
- **Получение ленты постов**
  - **GET** `/api/posts/feed`
  
- **Комментирование поста**
  - **POST** `/api/posts/{postId}/comments`
  - **Тело запроса:** `{ "content": "string", "userId": "string" }`

### 5. Функции ИИ

- **Запрос перевода звука**
  - **POST** `/api/realtime_voice_translate`
  - **Тело запроса:** `{ "stream": "line", "targetLanguage": "string" }`

- **Запрос перевода текста**
  - **POST** `/api/realtime_text_translate`
  - **Тело запроса:** `{ "text": "string", "targetLanguage": "string" }`
  
- **Получение суммирования созвонов**
  - **POST** `/api/calls/summarize`
  - **Тело запроса:** `{ "callRecording": "string" }`

### 6. Настройки и оформление

- **Получение доступных тем оформления**
  - **GET** `/api/themes`
  
- **Сохранение настроек пользователя**
  - **PUT** `/api/users/{userId}/settings`
  - **Тело запроса:** `{ "theme": "string", "notifications": "boolean" }`
