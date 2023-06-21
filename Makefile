all:
	install
	lint

install:
	pip install --upgrade pip 
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py

freeze:
	pip freeze > requirements.txt

corn:
	gunicorn --bind 0.0.0.0:9696 main:app

inference:
	python3 src/inference.py

senv:
	python3 -m venv .venv
	source .venv/bin/activate


