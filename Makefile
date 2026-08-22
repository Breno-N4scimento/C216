PYTHON = python
PIP = pip
VENV = .venv

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) main.py

test:
	$(PYTHON) -m pytest

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
