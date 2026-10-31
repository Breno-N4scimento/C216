
PYTHON = python
POETRY = $(PYTHON) -m poetry
BACKEND_DIR = backend
FRONTEND_DIR = frontend
NPM = npm

#Backend

install:
	cd $(BACKEND_DIR) && $(POETRY) install

run:
	cd $(BACKEND_DIR) && $(POETRY) run uvicorn app.main:app --reload

test: test-db
	cd $(BACKEND_DIR) && $(POETRY) run pytest -v

test-db:
	docker compose up -d db
	docker compose up --wait db
	$(PYTHON) -c "import subprocess; result = subprocess.run(['docker', 'compose', 'exec', '-T', 'db', 'psql', '-U', 'postgres', '-d', 'postgres', '-tAc', \"SELECT 1 FROM pg_database WHERE datname = 'backend_test_db'\"], capture_output=True, text=True, check=True); exists = result.stdout.strip() == '1'; print('Banco de testes já existe.' if exists else 'Criando banco de testes...'); subprocess.run(['docker', 'compose', 'exec', '-T', 'db', 'psql', '-U', 'postgres', '-d', 'postgres', '-c', 'CREATE DATABASE backend_test_db;'], check=True) if not exists else None"

lint:
	cd $(BACKEND_DIR) && $(POETRY) run ruff check .

format:
	cd $(BACKEND_DIR) && $(POETRY) run ruff format .

clean:
	cd $(BACKEND_DIR) && $(PYTHON) -c "import shutil; shutil.rmtree('__pycache__', ignore_errors=True)"


#Frontend

frontend-install:
	cd $(FRONTEND_DIR) && $(NPM) ci

frontend-run:
	cd $(FRONTEND_DIR) && $(NPM) run dev

frontend-build:
	cd $(FRONTEND_DIR) && $(NPM) run build

frontend-test:
	cd $(FRONTEND_DIR) && $(NPM) run test

frontend-lint:
	cd $(FRONTEND_DIR) && $(NPM) run lint

frontend-format:
	cd $(FRONTEND_DIR) && $(NPM) run format

frontend-check:
	cd $(FRONTEND_DIR) && $(NPM) run check


#docker

docker-build:
	docker compose build

docker-up:
	docker compose up -d

up-build:
	docker compose up -d --build

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f

docker-restart:
	docker compose restart

docker-ps:
	docker compose ps

docker-clean:
	docker compose down -v

help:
	@echo "Comandos disponíveis:"
	@echo ""
	@echo "Backend:"
	@echo "  make install          - Instala as dependências"
	@echo "  make run              - Executa o backend"
	@echo "  make format           - Formata o backend com Ruff"
	@echo "  make lint             - Verifica o backend com Ruff"
	@echo "  make test             - Prepara o banco e executa os testes"
	@echo ""
	@echo "Frontend:"
	@echo "  make frontend-install - Instala as dependências"
	@echo "  make frontend-run     - Executa o frontend"
	@echo "  make frontend-build   - Gera o build"
	@echo "  make frontend-test    - Executa os testes"
	@echo "  make frontend-lint    - Verifica o código com Biome"
	@echo "  make frontend-format  - Formata o código"
	@echo "  make frontend-check   - Executa as verificações do Biome"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build     - Constrói as imagens"
	@echo "  make docker-up        - Inicia os containers"
	@echo "  make up-build         - Constrói e inicia os serviços"
	@echo "  make docker-down      - Para os containers"
	@echo "  make docker-logs      - Exibe os logs"
	@echo "  make docker-ps        - Mostra o status dos containers"
	@echo "  make docker-clean     - Remove containers e volumes"


.PHONY: install run test test-db lint format clean frontend-install frontend-run frontend-build frontend-test frontend-lint frontend-format frontend-check docker-build docker-up up-build docker-down docker-logs docker-restart docker-ps docker-clean help
