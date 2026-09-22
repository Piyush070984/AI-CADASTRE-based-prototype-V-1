import axios from 'axios'

const baseURL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export const api = axios.create({
  baseURL: `${baseURL}/api/v1`,
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('aicadastre_token')
  if (token) {
    config.headers.Authorization = 'Bearer ' + token
  }
  return config
})
