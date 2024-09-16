install:
	pip install --upgrade pip && pip install -r requirements.txt 
format:
	black *.py
lint: 
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py .
test:
	python -m pytest -cov=main test_main.py *.ipynb

generate_and_push:
	python main.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"	
	git add .
	git commit -m "Prepare report"
	git push


all: install format lint test

