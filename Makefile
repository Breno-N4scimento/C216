PYTHON = python
POETRY = $(PYTHON) -m poetry
BACKEND_DIR = backend

install:
	cd $(BACKEND_DIR) && $(POETRY) install --no-root

run:
	cd $(BACKEND_DIR) && $(POETRY) run uvicorn main:app --reload

test:
	cd $(BACKEND_DIR) && $(POETRY) run pytest

clean:
	cd $(BACKEND_DIR) && $(PYTHON) -c "import shutil; shutil.rmtree('__pycache__', ignore_errors=True)"

# Docker

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
	@echo "  make install        - Instala as dependências"
	@echo "  make run            - Executa o projeto"
	@echo "  make test           - Executa os testes"
	@echo "  make clean          - Remove arquivos temporários"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build   - Constrói as imagens Docker"
	@echo "  make docker-up      - Inicia os containers"
	@echo "  make docker-down    - Para os containers"
	@echo "  make docker-logs    - Mostra os logs"
	@echo "  make docker-restart - Reinicia os containers"
	@echo "  make docker-ps      - Mostra os containers"
	@echo "  make docker-clean   - Remove containers e volumes"

.PHONY: install run test clean docker-build docker-up docker-down docker-logs docker-restart docker-ps docker-clean help