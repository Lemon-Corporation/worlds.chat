import api from './index'

export const createWorld = (worldData) => {
  return api.post('/worlds/', worldData)  // Изменен URL
}

export const generateInviteLink = (worldId) => {
  return api.post(`/worlds/${worldId}/invite`)
}