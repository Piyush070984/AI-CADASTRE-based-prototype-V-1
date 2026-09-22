import { NagpurMap } from '../maps/NagpurMap'

export function MapPage() {
  return (
    <section>
      <h1 className="text-xl font-bold text-blue-900">GIS Map</h1>
      <p className="mt-1 text-sm text-slate-600">Nagpur-centered demo parcel/building/road layers.</p>
      <div className="mt-4">
        <NagpurMap />
      </div>
    </section>
  )
}
