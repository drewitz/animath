.PHONY: all

all: Ableitung.html Allgemein.html BinomEins.html BinomZwei.html BinomDrei.html Teich.html Kathetensatz.html Linear.html Potenz.html Newton.html BinomialDist.html NormalDist.html Numbersets.html Pythagoras1.html Pythagoras2.html Sine.html SquareCompletion.html

BinomialDist.html: py/normal_dist.py
	manim-slides render py/normal_dist.py BinomialDist
	manim-slides convert -ccontrols=true BinomialDist docs/frames/BinomialDist.html

NormalDist.html: py/normal_dist.py
	manim-slides render py/normal_dist.py BinomialDist
	manim-slides convert -ccontrols=true BinomialDist docs/frames/BinomialDist.html


Ableitung.html: py/ableitung.py
	manim-slides render py/ableitung.py Ableitung
	manim-slides convert -ccontrols=true Ableitung docs/frames/Ableitung.html
Allgemein.html: py/binom.py
	manim-slides render py/binom.py Allgemein
	manim-slides convert -ccontrols=true Allgemein docs/frames/Allgemein.html
BinomEins.html: py/binom.py
	manim-slides render py/binom.py BinomEins
	manim-slides convert -ccontrols=true BinomEins docs/frames/BinomEins.html
BinomZwei.html: py/binom.py
	manim-slides render py/binom.py BinomZwei
	manim-slides convert -ccontrols=true BinomZwei docs/frames/BinomZwei.html
BinomDrei.html: py/binom.py
	manim-slides render py/binom.py BinomDrei
	manim-slides convert -ccontrols=true BinomDrei docs/frames/BinomDrei.html
DistanzEbenePunkt.html: py/distanz_ebene_punkt.py
	manim-slides render py/distanz_ebene_punkt.py DistanzEbenePunkt
	manim-slides convert -ccontrols=true DistanzEbenePunkt docs/frames/DistanzEbenePunkt.html
Teich.html: py/exp.py
	manim-slides render py/exp.py Teich
	manim-slides convert -ccontrols=true Teich docs/frames/Teich.html
Kathetensatz.html: py/kathetensatz.py
	manim-slides render py/kathetensatz.py Kathetensatz
	manim-slides convert -ccontrols=true Kathetensatz docs/frames/Kathetensatz.html
LGS.html: py/lgs.py
	manim-slides render py/lgs.py LGS
	manim-slides convert -ccontrols=true LGS docs/frames/LGS.html
Linear.html: py/linear.py
	manim-slides render py/linear.py Linear
	manim-slides convert -ccontrols=true Linear docs/frames/Linear.html
Potenz.html: py/monome.py
	manim-slides render py/monome.py Potenz
	manim-slides convert -ccontrols=true Potenz docs/frames/Potenz.html
Newton.html: py/newton.py
	manim-slides render py/newton.py Newton
	manim-slides convert -ccontrols=true Newton docs/frames/Newton.html
Numbersets.html: py/nzqrc.py
	manim-slides render py/nzqrc.py Numbersets
	manim-slides convert -ccontrols=true Numbersets docs/frames/Numbersets.html
Pythagoras1.html: py/pythagoras1.py
	manim-slides render py/pythagoras1.py Pythagoras1
	manim-slides convert -ccontrols=true Pythagoras1 docs/frames/Pythagoras1.html
Pythagoras2.html: py/pythagoras2.py
	manim-slides render py/pythagoras2.py Pythagoras2
	manim-slides convert -ccontrols=true Pythagoras2 docs/frames/Pythagoras2.html
Sine.html: py/sine.py
	manim-slides render py/sine.py Sine
	manim-slides convert -ccontrols=true Sine docs/frames/Sine.html
SquareCompletion.html: py/square-completion.py
	manim-slides render py/square-completion.py SquareCompletion
	manim-slides convert -ccontrols=true SquareCompletion docs/frames/SquareCompletion.html

