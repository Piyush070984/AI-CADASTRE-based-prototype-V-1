import { createContext, useContext, useEffect, useMemo, useState } from 'react'
import { authApi } from '../api/services'
import type { User } from '../types'

interface AuthContextType {
  user: User | null
  loading: boolean
  login: (email: string, password: string) => Promise<void>
  logout: () => void
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const token = localStorage.getItem('aicadastre_token')
    if (!token) {
      setLoading(false)
      return
    }
    authApi
      .me()
      .then(setUser)
      .finally(() => setLoading(false))
  }, [])

  const login = async (email: string, password: string) => {
    const token = await authApi.login(email, password)
    localStorage.setItem('aicadastre_token', token)
    const profile = await authApi.me()
    setUser(profile)
  }

  const logout = () => {
    localStorage.removeItem('aicadastre_token')
    setUser(null)
  }

  const value = useMemo(() => ({ user, loading, login, logout }), [user, loading])
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) {
    throw new Error('useAuth must be used within AuthProvider')
  }
  return ctx
}
