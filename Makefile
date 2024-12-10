.PHONY: setup run tests clean

install:
	python3 -m venv venv
	. venv/bin/activate; pip install --upgrade pip; pip install -r requirements.txt

run:
	. venv/bin/activate; FLASK_APP=app.py FLASK_ENV=development flask run --host=0.0.0.0 --port=5001

tests:
	. venv/bin/activate; pytest tests

clean:
	rm -rf venv
	find . -type f -name "*.pyc" -delete
