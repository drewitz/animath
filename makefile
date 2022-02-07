.PHONY: all

vidfolder = docs/videos

$(vidfolder)/Allgemein.mp4: py/binom.py
	manim render py/binom.py Allgemein
$(vidfolder)/BinomEins.mp4: py/binom.py
	manim render py/binom.py BinomEins
$(vidfolder)/BinomZwei.mp4: py/binom.py
	manim render py/binom.py BinomZwei
$(vidfolder)/BinomDrei.mp4: py/binom.py
	manim render py/binom.py BinomDrei

$(vidfolder)/Teich.mp4: py/exp.py
	manim render py/exp.py Teich
$(vidfolder)/Linear.mp4: py/linear.py
	manim render py/linear.py Linear
$(vidfolder)/Newton.mp4: py/newton.py
	manim render py/newton.py Newton
$(vidfolder)/Potenz.mp4: py/monome.py
	manim render py/monome.py Potenz
$(vidfolder)/Numbersets.mp4: py/nzqrc.py
	manim render py/nzqrc.py Numbersets

$(vidfolder)/sir-model.mp4: py/sir.py py/modules/particle.py py/modules/population.py

vid_data.js: $(vidfolder)/Allgemein.mp4 $(vidfolder)/BinomEins.mp4 $(vidfolder)/BinomZwei.mp4 $(vidfolder)/BinomDrei.mp4 \
		$(vidfolder)/Teich.mp4 $(vidfolder)/Linear.mp4 $(vidfolder)/Newton.mp4 $(vidfolder)/Potenz.mp4 $(vidfolder)/Numbersets.mp4
	echo "vid_data =" > docs/vid_data.js
	cat data.json >> docs/vid_data.js
	echo ";\n" >> docs/vid_data.js

all: vid_data.js