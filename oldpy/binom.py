from manim import *

from modules.data_write import write_data

# PARAMETERS

dist = 1
long = 10 #wait
short = 3 #wait
supershort = short/2

# colours
colour_aa = BLUE
colour_bb = YELLOW
colour_ab = GREEN
colour_rc = RED

common_kwargs = {"fill_opacity": 0.5}


class Allgemein(Scene):
    meta_data = {
        "title": "Allgemeines Binom",
        "timestamps": [],
        "filename": "Allgemein.mp4",
        "path": "videos/"
    }

    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))

        
    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def construct(self):
        self.draw_logo()
        # Parameters
        a, b = 4, 1.5
        c, d = 3, 2

        col_a = BLUE
        col_b = YELLOW
        col_c = RED
        col_d = GREEN

        col_ac = PURPLE
        col_ad = TEAL
        col_bc = ORANGE
        col_bd = PURE_GREEN
        # rectangles
        globalshift = (c-d)/2*DOWN + (a-b)/2*RIGHT

        acshift = c/2*UP + a/2*LEFT + globalshift
        rectac = Rectangle(width=a, height=c,
                color=col_ac, **common_kwargs).shift(
                acshift
                )

        bcshift = b/2*RIGHT + c/2*UP + globalshift
        rectbc = Rectangle(width=b, height=c, color=col_bc, **common_kwargs).shift(
                bcshift
                )

        adshift = d/2*DOWN + a/2*LEFT + globalshift
        rectad = Rectangle(
                width=a, height=d, color=col_ad, **common_kwargs
                ).shift(
                        adshift
                )

        bdshift = d/2*DOWN + b/2*RIGHT + globalshift
        rectbd = Rectangle(
                width=b, height=d, color=col_bd, **common_kwargs
                ).shift(
                        bdshift
                )

        rect_calc = Rectangle(
                width=a+b, height=c+d, color=WHITE, **common_kwargs
                )

        # braces
        brace_a = Brace(rectac, direction=UP, color=col_a)
        atext = brace_a.get_tex("a")
        atext.set_color(col_a)
        brace_b = Brace(rectbc, direction=UP, color=col_b)
        btext = brace_b.get_tex("b")
        btext.set_color(col_b)
        brace_c = Brace(rectac, direction=LEFT, color=col_c)
        ctext = brace_c.get_tex("c")
        ctext.set_color(col_c)
        brace_d = Brace(rectad, direction=LEFT, color=col_d)
        dtext = brace_d.get_tex("d")
        dtext.set_color(col_d)

        braces = [brace_a, brace_b, brace_c, brace_d,
                atext, btext, ctext, dtext]

        # labels
        textac = MathTex("ac").shift(acshift)
        textbc = MathTex("bc").shift(bcshift)
        textad = MathTex("ad").shift(adshift)
        textbd = MathTex("bd").shift(bdshift)
        textrc = MathTex("(a+b)(c+d)")

        # groups
        tac = VGroup(atext.copy(), ctext.copy())
        tbc = VGroup(btext.copy(), ctext.copy())
        tad = VGroup(atext.copy(), dtext.copy())
        tbd = VGroup(btext.copy(), dtext.copy())
        rc = VGroup(rect_calc, textrc)

        # Animation
        # to be calculated
        self.play(Create(rc))
        self.wait(supershort)
        self.play(*[Create(b) for b in braces])
        self.add_timestamp()
        # dissection
        self.play(
                textrc.animate.shift((a+dist)*LEFT + c*UP)
                )
        # get the rectangles/squares
        self.add_timestamp()
        self.play(Create(rectac),
                Transform(tac, textac)
                )
        self.add_timestamp()
        self.play(Create(rectad),
                Transform(tad, textad)
                )
        self.add_timestamp()
        self.play(Create(rectbc),
                Transform(tbc, textbc)
                )
        self.add_timestamp()
        self.play(Create(rectbd),
                Transform(tbd, textbd)
                )
        self.add_timestamp()

        write_data(self.meta_data)

# SCENE
class BinomEins(Scene):
    meta_data = {
        "title": "First Binomal Formula",
        "timestamps": [],
        "filename": "BinomEins.mp4",
        "path": "videos/"
    }

    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))

        
    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def construct(self):
        self.draw_logo()
        # Parameters
        a, b = 3, 2
        # rectangles
        globalshift = (a-b)/2*(DOWN + RIGHT)

        ashift = a/2*UP + a/2*LEFT + globalshift
        squarea = Square(a, color=colour_aa, **common_kwargs).shift(
                ashift
                )

        bshift = b/2*RIGHT + b/2*DOWN + globalshift
        squareb = Square(b, color=colour_bb, **common_kwargs).shift(
                bshift
                )

        abshift = b/2*DOWN + a/2*LEFT + globalshift
        rectab = Rectangle(
                width=a, height=b, color=colour_ab, **common_kwargs
                ).shift(
                        abshift
                )

        bashift = a/2*UP + b/2*RIGHT + globalshift
        rectba = Rectangle(
                width=b, height=a, color=colour_ab, **common_kwargs
                ).shift(
                        bashift
                )

        rect_calc = Square(
                a+b, color=colour_rc, **common_kwargs
                )
        rects = [squarea, squareb, rectab, rectba]

        # braces
        brace_upab = Brace(VGroup(squarea, rectba), direction=UP)
        buabtext = brace_upab.get_tex("a+b")

        brace_leftab = Brace(VGroup(squarea, rectab), direction=LEFT)
        blabtext = brace_leftab.get_tex("a + b")

        brace_downa = Brace(rectab, direction=DOWN)
        bdatext = brace_downa.get_tex("a")
        brace_downb = Brace(squareb, direction=DOWN)
        bdbtext = brace_downb.get_tex("b")
        brace_righta = Brace(rectba, direction=RIGHT)
        bratext = brace_righta.get_tex("a")
        brace_rightb = Brace(squareb, direction=RIGHT)
        brbtext = brace_rightb.get_tex("b")

        braces = [brace_upab, brace_leftab,
                buabtext, blabtext,
                brace_downa,brace_downb, brace_righta, brace_rightb,
                bdatext, bdbtext, bratext, brbtext]
        braces0 = braces[:4]
        braces1 = braces[4:]

        # labels
        texta = MathTex("a^2").shift(ashift)
        textb = MathTex("b^2").shift(bshift)
        textab = MathTex("ab").shift(abshift)
        textba = MathTex("ba").shift(bashift)
        labels = [texta, textb, textab, textba]
        textrc = MathTex("(a+b)^2")

        # groups
        ta = VGroup(bdatext.copy(), bratext.copy())
        tb = VGroup(bdbtext.copy(), brbtext.copy())
        tab = VGroup(bdatext.copy(), brbtext.copy())
        tba = VGroup(bdbtext.copy(), bratext.copy())
        aa = VGroup(squarea, ta)
        bb = VGroup(squareb, tb)
        ab = VGroup(rectab, tab)
        ba = VGroup(rectba, tba)
        rc = VGroup(rect_calc, textrc)

        # Animation
        # to be calculated
        self.play(Create(rc),
                *[Create(b) for b in braces0]
                )
        self.add_timestamp()
        # dissection
        self.play(
                textrc.animate.shift((a+dist)*LEFT + a*UP),
                *[Create(b) for b in braces1]
                )
        # get the rectangles/squares
        self.add_timestamp()
        self.play(Create(squarea),
                Transform(ta, texta)
                )
        self.add_timestamp()
        self.play(Create(squareb),
                Transform(tb, textb)
                )
        self.add_timestamp()
        self.play(Create(rectab),
                Transform(tab, textab)
                )
        self.play(Create(rectba),
                Transform(tba, textba)
                )
        self.play(FadeOut(rect_calc),
                Transform(tba, MathTex("ab").shift(tba.get_center()))
                )

        #self.play(*[Write(x) for x in labels])
        self.add_timestamp()

        self.play(*[FadeOut(b) for b in braces])
        #self.add_timestamp()

        # split rectangles
        self.play(bb.animate.shift(RIGHT + DOWN - globalshift),
                ab.animate.shift(DOWN - globalshift),
                ba.animate.shift(RIGHT - globalshift),
                aa.animate.shift(-globalshift)
                )
        # align them
        self.play(aa.animate.shift((a + dist)*LEFT - aa.get_center()),
                ab.animate.shift(- ab.get_center()),
                ba.animate.shift(- ba.get_center()),
                bb.animate.shift((b/2 + a/2 + dist)*RIGHT - bb.get_center()))
        self.play(
                FadeOut(tab),
                Transform(tba, MathTex("2\cdot ab"))
                )
        # text for equation
        gleich = MathTex("=").shift(3*(a+dist)/2*LEFT)
        plus1 = MathTex("+").shift((a+dist)/2*LEFT)
        plus2 = MathTex("+").shift(-(a+dist)/2*LEFT)
        self.play(
                Write(gleich),
                Write(plus1),
                Write(plus2)
                )
        self.add_timestamp()

        write_data(self.meta_data)


class BinomZwei(Scene):
    meta_data = {
        "title": "Second Binomial Formula",
        "timestamps": [],
        "filename": "BinomZwei.mp4",
        "path": "videos/"
    }

    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))
        
    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def construct(self):
        self.draw_logo()
        # Parameters
        a, b = 4, 1.5
        # rectangles
        ashift = 0*UP
        squarea = Square(a, color=colour_aa, **common_kwargs).shift(
                ashift
                )
        bshift = (a/2-b/2)*(RIGHT + DOWN)
        squareb = Square(b, color=colour_bb, **common_kwargs).shift(
                bshift
                )

        abshift = (a/2-b/2)*DOWN
        rectab = Rectangle(
                width=a, height=b, color=colour_ab, **common_kwargs
                ).shift(
                        abshift
                )

        bashift = (a/2-b/2)*RIGHT
        rectba = Rectangle(
                width=b, height=a, color=colour_ab, **common_kwargs
                ).shift(
                        bashift
                )

        rcshift = b/2*(UP + LEFT)
        rect_calc = Square(
                a-b, color=RED, **common_kwargs
                ).shift(rcshift)

        rects = [squarea, rectab, rectba, squareb]

        # braces
        brace_upb = Brace(rectba, direction=UP)
        bubtext = brace_upb.get_tex("b")
        brace_upab = Brace(
                Line().scale((a-b)/2).shift(a/2*UP + b/2*LEFT),
                direction=UP
                )
        buabtext = brace_upab.get_tex("a-b")

        brace_leftb = Brace(rectab, direction=LEFT)
        blbtext = brace_leftb.get_tex("b")
        brace_leftab = Brace(
                Line(UP, DOWN).scale((a-b)/2).shift(a/2*LEFT + b/2*UP),
                direction=LEFT
                )
        blabtext = brace_leftab.get_tex("a-b")

        brace_downa = Brace(squarea, direction=DOWN)
        bdatext = brace_downa.get_text("a")
        brace_righta = Brace(squarea, direction=RIGHT)
        bratext = brace_righta.get_text("a")

        braces = [brace_upab, brace_leftab,
                buabtext, blabtext,
                brace_upb, brace_leftb,
                bubtext, blbtext,
                brace_downa, brace_righta,
                bdatext, bratext]
        braces0 = braces[:4]
        braces1 = braces[4:]

        # labels
        texta = MathTex("a^2").shift(ashift)
        textb = MathTex("b^2").shift(bshift)
        textab = MathTex("ab").shift(abshift)
        textba = MathTex("ba").shift(bashift)
        labels = [texta, textb, textab, textba]

        textrc = MathTex("(a-b)^2").shift(rcshift)

        # groups
        ta = VGroup(bdatext.copy(), bratext.copy())
        tb = VGroup(bubtext.copy(), blbtext.copy())
        tab = VGroup(bdatext.copy(), blbtext.copy())
        tba = VGroup(bubtext.copy(), bratext.copy())
        aa = VGroup(squarea, ta)
        bb = VGroup(squareb, tb)
        ab = VGroup(rectab, tab)
        ba = VGroup(rectba, tba)
        rc = VGroup(rect_calc, textrc)

        # Animation
        # Highlight to calculate
        self.play(Create(rc),
                *[Create(b) for b in braces0]
                )
        self.add_timestamp()
        self.play(
                *[Create(b) for b in braces1],
                textrc.animate.shift((a/2+3*dist)*LEFT + (a/2)*UP)
                )
        self.add_timestamp()
        self.play(Create(squarea),
                Transform(ta, texta)
                )
        self.add_timestamp()
        self.play(Create(rectab),
                Transform(tab, textab)
                )
        self.add_timestamp()
        self.play(Create(rectba),
                Transform(tba, textba)
                )
        self.add_timestamp()
        self.play(Create(squareb),
                Transform(tb, textb)
                )
        self.wait(short)
        self.play(FadeOut(rect_calc),
                Transform(tba, MathTex("ab").shift(tba.get_center()))
                )

        self.add_timestamp()

        self.play(*[FadeOut(b) for b in braces])
        self.wait(supershort)

        # split rectangles
        globalshift = (b+dist)/2*(LEFT + UP)
        ashift2 = globalshift
        abshift2 = (b + dist)*DOWN + globalshift
        bashift2 = (b + dist)*RIGHT + globalshift
        bshift2 = (b + dist)*(RIGHT + DOWN) + globalshift
        self.play(aa.animate.shift(ashift2),
                ab.animate.shift(abshift2),
                ba.animate.shift(bashift2),
                bb.animate.shift(bshift2),
                )
        self.wait(supershort)
        self.play(Transform(tab, MathTex("-ab").shift(tab.get_center())),
                Transform(tba, MathTex("-ab").shift(tba.get_center()))
                )
        self.add_timestamp()

        # align them
        globalshift = (b-a)/2*LEFT
        self.play(aa.animate.shift(
                    (a + dist)*LEFT - aa.get_center() + globalshift
                    ),
                ab.animate.shift(- ab.get_center() + globalshift),
                ba.animate.shift(- ba.get_center() + globalshift),
                bb.animate.shift((b/2 + a/2 + dist)*RIGHT - bb.get_center() + globalshift))
        self.play(
                FadeOut(tab),
                Transform(tba, MathTex("-2\cdot ab").shift(globalshift))
                )
        # text for equation
        gleich = MathTex("=").shift(3*(a+dist)/2*LEFT+globalshift)
        plus1 = MathTex("-").shift((a+dist)/2*LEFT+globalshift)
        plus2 = MathTex("+").shift(-(a+dist)/2*LEFT+globalshift)
        self.wait(short)
        self.play(
                textrc.animate.shift(2*dist*RIGHT),
                Write(gleich),
                Write(plus1),
                Write(plus2),
                Transform(tba, MathTex("2\cdot ab").shift(globalshift))
                )
        self.add_timestamp()

        write_data(self.meta_data)
        

class BinomDrei(Scene):
    meta_data = {
        "title": "Third Binomial Formula",
        "timestamps": [],
        "filename": "BinomDrei.mp4",
        "path": "videos/"
    }

    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))

    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def construct(self):
        self.draw_logo()
        # Parameters
        a, b = 4, 1.5
        # rectangles
        bshift = a/2*RIGHT + (a/2 - b/2)*DOWN
        squareb = Square(b, color=colour_bb, **common_kwargs).shift(
                bshift
                )

        abshift = (a-b)/2*DOWN + b/2*LEFT
        rectab = Rectangle(
                width=a, height=b, color=colour_ab, **common_kwargs
                ).shift(
                        abshift
                )

        bashift = a/2*RIGHT
        rectba = Rectangle(
                width=b, height=a, color=colour_ab, **common_kwargs
                ).shift(
                        bashift
                )
        ashift = b/2*LEFT
        squarea = Square(a, color=colour_aa, **common_kwargs).shift(
                ashift
                )

        rcshift = b/2*UP
        rect_calc = Rectangle(
                width=a+b, height = a-b, color=RED, **common_kwargs
                ).shift(rcshift)

        rects = [squarea, rectba, rectab, squareb]

        # braces up/down
        brace_upab = Brace(VGroup(squarea, rectba), direction=UP)
        buabtext = brace_upab.get_tex("a+b")
        brace_downa = Brace(squarea, direction=DOWN)
        bdatext = brace_downa.get_tex("a")
        brace_downb = Brace(squareb, direction=DOWN)
        bdbtext = brace_downb.get_tex("b")

        # braces left/right
        brace_leftab = Brace(
                Line(UP, DOWN).scale((b-a)/2).shift((b+a)/2*LEFT + b/2*UP),
                direction=LEFT)
        bltext = brace_leftab.get_tex("a-b")
        brace_leftb = Brace(rectab, direction=LEFT)
        blbtext = brace_leftb.get_text("b")
        brace_righta = Brace(
                rectba, direction=RIGHT
                )
        bratext = brace_righta.get_tex("a")

        # collect braces
        braces = [brace_upab, brace_leftab,
                buabtext, bltext,
                brace_downa, brace_downb,
                bdatext, bdbtext,
                brace_righta, brace_leftb,
                bratext, blbtext
                ]
        braces0 = braces[:4]
        braces1 = braces[4:]

        # labels
        texta = MathTex("a^2").shift(ashift)
        textb = MathTex("b^2").shift(bshift)
        textab = MathTex("ab").shift(abshift)
        textba = MathTex("ba").shift(bashift)
        labels = [texta, textb, textab, textba]

        textrc = MathTex("(a+b)(a-b)").shift(rcshift)

        # groups
        ta = VGroup(bdatext.copy(), bratext.copy())
        tb = VGroup(bdbtext.copy(), blbtext.copy())
        tab = VGroup(bdatext.copy(), blbtext.copy())
        tba = VGroup(bdbtext.copy(), bratext.copy())
        aa = VGroup(squarea, ta)
        bb = VGroup(squareb, tb)
        ab = VGroup(rectab, tab)
        ba = VGroup(rectba, tba)
        rc = VGroup(rect_calc, textrc)

        # Animation
        # Highlight to calculate
        self.play(Create(rc),
                *[Create(b) for b in braces0]
                )
        self.add_timestamp()
        self.play(
                textrc.animate.shift((a+b)*LEFT + (a-b)*UP),
                *[Create(b) for b in braces1]
                )
        self.play(Create(squarea),
                Transform(ta, texta)
                )
        self.add_timestamp()
        self.play(Create(rectba),
                Transform(tba, textba)
                )
        self.add_timestamp()
        self.play(Create(rectab),
                Transform(tab, textab)
                )
        self.add_timestamp()
        self.play(Create(squareb),
                Transform(tb, textb)
                )
        self.add_timestamp()
        self.play(FadeOut(rect_calc),
                Transform(tba, MathTex("ab").shift(tba.get_center()))
                )

        self.add_timestamp()

        self.play(*[FadeOut(b) for b in braces])
        self.wait(supershort)

        # split rectangles
        globalshift = dist/2*(LEFT + UP) + b/2*UP
        ashift2 = globalshift
        abshift2 = (dist + b)*DOWN + globalshift
        bashift2 = dist*RIGHT + globalshift
        bshift2 = dist*RIGHT + (dist + b)*DOWN + globalshift
        self.play(aa.animate.shift(ashift2),
                ab.animate.shift(abshift2),
                ba.animate.shift(bashift2),
                bb.animate.shift(bshift2),
                )
        self.wait(supershort)
        self.play(
                Transform(tab, MathTex("-ab").shift(tab.get_center())),
                Transform(tb, MathTex("-b^2").shift(tb.get_center()))
                )
        self.add_timestamp()

        # align them
        globalshift = (b-a)/2*LEFT
        self.play(aa.animate.shift(
                    (a/2 + b/2 + dist)*LEFT - aa.get_center() + globalshift
                    ),
                ab.animate.shift(- ab.get_center() + globalshift),
                ba.animate.shift(- ba.get_center() + globalshift),
                #FadeOut(ab), FadeOut(ba),
                bb.animate.shift((b + dist)*RIGHT - bb.get_center() + globalshift))
        self.play(
                ab.animate.scale(0),
                ba.animate.scale(0)
                )
        self.play(
                FadeOut(ab),
                FadeOut(ba)
                )
        # text for equation
        gleich = MathTex("=").shift(3*(a+dist)/2*LEFT+globalshift)
        minus = MathTex("-").shift(globalshift)
        self.add_timestamp()
        self.play(
                #textrc.animate.shift(2*dist*RIGHT),
                Write(gleich),
                Write(minus),
                Transform(tb, MathTex("b^2").shift(tb.get_center()))
                )
        self.add_timestamp()

        write_data(self.meta_data)