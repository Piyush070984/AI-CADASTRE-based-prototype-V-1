import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { DashboardPage } from './DashboardPage'
import { AuthProvider } from '../contexts/AuthContext'

vi.mock('../api/services', () => ({
  authApi: {
    me: vi.fn().mockResolvedValue({ id: 1, name: 'Admin', email: 'admin@x.com', role: 'admin' }),
    login: vi.fn(),
  },
}))

describe('DashboardPage', () => {
  it('shows dashboard heading', async () => {
    localStorage.setItem('aicadastre_token', 'token')
    render(
      <MemoryRouter>
        <AuthProvider>
          <DashboardPage />
        </AuthProvider>
      </MemoryRouter>,
    )
    expect(await screen.findByText(/Dashboard/i)).toBeTruthy()
  })
})
