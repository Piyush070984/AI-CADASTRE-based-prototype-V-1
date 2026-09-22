.PHONY: backend-install backend-run backend-test frontend-install frontend-dev frontend-build frontend-test docker-up docker-down

backend-install:
	cd backend && python -m pip install -r requirements.txt

backend-run:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

backend-test:
	cd .. && pytest AI-CADASTRE/tests/backend -q

frontend-install:
	cd frontend && npm install

frontend-dev:
	cd frontend && npm run dev -- --host 0.0.0.0 --port 5173

frontend-build:
	cd frontend && npm run build

frontend-test:
	cd frontend && npm run test

docker-up:
	docker compose up --build

docker-down:
	docker compose down -v
