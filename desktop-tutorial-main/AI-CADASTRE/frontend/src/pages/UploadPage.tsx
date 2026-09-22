import { useState } from 'react'
import { api } from '../api/client'

export function UploadPage() {
  const [projectId, setProjectId] = useState('1')
  const [message, setMessage] = useState('')

  const onUpload = async (file: File | null) => {
    if (!file) return
    const formData = new FormData()
    formData.append('project_id', projectId)
    formData.append('file', file)

    try {
      const response = await api.post('/uploads', formData)
      setMessage(`Success: ${response.data.filename} uploaded in demo mode`)
    } catch {
      setMessage('Upload failed. Check file type/size.')
    }
  }

  return (
    <section>
      <h1 className="text-xl font-bold text-blue-900">Data Upload</h1>
      <p className="mt-1 text-sm text-slate-600">Allowed: .geojson, .json, .csv, .tif/.tiff, .zip (demo validation active).</p>
      <div className="mt-4 rounded bg-white p-4 shadow-sm">
        <label className="block text-sm">Project ID
          <input className="mt-1 w-32 rounded border p-2" value={projectId} onChange={(e) => setProjectId(e.target.value)} />
        </label>
        <input className="mt-3" type="file" onChange={(e) => onUpload(e.target.files?.[0] ?? null)} />
        {message && <p className="mt-3 rounded bg-blue-50 p-2 text-sm text-blue-800">{message}</p>}
      </div>
    </section>
  )
}
