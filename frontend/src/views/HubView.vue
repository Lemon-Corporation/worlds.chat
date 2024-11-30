<template>
  <div class="min-h-screen bg-gradient-to-b from-purple-900 via-gray-900 to-gray-950">
    <!-- Верхняя навигация -->
    <NavBar/>
    <div class="flex flex-col md:flex-row h-[calc(100vh-4rem)]">
      <!-- Боковая панель миров и каналов (скрыта на мобильных устройствах) -->
      <div
        class="hidden md:flex w-64 bg-gray-900/80 backdrop-blur-sm border-r border-purple-500/20 p-4 flex-col overflow-y-auto"
      >
        <div class="mb-4">
          <button
            @click="showCreateWorldModal = true"
            class="w-full bg-purple-500/20 hover:bg-purple-500/30 text-[#00ff9d] hover:text-[#00ff9d] py-2 rounded-lg flex items-center justify-center gap-2 transition-colors duration-200"
          >
            <Plus class="w-4 h-4" />
            Создать Мир
          </button>
        </div>

        <div class="space-y-2">
          <div v-for="world in worlds" :key="world.id" class="space-y-1">
            <div
              @click="toggleWorld(world.id)"
              class="flex items-center justify-between p-2 rounded-lg cursor-pointer hover:bg-purple-500/20 transition-colors duration-200"
              :class="{ 'bg-purple-500/20': world.expanded }"
            >
              <div class="flex items-center gap-2">
                <ChevronRight
                  v-if="!world.expanded"
                  class="w-4 h-4 text-gray-400"
                />
                <ChevronDown v-else class="w-4 h-4 text-gray-400" />
                <img 
                  :src="world.icon" 
                  :alt="world.name"
                  class="w-6 h-6 rounded-full ring-1 ring-purple-500/50"
                />
                <span class="text-gray-300">{{ world.name }}</span>
              </div>
              <div class="flex items-center gap-2">
                <span
                  v-if="world.notifications"
                  class="w-2 h-2 rounded-full bg-[#00ff9d]"
                ></span>
                <Settings 
                  @click.stop="openWorldSettings(world)"
                  class="w-4 h-4 text-gray-400 hover:text-[#00ff9d] transition-colors duration-200" 
                />
              </div>
            </div>
            <div v-if="world.expanded" class="ml-6 space-y-1">
              <div
                v-for="category in world.categories"
                :key="category.id"
                class="space-y-1"
              >
                <div
                  @click="toggleCategory(world.id, category.id)"
                  class="flex items-center justify-between p-2 rounded-lg cursor-pointer hover:bg-purple-500/20 group transition-colors duration-200"
                  :class="{ 'bg-purple-500/20': category.expanded }"
                >
                  <div class="flex items-center gap-2">
                    <ChevronRight
                      v-if="!category.expanded"
                      class="w-3 h-3 text-gray-400"
                    />
                    <ChevronDown v-else class="w-3 h-3 text-gray-400" />
                    <span class="text-gray-400 text-sm">{{
                      category.name
                    }}</span>
                  </div>
                  <button 
                    @click.stop="openCreateChannelModal(world.id, category.id)"
                    class="opacity-0 group-hover:opacity-100 transition-opacity duration-200"
                  >
                    <Plus class="w-3 h-3 text-gray-400 hover:text-[#00ff9d]" />
                  </button>
                </div>
                <div v-if="category.expanded" class="ml-4 space-y-1">
                  <div
                    v-for="channel in category.channels"
                    :key="channel.id"
                    draggable="true"
                    @dragstart="startDrag($event, channel)"
                    @dragend="endDrag"
                    @click="openChannel(channel)"
                    class="flex items-center gap-2 p-2 rounded-lg cursor-move hover:bg-purple-500/20 transition-colors duration-200"
                    :class="{ 'bg-purple-500/30': isChannelActive(channel.id) }"
                  >
                    <Hash
                      v-if="channel.type === 'text'"
                      class="w-3 h-3 text-gray-400"
                    />
                    <Mic
                      v-else-if="channel.type === 'voice'"
                      class="w-3 h-3 text-gray-400"
                    />
                    <Video
                      v-else-if="channel.type === 'video'"
                      class="w-3 h-3 text-gray-400"
                    />
                    <span class="text-gray-400 text-sm">{{
                      channel.name
                    }}</span>
                    <span
                      v-if="channel.unread"
                      class="ml-auto w-2 h-2 rounded-full bg-[#00ff9d]"
                    ></span>
                  </div>
                </div>
              </div>
              <button
                @click="openCreateCategoryModal(world.id)"
                class="w-full text-left text-gray-400 hover:text-[#00ff9d] text-sm p-2 rounded-lg hover:bg-purple-500/20 flex items-center gap-2 transition-colors duration-200"
              >
                <Plus class="w-3 h-3" />
                Добавить Категорию
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Кнопка для открытия боковой панели на мобильных устройствах -->
      <button
        @click="toggleMobileSidebar"
        class="md:hidden fixed bottom-4 left-4 z-50 bg-[#00ff9d] text-gray-900 rounded-full p-3 shadow-lg"
      >
        <Menu class="w-6 h-6" />
      </button>

      <!-- Мобильная боковая панель -->
      <div
        v-if="showMobileSidebar"
        class="fixed inset-0 bg-gray-900/95 z-40 md:hidden overflow-y-auto"
      >
        <div class="p-4">
          <button
            @click="toggleMobileSidebar"
            class="absolute top-4 right-4 text-gray-300 hover:text-[#00ff9d]"
          >
            <X class="w-6 h-6" />
          </button>
          <!-- Содержимое мобильной боковой панели -->
          <div class="mt-8">
            <div class="mb-4">
              <button
                @click="showCreateWorldModal = true; toggleMobileSidebar()"
                class="w-full bg-purple-500/20 hover:bg-purple-500/30 text-[#00ff9d] hover:text-[#00ff9d] py-2 rounded-lg flex items-center justify-center gap-2 transition-colors duration-200"
              >
                <Plus class="w-4 h-4" />
                Создать Новый Мир
              </button>
            </div>

            <div class="space-y-2">
              <div v-for="world in worlds" :key="world.id" class="space-y-1">
                <div
                  @click="toggleWorld(world.id)"
                  class="flex items-center justify-between p-2 rounded-lg cursor-pointer hover:bg-purple-500/20 transition-colors duration-200"
                  :class="{ 'bg-purple-500/20': world.expanded }"
                >
                  <div class="flex items-center gap-2">
                    <ChevronRight
                      v-if="!world.expanded"
                      class="w-4 h-4 text-gray-400"
                    />
                    <ChevronDown v-else class="w-4 h-4 text-gray-400" />
                    <img 
                      :src="world.icon" 
                      :alt="world.name"
                      class="w-6 h-6 rounded-full ring-1 ring-purple-500/50"
                    />
                    <span class="text-gray-300">{{ world.name }}</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <span
                      v-if="world.notifications"
                      class="w-2 h-2 rounded-full bg-[#00ff9d]"
                    ></span>
                    <Settings 
                      @click.stop="openWorldSettings(world)"
                      class="w-4 h-4 text-gray-400 hover:text-[#00ff9d] transition-colors duration-200" 
                    />
                  </div>
                </div>
                <div v-if="world.expanded" class="ml-6 space-y-1">
                  <!-- Категории и каналы (аналогично десктопной версии) -->
                  <div
                    v-for="category in world.categories"
                    :key="category.id"
                    class="space-y-1"
                  >
                    <div
                      @click="toggleCategory(world.id, category.id)"
                      class="flex items-center justify-between p-2 rounded-lg cursor-pointer hover:bg-purple-500/20 group transition-colors duration-200"
                      :class="{ 'bg-purple-500/20': category.expanded }"
                    >
                      <div class="flex items-center gap-2">
                        <ChevronRight
                          v-if="!category.expanded"
                          class="w-3 h-3 text-gray-400"
                        />
                        <ChevronDown v-else class="w-3 h-3 text-gray-400" />
                        <span class="text-gray-400 text-sm">{{
                          category.name
                        }}</span>
                      </div>
                      <button 
                        @click.stop="openCreateChannelModal(world.id, category.id)"
                        class="opacity-0 group-hover:opacity-100 transition-opacity duration-200"
                      >
                        <Plus class="w-3 h-3 text-gray-400 hover:text-[#00ff9d]" />
                      </button>
                    </div>
                    <div v-if="category.expanded" class="ml-4 space-y-1">
                      <div
                        v-for="channel in category.channels"
                        :key="channel.id"
                        @click="openChannel(channel); toggleMobileSidebar()"
                        class="flex items-center gap-2 p-2 rounded-lg cursor-pointer hover:bg-purple-500/20 transition-colors duration-200"
                        :class="{ 'bg-purple-500/30': isChannelActive(channel.id) }"
                      >
                        <Hash
                          v-if="channel.type === 'text'"
                          class="w-3 h-3 text-gray-400"
                        />
                        <Mic
                          v-else-if="channel.type === 'voice'"
                          class="w-3 h-3 text-gray-400"
                        />
                        <Video
                          v-else-if="channel.type === 'video'"
                          class="w-3 h-3 text-gray-400"
                        />
                        <span class="text-gray-400 text-sm">{{
                          channel.name
                        }}</span>
                        <span
                          v-if="channel.unread"
                          class="ml-auto w-2 h-2 rounded-full bg-[#00ff9d]"
                        ></span>
                      </div>
                    </div>
                  </div>
                  <button
                    @click="openCreateCategoryModal(world.id)"
                    class="w-full text-left text-gray-400 hover:text-[#00ff9d] text-sm p-2 rounded-lg hover:bg-purple-500/20 flex items-center gap-2 transition-colors duration-200"
                  >
                    <Plus class="w-3 h-3" />
                    Добавить Категорию
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Основной контент -->
      <div
        class="flex-1 flex flex-wrap bg-gray-900/60 backdrop-blur-sm relative overflow-hidden"
        @dragover.prevent
        @drop.prevent="onDrop($event)"
      >
        <template v-if="activeChannels.length > 0">
          <template v-for="(channel, index) in activeChannels" :key="index">
            <div
              :class="[
                'border border-purple-500/20 flex flex-col',
                getChannelClass(index),
              ]"
            >
              <template v-if="channel">
                <!-- Заголовок канала -->
                <div
                  class="h-14 border-b border-purple-500/20 px-4 flex justify-between items-center bg-gray-900/40"
                >
                  <div class="flex items-center gap-2 text-[#00ff9d]">
                    <Hash v-if="channel.type === 'text'" class="w-5 h-5" />
                    <Mic v-else-if="channel.type === 'voice'" class="w-5 h-5" />
                    <Video v-else-if="channel.type === 'video'" class="w-5 h-5" />
                    <h1 class="font-semibold">{{ channel.name }}</h1>
                  </div>
                  <button
                    @click="removeChannel(index)"
                    class="text-gray-400 hover:text-[#00ff9d] p-1 rounded transition-colors duration-200"
                  >
                    <X class="w-4 h-4" />
                  </button>
                </div>

                <!-- Сообщения или содержимое канала -->
                <div class="flex-1 p-4 overflow-y-auto space-y-4">

                  <div v-if="channel.type === 'text'">
                    <div
                      v-for="message in messages[channel.id]"
                      :key="message.id"
                      class="group flex items-start gap-3 p-2 rounded-lg hover:bg-purple-500/10 transition-colors duration-200"
                    >
                      <div class="relative">
                        <img
                          :src="message.avatar"
                          class="w-10 h-10 rounded-full bg-purple-500/20"
                          :alt="message.user + ' аватар'"
                        />
                        <span
                          class="absolute bottom-0 right-0 w-3 h-3 rounded-full bg-[#00ff9d] border-2 border-gray-900"
                          v-if="message.online"
                        ></span>
                      </div>
                      <div class="flex-1 min-w-0">
                        <div class="flex items-center gap-2">
                          <span class="font-semibold text-[#00ff9d]">{{
                            message.user
                          }}</span>
                          <span class="text-xs text-gray-400">{{
                            message.time
                          }}</span>
                        </div>
                        <p class="text-gray-300 break-words">
                          {{ message.content }}
                        </p>
                      </div>
                    </div>
                  </div>
                  <div id='video-container' v-else-if="channel.type === 'voice' || channel.type === 'video'" class="flex flex-col items-center justify-center h-full">
                    <div v-if="channel.connected" class="text-center"></div>
                    <div v-else class="text-gray-400 text-center">
                      <component :is="channel.type === 'voice' ? Mic : Video" class="w-12 h-12 mx-auto mb-4 text-[#00ff9d]" />
                      <p>{{ channel.type === 'voice' ? 'Голосовой' : 'Видео' }} канал</p>
                      <button
                        @click="connectToChannel(channel)"
                        class="mt-4 bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium py-2 px-4 rounded-md transition-colors duration-200"
                      >
                        Присоединиться к {{ channel.type === 'voice' ? 'голосовому' : 'видео' }} чату
                      </button>
                    </div>
                  </div>
                </div>

                <!-- Ввод сообщения (только для текстовых каналов) -->
                <div
                  v-if="channel.type === 'text'"
                  class="p-4 border-t border-purple-500/20 bg-gray-900/40"
                >
                  <div
                    class="flex items-center gap-2 bg-gray-800/60 rounded-lg p-2"
                  >
                    <button
                      class="text-gray-400 hover:text-[#00ff9d] p-2 rounded transition-colors duration-200"
                    >
                      <Plus class="w-5 h-5" />
                    </button>
                    <input
                      v-model="channel.inputValue"
                      type="text"
                      placeholder="Напишите сообщение..."
                      class="flex-1 bg-transparent border-none text-gray-300 placeholder-gray-500 focus:ring-0 focus:outline-none"
                    />
                    <button
                      class="text-gray-400 hover:text-[#00ff9d] p-2 rounded transition-colors duration-200"
                    >
                      <Smile class="w-5 h-5" />
                    </button>
                    <button
                      class="text-gray-400 hover:text-[#00ff9d] p-2 rounded transition-colors duration-200"
                    >
                      <Paperclip class="w-5 h-5" />
                    </button>
                    <button  @click="sendMessage(channel, channel.inputValue)"
                      class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 p-2 rounded transition-colors duration-200"
                    >
                      <Send class="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </template>
              <div
                v-else
                class="flex items-center justify-center h-full text-gray-400"
              >
                Перетащите канал сюда
              </div>
            </div>
          </template>
        </template>
        <template v-else>
          <!-- Информация, когда ни один канал не выбран -->
          <div class="flex-1 flex items-center justify-center p-4">
            <div class="text-center">
              <img src="./static/logo22.svg" alt="Worlds Logo" class="w-32 h-32 mx-auto mb-6" />
              <h2 class="text-2xl font-bold text-[#00ff9d] mb-4">Добро пожаловать в Worlds!</h2>
              <p class="text-gray-400 mb-6 max-w-md">Выберите канал слева или создайте новый мир, чтобы начать общение.</p>
              <button
                @click="showCreateWorldModal = true"
                class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium py-2 px-4 rounded-md transition-colors duration-200 flex items-center gap-2 mx-auto"
              >
                <Plus class="w-4 h-4" />
                Создать Новый Мир
              </button>
            </div>
          </div>
        </template>

        <!-- Оверлей для отображения разметки при перетаскивании -->
        <div
          v-if="isDragging"
          class="absolute inset-0 bg-gray-900/40 backdrop-blur-sm flex"
          :class="getOverlayClass()"
        >
          <template v-for="(_, index) in getOverlaySlots()" :key="index">
            <div
              class="border-2 border-dashed border-[#00ff9d] flex items-center justify-center text-[#00ff9d] text-lg font-bold"
              :class="getOverlaySlotClass(index)"
              @dragover.prevent
              @drop.prevent="onDropOverlay($event, index)"
            >
              Перетащите сюда
            </div>
          </template>
        </div>
      </div>
    </div>

    <!-- Модальное окно создания мира -->
    <div v-if="showCreateWorldModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gray-900 border border-purple-500/20 rounded-lg w-full max-w-md p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-[#00ff9d] text-xl font-bold">Создать Новый Мир</h2>
          <button @click="showCreateWorldModal = false" class="text-gray-400 hover:text-[#00ff9d] transition-colors duration-200">
            <X class="w-5 h-5" />
          </button>
        </div>
        <form @submit.prevent="createWorld" class="space-y-4">
          <div>
            <label class="block text-gray-300 text-sm font-medium mb-2">Шаблон Мира</label>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <button
                v-for="template in worldTemplates"
                :key="template.id"
                type="button"
                @click="selectWorldTemplate(template)"
                :class="[
                  'p-4 rounded-lg border-2 text-left transition-all duration-200',
                  newWorld.template === template.id 
                    ? 'border-[#00ff9d] bg-purple-500/20' 
                    : 'border-purple-500/20 hover:border-purple-500/40'
                ]"
              >
                <component :is="template.icon" class="w-6 h-6 mb-2 text-[#00ff9d]" />
                <h3 class="text-[#00ff9d] font-medium mb-1">{{ template.name }}</h3>
                <p class="text-sm text-gray-400">{{ template.description }}</p>
              </button>
            </div>
          </div>
          <div>
            <label for="worldName" class="block text-gray-300 text-sm font-medium mb-2">Название Мира</label>
            <input
              id="worldName"
              v-model="newWorld.name"
              type="text"
              class="w-full bg-gray-800 border border-purple-500/20 rounded-md px-3 py-2 text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] transition-colors duration-200"
              placeholder="Введите название мира"
            />
          </div>
          <div>
            <label class="block text-gray-300 text-sm font-medium mb-2">Иконка Мира</label>
            <div class="grid grid-cols-3 gap-4">
              <button
                v-for="(icon, index) in worldIcons"
                :key="index"
                type="button"
                @click="newWorld.icon = icon"
                :class="[
                  'p-2 rounded-lg border-2 transition-all duration-200',
                  newWorld.icon === icon ? 'border-[#00ff9d]' : 'border-transparent'
                ]"
              >
                <img :src="icon" :alt="'Иконка мира ' + (index + 1)" class="w-12 h-12 rounded-full" />
              </button>
            </div>
          </div>
          <div class="flex justify-end gap-3 mt-6">
            <button
              type="button"
              @click="showCreateWorldModal = false"
              class="px-4 py-2 text-gray-400 hover:text-gray-300 transition-colors duration-200"
            >
              Отмена
            </button>
            <button
              type="submit"
              class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium px-4 py-2 rounded-md transition-colors duration-200"
            >
              Создать Мир
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Модальное окно настроек мира -->
    <div v-if="showWorldSettings" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gray-900 border border-purple-500/20 rounded-lg w-full max-w-md p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-[#00ff9d] text-xl font-bold">Настройки Мира</h2>
          <button @click="showWorldSettings = false" class="text-gray-400 hover:text-[#00ff9d] transition-colors duration-200">
            <X class="w-5 h-5" />
          </button>
        </div>
        <div class="space-y-6">
          <div>
            <label for="editWorldName" class="block text-gray-300 text-sm font-medium mb-2">Название Мира</label>
            <input
              id="editWorldName"
              v-model="selectedWorld.name"
              type="text"
              class="w-full bg-gray-800 border border-purple-500/20 rounded-md px-3 py-2 text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] transition-colors duration-200"
            />
          </div>
          <div>
            <label class="block text-gray-300 text-sm font-medium mb-2">Иконка Мира</label>
            <div class="grid grid-cols-3 gap-4">
              <button
                v-for="(icon, index) in worldIcons"
                :key="index"
                type="button"
                @click="selectedWorld.icon = icon"
                :class="[
                  'p-2 rounded-lg border-2 transition-all duration-200',
                  selectedWorld.icon === icon ? 'border-[#00ff9d]' : 'border-transparent'
                ]"
              >
                <img :src="icon" :alt="'Иконка мира ' + (index + 1)" class="w-12 h-12 rounded-full" />
              </button>
            </div>
          </div>
          <!-- Новый раздел для создания приглашений -->
          <div>
            <h3 class="text-[#00ff9d] font-medium mb-2">Создать Приглашение</h3>
            <div class="flex items-center gap-2">
              <input
                type="text"
                readonly
                class="flex-1 bg-gray-800 border border-purple-500/20 rounded-md px-3 py-2 text-gray-300"
                :value="generateInvitationLink()"
              />
              <button
                @click="copyInvitationLink"
                class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium px-4 py-2 rounded-md transition-colors duration-200"
              >
                Копировать
              </button>
            </div>
          </div>
          <!-- Новая кнопка для просмотра участников мира -->
          <button
            @click="showParticipants"
            class="w-full bg-purple-500/20 hover:bg-purple-500/30 text-[#00ff9d] py-2 rounded-md transition-colors duration-200"
          >
            Просмотр Участников
          </button>
          <div class="space-y-4">
            <h3 class="text-[#00ff9d] font-medium">Опасная зона</h3>
            <button
              @click="deleteWorld"
              class="w-full bg-red-500/10 hover:bg-red-500/20 text-red-500 py-2 rounded-md transition-colors duration-200"
            >
              Удалить Мир
            </button>
          </div>
          <div class="flex justify-end gap-3 mt-6">
            <button
              @click="showWorldSettings = false"
              class="px-4 py-2 text-gray-400 hover:text-gray-300 transition-colors duration-200"
            >
              Отмена
            </button>
            <button
              @click="saveWorldSettings"
              class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium px-4 py-2 rounded-md transition-colors duration-200"
            >
              Сохранить Изменения
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Модальное окно создания категории -->
    <div v-if="showCreateCategoryModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gray-900 border border-purple-500/20 rounded-lg w-full max-w-md p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-[#00ff9d] text-xl font-bold">Создать Новую Категорию</h2>
          <button @click="showCreateCategoryModal = false" class="text-gray-400 hover:text-[#00ff9d] transition-colors duration-200">
            <X class="w-5 h-5" />
          </button>
        </div>
        <form @submit.prevent="createCategory" class="space-y-4">
          <div>
            <label for="categoryName" class="block text-gray-300 text-sm font-medium mb-2">Название Категории</label>
            <input
              id="categoryName"
              v-model="newCategory.name"
              type="text"
              class="w-full bg-gray-800 border border-purple-500/20 rounded-md px-3 py-2 text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] transition-colors duration-200"
              placeholder="Введите название категории"
            />
          </div>
          <div class="flex justify-end gap-3 mt-6">
            <button
              type="button"
              @click="showCreateCategoryModal = false"
              class="px-4 py-2 text-gray-400 hover:text-gray-300 transition-colors duration-200"
            >
              Отмена
            </button>
            <button
              type="submit"
              class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium px-4 py-2 rounded-md transition-colors duration-200"
            >
              Создать Категорию
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Модальное окно создания канала -->
    <div v-if="showCreateChannelModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gray-900 border border-purple-500/20 rounded-lg w-full max-w-md p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-[#00ff9d] text-xl font-bold">Создать Новый Канал</h2>
          <button @click="showCreateChannelModal = false" class="text-gray-400 hover:text-[#00ff9d] transition-colors duration-200">
            <X class="w-5 h-5" />
          </button>
        </div>
        <form @submit.prevent="createChannel" class="space-y-4">
          <div>
            <label for="channelName" class="block text-gray-300 text-sm font-medium mb-2">Название Канала</label>
            <input
              id="channelName"
              v-model="newChannel.name"
              type="text"
              class="w-full bg-gray-800 border border-purple-500/20 rounded-md px-3 py-2 text-gray-300 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-[#00ff9d] transition-colors duration-200"
              placeholder="Введите название канала"
            />
          </div>
          <div>
            <label class="block text-gray-300 text-sm font-medium mb-2">Тип Канала</label>
            <div class="grid grid-cols-3 gap-4">
              <button
                v-for="type in channelTypes"
                :key="type.id"
                type="button"
                @click="newChannel.type = type.id"
                :class="[
                  'p-4 rounded-lg border-2 flex flex-col items-center transition-all duration-200',
                  newChannel.type === type.id 
                    ? 'border-[#00ff9d] bg-purple-500/20' 
                    : 'border-purple-500/20 hover:border-purple-500/40'
                ]"
              >
                <component :is="type.icon" class="w-6 h-6 mb-2" :class="newChannel.type === type.id ? 'text-[#00ff9d]' : 'text-gray-400'" />
                <span :class="newChannel.type === type.id ? 'text-[#00ff9d]' : 'text-gray-400'">{{ type.name }}</span>
              </button>
            </div>
          </div>
          <div class="flex justify-end gap-3 mt-6">
            <button
              type="button"
              @click="showCreateChannelModal = false"
              class="px-4 py-2 text-gray-400 hover:text-gray-300 transition-colors duration-200"
            >
              Отмена
            </button>
            <button
              type="submit"
              class="bg-[#00ff9d] hover:bg-[#00cc7d] text-gray-900 font-medium px-4 py-2 rounded-md transition-colors duration-200"
            >
              Создать Канал
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Новое модальное окно для отображения участников мира -->
    <div v-if="showParticipantsModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gray-900 border border-purple-500/20 rounded-lg w-full max-w-md p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-[#00ff9d] text-xl font-bold">Участники Мира</h2>
          <button @click="showParticipantsModal = false" class="text-gray-400 hover:text-[#00ff9d] transition-colors duration-200">
            <X class="w-5 h-5" />
          </button>
        </div>
        <div class="space-y-4 max-h-96 overflow-y-auto">
          <div v-for="participant in worldParticipants" :key="participant.id" class="flex items-center gap-3 p-2 rounded-lg hover:bg-purple-500/10">
            <img :src="participant.avatar" :alt="participant.name" class="w-10 h-10 rounded-full bg-purple-500/20">
            <div>
              <p class="text-[#00ff9d] font-medium">{{ participant.name }}</p>
              <p class="text-gray-400 text-sm">{{ participant.role }}</p>
            </div>
            <div class="ml-auto flex items-center">
              <span :class="participant.online ? 'bg-green-500' : 'bg-gray-500'" class="w-2 h-2 rounded-full"></span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useStore } from 'vuex';
import axios from "axios";
import {
  Hash,
  Mic,
  Send,
  Smile,
  Paperclip,
  Plus,
  X,
  Settings,
  MessageSquare,
  ChevronRight,
  ChevronDown,
  Video,
  Users,
  Briefcase,
  AtSign,
  Bell,
  Menu,
  MicOff,
  VideoOff,
  PhoneOff,
} from "lucide-vue-next";
import NavBar from "@/components/NavBar.vue";

const store = useStore();
const accessToken = store.getters['auth/getAccessToken'];

// jitsi -----------------------------------

const connectToJitsi = async (channel, username, room, password) => {
  try {
    const domain = "localhost:7000";
    const options = {
        roomName: room,
        width: "100%",
        height: "100%",
        parentNode: document.getElementById('video-container'),
        configOverwrite: {
            startWithAudioMuted: true,
            startWithVideoMuted: true,
        },
        userInfo: {
            displayName: username
        }
    };

    // Create a new Jitsi Meet API instance
    const api = new JitsiMeetExternalAPI(domain, options);

    // Handle events (optional)
    api.addEventListener('videoConferenceJoined', () => {
        // prompt('Conference joined successfully!');
    });

    api.addEventListener('videoConferenceLeft', () => {
        disconnectFromChannel(channel);
    });

    api.addEventListener('participantRoleChanged', function(event) {
        if (event.role === "moderator") {
            api.executeCommand('password', password);
        }
    });

    api.addEventListener('passwordRequired', () => {
        api.executeCommand('password', password)
    })
  } catch (error) {
    console.warn(error);
  }
};

// -------------------------------------------------------

// Иконки миров
const worldIcons = [
  "https://i.imgur.com/dlFRtHv.png",
  "https://i.imgur.com/oPPTj4b.png",
  "https://i.imgur.com/w2LCHjF.png"
];

// Шаблоны миров
const worldTemplates = [
  {
    id: 'community',
    name: 'Сообщество',
    description: 'Идеально для создания сообщества вокруг общих интересов',
    icon: Users,
    defaultCategories: [
      {
        name: 'Информация',
        channels: [
          { name: 'приветствие', type: 'text' },
          { name: 'объявления', type: 'text' },
          { name: 'правила', type: 'text' },
        ]
      },
      {
        name: 'Общее',
        channels: [
          { name: 'общий-чат', type: 'text' },
          { name: 'знакомства', type: 'text' },
          { name: 'офтопик', type: 'text' },
        ]
      },
      {
        name: 'Голосовые каналы',
        channels: [
          { name: 'Общий голосовой', type: 'voice' },
          { name: 'Музыка', type: 'voice' },
        ]
      }
    ]
  },
  {
    id: 'work',
    name: 'Работа',
    description: 'Разработан для командного сотрудничества и управления проектами',
    icon: Briefcase,
    defaultCategories: [
      {
        name: 'Компания',
        channels: [
          { name: 'объявления', type: 'text' },
          { name: 'общее', type: 'text' },
          { name: 'кулер', type: 'text' },
        ]
      },
      {
        name: 'Проекты',
        channels: [
          { name: 'проект-а', type: 'text' },
          { name: 'проект-б', type: 'text' },
        ]
      },
      {
        name: 'Встречи',
        channels: [
          { name: 'Ежедневный созвон', type: 'voice' },
          { name: 'Командная встреча', type: 'video' },
        ]
      }
    ]
  },
];

// Типы каналов
const channelTypes = [
  { id: 'text', name: 'Текст', icon: MessageSquare },
  { id: 'voice', name: 'Голос', icon: Mic },
  { id: 'video', name: 'Видео', icon: Video },
];

// Состояния модальных окон
const showCreateWorldModal = ref(false);
const showWorldSettings = ref(false);
const showCreateCategoryModal = ref(false);
const showCreateChannelModal = ref(false);
const selectedWorld = ref(null);
const selectedWorldId = ref(null);
const selectedCategoryId = ref(null);

// Данные формы нового мира
const newWorld = ref({
  name: '',
  icon: worldIcons[0],
  template: 'community'
});

// Данные формы новой категории
const newCategory = ref({
  name: ''
});

// Данные формы нового канала
const newChannel = ref({
  name: '',
  type: 'text'
});

const getUserData = async (user_id) => {
  try {
    // Fetch user worlds
    const userData = await axios.get(`http://localhost:8000/user/${user_id}`, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'accept': 'application/json'
      }
    });
    return userData.data;
  } catch (error) {
    console.warn(error);
  }
}

const worlds = ref([]);

const fetchAvailableWorlds = async () => {
  const accessToken = store.getters['auth/getAccessToken'];

  try {
    // Fetch user worlds
    const worldsResponse = await axios.get('http://localhost:8000/user/worlds', {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'accept': 'application/json'
      }
    });

    const allWorlds = worldsResponse.data.worlds;
   

    // Ensure unique IDs and correct categorization
    const mainWorlds = allWorlds.filter(world => world.parent_world_id === null);
    const categoryWorlds = allWorlds.filter(world => world.parent_world_id !== null);

    // Fetch all channels
    const channelsResponse = await axios.get('http://localhost:8000/channels/all?page=1&per_page=40', {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'accept': 'application/json'
      }
    });

    const allChannels = channelsResponse.data.channels;

    // Create a map to easily find parent worlds by id
    const worldMap = new Map();
    mainWorlds.forEach(world => {
      worldMap.set(world.id, {
        id: world.id,
        name: world.name,
        icon: world.icon_url,
        expanded: false,
        notifications: false,
        categories: [],
        channels: [], // Initialize channels array
      });
    });

    // Assign category worlds to their parent worlds
    categoryWorlds.forEach(category => {
      const parentWorld = worldMap.get(category.parent_world_id);
      if (parentWorld) {
        parentWorld.categories.push({
          id: category.id,
          name: category.name,
          expanded: false,
          channels: [], // Initialize channels array
        });
      }
    });

    // Assign channels to their respective worlds and categories
    allChannels.forEach(channel => {
  // Найти мир, к которому принадлежит категория
  let categoryFound = false;

  worldMap.forEach(world => {
    const category = world.categories.find(cat => cat.id === channel.world_id);
    if (category) {
      // Добавить канал в категорию
      category.channels.push({
        id: channel.id,
        name: channel.name,
        type: channel.type,
        unread: false
      });
      categoryFound = true;
    }
  });

  if (!categoryFound) {
    // console.warn(`Category not found for channel ID ${channel.id}, world_id ${channel.world_id}`);
  }
});

    // Convert map back to an array for worlds ref
    worlds.value = Array.from(worldMap.values());
  } catch (error) {
    console.error('Failed to fetch available worlds and channels:', error);
  }
};


fetchAvailableWorlds();

const messages = ref([]);

const sendMessage = async (channel, newMessage) => {
  // Проверяем, что сообщение не пустое и есть активный канал
  if (!newMessage) {
    console.warn('Message content is empty');

    return;
  }

  try {
    // Отправляем сообщение на сервер
    const userData = await axios.get('http://localhost:8000/user/me', {
      headers: {
        'Authorization': `Bearer ${store.getters['auth/getAccessToken']}`,
        'accept': 'application/json'
      }
    });
    const response = await axios.post('http://localhost:8000/messages/send', {
      channel_id: channel.id,
      content: newMessage,
      user_id: userData.data.id
    }, {
      headers: {
        'Authorization': `Bearer ${store.getters['auth/getAccessToken']}`,
        'accept': 'application/json'
      }
    });

    // Добавляем сообщение в список сообщений
    
    const newMessageData = {
      id: response.data.id,
      user_id: userData.data.id,
      user: userData.data.username || 'Вы',
      content: response.data.content,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      avatar: userData.data.profile_pic_url || "https://i.imgur.com/dlFRtHv.png",
      online: true
    };

    // Добавляем сообщение в индекс channel id
    if (!messages.value[channel.id]) {
      messages.value[channel.id] = [];
    }
    messages.value[channel.id].push(newMessageData);

    // Очистка поля ввода
    channel.inputValue = '';
  } catch (error) {
    console.error('Failed to send message:', error);
  }
};


const activeChannels = ref([]);
const isDragging = ref(false);

// Новое состояние для мобильной боковой панели
const showMobileSidebar = ref(false);

// Функция для переключения мобильной боковой панели
const toggleMobileSidebar = () => {
  showMobileSidebar.value = !showMobileSidebar.value;
};

const getChannelClass = (index) => {
  const totalChannels = activeChannels.value.length;
  if (totalChannels === 1) return "w-full h-full";
  if (totalChannels === 2) return "w-full md:w-1/2 h-1/2 md:h-full";
  if (totalChannels === 3 || totalChannels === 4) return "w-full md:w-1/2 h-1/2";
};

const getOverlayClass = () => {
  const totalChannels = activeChannels.value.length;
  if (totalChannels === 0) return "flex-col";
  if (totalChannels === 1) return "flex-col md:flex-row";
  return "flex-col md:flex-row md:flex-wrap";
};

const getOverlaySlots = () => {
  const totalChannels = activeChannels.value.length;
  if (totalChannels < 4) return new Array(totalChannels + 1).fill(null);
  return [];
};

const getOverlaySlotClass = (index) => {
  const totalSlots = getOverlaySlots().length;
  if (totalSlots === 1) return "w-full h-full";
  if (totalSlots === 2) return "w-full md:w-1/2 h-1/2 md:h-full";
  return "w-full md:w-1/2 h-1/2";
};

const toggleWorld = (worldId) => {
  const world = worlds.value.find((w) => w.id === worldId);
  if (world) {
    world.expanded = !world.expanded;
  }
};

const toggleCategory = (worldId, categoryId) => {
  const world = worlds.value.find((w) => w.id === worldId);
  if (world) {
    const category = world.categories.find((c) => c.id === categoryId);
    if (category) {
      category.expanded = !category.expanded;
    }
  }
};

const getMessages = async (channel) => {
  if (!channel || !channel.id) {
    console.warn('No channel selected');
    return;
  }

  try {
    // Initialize the messages array for the channel
    messages.value[channel.id] = [];
    const response = await axios.get(`http://localhost:8000/channels/${channel.id}/get_messages?page=1&per_page=100`, {
      headers: {
        'Authorization': `Bearer ${store.getters['auth/getAccessToken']}`,
        'accept': 'application/json'
      }
    });

    // Retrieve messages from the response
    const messagesData = response.data.messages || [];

    // Format and add messages to the list

    const userPromises = messagesData.map(msg => getUserData(msg.user_id));
    const userDataArray = await Promise.all(userPromises);
    
    const formattedMessages = messagesData.map((msg, index) => ({
      id: msg.id,
      user: userDataArray[index].username,
      content: msg.content,
      time: new Date(msg.timestamp).toLocaleString(),
      avatar: userDataArray[index].profile_pic_url,
      online: msg.online || false,
      channelId: `[${Number(channel.id)}]`  // Store channel ID as a number in square brackets
    }));

    // Update the messages list for the channel
    messages.value[channel.id].push(...formattedMessages);

  } catch (error) {
    console.error('Failed to fetch messages:', error);
  }
}

let draggedChannel = null;
const startDrag = (event, channel) => {

  getMessages(channel);

  draggedChannel = channel;
  isDragging.value = true;
  event.dataTransfer.setData("text/plain", JSON.stringify(channel));
};
const endDrag = () => {
  isDragging.value = false;
};
const onDrop = (event) => {
  isDragging.value = false;
  const channelData = JSON.parse(event.dataTransfer.getData("text/plain"));
  if (activeChannels.value.length < 4 && !isChannelActive(channelData.id)) {
    activeChannels.value.push(channelData);
  }
};
const onDropOverlay = (event, index) => {
  isDragging.value = false;
  const channelData = JSON.parse(event.dataTransfer.getData("text/plain"));
  if (index < activeChannels.value.length) {
    if (!isChannelActive(channelData.id)) {
      activeChannels.value[index] = channelData;
    }
  } else if (
    activeChannels.value.length < 4 &&
    !isChannelActive(channelData.id)
  ) {
    activeChannels.value.push(channelData);
  }
};

const removeChannel = (index) => {
  activeChannels.value.splice(index, 1);
};

const openChannel = async (channel) => {
  if (!channel || !channel.id) {
    console.warn('No channel selected');
    return;
  }

  try {
    // Initialize the messages array for the channel
    messages.value[channel.id] = [];
    const response = await axios.get(`http://localhost:8000/channels/${channel.id}/get_messages?page=1&per_page=100`, {
      headers: {
        'Authorization': `Bearer ${store.getters['auth/getAccessToken']}`,
        'accept': 'application/json'
      }
    });

    // Retrieve messages from the response
    const messagesData = response.data.messages || [];

    const userPromises = messagesData.map(msg => getUserData(msg.user_id));
    const userDataArray = await Promise.all(userPromises);
    
    const formattedMessages = messagesData.map((msg, index) => ({
      id: msg.id,
      user: userDataArray[index].username,
      content: msg.content,
      time: new Date(msg.timestamp).toLocaleString(),
      avatar: userDataArray[index].profile_pic_url,
      online: msg.online || false,
      channelId: `[${Number(channel.id)}]`  // Store channel ID as a number in square brackets
    }));

    // Update the messages list for the channel
    messages.value[channel.id].push(...formattedMessages);

  } catch (error) {
    console.error('Failed to fetch messages:', error);
  }

  if (!isChannelActive(channel.id)) {
    if (!isDragging.value) {
      // Replace all active channels with the new one if not dragging
      activeChannels.value = [channel];
    } else if (activeChannels.value.length < 4) {
      // Add the channel if dragging and there is space
      activeChannels.value.push(channel);
    }
  }
};

const isChannelActive = (channelId) => {
  return activeChannels.value.some((channel) => channel.id === channelId);
};

const createWorld = async () => {
  const newId = Math.max(...worlds.value.map(w => w.id)) + 1;
  const selectedTemplate = worldTemplates.find(t => t.id === newWorld.value.template);

  const newWorldObj = {
    id: newId,
    name: newWorld.value.name,
    icon: newWorld.value.icon,
    expanded: false,
    notifications: false,
    categories: selectedTemplate.defaultCategories.map((category, categoryIndex) => ({
      id: newId * 100 + categoryIndex + 1,
      name: category.name,
      expanded: false,
      channels: category.channels.map((channel, channelIndex) => ({
        id: `${newId}-${categoryIndex + 1}-${channelIndex + 1}`,
        name: channel.name,
        type: channel.type,
        unread: false
      }))
    }))
  };

  try {
    const response = await axios.post('/worlds/', {
      name: newWorld.value.name,
      description: `World created with template ${newWorld.value.template}`,
      icon_url: newWorld.value.icon,
      is_personal_chat: false,
      partner_id: null,
    });

    if (response.data.id) {
      worlds.value.push(newWorldObj);
    } else {
      alert('Failed to create world on backend');
    }
  } catch (error) {
    console.error('Error creating world:', error);
    alert('Failed to create world on backend');
  }

  // Reset form and close modal
  newWorld.value = { name: '', icon: worldIcons[0], template: 'community' };
  showCreateWorldModal.value = false;
};

const openWorldSettings = (world) => {
  selectedWorld.value = { ...world };
  showWorldSettings.value = true;
};

const saveWorldSettings = () => {
  const index = worlds.value.findIndex(w => w.id === selectedWorld.value.id);
  if (index !== -1) {
    worlds.value[index] = {
      ...worlds.value[index],
      name: selectedWorld.value.name,
      icon: selectedWorld.value.icon,
    };
  }
  showWorldSettings.value = false;
};

const deleteWorld = async () => {
  if (confirm('Вы уверены, что хотите удалить этот мир? Это действие нельзя отменить.')) {
    try {
      await axios.delete(`http://localhost:8000/worlds/${selectedWorld.value.id}`, {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'accept': 'application/json'
        }
      });
      worlds.value = worlds.value.filter(w => w.id !== selectedWorld.value.id);
      showWorldSettings.value = false;
    } catch (error) {
      console.error('Failed to delete world:', error);
    }
  }
};

const openCreateCategoryModal = (worldId) => {
  selectedWorldId.value = worldId;
  showCreateCategoryModal.value = true;
};

const createCategory = async () => {
  const world = worlds.value.find(w => w.id === selectedWorldId.value);

  if (!world) {
    alert('World not found');
    return;
  }

  const newId = Math.max(...world.categories.map(c => c.id), 0) + 1;

  try {
    // Отправляем запрос на создание категории
    const response = await axios.post('/worlds/', {
      name: newCategory.value.name,
      description: '', // Оставляем пустым
      icon_url: '', // Оставляем пустым
      is_personal_chat: false,
      parent_world_id: selectedWorldId.value, // ID родительского мира
    });

    if (response.data.id) {
      // Если успешно создано на сервере, добавляем локально
      world.categories.push({
        id: newId,
        name: newCategory.value.name,
        expanded: false,
        channels: [],
      });
    } else {
      alert('Failed to create category on backend');
    }
  } catch (error) {
    console.error('Error creating category:', error);
    alert('Failed to create category on backend');
  }

  // Сброс формы и закрытие модального окна
  newCategory.value = { name: '' };
  showCreateCategoryModal.value = false;
};

const openCreateChannelModal = (worldId, categoryId) => {
  selectedWorldId.value = worldId;
  selectedCategoryId.value = categoryId;
  showCreateChannelModal.value = true;
};

const createChannel = async () => {
  const world = worlds.value.find(w => w.id === selectedWorldId.value);
  if (world) {
    const category = world.categories.find(c => c.id === selectedCategoryId.value);
    if (category) {
      console.log("create channel info:", 
          newChannel.value.name,
          newChannel.value.type,
          selectedCategoryId.value,
      )
      try {
        const accessToken = store.getters['auth/getAccessToken'];
        const response = await axios.post('http://localhost:8000/channels/create', {
          name: newChannel.value.name,
          type: newChannel.value.type,
          world_id: selectedCategoryId.value
        }, {
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            'Accept': 'application/json'
          }
        });
        const newId = `${world.id}-${category.id}-${category.channels.length + 1}`;
        category.channels.push({
          id: newId,
          name: response.data.name,
          type: response.data.type,
          unread: false
        });
      } catch (error) {
        console.error('Failed to create channel:', error);
      }
    }
  }
  newChannel.value = { name: '', type: 'text' };
  showCreateChannelModal.value = false;
};

// Новые реактивные ссылки
const showParticipantsModal = ref(false);
const invitationLink = ref('');
const worldParticipants = ref([
  { id: 1, name: 'Система', role: 'Администратор', avatar: 'https://i.pinimg.com/736x/75/0c/8e/750c8e51c3a20bfa9579d62854da474d.jpg', online: true },
  { id: 2, name: 'Борис', role: 'Модератор', avatar: 'https://i.pinimg.com/736x/75/0c/8e/750c8e51c3a20bfa9579d62854da474d.jpg', online: true },
  { id: 3, name: 'Чарли', role: 'Участник', avatar: 'https://i.pinimg.com/736x/75/0c/8e/750c8e51c3a20bfa9579d62854da474d.jpg', online: false },
  // Добавьте больше участников по необходимости
]);

// Функция для генерации ссылки-приглашения
const generateInvitationLink = () => {
  return `https://theworlds.space/invite/${selectedWorld.value.id}-${Date.now()}`;
};

// Функция для копирования ссылки-приглашения
const copyInvitationLink = () => {
  navigator.clipboard.writeText(invitationLink.value).then(() => {
    // Здесь вы можете добавить уведомление пользователю о том, что ссылка скопирована
    console.log('Ссылка-приглашение скопирована в буфер обмена');
  });
};

// Функция для отображения модального окна с участниками
const showParticipants = () => {
  showParticipantsModal.value = true;
};

const getRoomConnection = async (channel_id) => {
  try {
    const roomResponse = await axios.post(`http://localhost:8000/voice/${channel_id}/join`,
      {}, 
      {
        headers: {
          'Authorization': `Bearer ${store.getters['auth/getAccessToken']}`,
          'accept': 'application/json'
        }
      }
    );
    return roomResponse.data;
  } catch (error) {
    console.log(error)
  }
}

// Функция для подключения ёосовому или видео каналу
const connectToChannel = async (channel) => {
  const roomData = await getRoomConnection(channel.id)
  const userData = await getUserData()

  channel.connected = true;
  connectToJitsi(
    channel,
    userData.username,
    roomData.room_id, 
    roomData.password
  );
};

// Функция для отключения от голосового или видео канала
const disconnectFromChannel = async (channel) => {
  const elements = document.querySelectorAll('[id^="jitsiConferenceFrame"]');
  elements.forEach(element => {
    element.parentNode.removeChild(element);
  })

  const roomResponse = await axios.post(
    `http://localhost:8000/voice/${channel.id}/leave`, {}, {
      headers: {
        'Authorization': `Bearer ${store.getters['auth/getAccessToken']}`,
        'accept': 'application/json'
    }
  });

  channel.connected = false;
};

// Анимации
onMounted(() => {
  const animateCSS = (element, animation, prefix = 'animate__') =>
    new Promise((resolve, reject) => {
      const animationName = `${prefix}${animation}`;
      const node = document.querySelector(element);

      node.classList.add(`${prefix}animated`, animationName);

      function handleAnimationEnd(event) {
        event.stopPropagation();
        node.classList.remove(`${prefix}animated`, animationName);
        resolve('Animation ended');
      }

      node.addEventListener('animationend', handleAnimationEnd, {once: true});
    });
});
</script>


<style>

/* Дополнительные стили для анимаций */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}
.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>