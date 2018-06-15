DOC_SOURCES = config docs dq Makefile

.PHONY: bootstrap
bootstrap:
	pip3 -q install -r requirements.txt
	python3 setup.py develop

.PHONY: create-db
create-db:
	@dbadmin create

.PHONY: drop-db
drop-db:
	@dbadmin drop

.PHONY: migrate-db
migrate-db:
	@alembic upgrade head

.PHONY: bootstrap-db
bootstrap-db: drop-db create-db migrate-db
	@echo Successfully bootstrapped database

.PHONY: build
build:
	@python3 setup.py sdist bdist_wheel

.PHONY: upload
upload:
	@twine upload dist/*

.PHONY: lint
lint:
	@flake8 dq

.PHONY: docs
docs:
	git checkout gh-pages
	rm -rf _sources _static _modules *.html *.js
	git checkout master $(DOC_SOURCES)
	git reset HEAD
	sphinx-build -b html docs docs/build
	mv -fv docs/build/* ./
	rm -rf $(DOC_SOURCES)
	touch .nojekyll
	git add -A
	git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout master

.PHONY: test
test: lint
	@set -e; \
	$(MAKE) bootstrap-db; \
	py.test --cov-report term-missing --cov=dq tests/
