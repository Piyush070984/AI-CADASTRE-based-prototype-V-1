import { useEffect, useState } from 'react'
import { api } from '../api/client'

interface Summary {
  mode: string
  warning: string
  total_projects: number
  total_processing_jobs: number
  total_parcels: number
  verified_parcels: number
}

export function ReportsPage() {
  const [summary, setSummary] = useState<Summary | null>(null)

  useEffect(() => {
    api.get('/reports/summary').then((response) => setSummary(response.data))
  }, [])

  return (
    <section>
      <h1 className="text-xl font-bold text-blue-900">Reports & Exports</h1>
      {summary ? (
        <div className="mt-3 rounded bg-white p-4 shadow-sm">
          <p className="text-xs text-yellow-700">{summary.warning}</p>
          <ul className="mt-2 space-y-1 text-sm">
            <li>Total projects: {summary.total_projects}</li>
            <li>Processing jobs: {summary.total_processing_jobs}</li>
            <li>Total parcels: {summary.total_parcels}</li>
            <li>Verified parcels: {summary.verified_parcels}</li>
          </ul>
          <div className="mt-3 flex gap-2">
            <a className="rounded bg-blue-700 px-3 py-2 text-sm text-white" href={`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/api/v1/exports/parcels.geojson`} target="_blank">Export GeoJSON</a>
            <a className="rounded bg-slate-700 px-3 py-2 text-sm text-white" href={`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/api/v1/exports/parcels.csv`} target="_blank">Export CSV</a>
          </div>
        </div>
      ) : (
        <p className="mt-3 rounded bg-blue-50 p-3 text-blue-800">Loading report...</p>
      )}
    </section>
  )
}
