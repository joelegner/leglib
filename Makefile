.PHONY: docs
docs:
	cd docs && make html
	
.PHONY:test
test:
	pipenv run python3 -m unittest discover -s leglib -v
	# Doctests must be added manually for now
	pipenv run python3 -m doctest leglib/unitval.py
