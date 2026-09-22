import L from 'leaflet'
import type { GeoJsonObject } from 'geojson'
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import demoLayer from '../data/nagpur-demo.json'

const center: [number, number] = [21.1458, 79.0882]

export function NagpurMap() {
  return (
    <div>
      <p className="mb-3 rounded bg-yellow-50 p-3 text-xs text-yellow-800">
        Demo layer only: Not official cadastral data. Replace with authorized uploaded GIS data.
      </p>
      <MapContainer center={center} zoom={15} className="h-[500px] w-full rounded-lg border" scrollWheelZoom>
        <TileLayer attribution='&copy; OpenStreetMap contributors' url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png' />
        <GeoJSON
          data={demoLayer as GeoJsonObject}
          style={(feature) => {
            const kind = feature?.properties?.kind as string | undefined
            if (kind === 'parcel') return { color: '#1d4ed8', weight: 2, fillOpacity: 0.25 }
            if (kind === 'building') return { color: '#0f766e', weight: 1, fillOpacity: 0.45 }
            return { color: '#7c3aed', weight: 2 }
          }}
          onEachFeature={(feature, layer) => {
            layer.bindTooltip(`${feature.properties?.name ?? 'Feature'} (${feature.properties?.kind ?? 'demo'})`)
          }}
        />
      </MapContainer>
    </div>
  )
}

// Fix Leaflet marker icon paths for Vite builds
// eslint-disable-next-line @typescript-eslint/no-explicit-any
;(delete (L.Icon.Default.prototype as any)._getIconUrl)
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png',
  iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
})
