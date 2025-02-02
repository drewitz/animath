.PHONY: all

all: BinomialDist.html

BinomialDist.html: py/normal_dist.py
	manim-slides render py/normal_dist.py BinomialDist
	manim-slides convert -ccontrols=true BinomialDist docs/slides/BinomialDist.html

