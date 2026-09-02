PYTHON = python
POETRY = $(PYTHON) -m poetry

install:
	$(POETRY) install --no-root

run:
	$(POETRY) run uvicorn main:app --reload

test:
	$(POETRY) run pytest

clean:
	$(PYTHON) -c "import shutil; shutil.rmtree('__pycache__', ignore_errors=True)"

help:
	@echo "Comandos disponíveis:"
	@echo "  make install  - Instala as dependências"
	@echo "  make run      - Executa o projeto"
	@echo "  make test     - Executa os testes"
	@echo "  make clean    - Remove arquivos temporários"
	@echo "  make help     - Mostra esta ajuda"

.PHONY: install run test clean help