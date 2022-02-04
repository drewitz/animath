.PHONY: all

all: py/*.py
	@for f in $(shell ls py/*.py); do manim render $${f}; done

	echo "vid_data =" > docs/vid_data.js
	cat data.json >> docs/vid_data.js
	echo ";\n" >> docs/vid_data.js