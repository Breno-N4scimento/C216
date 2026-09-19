```makefile
PYTHON = python
POETRY = $(PYTHON) -m poetry
BACKEND_DIR = backend

# =========================
# Desenvolvimento
# =========================

install:
	cd $(BACKEND_DIR) && $(POETRY) install

run:
	cd $(BACKEND_DIR) && $(POETRY) run uvicorn main:app --reload

test:
	cd $(BACKEND_DIR) && $(POETRY) run pytest

lint:
	cd $(BACKEND_DIR) && $(POETRY) run ruff check .

format:
	cd $(BACKEND_DIR) && $(POETRY) run ruff format .

clean:
	cd $(BACKEND_DIR) && $(PYTHON) -c "import shutil; shutil.rmtree('__pycache__', ignore_errors=True)"

# =========================
# Docker
# =========================

docker-build:
	docker compose build

docker-up:
	docker compose up -d

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
	@echo "Desenvolvimento:"
	@echo "  make install        - Instala as dependências"
	@echo "  make run            - Executa o backend localmente"
	@echo "  make test           - Executa os testes com pytest"
	@echo "  make lint           - Verifica o código com Ruff"
	@echo "  make format         - Formata o código com Ruff"
	@echo "  make clean          - Remove arquivos temporários"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build   - Constrói as imagens Docker"
	@echo "  make docker-up      - Inicia os containers"
	@echo "  make docker-down    - Para os containers"
	@echo "  make docker-logs    - Mostra os logs dos containers"
	@echo "  make docker-restart - Reinicia os containers"
	@echo "  make docker-ps      - Mostra o status dos containers"
	@echo "  make docker-clean   - Remove containers e volumes"

.PHONY: install run test lint format clean docker-build docker-up docker-down docker-logs docker-restart docker-ps docker-clean help
```
