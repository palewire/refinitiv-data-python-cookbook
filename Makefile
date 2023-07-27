serve:
	cd ./docs && pipenv run make livhtml

build:
	pip install -r docs/requirements.txt
	cd ./docs && sphinx-build -b html src _build