DOCS_DIR = docs

.PHONY:test
test:
	python docs/source/structural/_static/usage.py > docs/source/structural/_static/usage.txt
	cd structural/examples && python __init__.py
	coverage run --omit *virtualenvs* -m unittest discover
	coverage html -d docs/coverage
	coverage report >> docs/source/coverage.txt
	coverage report

.PHONY:clean
clean:
	find . -name '*.pyc' -exec rm {} \;

.PHONY:html
html:
	make -C $(DOCS_DIR) html

.PHONY:examples
examples:
	cd structural/examples && python __init__.py

