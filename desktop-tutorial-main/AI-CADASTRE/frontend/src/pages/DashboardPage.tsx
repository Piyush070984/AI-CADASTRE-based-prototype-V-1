import { StatusCard } from '../components/StatusCard'
import { useAuth } from '../contexts/AuthContext'

export function DashboardPage() {
  const { user } = useAuth()
  return (
    <section>
      <h1 className="text-2xl font-bold text-blue-900">{user?.role === 'admin' ? 'Admin Dashboard' : 'Surveyor Dashboard'}</h1>
      <p className="mt-1 text-sm text-slate-600">Demo processing and map statistics until real AI/GIS pipeline is integrated.</p>
      <div className="mt-5 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <StatusCard title="Projects" value={1} hint="Nagpur demo project" />
        <StatusCard title="Uploads" value={2} hint="GeoJSON + CSV demo" />
        <StatusCard title="Processing" value="demo_complete" hint="Deterministic placeholder" />
        <StatusCard title="Verification Queue" value={4} hint={user?.role === 'admin' ? 'Monitor surveyor progress' : 'Review and submit decisions'} />
      </div>
    </section>
  )
}
