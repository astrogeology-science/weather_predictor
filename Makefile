all: save
	python3 app.py

init:
	virtualenv .
	pip3 install -r requirements.txt

save: *.py
	pip3 freeze > requirements.txt
