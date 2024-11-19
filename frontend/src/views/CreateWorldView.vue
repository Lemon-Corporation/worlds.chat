<template>
  <div class="nexus-create-world">
    <div class="nexus-main-content">
      <h1 class="nexus-page-title">Create a New World</h1>
      <div class="nexus-steps-container">
        <div
          v-for="(step, index) in steps"
          :key="index"
          class="nexus-step"
          :class="{
            'nexus-step-active': currentStep === index,
            'nexus-step-completed': currentStep > index,
          }"
        >
          <div class="nexus-step-number">{{ index + 1 }}</div>
          <div class="nexus-step-label">{{ step }}</div>
        </div>
      </div>
      <form @submit.prevent="submitForm" class="nexus-world-form">
        <!-- Step 1: Basic Information -->
        <div v-if="currentStep === 0" class="nexus-step-content">
          <div class="nexus-form-group">
            <label for="serverName" class="nexus-form-label">World Name</label>
            <input
              id="serverName"
              v-model="serverName"
              type="text"
              required
              class="nexus-form-input"
              placeholder="Enter world name"
            />
          </div>
          <div class="nexus-form-group">
            <label class="nexus-form-label">World Logo</label>
            <div class="nexus-logo-upload">
              <div
                class="nexus-logo-preview"
                :class="{ 'nexus-has-logo': logoPreview }"
              >
                <img
                  v-if="logoPreview"
                  :src="logoPreview"
                  alt="World Logo"
                  class="nexus-logo-image"
                />
                <Upload v-else class="nexus-upload-icon" />
              </div>
              <label for="logoUpload" class="nexus-upload-button">
                Upload Logo
              </label>
              <input
                id="logoUpload"
                type="file"
                accept="image/*"
                class="nexus-hidden-input"
                @change="handleLogoUpload"
              />
            </div>
          </div>
          <div class="nexus-form-group">
            <label class="nexus-form-label">World Privacy</label>
            <div class="nexus-privacy-options">
              <label class="nexus-privacy-option">
                <input
                  type="radio"
                  v-model="isPrivate"
                  :value="false"
                  class="nexus-privacy-radio"
                />
                <span class="nexus-privacy-label">Public</span>
              </label>
              <label class="nexus-privacy-option">
                <input
                  type="radio"
                  v-model="isPrivate"
                  :value="true"
                  class="nexus-privacy-radio"
                />
                <span class="nexus-privacy-label">Private</span>
              </label>
            </div>
          </div>
        </div>

        <!-- Step 2: Description and Category -->
        <div v-if="currentStep === 1" class="nexus-step-content">
          <div class="nexus-form-group">
            <label for="serverDescription" class="nexus-form-label"
              >World Description</label
            >
            <textarea
              id="serverDescription"
              v-model="serverDescription"
              rows="3"
              class="nexus-form-textarea"
              placeholder="Describe your world"
            ></textarea>
          </div>
          <div class="nexus-form-group">
            <label for="serverCategory" class="nexus-form-label"
              >World Category</label
            >
            <select
              id="serverCategory"
              v-model="serverCategory"
              class="nexus-form-select"
            >
              <option value="">Select a category</option>
              <option value="gaming">Gaming</option>
              <option value="education">Education</option>
              <option value="technology">Technology</option>
              <option value="art">Art & Design</option>
              <option value="music">Music</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div class="nexus-form-group">
            <label for="serverTags" class="nexus-form-label">World Tags</label>
            <div class="nexus-tags-container">
              <div
                v-for="(tag, index) in serverTags"
                :key="index"
                class="nexus-tag"
              >
                {{ tag }}
                <button
                  @click="removeTag(index)"
                  class="nexus-remove-tag"
                  type="button"
                >
                  <X class="nexus-remove-icon" />
                </button>
              </div>
              <input
                v-model="newTag"
                @keydown.enter.prevent="addTag"
                type="text"
                class="nexus-tag-input"
                placeholder="Add tags (press Enter)"
              />
            </div>
          </div>
        </div>

        <!-- Step 3: Channels -->
        <div v-if="currentStep === 2" class="nexus-step-content">
          <div class="nexus-form-group">
            <label class="nexus-form-label">Initial Channels</label>
            <div class="nexus-channels-container">
              <div
                v-for="(channel, index) in channels"
                :key="index"
                class="nexus-channel-item"
              >
                <input
                  v-model="channel.name"
                  type="text"
                  class="nexus-channel-input"
                  placeholder="Channel name"
                />
                <div class="nexus-channel-type-selector">
                  <button
                    @click="channel.type = 'text'"
                    class="nexus-channel-type-button"
                    :class="{
                      'nexus-channel-type-active': channel.type === 'text',
                    }"
                    type="button"
                  >
                    <MessageSquare class="nexus-channel-type-icon" />
                    Text
                  </button>
                  <button
                    @click="channel.type = 'voice'"
                    class="nexus-channel-type-button"
                    :class="{
                      'nexus-channel-type-active': channel.type === 'voice',
                    }"
                    type="button"
                  >
                    <Mic class="nexus-channel-type-icon" />
                    Voice
                  </button>
                </div>
                <button
                  @click="removeChannel(index)"
                  class="nexus-remove-channel"
                  type="button"
                >
                  <Trash2 class="nexus-remove-icon" />
                </button>
              </div>
              <button
                @click="addChannel"
                class="nexus-add-channel"
                type="button"
              >
                <Plus class="nexus-add-icon" /> Add Channel
              </button>
            </div>
          </div>
        </div>

        <!-- Step 4: Roles -->
        <div v-if="currentStep === 3" class="nexus-step-content">
          <div class="nexus-form-group">
            <label class="nexus-form-label">Initial Roles</label>
            <div class="nexus-roles-container">
              <div
                v-for="(role, index) in roles"
                :key="index"
                class="nexus-role-item"
              >
                <input
                  v-model="role.name"
                  type="text"
                  class="nexus-role-input"
                  placeholder="Role name"
                />
                <div class="nexus-role-color-picker">
                  <input
                    v-model="role.color"
                    type="color"
                    class="nexus-role-color-input"
                    :id="`role-color-${index}`"
                  />
                  <label
                    :for="`role-color-${index}`"
                    class="nexus-role-color-preview"
                    :style="{ backgroundColor: role.color }"
                  ></label>
                </div>
                <button
                  @click="removeRole(index)"
                  class="nexus-remove-role"
                  type="button"
                >
                  <Trash2 class="nexus-remove-icon" />
                </button>
              </div>
              <button @click="addRole" class="nexus-add-role" type="button">
                <Plus class="nexus-add-icon" /> Add Role
              </button>
            </div>
          </div>
        </div>

        <!-- Step 5: Confirmation -->
        <div v-if="currentStep === 4" class="nexus-step-content">
          <h2 class="nexus-confirmation-title">Confirm World Details</h2>
          <div class="nexus-confirmation-details">
            <p><strong>Name:</strong> {{ serverName }}</p>
            <p>
              <strong>Privacy:</strong> {{ isPrivate ? "Private" : "Public" }}
            </p>
            <p><strong>Category:</strong> {{ serverCategory }}</p>
            <p><strong>Description:</strong> {{ serverDescription }}</p>
            <p><strong>Tags:</strong> {{ serverTags.join(", ") }}</p>
            <p>
              <strong>Channels:</strong>
              {{ channels.map((c) => `${c.name} (${c.type})`).join(", ") }}
            </p>
            <p>
              <strong>Roles:</strong>
              {{ roles.map((r) => `${r.name} (${r.color})`).join(", ") }}
            </p>
          </div>
        </div>

        <div class="nexus-form-actions">
          <button
            v-if="currentStep > 0"
            @click="prevStep"
            class="nexus-prev-button"
            type="button"
          >
            Previous
          </button>
          <button
            v-if="currentStep < steps.length - 1"
            @click="nextStep"
            class="nexus-next-button"
            :disabled="!isStepValid"
            type="button"
          >
            Next
          </button>
          <button
            v-if="currentStep === steps.length - 1"
            type="submit"
            class="nexus-create-button"
            :disabled="!isFormValid"
          >
            Create World
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { Upload, X, Trash2, Plus, MessageSquare, Mic } from "lucide-vue-next";

const steps = ["Basic Info", "Description", "Channels", "Roles", "Confirm"];
const currentStep = ref(0);

const serverName = ref("");
const logoPreview = ref("");
const isPrivate = ref(false);
const serverDescription = ref("");
const serverCategory = ref("");
const serverTags = ref([]);
const newTag = ref("");
const channels = ref([
  { name: "general", type: "text" },
  { name: "voice-chat", type: "voice" },
]);
const roles = ref([
  { name: "Admin", color: "#ff0000" },
  { name: "Moderator", color: "#00ff00" },
]);

const handleLogoUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      logoPreview.value = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};

const addTag = () => {
  if (newTag.value.trim() && !serverTags.value.includes(newTag.value.trim())) {
    serverTags.value.push(newTag.value.trim());
    newTag.value = "";
  }
};

const removeTag = (index) => {
  serverTags.value.splice(index, 1);
};

const addChannel = () => {
  channels.value.push({ name: "", type: "text" });
};

const removeChannel = (index) => {
  channels.value.splice(index, 1);
};

const addRole = () => {
  roles.value.push({ name: "", color: "#ffffff" });
};

const removeRole = (index) => {
  roles.value.splice(index, 1);
};

const isStepValid = computed(() => {
  switch (currentStep.value) {
    case 0:
      return serverName.value.trim() !== "";
    case 1:
      return serverCategory.value !== "";
    case 2:
      return channels.value.every((channel) => channel.name.trim() !== "");
    case 3:
      return roles.value.every((role) => role.name.trim() !== "");
    default:
      return true;
  }
});

const isFormValid = computed(() => {
  return (
    serverName.value.trim() !== "" &&
    serverCategory.value !== "" &&
    channels.value.every((channel) => channel.name.trim() !== "") &&
    roles.value.every((role) => role.name.trim() !== "")
  );
});

const nextStep = () => {
  if (currentStep.value < steps.length - 1 && isStepValid.value) {
    currentStep.value++;
  }
};

const prevStep = () => {
  if (currentStep.value > 0) {
    currentStep.value--;
  }
};

const submitForm = () => {
  if (!isFormValid.value) return;

  const serverData = {
    name: serverName.value,
    logo: logoPreview.value,
    isPrivate: isPrivate.value,
    description: serverDescription.value,
    category: serverCategory.value,
    tags: serverTags.value,
    channels: channels.value,
    roles: roles.value,
  };
  console.log("Creating world with data:", serverData);
  // You would then make an API call to create the server
  // For example: await api.createServer(serverData);
  // After successful creation, you might want to redirect the user or show a success message
};
</script>

<style scoped>
.nexus-create-world {
  display: flex;
  min-height: 100vh;
  font-family: "Orbitron", sans-serif;
  background-color: #0f1117;
  color: #8b9bb4;
}

.nexus-main-content {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
}

.nexus-page-title {
  font-size: 2.5rem;
  font-weight: bold;
  color: #4169e1;
  text-align: center;
  margin-bottom: 2rem;
}

.nexus-steps-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 2rem;
}

.nexus-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
}

.nexus-step-number {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #1e2533;
  color: #8b9bb4;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.nexus-step-active .nexus-step-number {
  background-color: #4169e1;
  color: #ffffff;
}

.nexus-step-completed .nexus-step-number {
  background-color: #4caf50;
  color: #ffffff;
}

.nexus-step-label {
  font-size: 0.8rem;
  text-align: center;
}

.nexus-world-form {
  max-width: 800px;
  margin: 0 auto;
}

.nexus-step-content {
  margin-bottom: 2rem;
}

.nexus-form-group {
  margin-bottom: 1.5rem;
}

.nexus-form-label {
  display: block;
  font-size: 0.9rem;
  font-weight: 500;
  color: #8b9bb4;
  margin-bottom: 0.5rem;
}

.nexus-form-input,
.nexus-form-textarea,
.nexus-form-select,
.nexus-tag-input,
.nexus-channel-input,
.nexus-role-input {
  width: 100%;
  padding: 0.75rem;
  background-color: #1e2533;
  border: 1px solid #2c3647;
  border-radius: 4px;
  color: #ffffff;
  font-family: "Orbitron", sans-serif;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.nexus-form-input:focus,
.nexus-form-textarea:focus,
.nexus-form-select:focus,
.nexus-tag-input:focus,
.nexus-channel-input:focus,
.nexus-role-input:focus {
  outline: none;
  border-color: #4169e1;
  box-shadow: 0 0 0 2px rgba(65, 105, 225, 0.2);
}

.nexus-logo-upload {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nexus-logo-preview {
  width: 100px;
  height: 100px;
  background-color: #1e2533;
  border: 2px dashed #2c3647;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.nexus-has-logo {
  border: none;
}

.nexus-logo-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.nexus-upload-icon {
  width: 32px;
  height: 32px;
  color: #4169e1;
}

.nexus-upload-button {
  padding: 0.5rem 1rem;
  background-color: #4169e1;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.nexus-upload-button:hover {
  background-color: #3a5fcd;
}

.nexus-hidden-input {
  display: none;
}

.nexus-privacy-options {
  display: flex;
  gap: 1rem;
}

.nexus-privacy-option {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.nexus-privacy-radio {
  margin-right: 0.5rem;
}

.nexus-privacy-label {
  font-size: 0.9rem;
}

.nexus-tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.nexus-tag {
  display: flex;
  align-items: center;
  background-color: #4169e1;
  color: #ffffff;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
}

.nexus-remove-tag,
.nexus-remove-channel,
.nexus-remove-role {
  background: none;
  border: none;
  color: #ffffff;
  cursor: pointer;
  padding: 0;
  margin-left: 0.25rem;
}

.nexus-remove-icon {
  width: 16px;
  height: 16px;
}

.nexus-channels-container,
.nexus-roles-container {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.nexus-channel-item,
.nexus-role-item {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.nexus-channel-type-selector {
  display: flex;
  gap: 0.5rem;
}

.nexus-channel-type-button {
  display: flex;
  align-items: center;
  padding: 0.5rem;
  background-color: #1e2533;
  border: 1px solid #2c3647;
  border-radius: 4px;
  color: #8b9bb4;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.nexus-channel-type-active {
  background-color: #4169e1;
  color: #ffffff;
}

.nexus-channel-type-icon {
  width: 16px;
  height: 16px;
  margin-right: 0.25rem;
}

.nexus-role-color-picker {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nexus-role-color-input {
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
}

.nexus-role-color-preview {
  width: 24px;
  height: 24px;
  border-radius: 4px;
  border: 1px solid #2c3647;
  cursor: pointer;
}

.nexus-add-channel,
.nexus-add-role {
  display: flex;
  align-items: center;
  background: none;
  border: 2px dashed #2c3647;
  color: #4169e1;
  padding: 0.5rem;
  border-radius: 4px;
  cursor: pointer;
  transition: border-color 0.3s, color 0.3s;
}

.nexus-add-channel:hover,
.nexus-add-role:hover {
  border-color: #4169e1;
  color: #ffffff;
}

.nexus-add-icon {
  width: 20px;
  height: 20px;
  margin-right: 0.5rem;
}

.nexus-form-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
}

.nexus-prev-button,
.nexus-next-button,
.nexus-create-button {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.nexus-prev-button {
  background-color: #2c3647;
  color: #ffffff;
}

.nexus-prev-button:hover {
  background-color: #3a4556;
}

.nexus-next-button,
.nexus-create-button {
  background-color: #4169e1;
  color: #ffffff;
}

.nexus-next-button:hover:not(:disabled),
.nexus-create-button:hover:not(:disabled) {
  background-color: #3a5fcd;
}

.nexus-next-button:disabled,
.nexus-create-button:disabled {
  background-color: #2c3647;
  cursor: not-allowed;
}

.nexus-confirmation-title {
  font-size: 1.5rem;
  color: #4169e1;
  margin-bottom: 1rem;
}

.nexus-confirmation-details {
  background-color: #1e2533;
  padding: 1rem;
  border-radius: 4px;
}

.nexus-confirmation-details p {
  margin-bottom: 0.5rem;
}

@media (max-width: 768px) {
  .nexus-main-content {
    padding: 1rem;
  }

  .nexus-page-title {
    font-size: 2rem;
  }

  .nexus-steps-container {
    flex-wrap: wrap;
  }

  .nexus-step {
    flex-basis: 50%;
    margin-bottom: 1rem;
  }

  .nexus-logo-upload {
    flex-direction: column;
    align-items: flex-start;
  }

  .nexus-privacy-options {
    flex-direction: column;
  }

  .nexus-channel-item,
  .nexus-role-item {
    flex-direction: column;
    align-items: stretch;
  }

  .nexus-channel-type-selector {
    margin-top: 0.5rem;
  }

  .nexus-role-color-picker {
    margin-top: 0.5rem;
  }

  .nexus-form-actions {
    flex-direction: column;
    gap: 1rem;
  }

  .nexus-prev-button,
  .nexus-next-button,
  .nexus-create-button {
    width: 100%;
  }
}
</style>
