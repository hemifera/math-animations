from manim import *
import numpy as np

class mtds_00(Scene):
    def construct(self):
        img = ImageMobject("../../img/udb_logo_high.png")
        t1 = Text(r"Polinomios de mayor orden")
        t2 = Text(r"División Sintética", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))

class mtds_010(Scene):
    def construct(self):
        f = [
            MathTex(r"x^{2}-5x+6=0"),
            MathTex(r"{{1}}x^{2}{{-5}}x^{1}+{{6}}x^{0}=0"),
            MathTex(r"(x-3)(x-2)=0"),
            MathTex(r"6 \to \pm 6 \pm 3\, \pm 2\, \pm {{1}}"),
            MathTex(r"\begin{cases}x = 2 \\x=3 \\\end{cases}"),
            MathTex(r""),
        ]
    
        v0 = [
            [[mt(r"x^2")], [mt(r"x^1")], [mt(r"x^0")], [t(r"DIV")], ],
            [[mt(r"1")], [mt(r"-5")], [mt(r"6")], [mt(r"+1")], ],
            [[mt(r"0")], [mt(r"1")], [mt(r"-4")], [mt(r"0")], ],
            [[mt(r"1")], [mt(r"-4")], [mt(r"2")], [mt(r"0")], ],
        ]
        vv0 = l_to_vgroup(v0).arrange_in_grid(cols=4, rows=4, buff=(1.5, 0.75), )

        lh0 = h_line(vv0[8], vv0[12], vv0[11], vv0[15])
        lv0 = v_line(vv0[2], vv0[3], vv0[11], vv0[15])

        self.play(Write(f[0]))
        self.wait(1)
        self.play(
            TransformMatchingShapes(f[0].copy(), f[2].next_to(f[0], DOWN)),
            run_time = 0.5
        )

        v1 = VGroup(f[0], f[2])
        self.play(v1.animate.move_to(ORIGIN), run_time = 0.3)
        self.wait(1)
        self.play(v1.animate.next_to(vv0, UP*1.2))
        self.wait(1)
        self.play(ReplacementTransform(f[0], f[1].move_to(f[0])))
        self.wait(1)
        self.play(FadeIn(vv0[0], vv0[1], vv0[2]))
        self.wait(1)

        self.play(
            TransformMatchingTex(
                f[1].copy(),
                Group(vv0[4], vv0[5], vv0[6],)
            )
        )
        self.wait(1)
        self.play(FadeIn(lh0, lv0))
        self.wait(1)
        self.play(FadeOut(f[1], f[2]))
        self.wait(1)
        self.play(Transform(vv0[6].copy(), f[3].next_to(vv0, UP*2)))
        self.wait(1)
        self.play(TransformMatchingTex(f[3].copy(), vv0[7]))
        self.wait(1)
        self.play(TransformFromCopy(vv0[4], vv0[12]))
        self.wait(1)

        self.play(TransformMatchingShapes(vv0[12].copy(), vv0[9]))
        self.wait(1)
        self.play(TransformMatchingShapes(Group(vv0[9], vv0[5]).copy(), vv0[13]))
        self.wait(1)

        self.play(TransformMatchingShapes(vv0[13].copy(), vv0[10]))
        self.wait(1)
        self.play(TransformMatchingShapes(Group(vv0[10], vv0[6]).copy(), vv0[14]))
        self.wait(1)

        self.add(vv0)
        self.add(
            vv0[3].set_opacity(0),
            vv0[11].set_opacity(0),
            vv0[15].set_opacity(0),
            
        )
        # self.clear()

        # self

        self.add(lh0)
        self.add(lv0)
        # print(l0)


class mtds_011(Scene):
    def construct(self):
        f = [
            MathTex(r"x^{2}-5x+6=0"),
            MathTex(r"{{1}}x^{2}{{-5}}x^{1}+{{6}}x^{0}=0"),
            MathTex(r"(x-3)(x-2)=0"),
            MathTex(r"6 \to \pm 6 \pm 3\, \pm 2\, \pm {{1}}"),
            MathTex(r"x = {{+2}}\\ x = +3"),
            MathTex(r"1x^{1} - 3 x^{0}=0"),
            MathTex(r"x-3=0"),
            MathTex(r"x=2"),
            MathTex(r"x-2=0"),


        ]
    
        v0 = [
            [[mt(r"x^2")], [mt(r"x^1")], [mt(r"x^0")], [t(r"DIV")], ],
            [[mt(r"1")], [mt(r"-5")], [mt(r"6")], [mt(r"+2")], ],
            [[mt(r"0")], [mt(r"2")], [mt(r"-6")], [mt(r"0")], ],
            [[mt(r"1")], [mt(r"-3")], [mt(r"0")], [mt(r"0")], ],
        ]
        vv0 = l_to_vgroup(v0).arrange_in_grid(cols=4, rows=4, buff=(1.5, 0.75), )

        lh0 = h_line(vv0[8], vv0[12], vv0[11], vv0[15])
        lv0 = v_line(vv0[2], vv0[3], vv0[11], vv0[15])
        tb0 = VGroup(vv0, lh0, lv0)
        self.wait(0.5)
        self.play(Write(f[2].move_to(ORIGIN).shift(UP*1.5)))
        self.wait(1)
        self.play(Write(f[4].next_to(f[2], DOWN)))

        self.wait(1)
        
        self.play(
            FadeOut(f[2]),
            f[4].animate.next_to(tb0, RIGHT*1.5)
        )

        self.wait(1)
        self.play(
            FadeIn(vv0[0], vv0[1], vv0[2], vv0[4], vv0[5], vv0[6]),
            FadeIn(lh0, lv0)
        )
        self.wait(1)

        self.play(
            TransformMatchingTex(f[4].copy(), vv0[7])
        )
        self.wait(1)
        
        self.play(TransformFromCopy(vv0[4], vv0[12]))
        self.wait(1)


        self.play(TransformFromCopy(VGroup(vv0[7], vv0[12]), vv0[9]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[5], vv0[9]), vv0[13]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[7], vv0[13]), vv0[10]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[6], vv0[10]), vv0[14]))


        self.wait(1)

        k = VGroup(vv0[1].copy(), vv0[2].copy())
        self.play(
            k[0].animate.next_to(vv0[12], DOWN*2),
            k[1].animate.next_to(vv0[13], DOWN*2)
            )
        self.wait(1)

        self.play(
            FadeOut(
                vv0[0], vv0[1], vv0[2], 
                vv0[4], vv0[5], vv0[6],
                vv0[9], vv0[10],
                vv0[14], lv0, lh0, f[4]
                )
        )
        self.wait(1)

        self.play(TransformMatchingTex(vv0[7], f[7]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[7], f[8], path_arc=PI/2))
        self.wait(1)   
        self.play(TransformMatchingTex(Group(vv0[12], vv0[13], k), f[5].next_to(f[8], DOWN)))
        self.wait(1)
        self.play(TransformMatchingShapes(f[5], f[6].move_to(f[5])), path_arc=PI/2)
        self.wait(1)

        self.play(TransformMatchingTex(Group(f[6], f[8]), f[2].move_to(ORIGIN)))

class mtds_020(Scene):
    def construct(self):
        f = [
            MathTex(r"m^{3}-8m^{2}+17m-10=0"),
            MathTex(r"{{1}}{{m^{3}}} {{-8}}{{m^{2}}} {{+17}} {{m^1}} {{-10}}{{m^0}}=0"),
            MathTex(r"(m-1)(m^{2}-7m+10)=0"),
            MathTex(r"(m-1)(m-2)(m-5)=0"),

            MathTex(r"-10 \to \pm 10 \pm 5 \pm {{2}}\, \pm {{1}}"),
            MathTex(r"(m-1)=0"),
            MathTex(r"(m-2)=0"),
            MathTex(r"({{1}}m^{2}{{-7}}m+{{10}})=0"),

            MathTex(r"10 \to \pm 10 \pm 5 \pm {{2}}\, \pm {{1}}"),
            MathTex(r"(m-5)=0"),
        ]
    
        v0 = [
            [[mt(r"m^3")], [mt(r"m^2")], [mt(r"m^1")], [mt(r"m^0")], [t(r"DIV")], ],

            [[mt(r"1")], [mt(r"-8")], [mt(r"17")], [mt(r"-10")], [mt(r"1")],],
            [[mt(r"0")], [mt(r"1")], [mt(r"-7")], [mt(r"10")], [mt(r"m={{1}}")],],

            [[mt(r"1")], [mt(r"-7")], [mt(r"10")], [mt(r"0")], [mt(r"DIV")],],

            [[mt(r"0")], [mt(r"2")], [mt(r"-10")], [mt(r"m=2")], [mt(r"0")],],
            [[mt(r"1")], [mt(r"-5")], [mt(r"0")], [mt(r"0")], [mt(r"0")],],
        ]
        vv0 = l_to_vgroup(v0).arrange_in_grid(cols=5, rows=6, buff=(1.5, 0.75), )


        lv0 = v_line(vv0[8], vv0[9], vv0[14], vv0[15])
        lv1 = v_line(vv0[18], vv0[17], vv0[27], vv0[28])


        lh0 = h_line(vv0[10], vv0[15], vv0[14], vv0[19])
        lh1 = h_line(vv0[20], vv0[25], vv0[23], vv0[28])
        
        self.add(VGroup(
            vv0[4], vv0[10] , 
            vv0[19], vv0[20], vv0[24],
            vv0[28], vv0[29],
            ).set_opacity(0))
        
        # 14 y 28
        self.play(Write(f[0]))
        self.wait(1)
        self.play(f[0].animate.next_to(vv0, UP))
        self.play(TransformMatchingTex(f[0], f[1].move_to(f[0])))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                Group(f[1]).copy(),
                Group(vv0[0], vv0[1], vv0[2], vv0[3],
                      vv0[5], vv0[6], vv0[7], vv0[8],
                      )
            )
        )
        self.wait(1)
        self.play(FadeIn(lv0, lh0))
        self.wait(1)

        self.play(Write(f[4].shift(DOWN*2)))
        self.wait(1)

        self.play(TransformMatchingTex(f[4], vv0[14]))
        self.wait(1)
        self.play(TransformFromCopy(vv0[5], vv0[15]))
        self.wait(1)

        self.play(ReplacementTransform(Group(vv0[14], vv0[15]).copy(), vv0[11]))
        self.wait(1)
        self.play(ReplacementTransform(Group(vv0[6], vv0[11]).copy(), vv0[16]))
        self.wait(1)


        self.play(ReplacementTransform(Group(vv0[14], vv0[16]).copy(), vv0[12]))
        self.wait(1)
        self.play(ReplacementTransform(Group(vv0[7], vv0[12]).copy(), vv0[17]))
        self.wait(1)

        self.play(ReplacementTransform(Group(vv0[14], vv0[17]).copy(), vv0[13]))
        self.wait(1)
        self.play(ReplacementTransform(Group(vv0[8], vv0[13]).copy(), vv0[18]))
        self.wait(1)

        self.play(TransformMatchingShapes(vv0[14], f[5].move_to(vv0[14]).shift(RIGHT), path_arc=PI/2 ))
        self.wait(1)
        k = VGroup(vv0[1], vv0[2], vv0[3]).copy()
        self.play(
            k[0].animate.next_to(vv0[15], DOWN),
            k[1].animate.next_to(vv0[16], DOWN),
            k[2].animate.next_to(vv0[17], DOWN),
        )
        self.wait(1)
        self.play(TransformMatchingTex(
            Group(vv0[15], vv0[16], vv0[17]).copy(),
            f[7].next_to(k, DOWN)
        ))
        self.wait(1)

        self.play(ReplacementTransform(Group(f[7], f[5].copy()), f[2].move_to(f[7])))
        self.wait(1)
        self.play(ReplacementTransform(f[2], f[2].move_to(f[7])))
        self.play(
            f[2].animate.move_to(f[1]),
            f[1].animate.set_opacity(0),
            k.animate.set_opacity(0),
        )
        self.wait(1)
        self.play(FadeIn(lh1, lv1))
        self.wait(1)

        self.play(TransformMatchingTex(vv0[17].copy(), f[8].move_to(vv0[29].shift(LEFT))))
        self.wait(1)
        self.play(TransformMatchingTex(f[8].copy(), vv0[23]))
        self.wait(1)


        self.play(TransformMatchingShapes(vv0[15].copy(), vv0[25]))
        self.wait(1)

        self.play(
            ReplacementTransform(
                Group(vv0[23], vv0[25]).copy(),
                vv0[21],
            )
        )
        self.wait(1)
        self.play(
            ReplacementTransform(
                Group(vv0[16], vv0[21]).copy(),
                vv0[26],
            )
        )
        self.wait(1)
        # ///
        self.play(
            ReplacementTransform(
                Group(vv0[23], vv0[26]).copy(),
                vv0[22],
            )
        )
        self.wait(1)
        self.play(
            ReplacementTransform(
                Group(vv0[17], vv0[22]).copy(),
                vv0[27],
            )
        )
        self.wait(1)

        self.play(
            f[8].animate.set_opacity(0),

        )

        self.play(TransformMatchingShapes(vv0[23], f[6].move_to(vv0[23]).shift(RIGHT), path_arc=PI/2))
        self.wait(1)
        k1 = VGroup(vv0[2], vv0[3]).copy()
        self.play(
            k1[0].animate.next_to(vv0[25], DOWN),
            k1[1].animate.next_to(vv0[26], DOWN),
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(
                Group(k1, vv0[25], vv0[26]).copy(),
                f[9].move_to(vv0[28]).shift(RIGHT)
            )
        )
        self.wait(1)
        self.play(VGroup(vv0, lh0, lv0, lh1, lv1, k1).animate.set_opacity(0))
        self.wait(1)
        self.play(f[2].animate.move_to(ORIGIN))
        self.play(TransformMatchingShapes(
            Group(f[2],f[5], f[6], f[9]),
            f[3].move_to(ORIGIN)
        ))
        self.wait(1)
        # self.play()
        # self.add(vv0, lv0, lv1, lh0, lh1)
        
        # tb0 = VGroup(vv0, lh0, lv0)


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
