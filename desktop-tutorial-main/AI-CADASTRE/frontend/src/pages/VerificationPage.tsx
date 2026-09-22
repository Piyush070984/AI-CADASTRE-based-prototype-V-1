import { useEffect, useState } from 'react'
import { parcelApi } from '../api/services'
import type { Parcel } from '../types'

export function VerificationPage() {
  const [parcels, setParcels] = useState<Parcel[]>([])
  const [message, setMessage] = useState('')

  const load = () => parcelApi.list(1).then(setParcels)
  useEffect(() => {
    void load()
  }, [])

  const review = async (parcelId: number, decision: 'accept' | 'reject' | 'correction') => {
    await parcelApi.review(parcelId, decision, 'Ground review submitted from demo UI')
    setMessage(`Parcel ${parcelId}: ${decision}`)
    load()
  }

  return (
    <section>
      <h1 className="text-xl font-bold text-blue-900">Parcel Verification</h1>
      <p className="mt-1 text-sm text-slate-600">Select parcels and submit accept/reject/correction with demo workflow.</p>
      {message && <p className="mt-3 rounded bg-green-50 p-2 text-sm text-green-700">{message}</p>}
      <ul className="mt-4 space-y-2">
        {parcels.map((parcel) => (
          <li key={parcel.id} className="rounded bg-white p-3 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <span>
                <strong>{parcel.name}</strong> • {parcel.area_sq_m.toFixed(1)} m² • status: {parcel.verification_status}
              </span>
              <div className="flex gap-2">
                <button className="rounded bg-green-600 px-2 py-1 text-xs text-white" onClick={() => review(parcel.id, 'accept')}>Accept</button>
                <button className="rounded bg-red-600 px-2 py-1 text-xs text-white" onClick={() => review(parcel.id, 'reject')}>Reject</button>
                <button className="rounded bg-amber-600 px-2 py-1 text-xs text-white" onClick={() => review(parcel.id, 'correction')}>Correction</button>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </section>
  )
}
