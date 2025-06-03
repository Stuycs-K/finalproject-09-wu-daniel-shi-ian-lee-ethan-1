.PHONY: run

run:
	@python3 src/main.py
test:
	@python3 test/util_tests.py
	@python3 test/sha256_tests.py
