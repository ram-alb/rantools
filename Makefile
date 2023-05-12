install:
	poetry install

shell:
	poetry run python manage.py shell_plus --ipython

lint:
	poetry run flake8

test:
	poetry run coverage run --source='.' manage.py test

test-coverage-report: test
	poetry run coverage report -m $(ARGS)
	poetry run coverage erase

test-coverage-report-xml:
	poetry run coverage xml

check: lint test

dev:
	poetry run python manage.py runserver

.PHONY: install shell lint test check dev