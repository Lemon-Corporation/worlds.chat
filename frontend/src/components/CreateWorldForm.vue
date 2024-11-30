<template>
  <div class="create-world-form">
    <h2>Create New World</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label>World Name:</label>
        <input 
          v-model="worldData.name" 
          type="text" 
          required
        />
      </div>
      
      <div class="form-group">
        <label>Description:</label>
        <textarea 
          v-model="worldData.description" 
          required
        ></textarea>
      </div>

      <button type="submit">Create World</button>
    </form>

    <div v-if="inviteLink" class="invite-link">
      <p>Invite Link:</p>
      <div class="link-container">
        <input type="text" :value="inviteLink" readonly />
        <button @click="copyLink">Copy</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'CreateWorldForm',
  setup() {
    const store = useStore()
    const worldData = ref({
      name: '',
      description: 'New World',
      icon_url: 'https://example.com/default-icon.png', // можно поменять на реальный URL
      is_personal_chat: false,
      partner_id: null
    })
    const inviteLink = ref(null)

    const handleSubmit = async () => {
      try {
        console.log('Submitting world data:', worldData.value)
        const world = await store.dispatch('createWorld', worldData.value)
        console.log('World created:', world)
        
        const link = await store.dispatch('generateInviteLink', world.id)
        console.log('Invite link generated:', link)
        
        inviteLink.value = link
      } catch (error) {
        console.error('Error creating world:', error)
      }
    }

    const copyLink = () => {
      navigator.clipboard.writeText(inviteLink.value)
    }

    return {
      worldData,
      inviteLink,
      handleSubmit,
      copyLink
    }
  }
}
</script>

<style scoped>
.create-world-form {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.invite-link {
  margin-top: 20px;
  padding: 15px;
  background-color: #f5f5f5;
  border-radius: 4px;
}

.link-container {
  display: flex;
  gap: 10px;
}
</style>