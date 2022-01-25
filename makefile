.PHONY: all

all: py/*.py
	@for f in $(shell ls py/*.py); do manim render -qm -a $${f}; done
