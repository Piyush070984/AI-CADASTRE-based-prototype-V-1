export function AsyncState({ loading, error, empty, children }: { loading: boolean; error?: string; empty?: boolean; children: React.ReactNode }) {
  if (loading) return <p className="rounded bg-blue-50 p-3 text-blue-800">Loading...</p>
  if (error) return <p className="rounded bg-red-50 p-3 text-red-700">{error}</p>
  if (empty) return <p className="rounded bg-slate-100 p-3 text-slate-700">No data available yet.</p>
  return <>{children}</>
}
