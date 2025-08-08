from manim import *
import numpy as np

class mtds_00(Scene):
    def construct(self):
        img = ImageMobject("img/udb_logo_high.png")
        t1 = Text(r"Polinomios de mayor orden")
        t2 = Text(r"División Sintética", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))

class mtds_010(Scene):
    def construct(self):
        f = [
            MathTex(r"x^{2}-5x+6=0"),
            MathTex(r"(x-3)(x-2)"),
            MathTex(r"6 \to \pm 3\, \pm 2\, \pm 1"),
            MathTex(r""),
            MathTex(r""),
        ]
    
        v0 = [
            [[mt(r"x^2")], [mt(r"x^1")], [mt(r"x^0")], [t(r"DIV")], ],
            [[mt(r"1")], [mt(r"-5")], [mt(r"-6")], [mt(r"1")], ],
            [[mt(r"0")], [mt(r"1")], [mt(r"-4")], [mt(r"0")], ],
            [[mt(r"1")], [mt(r"-4")], [mt(r"2")], [mt(r"0")], ],
        ]
        vv0 = l_to_vgroup(v0).arrange_in_grid(cols=4, rows=4, buff=(1.5, 0.75), )

        lh0 = h_line(vv0[8], vv0[12], vv0[11], vv0[15])
        lv0 = v_line(vv0[2], vv0[3], vv0[11], vv0[15])
        self.add(vv0)
        self.add(lh0)
        self.add(lv0)
        # print(l0)


def mt(t: str):
    return MathTex(t)

def t(t: str):
    return Tex(t)

def h_line(a_0: Mobject, a_1: Mobject, b_0: Mobject, b_1: Mobject):
    x0 = (a_0.get_left()[0] + a_1.get_left()[0])/2
    y0 = (a_0.get_bottom()[1] + a_1.get_top()[1])/2
    initial = Point(np.array([x0*1.1, y0, 0]))

    x1 = (b_0.get_right()[0] + b_1.get_right()[0])/2
    # y1 = (b_0.get_bottom()[1] + b_1.get_top()[1])/2
    final = Point(np.array([x1*1.1, y0, 0]))
    
    return Line(initial, final)

def v_line(a_0: Mobject, a_1: Mobject, b_0: Mobject, b_1: Mobject):
    x0 = (a_0.get_right()[0] + a_1.get_left()[0])/2
    y0 = (a_0.get_top()[1] + a_1.get_top()[1])/2
    initial = Point(np.array([x0*1.1, y0*1.1, 0]))

    # x1 = (b_0.get_right()[0] + b_1.get_left()[0])/2
    y1 = (b_0.get_bottom()[1] + b_1.get_top()[1])/2
    final = Point(np.array([x0*1.1, y1, 0]))
    
    return Line(initial, final)


def l_to_vgroup(l: list) -> VGroup:
    vg = VGroup()
    for i in l:
        for x in i:
            vg.add(x)
    return vg
