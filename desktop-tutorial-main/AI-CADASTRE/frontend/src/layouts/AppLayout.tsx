import { Link, NavLink, Outlet } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'

const navItems = [
  ['dashboard', 'Dashboard'],
  ['projects', 'Projects'],
  ['upload', 'Data Upload'],
  ['processing', 'Processing Monitor'],
  ['map', 'GIS Map'],
  ['verification', 'Parcel Verification'],
  ['reports', 'Reports & Exports'],
  ['settings', 'Settings / User Management'],
]

export function AppLayout() {
  const { user, logout } = useAuth()

  return (
    <div className="min-h-screen bg-blue-50 text-slate-900">
      <header className="flex items-center justify-between bg-blue-900 px-6 py-4 text-white">
        <Link to="/dashboard" className="text-xl font-bold">AI-CADASTRE</Link>
        <div className="flex items-center gap-3 text-sm">
          <span>{user?.name} ({user?.role})</span>
          <button className="rounded bg-white/20 px-3 py-1 hover:bg-white/30" onClick={logout}>Logout</button>
        </div>
      </header>
      <div className="grid min-h-[calc(100vh-64px)] grid-cols-[250px_1fr]">
        <aside className="border-r border-blue-100 bg-white p-4">
          <nav className="space-y-2">
            {navItems.map(([path, label]) => (
              <NavLink
                key={path}
                to={`/${path}`}
                className={({ isActive }) =>
                  `block rounded px-3 py-2 text-sm ${isActive ? 'bg-blue-100 text-blue-900' : 'text-slate-700 hover:bg-blue-50'}`
                }
              >
                {label}
              </NavLink>
            ))}
          </nav>
        </aside>
        <main className="p-6">
          <Outlet />
        </main>
      </div>
    </div>
  )
}
