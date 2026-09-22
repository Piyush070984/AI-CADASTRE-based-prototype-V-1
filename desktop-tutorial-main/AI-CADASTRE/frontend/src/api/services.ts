import { api } from './client'
import type { Parcel, Project, User } from '../types'

export const authApi = {
  async login(email: string, password: string): Promise<string> {
    const response = await api.post('/auth/login', { email, password })
    return response.data.access_token
  },
  async me(): Promise<User> {
    const response = await api.get('/auth/me')
    return response.data
  },
}

export const projectApi = {
  async list(): Promise<Project[]> {
    const response = await api.get('/projects')
    return response.data
  },
  async create(name: string, location: string): Promise<Project> {
    const response = await api.post('/projects', { name, location })
    return response.data
  },
}

export const parcelApi = {
  async list(projectId?: number): Promise<Parcel[]> {
    const response = await api.get('/parcels', { params: projectId ? { project_id: projectId } : undefined })
    return response.data
  },
  async review(parcelId: number, decision: 'accept' | 'reject' | 'correction', comment: string): Promise<void> {
    await api.post(`/parcels/${parcelId}/review`, { decision, comment })
  },
}
