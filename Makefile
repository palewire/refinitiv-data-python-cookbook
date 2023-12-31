serve:
	pipenv run sphinx-autobuild -b html docs/src docs/_build_html

build:
	pip install -r docs/requirements.txt
	python docs/createconf.py
	cd ./docs && sphinx-build -b html src _build
