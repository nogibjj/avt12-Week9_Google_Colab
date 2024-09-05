install:
	pip install --upgrade && pip install -r requirements.txt 
format:
	black*.py
lint: 
	pylint --disable=R, C --ignore-patters=test_.*?py *.py
test:
	python -m pytest -cov=main test_main.py

all: install format lint test

