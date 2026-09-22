import { useAuth } from '../contexts/AuthContext'

export function SettingsPage() {
  const { user } = useAuth()
  return (
    <section>
      <h1 className="text-xl font-bold text-blue-900">Settings & User Management</h1>
      <div className="mt-3 rounded bg-white p-4 shadow-sm text-sm">
        <p>Current role: <strong>{user?.role}</strong></p>
        <p className="mt-2">Admin users can manage users via backend endpoint <code>/api/v1/users</code>.</p>
        <p className="mt-2">This page is intentionally lightweight for the first implementation foundation.</p>
      </div>
    </section>
  )
}
