.PHONY: docs
docs:
	cd docs && make html
	
.PHONY:test
test:
	pipenv run python3 -m unittest discover -s leglib -v

