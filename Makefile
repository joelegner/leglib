.PHONY: docs
docs:
	cd docs && make html
	
.PHONY:test
test: doctest mypy unittest

.PHONY:unittest
unittest:
	pipenv run python3 -m unittest discover -s leglib -v

.PHONY:doctest
doctest:
	pipenv run python3 -m doctest leglib/unitval.py

.PHONY:mypy
mypy:
	mypy leglib/*.py