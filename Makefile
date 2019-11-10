
SCAN_DIRS=ecs_testing_intro/*.py tests/*.py

lint:
	black -l 80 ${SCAN_DIRS}
	pylint ${SCAN_DIRS}
	mypy --strict ${SCAN_DIRS}
	pydocstyle ${SCAN_DIRS}

test:
	py.test
