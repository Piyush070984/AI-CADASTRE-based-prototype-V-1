export type Role = 'admin' | 'surveyor'

export interface User {
  id: number
  name: string
  email: string
  role: Role
}

export interface Project {
  id: number
  name: string
  location: string
  status: string
  created_by_id: number
  created_at: string
}

export interface Parcel {
  id: number
  project_id: number
  name: string
  geometry_geojson: string
  area_sq_m: number
  confidence: number
  verification_status: string
  is_demo: boolean
}
