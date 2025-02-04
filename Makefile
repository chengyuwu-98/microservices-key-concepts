install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv testadd.py testfastapi.py testflask.py

format:
	black *.py

lint:
	pylint --disable=R,C mainflask.py mainfastapi.py

all: install lint