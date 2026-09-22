import { useState } from 'react'
import { api } from '../api/client'

export function ProcessingPage() {
  const [projectId, setProjectId] = useState('1')
  const [result, setResult] = useState<string>('')

  const start = async () => {
    const response = await api.post('/processing/start', { project_id: Number(projectId) })
    setResult(JSON.stringify(response.data, null, 2))
  }

  return (
    <section>
      <h1 className="text-xl font-bold text-blue-900">Processing Monitor</h1>
      <p className="mt-1 text-sm text-slate-600">Pipeline output is deterministic demo metadata until worker + trained model integration.</p>
      <div className="mt-3 flex gap-2">
        <input className="rounded border p-2" value={projectId} onChange={(e) => setProjectId(e.target.value)} />
        <button className="rounded bg-blue-700 px-4 py-2 text-white" onClick={start}>Start Processing</button>
      </div>
      {result && <pre className="mt-4 overflow-auto rounded bg-slate-900 p-4 text-xs text-green-200">{result}</pre>}
    </section>
  )
}
