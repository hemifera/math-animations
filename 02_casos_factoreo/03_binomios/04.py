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


class mtds_030(Scene):
    def construct(self):
        f = [
            MathTex(r"9k^{2}+12k+4=0"),
            MathTex(r"{{9}}{{k^{2}}}{{+12}}{{k^1}}{{+4}}{{k^0}}=0"),
            MathTex(r"k=4"),
            MathTex(r"k=-4"),

            MathTex(r"k=-1"),
            MathTex(r"k=-4/3"),
            MathTex(r"k=-2/3"),
            MathTex(r"(k+2/3)=0"),

            MathTex(r"+4 \to \pm 4 \pm 2 \pm 1"),
            MathTex(r"+9 \to \pm 9 \pm 3 \pm 1"),
            MathTex(r"(4, 9) \to", r"\pm 4", r"\,, \pm 2 \,,", r"\pm 1", r"\,, \pm \frac{4}{9}\,, \pm", r"\frac{4}{3}", r"\,, \pm \frac{2}{9}\, ,\pm", r"\frac{2}{3}", r"\,, \pm \frac{1}{9}\,, \pm \frac{1}{3}"),



        ]
    
        v0 = [
            [[mt(r"k^2")], [mt(r"k^1")], [mt(r"k^0")], [mt(r"DIV")],],

            [[mt(r"9")], [mt(r"12")], [mt(r"4")], [mt(r"0")], ],
            [[mt(r"0")], [mt(r"36")], [mt(r"192")], [mt(r"k=4")], ],

            [[mt(r"9")], [mt(r"48")], [mt(r"196")], [mt(r"0")], ],
        ]
        vv0 = l_to_vgroup(v0).arrange_in_grid(cols=4, rows=4, buff=(1.5, 0.75), )


        lv0 = v_line(vv0[6], vv0[7], vv0[14], vv0[15])
        # lv1 = v_line(vv0[18], vv0[17], vv0[27], vv0[28])


        lh0 = h_line(vv0[8], vv0[12], vv0[11], vv0[15])
        # lh1 = h_line(vv0[20], vv0[25], vv0[23], vv0[28])
        
        self.add(VGroup(
            vv0[3], vv0[7], vv0[8],  vv0[15],  
            # vv0[15], vv0[20], vv0[24],
            # vv0[28], vv0[29],
            ).set_opacity(0))
        
        # self.add(vv0, lh0, lv0)

        self.play(Write(f[0]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[0], f[1]))
        self.wait(1)
        self.play(f[1].animate.next_to(vv0, UP*2))
        self.wait(1)

        self.play(TransformFromCopy(f[1], f[8].next_to(f[1], DOWN)))
        self.wait(1)
        self.play(TransformFromCopy(f[1], f[9].next_to(f[8], DOWN)))
        self.wait(1)
        self.play(
            TransformFromCopy(
                    VGroup(f[8], f[9]), 
                    f[10].next_to(f[9], DOWN*2)
            )
        )
        self.wait(1)
        fb0 = SurroundingRectangle(f[10], buff=0.1)
        fb1 = SurroundingRectangle(f[10][1])

        self.play(Create(fb0))
        self.play(ReplacementTransform(fb0, fb1))
        self.wait(1)
        self.play(FadeOut(fb1, f[8], f[9]))
        self.play(ReplacementTransform(f[10], vv0[11]))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                f[1].copy(),
                VGroup(vv0[0], vv0[1], vv0[2], vv0[4], vv0[5], vv0[6])
            ),
            FadeIn(lh0, lv0),
        )
        self.wait(1)

        self.play(TransformFromCopy(vv0[8], vv0[12]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[12], vv0[11]), vv0[9]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[5], vv0[9]), vv0[13]))
        self.wait(1)


        # self.play(TransformFromCopy(vv0[9], vv0[13]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[13], vv0[11]), vv0[10]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[6], vv0[10]), vv0[14]))
        self.wait(1)
        self.play(FadeOut(lh0, lv0, vv0))

class mtds_031(Scene):
    def construct(self):
        f = [
            MathTex(r"9k^{2}+12k+4=0"),
            MathTex(r"{{9}}{{k^{2}}}{{+12}}{{k^1}}{{+4}}{{k^0}}=0"),
            MathTex(r"k=4"),
            MathTex(r"k=-4"),

            MathTex(r"k=-1"),
            MathTex(r"k=-4/3"),
            MathTex(r"k=-2/3"),
            MathTex(r"(k+2/3)=0"),

            MathTex(r"+4 \to \pm 4 \pm 2 \pm 1"),
            MathTex(r"+9 \to \pm 9 \pm 3 \pm 1"),
            MathTex(r"(4, 9) \to", r"\pm 4", r"\,, \pm 2 \,,", r"\pm 1", r"\,, \pm \frac{4}{9}\,, \pm", r"\frac{4}{3}", r"\,, \pm \frac{2}{9}\, ,\pm", r"\frac{2}{3}", r"\,, \pm \frac{1}{9}\,, \pm \frac{1}{3}"),



        ]
    
        v0 = [
            [[mt(r"k^2")], [mt(r"k^1")], [mt(r"k^0")], [mt(r"DIV")],],

            [[mt(r"9")], [mt(r"12")], [mt(r"4")], [mt(r"0")], ],
            [[mt(r"0")], [mt(r"-36")], [mt(r"96")], [mt(r"k=-4")], ],

            [[mt(r"9")], [mt(r"-24")], [mt(r"100")], [mt(r"0")], ],
        ]
        vv0 = l_to_vgroup(v0).arrange_in_grid(cols=4, rows=4, buff=(1.5, 0.75), )


        lv0 = v_line(vv0[6], vv0[7], vv0[14], vv0[15])
        # lv1 = v_line(vv0[18], vv0[17], vv0[27], vv0[28])


        lh0 = h_line(vv0[8], vv0[12], vv0[11], vv0[15])
        # lh1 = h_line(vv0[20], vv0[25], vv0[23], vv0[28])
        
        self.add(VGroup(
            vv0[3], vv0[7], vv0[8],  vv0[15],  
            # vv0[15], vv0[20], vv0[24],
            # vv0[28], vv0[29],
            ).set_opacity(0))
        
        self.add(f[1].next_to(vv0, UP*2))
        self.play(FadeIn(f[10].shift(DOWN*2.5)))

        self.wait(1)
        fb0 = SurroundingRectangle(f[10], buff=0.1)
        fb1 = SurroundingRectangle(f[10][1])

        self.play(Create(fb0))
        self.play(ReplacementTransform(fb0, fb1))
        self.wait(1)
        self.play(FadeOut(fb1))
        self.play(ReplacementTransform(f[10], vv0[11]))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                f[1].copy(),
                VGroup(vv0[0], vv0[1], vv0[2], vv0[4], vv0[5], vv0[6])
            ),
            FadeIn(lh0, lv0),
        )
        self.wait(1)

        self.play(TransformFromCopy(vv0[8], vv0[12]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[12], vv0[11]), vv0[9]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[5], vv0[9]), vv0[13]))
        self.wait(1)


        # self.play(TransformFromCopy(vv0[9], vv0[13]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[13], vv0[11]), vv0[10]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[6], vv0[10]), vv0[14]))
        self.wait(1)
        self.play(FadeOut(lh0, lv0, vv0))

class mtds_032(Scene):
    def construct(self):
        f = [
            MathTex(r"9k^{2}+12k+4=0"),
            MathTex(r"{{9}}{{k^{2}}}{{+12}}{{k^1}}{{+4}}{{k^0}}=0"),
            MathTex(r"k=4"),
            MathTex(r"k=-4"),

            MathTex(r"k=-1"),
            MathTex(r"k=-4/3"),
            MathTex(r"k=-2/3"),
            MathTex(r"(k+2/3)=0"),

            MathTex(r"+4 \to \pm 4 \pm 2 \pm 1"),
            MathTex(r"+9 \to \pm 9 \pm 3 \pm 1"),
            MathTex(r"(4, 9) \to", r"\pm 4", r"\,, \pm 2 \,,", r"\pm 1", r"\,, \pm \frac{4}{9}\,, \pm", r"\frac{4}{3}", r"\,, \pm \frac{2}{9}\, ,\pm", r"\frac{2}{3}", r"\,, \pm \frac{1}{9}\,, \pm \frac{1}{3}"),



        ]
    
        v0 = [
            [[mt(r"k^2")], [mt(r"k^1")], [mt(r"k^1")], [mt(r"DIV")],],

            [[mt(r"9")], [mt(r"12")], [mt(r"4")], [mt(r"0")], ],
            [[mt(r"0")], [mt(r"-12")], [mt(r"0")], [mt(r"k=-\frac{4}{3}")], ],

            [[mt(r"9")], [mt(r"0")], [mt(r"4")], [mt(r"0")], ],
        ]
        vv0 = l_to_vgroup(v0).arrange_in_grid(cols=4, rows=4, buff=(1.5, 0.75), )


        lv0 = v_line(vv0[6], vv0[7], vv0[14], vv0[15])
        # lv1 = v_line(vv0[18], vv0[17], vv0[27], vv0[28])


        lh0 = h_line(vv0[8], vv0[12], vv0[11], vv0[15])
        # lh1 = h_line(vv0[20], vv0[25], vv0[23], vv0[28])
        
        self.add(VGroup(
            vv0[3], vv0[7], vv0[8],  vv0[15],  
            # vv0[15], vv0[20], vv0[24],
            # vv0[28], vv0[29],
            ).set_opacity(0))
        
        self.add(f[1].next_to(vv0, UP*2))
        self.play(FadeIn(f[10].shift(DOWN*2.5)))

        self.wait(1)
        fb0 = SurroundingRectangle(f[10], buff=0.1)
        fb1 = SurroundingRectangle(f[10][5])

        self.play(Create(fb0))
        self.play(ReplacementTransform(fb0, fb1))
        self.wait(1)
        self.play(FadeOut(fb1))
        self.play(ReplacementTransform(f[10], vv0[11]))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                f[1].copy(),
                VGroup(vv0[0], vv0[1], vv0[2], vv0[4], vv0[5], vv0[6])
            ),
            FadeIn(lh0, lv0),
        )
        self.wait(1)

        self.play(TransformFromCopy(vv0[8], vv0[12]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[12], vv0[11]), vv0[9]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[5], vv0[9]), vv0[13]))
        self.wait(1)


        # self.play(TransformFromCopy(vv0[9], vv0[13]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[13], vv0[11]), vv0[10]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[6], vv0[10]), vv0[14]))
        self.wait(1)
        self.play(FadeOut(lh0, lv0, vv0))

class mtds_033(Scene):
    def construct(self):
        f = [
            MathTex(r"9k^{2}+12k+4=0"),
            MathTex(r"{{9}}{{k^{2}}}{{+12}}{{k^1}}{{+4}}{{k^0}}=0"),
            MathTex(r"k=4"),
            MathTex(r"k=-4"),

            MathTex(r"k=-1"),
            MathTex(r"k=-4/3"),
            MathTex(r"k=-2/3"),
            MathTex(r"(k+\frac{2}{3})=0"),

            MathTex(r"+4 \to \pm 4 \pm 2 \pm 1"),
            MathTex(r"+9 \to \pm 9 \pm 3 \pm 1"),
            MathTex(r"(4, 9) \to", r"\pm 4", r"\,, \pm 2 \,,", r"\pm 1", r"\,, \pm \frac{4}{9}\,, \pm", r"\frac{4}{3}", r"\,, \pm \frac{2}{9}\, ,\pm", r"\frac{2}{3}", r"\,, \pm \frac{1}{9}\,, \pm \frac{1}{3}"),
            MathTex(r"({{9}}{{k}}+{{6}})=0"),

            MathTex(r"(9k+6)(k+\frac{2}{3})=0"),
            MathTex(r"3(3k+2)(k+\frac{2}{3})=0"),
            MathTex(r"(3k+2)(3k+2)=0"),
            MathTex(r"(3k+2)^2=0"),


        ]
    
        v0 = [
            [[mt(r"k^2")], [mt(r"k^1")], [mt(r"k^0")], [mt(r"DIV")],],

            [[mt(r"9")], [mt(r"12")], [mt(r"4")], [mt(r"0")], ],
            [[mt(r"0")], [mt(r"-6")], [mt(r"-4")], [mt(r"k=-\frac{2}{3}")], ],

            [[mt(r"9")], [mt(r"6")], [mt(r"0")], [mt(r"0")], ],
        ]
        vv0 = l_to_vgroup(v0).arrange_in_grid(cols=4, rows=4, buff=(1.5, 0.75), )


        lv0 = v_line(vv0[6], vv0[7], vv0[14], vv0[15])
        # lv1 = v_line(vv0[18], vv0[17], vv0[27], vv0[28])


        lh0 = h_line(vv0[8], vv0[12], vv0[11], vv0[15])
        # lh1 = h_line(vv0[20], vv0[25], vv0[23], vv0[28])
        
        self.add(VGroup(
            vv0[3], vv0[7], vv0[8],  vv0[15],  
            # vv0[15], vv0[20], vv0[24],
            # vv0[28], vv0[29],
            ).set_opacity(0))
        
        self.add(f[1].next_to(vv0, UP*2))
        self.play(FadeIn(f[10].shift(DOWN*2.5)))

        self.wait(1)
        fb0 = SurroundingRectangle(f[10], buff=0.1)
        fb1 = SurroundingRectangle(f[10][7])

        self.play(Create(fb0))
        self.play(ReplacementTransform(fb0, fb1))
        self.wait(1)
        self.play(FadeOut(fb1))
        self.play(ReplacementTransform(f[10], vv0[11]))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                f[1].copy(),
                VGroup(vv0[0], vv0[1], vv0[2], vv0[4], vv0[5], vv0[6])
            ),
            FadeIn(lh0, lv0),
        )
        self.wait(1)

        self.play(TransformFromCopy(vv0[8], vv0[12]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[12], vv0[11]), vv0[9]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[5], vv0[9]), vv0[13]))
        self.wait(1)


        # self.play(TransformFromCopy(vv0[9], vv0[13]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[13], vv0[11]), vv0[10]))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(vv0[6], vv0[10]), vv0[14]))
        self.wait(1)
        self.play(TransformMatchingShapes(vv0[11], f[7].move_to(vv0[11]).shift(RIGHT), path_arc=PI/2))
        self.wait(1)
        # self.add(f[6].move_to(vv0[11]))
        k0 = VGroup(vv0[1], vv0[2]).copy()
        self.play(
            k0[0].animate.next_to(vv0[12], DOWN),
            k0[1].animate.next_to(vv0[13], DOWN),
            )
        self.play(
            FadeOut(
                lh0, lv0, 
                vv0[0], vv0[1], vv0[2],
                vv0[4], vv0[5], vv0[6],
                vv0[9], vv0[10], vv0[14]
            )
        )
        self.wait(1)

        self.play(
            TransformMatchingTex(VGroup(k0, vv0[12], vv0[13]), f[11].move_to(VGroup(k0, vv0[12], vv0[13])))
        )
        self.wait(1)
        self.play(f[1].animate.move_to(ORIGIN))
        self.play(ReplacementTransform(VGroup(f[1], f[11], f[7]), f[12]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[12], f[13]))
        self.wait(1)
        self.play(TransformMatchingTex(f[13], f[14]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[14], f[15], path_arc = PI/2))
        self.wait(1)
        

class mtds_040(Scene):
    def construct(self):
        f = [
            MathTex(r"27r^{5}-168r^{4}+260r^{3}+130r^{2}-367r-42=0"),
            MathTex(r"{{27}}", r"r^{5}-168r^{4}+260r^{3}+130r^{2}-367r^1", r"-42", r"r^0=0"),

            MathTex(r"42 \to ", r"\pm 42,", r"\pm 21,", r"\pm 14 ,", r" \pm 7 ,", r" \pm 6,", r" \pm 3 ,", r" \pm 2, ", r"\pm 1"),
            MathTex(r"27 \to \pm 27, \pm 9, \pm 3, \pm 1"),
            MathTex(r"\pm \frac{42}{27}, \pm \frac{42}{9}, \pm \frac{42}{3} , \pm \frac{42}{1} \dots \pm \frac{1}{27} ,\pm \frac{1}{9}, \pm \frac{1}{3} , \pm \frac{1}{1}"),
            MathTex(r"(k+\frac{2}{3})=0"),
            
        ]
    

        v1 = [
            [[mt(r"42")], [mt(r"2")]],
            [[mt(r"21")], [mt(r"3")]],
            [[mt(r"7")], [mt(r"7")]],
            [[mt(r"1")], [mt(r"0")]],

        ]

        vv1 = l_to_vgroup(v1).arrange_in_grid(cols=2, rows=4, buff=(1.5, 0.75), )
        lv1 = v_line(vv1[0], vv1[1], vv1[6], vv1[7])
        v2 = [
            [[mt(r"27")], [mt(r"3")]],
            [[mt(r"9")], [mt(r"3")]],
            [[mt(r"3")], [mt(r"3")]],
            [[mt(r"1")], [mt(r"0")]],

        ]

        vv2 = l_to_vgroup(v2).arrange_in_grid(cols=2, rows=4, buff=(1.5, 0.75), )
        lv2 = v_line(vv2[0], vv2[1], vv2[6], vv2[7])
        
        tb1 = VGroup(vv1, lv1)
        tb2 = VGroup(vv2, lv2)
        # vx0 = VGroup(tb1, tb2).arrange(buff=3)

        self.play(Write(f[0]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[0], f[1]))
        self.wait(1)
        self.play(f[1].animate.shift(UP*3))
        self.wait(1)
        self.play(FadeIn(lv1))
        self.play(TransformMatchingShapes(VGroup(f[1][2]).copy(), vv1[0]))
        for i in range(1, 7):
            self.play(FadeIn(vv1[i]))
            self.wait(1)
        self.wait(1)
        self.play(Write(f[2].next_to(vv1, DOWN)))
        self.wait(1)

        
        
            
        sc0 = SurroundingRectangle(vv1[0])
        sc1 = SurroundingRectangle(f[2][1])
        self.play(Create(sc0))
        self.play(ReplacementTransform(sc0, sc1))
        self.wait(1)

        l = [
            [3, 5, 2],
            [1, 5, 3],
            [5, 0, 4],
            [1, 3, 5],
            [3, 0, 6],
            [1, 0, 7],
            [6, 0, 8],
        ]
        self.play(FadeOut(sc1))
        for i in range(7):
            sc01 = SurroundingRectangle(vv1[l[i][0]])
            if l[i][1] != 0:
                sc02 = SurroundingRectangle(vv1[l[i][1]])
            sc1 = SurroundingRectangle(f[2][l[i][2]])
            self.play(Create(sc01), Create(sc02))
            # self.wait(1)
            if l[i][1] != 0:
                self.play(ReplacementTransform(VGroup(sc01, sc02), sc1))
            else:
                self.play(ReplacementTransform(VGroup(sc01), sc1))
            # self.wait(1)
            self.play(FadeOut(sc1))
        self.wait(1)

        self.play(FadeOut(vv1, lv1,f[2]))
        self.wait(1)

class mtds_041(Scene):
    def construct(self):
        f = [
            MathTex(r"27r^{5}-168r^{4}+260r^{3}+130r^{2}-367r-42=0"),
            MathTex(r"{{27}}", r"r^{5}-168r^{4}+260r^{3}+130r^{2}-367r^1", r"-42", r"r^0=0"),

            
            MathTex(r"27 \to ", r"\pm 27, ", r"\pm 9, ", r"\pm 3, ", r"\pm 1"),
            MathTex(r"42 \to ", r"\pm 42,", r"\pm 21,", r"\pm 14 ,", r" \pm 7 ,", r" \pm 6,", r" \pm 3 ,", r" \pm 2, ", r"\pm 1"),
            MathTex(r"\pm \frac{42}{27}, ", r"\pm \frac{42}{9}, ", r"\pm \frac{42}{3} , ", r"\pm \frac{42}{1}, ",  r"\dots", r" \pm \frac{1}{27} ,", r"\pm \frac{1}{9}, ", r"\pm \frac{1}{3} , ", r"\pm \frac{1}{1}"),
        ]
    
        v1 = [
            [[mt(r"27")], [mt(r"3")]],
            [[mt(r"9")], [mt(r"3")]],
            [[mt(r"3")], [mt(r"3")]],
            [[mt(r"1")], [mt(r"0")]],

        ]

        vv1 = l_to_vgroup(v1).arrange_in_grid(cols=2, rows=4, buff=(1.5, 0.75), )
        lv1 = v_line(vv1[0], vv1[1], vv1[6], vv1[7])
        
        tb1 = VGroup(vv1, lv1)
        # tb2 = VGroup(vv2, lv2)
        # vx0 = VGroup(tb1, tb2).arrange(buff=3)

        self.add(f[1].shift(UP*3))
        self.wait(1)
        self.play(FadeIn(lv1))
        self.play(TransformMatchingShapes(VGroup(f[1][2]).copy(), vv1[0]))
        for i in range(1, 7):
            self.play(FadeIn(vv1[i]))
            self.wait(1)
        self.wait(1)
        self.play(Write(f[2].next_to(vv1, DOWN)))
        self.wait(1)

        sc0 = SurroundingRectangle(vv1[0])
        sc1 = SurroundingRectangle(f[2][1])
        self.play(Create(sc0))
        self.play(ReplacementTransform(sc0, sc1))
        self.wait(1)

        l = [
            [1, 3, 2],
            [1, 0, 3],
            [6, 0, 4],
        ]
        self.play(FadeOut(sc1))
        for i in range(3):
            sc01 = SurroundingRectangle(vv1[l[i][0]])
            if l[i][1] != 0:
                sc02 = SurroundingRectangle(vv1[l[i][1]])
            sc1 = SurroundingRectangle(f[2][l[i][2]])
            self.play(Create(sc01), Create(sc02))
            # self.wait(1)
            if l[i][1] != 0:
                self.play(ReplacementTransform(VGroup(sc01, sc02), sc1))
            else:
                self.play(ReplacementTransform(VGroup(sc01), sc1))
            # self.wait(1)
            self.play(FadeOut(sc1))
        self.wait(1)

        self.play(FadeOut(vv1, lv1))
        self.wait(1)
        self.play(Write(f[3]))
        self.wait(1)
        self.play(
            VGroup(f[1], f[3], f[2],).animate.arrange(DOWN, buff=1)
        )
        self.wait(1)
        f[3].move_to(f[3])
        self.play(VGroup(f[1], f[3], f[2], f[4]).animate.arrange(DOWN, buff=1))
        self.wait(1)

class mtds_042(Scene):
    def construct(self):
        f = [
            MathTex(r"27r^{5}-168r^{4}+260r^{3}+130r^{2}-367r-42=0"),
            MathTex(r"{{27}}", r"r^{5}-168r^{4}+260r^{3}+130r^{2}-367r^1", r"-42", r"r^0=0"),

            MathTex(r"42 \to ", r"\pm 42,", r"\pm 21,", r"\pm 14 ,", r" \pm 7 ,", r" \pm 6,", r" \pm 3 ,", r" \pm 2, ", r"\pm 1"),
            MathTex(r"27 \to ", r"\pm 27, ", r"\pm 9, ", r"\pm 3, ", r"\pm 1"),
            MathTex(r"\pm \frac{42}{27}, ", r"\pm \frac{42}{9}, ", r"\pm \frac{42}{3} , ", r"\pm \frac{42}{1}, ",  r"\dots", r" \pm \frac{1}{27} ,", r"\pm \frac{1}{9}, ", r"\pm \frac{1}{3} , ", r"\pm \frac{1}{1}"),
        ]
    
        v1 = [
            [[mt(r"42")], [mt(r"2")]],
            [[mt(r"21")], [mt(r"3")]],
            [[mt(r"7")], [mt(r"7")]],
            [[mt(r"1")], [mt(r"0")]],
        ]

        vv1 = l_to_vgroup(v1).arrange_in_grid(cols=2, rows=4, buff=(1.5, 0.75), )
        lv1 = v_line(vv1[0], vv1[1], vv1[6], vv1[7])
        v2 = [
            [[mt(r"27")], [mt(r"3")]],
            [[mt(r"9")], [mt(r"3")]],
            [[mt(r"3")], [mt(r"3")]],
            [[mt(r"1")], [mt(r"0")]],
        ]

        vv2 = l_to_vgroup(v2).arrange_in_grid(cols=2, rows=4, buff=(1.5, 0.75), )
        lv2 = v_line(vv2[0], vv2[1], vv2[6], vv2[7])
        VGroup(f[1], f[3], f[2], f[4]).arrange(DOWN, buff=1)
        c = f[2].copy()
        f[2].move_to(f[3])
        f[3].move_to(c)
        
        self.add(
            f[1], f[2], f[3], f[4]
        )

        l = [
            [1, 1, 0],
            [1, 2, 1],
            [1, 3, 2],
            [1, 4, 3],

            [8, 1, 5],
            [8, 2, 6],
            [8, 3, 7],
            [8, 4, 8],

        ]
        # self.play(FadeOut(sc1))

        for i in range(7):
            sc01 = SurroundingRectangle(f[2] [l[i][0]])
            sc02 = SurroundingRectangle(f[3] [l[i][1]])
            sc1 = SurroundingRectangle(f[4] [l[i][2]])
            self.play(Create(sc01), Create(sc02))
            # self.wait(1)
            
            self.play(ReplacementTransform(VGroup(sc01, sc02), sc1))
            # self.wait(1)
            self.play(FadeOut(sc1))
        self.wait(1)

        self.play(
            FadeOut(f[3]),
            VGroup(f[1], f[2], f[4]).animate.arrange(DOWN, buff=0.5)
        )
        self.wait(1)

class mtds_043(Scene):
    def construct(self):
        f = [
            MathTex(r"27r^{5}-168r^{4}+260r^{3}+130r^{2}-367r-42=0"),
            MathTex(r"{{27}}{{r^{5}}}{{-168}}{{r^{4}}}{{+260}}{{r^{3}}}{{+130}}{{r^{2}}}{{-367}}{{r^1}}{{-42}}{{r^0}}=0"),

            MathTex(r"42 \to ", r"\pm 42,", r"\pm 21,", r"\pm 14 ,", r" \pm 7 ,", r" \pm 6,", r" \pm 3 ,", r" \pm 2, ", r"\pm 1"),
            MathTex(r"27 \to ", r"\pm 27, ", r"\pm 9, ", r"\pm 3, ", r"\pm 1"),
            MathTex(r"\pm \frac{42}{27}, ", r"\pm \frac{42}{9}, ", r"\pm \frac{42}{3} , ", r"\pm \frac{42}{1}, ",  r"\dots", r" \pm \frac{1}{27} ,", r"\pm \frac{1}{9}, ", r"\pm \frac{1}{3} , ", r"\pm \frac{1}{1}"),
            MathTex(r"{{(r+1)}}=0"),

            MathTex(r"{{(27r^{4}-195r^{3}+455r^{2}-325r-42)}}=0"),
            MathTex(r"{{(r+1)}}{{(27r^{4}-195r^{3}+455r^{2}-325r-42)}}=0"),

        ]
    
        v1 = [
            [[mt(r"r^5")], [mt(r"r^4")], [mt(r"r^3")], [mt(r"r^2")], [mt(r"r^1")], [mt(r"r^0")], [t(r"DIV")]],
            [[mt(r"27")], [mt(r"-168")], [mt(r"260")], [mt(r"130")], [mt(r"-367")], [mt(r"-42")], [mt(r"0")]],
            [[mt(r"0")], [mt(r"-27")], [mt(r"195")], [mt(r"-455")], [mt(r"325")], [mt(r"42")], [mt(r"r=-1")]],
            [[mt(r"27")], [mt(r"-195")], [mt(r"455")], [mt(r"-325")], [mt(r"-42")], [mt(r"0")], [mt(r"0")]],
        ]

        vv1 = l_to_vgroup(v1).arrange_in_grid(cols=7, rows=4, buff=(0.75, 0.75), )
        lv1 = v_line(vv1[12], vv1[13], vv1[26], vv1[27])
        lh1 = h_line(vv1[14], vv1[21], vv1[13], vv1[27])

        self.add(VGroup(f[1], f[2], f[4]).arrange(DOWN, buff=0.5))
        self.wait(1)
        self.play(FadeOut(f[2], f[4]), f[1].animate.next_to(vv1, UP*1.5))
        self.wait(1)
        self.play(FadeIn(lv1, lh1))
        self.play(
            TransformMatchingTex(
                f[1].copy(), 
                VGroup(
                    vv1[0], vv1[1], vv1[2], vv1[3], vv1[4], vv1[5],
                    vv1[7], vv1[8], vv1[9], vv1[10], vv1[11], vv1[12],
                )
            )
        )
        self.wait(1)
        
        self.play(Write(vv1[20].shift(RIGHT)))
        self.wait(1)
        self.play(TransformFromCopy(vv1[7], vv1[21]))
        self.wait(1)
        
        for i in range(5):
            self.play(
                TransformFromCopy(
                    VGroup(vv1[21+i], vv1[20]),
                    vv1[15+i],
                )
            )
            self.wait(1)
            self.play(TransformFromCopy(VGroup(vv1[8+i], vv1[15+i]), vv1[22+i]))
            self.wait(1)
        self.wait(1)

        self.play(TransformMatchingShapes(vv1[20], f[5].move_to(vv1[20]), path_arc = PI/2))
        self.wait(1)
        k = VGroup(vv1[1], vv1[2], vv1[3], vv1[4], vv1[5]).copy()
        self.play(
            k[0].animate.next_to(vv1[21], DOWN),
            k[1].animate.next_to(vv1[22], DOWN),
            k[2].animate.next_to(vv1[23], DOWN),
            k[3].animate.next_to(vv1[24], DOWN),
            k[4].animate.next_to(vv1[25], DOWN),
        )
        self.wait(1)
        self.play(
            FadeOut(
                vv1[0:6], vv1[7:13], vv1[15:20], vv1[26], lv1, lh1 
            )
        )
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(k, vv1[21:26]), f[6].move_to(k)))
        self.wait(1)
        self.play(
            TransformMatchingTex(VGroup(f[5], f[6], f[1]), f[7])
            )
        self.wait(1)

class mtds_044(Scene):
    def construct(self):
        f = [
            MathTex(r"(r+1)(27r^{4}-195r^{3}+455r^{2}-325r-42)=0"),
            MathTex(r"(r+1)({{27}}{{r^{4}}}{{-195}}{{r^{3}}}{{+455}}{{r^{2}}}{{-325}}{{r^1}}{{-42}}{{r^0}})=0"),

            MathTex(r"42 \to ", r"\pm 42,", r"\pm 21,", r"\pm 14 ,", r" \pm 7 ,", r" \pm 6,", r" \pm 3 ,", r" \pm 2, ", r"\pm 1"),
            MathTex(r"\pm \frac{42}{27}, ", r"\pm \frac{42}{9}, ", r"\pm \frac{42}{3} , ", r"\pm \frac{42}{1}, ",  r"\dots", r" \pm \frac{1}{27} ,", r"\pm \frac{1}{9}, ", r"\pm \frac{1}{3} , ", r"\pm \frac{1}{1}"),
            MathTex(r"{{(r-2)}}=0"),

            MathTex(r"{{(27r^{3}-141r^{2}+173r+21)}}=0"),
            MathTex(r"(r+1)(r-2)(27r^{3}-141r^{2}+173r+21)=0"),

        ]
    
        v1 = [
            [[mt(r"{{r^4}}")], [mt(r"{{r^3}}")], [mt(r"{{r^2}}")], [mt(r"{{r^1}}")], [mt(r"{{r^0}}")], [t(r"0")]],
            [[mt(r"{{27}}")], [mt(r"{{-195}}")], [mt(r"{{455}}")], [mt(r"{{-325}}")], [mt(r"{{-42}}")], [mt(r"DIV")]],
            [[mt(r"0")], [mt(r"54")], [mt(r"-282")], [mt(r"346")], [mt(r"42")], [mt(r"r=2")]],
            [[mt(r"27")], [mt(r"-141")], [mt(r"173")], [mt(r"21")], [mt(r"0")], [mt(r"0")]],
        ]

        vv1 = l_to_vgroup(v1).arrange_in_grid(cols=6, rows=4, buff=(0.75, 0.75), )
        lv1 = v_line(vv1[10], vv1[11], vv1[22], vv1[23])
        lh1 = h_line(vv1[12], vv1[18], vv1[17], vv1[23])


        VGroup(vv1[5], vv1[11], vv1[12], vv1[23]).set_opacity(0)
        self.add(f[0])
        self.wait(1)
        self.play(f[0].animate.next_to(vv1, UP))
        self.play(TransformMatchingShapes(f[0], f[1].move_to(f[0])))
        self.wait(1)
        self.play(FadeIn(lv1, lh1))
        self.wait(1)
        self.play(FadeIn(vv1[17].shift(RIGHT*0.5)))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                f[1].copy(), 
                VGroup(vv1[0:5], vv1[6:11])
                )
        )
        self.wait(1)
        self.play(TransformFromCopy(vv1[6], vv1[18]))
        self.wait(1)


        for i in range(4):
            self.play(
                TransformFromCopy(
                    VGroup(vv1[18+i], vv1[17]),
                    vv1[13+i],
                )
            )
            self.wait(1)
            self.play(TransformFromCopy(VGroup(vv1[7+i], vv1[13+i]), vv1[19+i]))
            self.wait(1)
        self.wait(1)

        self.play(TransformMatchingShapes(vv1[17], f[4].move_to(vv1[17]).shift(RIGHT*0.5), path_arc = PI/2))
        self.wait(1)
        self.play(FadeOut(vv1[0:5], vv1[6:11], vv1[13:17], vv1[22], lh1, lv1))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(vv1[18:22]), f[5].move_to(VGroup(vv1[18:22]))))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[4], f[1], f[5]), f[6]))
        self.wait(1)
    
class mtds_045(Scene):
    def construct(self):
        f = [
            MathTex(r"(r+1)(r-2)(27r^{3}-141r^{2}+173r+21)=0"),
            MathTex(r"(r+1)(r-2)({{27}}{{r^{3}}}{{-141}}{{r^{2}}}{{+173}}{{r^1}}{{+21}}{{r^0}})=0"),

            MathTex(r"21 \to ", r"\pm 21,", r"\pm 7,", r"\pm 3 ,", r" \pm 1"),
            MathTex(r"27 \to \pm 27, \pm 9, \pm 3, \pm 1"),
            MathTex(r"\pm \frac{21}{27}, ", r"\pm \frac{21}{9}, ", r"\pm \frac{21}{3} , ", r"\pm \frac{21}{1}, ",  r"\dots", r" \pm \frac{1}{27} ,", r"\pm \frac{1}{9}, ", r"\pm \frac{1}{3} , ", r"\pm \frac{1}{1}"),
            MathTex(r"{{(r-3)}}=0"),

            MathTex(r"{{(27r^{2}-60r-7)}}=0"),
            MathTex(r"(r+1)(r-2)(r-3)(27r^{2}-60r-7)=0"),

        ]
    
        v1 = [
            [[mt(r"{{r^3}}")], [mt(r"{{r^2}}")], [mt(r"{{r^1}}")], [mt(r"{{r^0}}")], [t(r"0")]],
            [[mt(r"27")], [mt(r"-141")], [mt(r"173")], [mt(r"21")], [mt(r"DIV")]],
            [[mt(r"0")], [mt(r"81")], [mt(r"-180")], [mt(r"-21")], [mt(r"r=3")]],
            [[mt(r"27")], [mt(r"-60")], [mt(r"-7")], [mt(r"0")], [mt(r"0")]],
        ]

        vv1 = l_to_vgroup(v1).arrange_in_grid(cols=5, rows=4, buff=(0.75, 0.75), )
        lv1 = v_line(vv1[8], vv1[9], vv1[18], vv1[19])
        lh1 = h_line(vv1[10], vv1[15], vv1[14], vv1[19])


        VGroup(vv1[4], vv1[9], vv1[10], vv1[19]).set_opacity(0)
        self.add(f[0])
        self.wait(1)
        self.play(f[0].animate.next_to(vv1, UP))
        self.play(TransformMatchingShapes(f[0], f[1].move_to(f[0])))
        self.wait(1)
        self.play(TransformMatchingTex(f[1].copy(), f[2]), f[3].animate.next_to(f[2], DOWN))
        self.wait(1)

        self.play(TransformMatchingTex(VGroup(f[2].copy(), f[3]), f[4].next_to(f[3], DOWN*2)))
        # self.wait(1)
        self.play(VGroup(f[2], f[4]).animate.arrange(DOWN))
        self.wait(1)
        self.play(FadeOut(VGroup(f[2], f[4])))


        self.wait(1)
        self.play(FadeIn(lv1, lh1))
        self.wait(1)
        self.play(FadeIn(vv1[14].shift(RIGHT*0.5)))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                f[1].copy(), 
                VGroup(vv1[0:4], vv1[5:9])
                )
        )
        self.wait(1)
        self.play(TransformFromCopy(vv1[5], vv1[15]))
        self.wait(1)


        for i in range(3):
            self.play(
                TransformFromCopy(
                    VGroup(vv1[15+i], vv1[14]),
                    vv1[11+i],
                )
            )
            self.wait(1)
            self.play(TransformFromCopy(VGroup(vv1[6+i], vv1[11+i]), vv1[16+i]))
            self.wait(1)
        self.wait(1)

        self.play(TransformMatchingShapes(vv1[14], f[5].move_to(vv1[14]).shift(RIGHT*0.5), path_arc = PI/2))
        self.wait(1)
        self.play(FadeOut(vv1[0:4], vv1[5:9], vv1[11:14], vv1[18], lh1, lv1))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(vv1[15:18]), f[6].move_to(VGroup(vv1[15:18]))))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[1], f[5], f[6]), f[7]))
        self.wait(1)

class mtds_046(Scene):
    def construct(self):
        f = [
            MathTex(r"(r+1)(r-2)(r-3)(27r^{2}-60r-7)=0"),
            MathTex(r"(r+1)(r-2)(r-3)({{27}}{{r^{2}}}{{-60}}{{r^1}}{{-7}}{{r^0}})=0"),

            MathTex(r"-7 \to ", r"\pm 7,", r" \pm 1"),
            MathTex(r"27 \to \pm 27, \pm 9, \pm 3, \pm 1"),
            MathTex(r"\pm \frac{7}{27}, ", r"\pm \frac{7}{9}, ", r"\pm \frac{7}{3} , ", r"\pm \frac{7}{1}, ", r" \pm \frac{1}{27} ,", r"\pm \frac{1}{9}, ", r"\pm \frac{1}{3} , ", r"\pm \frac{1}{1}"),
            MathTex(r"{{(r-\frac{7}{3})}}=0"),

            MathTex(r"{{(27r+3)}}=0"),
            MathTex(r"(r+1)(r-2)(r-3)", r"\left( r-\frac{7}{3} \right)(27r+3)", r"=0"),
            MathTex(r"(r+1)(r-2)(r-3)", r"\left( r-\frac{7}{3} \right)", r"[3(9r+1)]", r"=0"),
            MathTex(r"(r+1)(r-2)(r-3)", r"( 3r-7)", r"(9r+1)", r"=0"),

        ]
    
        v1 = [
            [[mt(r"{{r^2}}")], [mt(r"{{r^1}}")], [mt(r"{{r^0}}")], [t(r"0")]],
            [[mt(r"27")], [mt(r"-60")], [mt(r"-7")], [mt(r"DIV")]],
            [[mt(r"0")], [mt(r"63")], [mt(r"7")], [mt(r"r=\frac{7}{3}")]],
            [[mt(r"27")], [mt(r"3")], [mt(r"0")], [mt(r"0")]],
        ]

        vv1 = l_to_vgroup(v1).arrange_in_grid(cols=4, rows=4, buff=(0.75, 0.75), )
        lv1 = v_line(vv1[6], vv1[7], vv1[14], vv1[15])
        lh1 = h_line(vv1[8], vv1[12], vv1[11], vv1[15])


        VGroup(vv1[3], vv1[7], vv1[8], vv1[15]).set_opacity(0)
        self.add(f[0])
        self.wait(1)
        self.play(f[0].animate.next_to(vv1, UP))
        self.play(TransformMatchingShapes(f[0], f[1].move_to(f[0])))
        self.wait(1)
        self.play(TransformMatchingTex(f[1].copy(), f[2]), f[3].animate.next_to(f[2], DOWN))
        self.wait(1)

        self.play(TransformMatchingTex(VGroup(f[2].copy(), f[3]), f[4].next_to(f[3], DOWN*2)))
        # self.wait(1)
        self.play(VGroup(f[2], f[4]).animate.arrange(DOWN))
        self.wait(1)
        self.play(FadeOut(VGroup(f[2], f[4])))


        self.wait(1)
        self.play(FadeIn(lv1, lh1))
        self.wait(1)
        self.play(FadeIn(vv1[11].shift(RIGHT*0.5)))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                f[1].copy(), 
                VGroup(vv1[0:3], vv1[4:7])
                )
        )
        self.wait(1)
        self.play(TransformFromCopy(vv1[4], vv1[12]))
        self.wait(1)


        for i in range(2):
            self.play(
                TransformFromCopy(
                    VGroup(vv1[12+i], vv1[11]),
                    vv1[9+i],
                )
            )
            self.wait(1)
            self.play(TransformFromCopy(VGroup(vv1[5+i], vv1[9+i]), vv1[13+i]))
            self.wait(1)
        self.wait(1)

        self.play(TransformMatchingShapes(vv1[11], f[5].move_to(vv1[11]).shift(RIGHT*0.5), path_arc = PI/2))
        self.wait(1)
        self.play(FadeOut(vv1[0:3], vv1[4:7], vv1[9:11], vv1[14], lh1, lv1))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(vv1[12:14]), f[6].move_to(VGroup(vv1[12:14]))))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[1], f[5], f[6]), f[7]))
        self.wait(1)
        sc0 = SurroundingRectangle(f[7][1])
        self.play(Create(sc0))
        self.wait(1)
        sc1 = SurroundingRectangle(VGroup(f[8][1], f[8][2]))
        self.play(TransformMatchingShapes(f[7], f[8]), ReplacementTransform(sc0, sc1))
        self.wait(1)
        sc2 = SurroundingRectangle(f[8][1])
        self.play(ReplacementTransform(sc1, sc2))
        self.wait(1)
        self.play(
            TransformMatchingShapes(f[8], f[9]),
            FadeOut(sc2)
        )
        self.wait(1)

class mtds_050(Scene):
    def construct(self):
        f = [
            MathTex(r"x^{4}-1=0"),
            MathTex(r"{{1}}{{x^{4}}}+{{0}}{{x^3}}+{{0}}{{x^2}}+{{0}}{{x^1}} {{-1}}{{x^0}}=0"),

            MathTex(r"(x+1)=0"),
            MathTex(r"(x-1)=0"),

            MathTex(r"x^2+1=0"),


            MathTex(r"{{(x^{3}-x^{2}+x-1)}}=0"),
            MathTex(r"{{(x+1)}}{{(x^{3}-x^{2}+x-1)}}=0"),

        ]
    
        v1 = [
            [[mt(r"{{x^4}}")], [mt(r"{{x^3}}")], [mt(r"{{x^2}}")], [mt(r"{{x^1}}")], [mt(r"{{x^0}}")], [t(r"0")]],
            [[mt(r"{{1}}")], [mt(r"{{0}}")], [mt(r"{{0}}")], [mt(r"{{0}}")], [mt(r"{{-1}}")], [mt(r"DIV")]],
            [[mt(r"0")], [mt(r"-1")], [mt(r"1")], [mt(r"-1")], [mt(r"1")], [mt(r"x=-1")]],
            [[mt(r"1")], [mt(r"-1")], [mt(r"1")], [mt(r"-1")], [mt(r"0")], [mt(r"0")]],
        ]

        vv1 = l_to_vgroup(v1).arrange_in_grid(cols=6, rows=4, buff=(0.75, 0.75), )
        lv1 = v_line(vv1[10], vv1[11], vv1[22], vv1[23])
        lh1 = h_line(vv1[12], vv1[18], vv1[17], vv1[23])


        VGroup(vv1[5], vv1[11], vv1[12], vv1[23]).set_opacity(0)
        self.add(f[0])
        self.wait(1)
        self.play(f[0].animate.next_to(vv1, UP))
        self.play(TransformMatchingShapes(f[0], f[1].move_to(f[0])))
        self.wait(1)
        self.play(FadeIn(lv1, lh1))
        self.wait(1)
        self.play(FadeIn(vv1[17].shift(RIGHT*0.5)))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                f[1].copy(), 
                VGroup(vv1[0:5], vv1[6:11])
                )
        )
        self.wait(1)
        self.play(TransformFromCopy(vv1[6], vv1[18]))
        self.wait(1)


        for i in range(4):
            self.play(
                TransformFromCopy(
                    VGroup(vv1[18+i], vv1[17]),
                    vv1[13+i],
                )
            )
            self.wait(1)
            self.play(TransformFromCopy(VGroup(vv1[7+i], vv1[13+i]), vv1[19+i]))
            self.wait(1)
        self.wait(1)

        self.play(TransformMatchingShapes(vv1[17], f[2].move_to(vv1[17]).shift(RIGHT*0.5), path_arc = PI/2))
        self.wait(1)
        self.play(FadeOut(vv1[0:5], vv1[6:11], vv1[13:17], vv1[22], lh1, lv1))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(vv1[18:22]), f[5].move_to(VGroup(vv1[18:22]))))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[2], f[1], f[5]), f[6]))
        self.wait(1)

class mtds_051(Scene):
    def construct(self):
        f = [
            MathTex(r"(x+1)(x^{3}-x^{2}+x-1)=0"),
            MathTex(r"(x+1)({{1}}{{x^{3}}}{{-1}}{{x^{2}}}{{+1}}{{x^1}}{{-1}}{{x^0}})=0"),
            
            MathTex(r"{{(x-1)}}=0"),
            MathTex(r"{{(x^{2}+1)}}=0"),



            MathTex(r"{{(x-1)}}{{(x+1)}}{{(x^{2}+1)}}=0"),

        ]
    
        v1 = [
            [[mt(r"{{x^3}}")], [mt(r"{{x^2}}")], [mt(r"{{x^1}}")], [mt(r"{{x^0}}")], [t(r"0")]],
            [[mt(r"1")], [mt(r"-1")], [mt(r"1")], [mt(r"-1")], [mt(r"DIV")]],
            [[mt(r"0")], [mt(r"1")], [mt(r"0")], [mt(r"1")], [mt(r"x=1")]],
            [[mt(r"1")], [mt(r"0")], [mt(r"1")], [mt(r"0")], [mt(r"0")]],
        ]

        vv1 = l_to_vgroup(v1).arrange_in_grid(cols=5, rows=4, buff=(0.75, 0.75), )
        lv1 = v_line(vv1[8], vv1[9], vv1[18], vv1[19])
        lh1 = h_line(vv1[10], vv1[15], vv1[14], vv1[19])


        VGroup(vv1[4], vv1[9], vv1[10], vv1[19]).set_opacity(0)
        self.add(f[0])
        self.wait(1)
        self.play(f[0].animate.next_to(vv1, UP))
        self.play(TransformMatchingShapes(f[0], f[1].move_to(f[0])))
        self.wait(1)
        self.play(FadeIn(lv1, lh1))
        self.wait(1)
        self.play(FadeIn(vv1[14].shift(RIGHT*0.5)))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                f[1].copy(), 
                VGroup(vv1[0:4], vv1[5:9])
                )
        )
        self.wait(1)
        self.play(TransformFromCopy(vv1[5], vv1[15]))
        self.wait(1)


        for i in range(3):
            self.play(
                TransformFromCopy(
                    VGroup(vv1[15+i], vv1[14]),
                    vv1[11+i],
                )
            )
            self.wait(1)
            self.play(TransformFromCopy(VGroup(vv1[6+i], vv1[11+i]), vv1[16+i]))
            self.wait(1)
        self.wait(1)

        self.play(TransformMatchingShapes(vv1[14], f[2].move_to(vv1[14]).shift(RIGHT*0.5), path_arc = PI/2))
        self.wait(1)
        self.play(FadeOut(vv1[0:4], vv1[5:9], vv1[11:14], vv1[18], lh1, lv1))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(vv1[15:18]), f[3].move_to(VGroup(vv1[15:18]))))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[1], f[2], f[3]), f[4]))
        self.wait(1)

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
