import { useEffect, useState } from 'react'
import type { FormEvent } from 'react'
import { projectApi } from '../api/services'
import { AsyncState } from '../components/AsyncState'
import type { Project } from '../types'

export function ProjectsPage() {
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [name, setName] = useState('')
  const [location, setLocation] = useState('Nagpur')

  const load = () => {
    setLoading(true)
    setError('')
    projectApi.list().then(setProjects).catch(() => setError('Could not load projects')).finally(() => setLoading(false))
  }

  useEffect(load, [])

  const create = async (event: FormEvent) => {
    event.preventDefault()
    await projectApi.create(name, location)
    setName('')
    load()
  }

  return (
    <section>
      <h1 className="text-xl font-bold text-blue-900">Projects</h1>
      <form className="mt-3 grid gap-3 rounded bg-white p-4 shadow-sm md:grid-cols-3" onSubmit={create}>
        <input className="rounded border p-2" placeholder="Project name" value={name} onChange={(e) => setName(e.target.value)} required />
        <input className="rounded border p-2" placeholder="Location" value={location} onChange={(e) => setLocation(e.target.value)} required />
        <button className="rounded bg-blue-700 px-4 py-2 text-white">Create Project</button>
      </form>
      <div className="mt-4">
        <AsyncState loading={loading} error={error} empty={!projects.length}>
          <ul className="space-y-2">
            {projects.map((project) => (
              <li key={project.id} className="rounded bg-white p-3 shadow-sm">
                <strong>{project.name}</strong> • {project.location} • {project.status}
              </li>
            ))}
          </ul>
        </AsyncState>
      </div>
    </section>
  )
}
