.PHONY: run

run:
	@python3 src/main.py
test:
	@python3 src/util_tests.py
	@python3 src/sha256_tests.py
