import { createWorld, generateInviteLink } from '@/api/worlds'

export default {
  state: {
    currentWorld: null,
    inviteLink: null
  },
  mutations: {
    setCurrentWorld(state, world) {
      state.currentWorld = world
    },
    setInviteLink(state, link) {
      state.inviteLink = link
    }
  },
  actions: {
    async createNewWorld({ commit }, worldData) {
      try {
        const response = await createWorld(worldData)
        commit('setCurrentWorld', response.data)
        return response.data
      } catch (error) {
        throw error
      }
    },
    async getInviteLink({ commit }, worldId) {
      try {
        const response = await generateInviteLink(worldId)
        commit('setInviteLink', response.data.invite_link)
        return response.data.invite_link
      } catch (error) {
        throw error
      }
    }
  }
}