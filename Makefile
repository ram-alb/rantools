install:
	poetry install

shell:
	poetry run python manage.py shell_plus --ipython

lint:
	poetry run flake8

test:
	poetry run python manage.py test

check: lint test

dev:
	poetry run python manage.py runserver

.PHONY: install shell lint test check dev