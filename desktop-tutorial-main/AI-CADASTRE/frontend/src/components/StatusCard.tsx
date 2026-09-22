export function StatusCard({ title, value, hint }: { title: string; value: string | number; hint?: string }) {
  return (
    <article className="rounded-lg border border-blue-200 bg-white p-4 shadow-sm">
      <h3 className="text-sm font-semibold text-blue-900">{title}</h3>
      <p className="mt-2 text-2xl font-bold text-slate-900">{value}</p>
      {hint && <p className="mt-1 text-xs text-slate-500">{hint}</p>}
    </article>
  )
}
