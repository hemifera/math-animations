from manim import (
    DL,
    DOWN,
    LEFT,
    ORIGIN,
    PI,
    RIGHT,
    UP,
    Circumscribe,
    FadeIn,
    FadeOut,
    Group,
    ImageMobject,
    MathTex,
    ReplacementTransform,
    Scene,
    Text,
    TransformFromCopy,
    TransformMatchingShapes,
    TransformMatchingTex,
    VGroup,
    Write,
)
from manim.animation.transform_matching_parts import TransformMatchingAbstractBase

# cambios de codigo
# renderizar desde la direccion actual del archivo


class difp_00(Scene):
    def construct(self):
        img = ImageMobject("../img/udb_logo_high.png")
        t1 = Text(r"División de polinómios")
        t2 = Text(r"Fracciones parciales", font_size=32)

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))


class difp_10(Scene):
    def construct(self):
        f = [
            MathTex(r"\frac{Ax^{2}+Bx+C}{Dx{^5}+Ex{^4}+Fx{^3}+\dots}", font_size=40),
            MathTex(r"= \frac{G}{Hx+I} + \frac{J}{Kx+L}+\dots", font_size=40),
            MathTex(
                r"=\frac{G}{Hx+I} + \frac{J}{(Hx+I)^{2}}+\dots\frac{K}{(Hx+I)^{n}}",
                font_size=40,
            ),
            MathTex(r"=\frac{G}{x^{2}+H}+\frac{I}{x^{2}+J}+\dots", font_size=40),
            MathTex(
                r"=\frac{Gx+H}{x^{2}+I}+\frac{Jx+K}{(x^{2}+I)^{2}}+\dots+\frac{Lx+M}{(x^{2}+I)^{n}}",
                font_size=40,
            ),
            MathTex(
                r"\frac{2663x^{2}-1079x-1702}{66x^{3}-25x^{2}-46x}",
            ),
            MathTex(r"=\frac{37}{x} +\frac{8}{3x+2}-\frac{15}{23-22x}", font_size=40),
            MathTex(r"66x^{3}-25x^{2}-46x"),
            MathTex(r"(x)(66x^{2}-25x-46)"),
            MathTex(r"(x)(3x+2)(22x-23)"),
            MathTex(r"x=\frac{-(-25)\pm \sqrt{ (-25)^{2} -4(66)(-46)}}{2(66)}"),
            MathTex(r"x=-\frac{2}{3}"),
            MathTex(r"x=\frac{23}{22}"),
            MathTex(r"3x=-2"),
            MathTex(r"(3x+2)=0"),
            MathTex(r"22x=23"),
            # 16
            MathTex(r"(22x-23)=0"),
            MathTex(r"66x^{2}-25x-46", r" = (3x+2)(22x-23)"),
            MathTex(
                r"\frac{2663x^{2}-1079x-1702}{(x)(3x+2)(22x-23)}",
                r"=",
                r"\frac{A}{x}",
                r"+\frac{B}{3x+2}",
                r"+\frac{C}{22x-23}",
                font_size=40,
            ),
            MathTex(
                r"2663x^{2}-1079x-1702 = \left( ",
                r"\frac{A}{x}",
                r"+\frac{B}{3x+2}+\frac{C}{22x-23} \right) ",
                r"(x)(3x+2)(22x-23) ",
                font_size=40,
            ),
            MathTex(r"\frac{A}{x}(x)(3x+2)(22x-23)", r" = A(3x+2)(22x-23)"),
            MathTex(
                r"2663x^{2}-1079x-1702 ",
                r"&= A(3x+2)(22x-23) \\",
                r"&\quad +B(x)(22x-23)\\ ",
                r"&\quad +  C(x)(3x+2)",
                font_size=40,
            ),
            MathTex(r"(3x+2)=0 \leftrightarrow ", r"x=-\frac{2}{3}"),
            MathTex(r"3\left( -\frac{2}{3} \right)+2 ", r"=-2+2=0 "),
            MathTex(r"x=-\frac{2}{3}"),
            MathTex(
                r"A(3x+2)(22x-23)",
            ),
            MathTex(
                r"\to A\left( 3\left( -\frac{2}{3}\right) +2\right)\left( 22\left( -\frac{2}{3} \right) +23\right)",
                font_size=40,
            ),
            MathTex(r"A(0)\left( -\frac{44}{3} \right)", r"=0", font_size=40),
            # 28
            MathTex(r"x={{0}}", font_size=40),
            MathTex(
                r"2663x^{2}-1079x-1702 ",
                r"&= A(3x+2)(22x-23) \\",
                r"&\quad +B(x)(22x-23)\\ ",
                r"&\quad +  C(x)(3x+2)",
                font_size=40,
            ),
            MathTex(
                r"2663(0)^{2}-1079(0)",
                r"-1702 &= ",
                r"A(3(0)+2)(22(0)-23)\\",
                r"&+B(0)(22(0)-23)\\",
                r"&+C(0)(3(0)+2)",
                font_size=40,
            ),
            MathTex(r"-46A=-1702", font_size=40),
            MathTex(r"A=\frac{-1702}{-46}", font_size=40),
            MathTex(r"A=37", font_size=40),
            MathTex(r"x={{-\frac{2}{3}}}", font_size=40),
            MathTex(
                r"2663\left( -\frac{2}{3} \right)^{2}-1079 \left( -\frac{2}{3} \right) -1702 ",
                r"&= A\left( 3\left( -\frac{2}{3} \right)+2\right)\left(22\left( -\frac{2}{3} \right)-23\right)\\",
                r"&+B \left(-\frac{2}{3} \right)\left(22\left(-\frac{2}{3} \right)-23\right)\\",
                r"&+C\left(-\frac{2}{3} \right)\left(3\left(-\frac{2}{3} \right)+2\right)",
                font_size=40,
            ),
            # 36
            MathTex(r"\frac{226}{9}B=\frac{1808}{9}", font_size=40),
            MathTex(r"B=\frac{\frac{1808}{9}}{\frac{226}{9}}", font_size=40),
            MathTex(r"B=8", font_size=40),
            MathTex(r"x={{\frac{23}{22}}}", font_size=40),
            MathTex(
                r"2663\left( \frac{23}{22} \right)^{2}-1079 \left( \frac{23}{22} \right) -1702 ",
                r"&= A\left( 3\left( \frac{23}{22} \right)+2\right)\left(22\left( \frac{23}{22} \right)-23\right)\\",
                r"&+B \left(\frac{23}{22} \right)\left(22\left(\frac{23}{22} \right)-23\right)\\",
                r"&+C\left(\frac{23}{22} \right)\left(3\left(\frac{23}{22} \right)+2\right)",
                font_size=40,
            ),
            MathTex(
                r"2663\left( \frac{23}{22} \right)^{2}-1079\left( \frac{23}{22} \right)-1702 = C\left( \frac{23}{22} \right)\left( 3\cdot \frac{23}{22} +2\right)",
                font_size=40,
            ),
            MathTex(
                r"\frac{2663\left( \frac{23}{22} \right)^{2}-1079\left( \frac{23}{22} \right)-1702}{\left( \frac{23}{22} \right)\left( 3\cdot \frac{23}{22} +2\right)}=C",
                font_size=40,
            ),
            MathTex(r"15=C", font_size=40),
            MathTex(r"C=15", font_size=40),
            MathTex(
                r"\frac{2663x^{2}-1079x-1702}{(x)(3x+2)(22x-23)} = \frac{A}{x}+\frac{B}{3x+2}+\frac{C}{22x-23}",
                font_size=40,
            ),
            MathTex(
                r"\frac{2663x^{2}-1079x-1702}{(x)(3x+2)(22x-23)} = ",
                r"\frac{37}{x}+\frac{8}{3x+2}+\frac{15}{22x-23}",
                font_size=40,
            ),
            MathTex(r""),
            MathTex(r""),
            MathTex(r""),
            MathTex(r""),
            MathTex(r""),
        ]

        self.play(Write(f[0]), run_time=0.7)
        self.wait()
        self.play(f[0].animate.shift(LEFT * 4))

        self.play(Write(f[1].next_to(f[0], RIGHT)), run_time=0.7)
        self.wait()
        self.play(FadeOut(f[1]), run_time=0.7)
        self.wait()

        self.play(Write(f[2].next_to(f[0], RIGHT)), run_time=0.7)
        self.wait()
        self.play(FadeOut(f[2]), run_time=0.7)
        self.wait()

        self.play(Write(f[3].next_to(f[0], RIGHT)), run_time=0.7)
        self.wait()
        self.play(FadeOut(f[3]), run_time=0.7)
        self.wait()

        self.play(Write(f[4].next_to(f[0], RIGHT)), run_time=0.7)
        self.wait()
        v0 = VGroup(f[1], f[2], f[3], f[4])
        self.play(
            v0.animate.arrange(DOWN, aligned_edge=LEFT).next_to(f[0], RIGHT),
            run_time=0.7,
        )
        self.wait()

        self.play(FadeOut(v0, f[0]))
        self.wait()

        self.play(Write(f[5]), run_time=0.7)
        self.wait()
        self.play(f[5].animate.shift(LEFT * 3))
        self.play(Write(f[6].next_to(f[5], RIGHT)), run_time=0.7)
        self.wait()

        self.play(FadeOut(f[6]), f[5].animate.move_to(ORIGIN).shift(UP * 3))
        self.wait()

        self.play(TransformFromCopy(f[5], f[7]))
        self.wait()
        self.play(f[9].animate.next_to(f[7], DOWN))
        self.wait()
        self.play(FadeOut(f[9]))
        self.wait()
        f[9].move_to(ORIGIN)
        self.play(TransformMatchingShapes(f[7], f[8]))
        self.wait()
        self.play(TransformMatchingShapes(f[8].copy(), f[10].next_to(f[8], DOWN)))
        self.wait()
        v1 = VGroup(f[11], f[12]).arrange(buff=3)
        self.play(TransformFromCopy(f[10], v1.next_to(f[10], DOWN)))
        self.wait()

        self.play(Circumscribe(f[11]))
        self.wait()
        f[13].move_to(f[11])
        self.play(TransformMatchingShapes(f[11], f[13], path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[13], f[14].move_to(f[13]), path_arc=PI / 2))
        self.wait()

        self.play(Circumscribe(f[12]))
        self.wait()
        f[15].move_to(f[12])
        self.play(TransformMatchingShapes(f[12], f[15], path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[15], f[16].move_to(f[15]), path_arc=PI / 2))
        self.wait()
        self.play(FadeOut(f[10]))
        self.wait()
        f[17].next_to(f[8], DOWN)
        self.play(Write(f[17][0]))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(f[14], f[16]), f[17][1]))
        self.wait()
        self.play(
            FadeOut(f[17][0]), TransformMatchingShapes(VGroup(f[8], f[17][1]), f[9])
        )
        self.wait()

        f[18].move_to(f[5])
        self.play(TransformMatchingShapes(VGroup(f[5], f[9]), f[18][0]))
        self.wait()
        self.play(Write(VGroup(*f[18][1:5])))
        self.wait()
        self.play(f[18].animate.move_to(ORIGIN))
        self.wait()
        self.play(TransformMatchingShapes(f[18], f[19], path_arc=PI / 2))
        self.wait()
        self.play(Circumscribe(f[19][1]))
        self.wait()
        self.play(Circumscribe(f[19][3]))
        self.wait()
        f[20].next_to(f[19], DOWN)
        self.play(TransformMatchingShapes(f[19].copy(), f[20][0]))
        self.wait()
        self.play(Write(f[20][1]), run_time=0.7)
        self.wait()
        self.play(FadeOut(f[20]))
        self.wait()
        self.play(TransformMatchingShapes(f[19], f[21], path_arc=PI / 2))
        self.wait()

        # # recordar la linea siguiente
        self.play(f[21].animate.shift(UP * 2.8))
        self.wait()
        self.play(Write(f[22]), run_time=0.7)
        self.wait()
        f[23].next_to(f[22], DOWN)
        self.play(
            TransformMatchingShapes(
                f[22].copy(), f[23][0], key_map={r"-\frac{2}{3}": r"-\frac{2}{3}"}
            )
        )
        self.wait()
        self.play(Write(f[23][1]), run_time=0.7)
        self.wait()
        self.play(FadeOut(f[23]), TransformMatchingShapes(f[22], f[24]))
        self.wait()
        self.play(Circumscribe(f[21][1]))
        self.wait()
        self.play(
            TransformMatchingShapes(
                f[21][1].copy(), f[25].next_to(f[24], DOWN * 1.3).shift(LEFT * 3)
            )
        )
        self.wait()
        self.play(Write(f[26].next_to(f[25], RIGHT)), run_time=0.7)
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(f[26], f[25]), f[27].next_to(f[24], DOWN * 1.3)
            )
        )
        self.wait()
        self.play(FadeOut(f[27]))
        self.wait()
        self.play(ReplacementTransform(f[24], f[28]))
        self.wait()

        # despues de pruebas quitar la siguiente linea:
        # self.add(f[21].shift(UP*2.8))

        self.play(f[28].animate.next_to(f[21], DOWN))
        self.wait()

        self.play(TransformFromCopy(f[21], f[29]))
        self.wait()
        self.play(
            TransformMatchingShapes(VGroup(f[28].copy(), f[29]), f[30]),
            key_map={r"x": r"0"},
        )

        self.wait()
        self.play(
            Circumscribe(f[30][0]), Circumscribe(f[30][3]), Circumscribe(f[30][4])
        )
        self.wait()
        self.play(TransformMatchingShapes(f[30], f[31]))
        self.wait()
        self.play(TransformMatchingShapes(f[31], f[32]))
        self.wait()
        self.play(TransformMatchingShapes(f[32], f[33]))
        self.wait()
        self.play(f[33].animate.next_to(f[21], DL))
        self.wait()

        self.play(ReplacementTransform(f[28], f[34].next_to(f[21], DOWN)))
        self.wait()

        self.play(TransformFromCopy(f[21], f[29].next_to(f[34], DOWN)))
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(f[34].copy(), f[29]), f[35].next_to(f[34], DOWN)
            ),
            key_map={r"x": r"-\frac{2}{3}"},
        )
        self.wait()

        self.play(Circumscribe(f[35][1]), Circumscribe(f[35][3]))
        self.wait()
        self.play(TransformMatchingShapes(f[35], f[36].move_to(f[35])))
        self.wait()
        self.play(TransformMatchingShapes(f[36], f[37].move_to(f[36]), path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[37], f[38].move_to(f[37])))
        self.wait()

        self.play(f[38].animate.next_to(f[33], DOWN, aligned_edge=LEFT))
        self.wait()

        self.play(ReplacementTransform(f[34], f[39].next_to(f[21], DOWN)))
        self.wait()

        self.play(TransformFromCopy(f[21], f[29].next_to(f[39], DOWN)))
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(f[34].copy(), f[29]), f[40].next_to(f[34], DOWN)
            ),
            key_map={r"x": r"-\frac{2}{3}"},
        )
        self.wait()

        self.play(Circumscribe(f[40][1]), Circumscribe(f[40][2]))
        self.wait()

        self.play(TransformMatchingShapes(f[40], f[41].move_to(f[40])))
        self.wait()
        self.play(TransformMatchingShapes(f[41], f[42].move_to(f[41]), path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[42], f[43].move_to(f[42])))
        self.wait()
        self.play(TransformMatchingShapes(f[43], f[44].move_to(f[43]), path_arc=PI / 2))
        self.wait()

        self.play(f[44].animate.next_to(f[38], DOWN, aligned_edge=LEFT))

        self.play(FadeOut(f[21], f[39]), VGroup(f[33], f[38], f[44]).animate.shift(UP))
        self.wait()
        self.play(Write(f[45]))
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(f[33].copy(), f[38].copy(), f[44].copy(), f[45]),
                f[46],
                key_map={
                    r"A": r"37",
                    r"B": r"8",
                    r"C": r"15",
                },
            )
        )
        self.wait()
        self.play(Circumscribe(f[46][1]))
        self.wait()


class difp_11(Scene):
    def construct(self):
        f = VGroup(
            MathTex(
                r"2663x^{2}-1079x-1702 ",
                r"&= A(3x+2)(22x-23) \\",
                r"&\quad +B(x)(22x-23)\\ ",
                r"&\quad +  C(x)(3x+2)",
                font_size=40,
            ),
            MathTex(
                r"2663x^{2}",  # 0
                r"-1079x",
                r"-1702",
                r"&= ",
                r"A",
                r"(",
                r"66x^{2}  ",  # 6
                r"-25x ",
                r"-46",
                r") \\",
                r"&\quad +",
                r"B",
                r"(",
                r"22x^{2}",  # 13
                r"-23x",
                r")\\ ",
                r"&\quad +  ",
                r"C",
                r"(",
                r"3x^{2}",  # 19
                r"+2x)",
                font_size=40,
            ),
            MathTex(
                r"{{66}}{{A}} + {{22}}{{B}} + {{3}}{{C}} = {{2663}}",
                font_size=40,
            ),
            MathTex(
                r"{{-25}}{{A}} {{-23}}{{B}} + {{2}}{{C}} = {{-1079}}",
                font_size=40,
            ),
            MathTex(
                r"{{-46}}{{A}} = {{-1702}}",
                font_size=40,
            ),
            MathTex(
                r"A=37",
                font_size=40,
            ),
            MathTex(
                r"B=8",
                font_size=40,
            ),
            MathTex(
                r"C=15",
                font_size=40,
            ),
            MathTex(
                r"\frac{2663x^{2}-1079x-1702}{(x)(3x+2)(22x-23)} = \frac{A}{x}+\frac{B}{3x+2}+\frac{C}{22x-23}",
                font_size=40,
            ),
            MathTex(
                r"\frac{2663x^{2}-1079x-1702}{(x)(3x+2)(22x-23)} = ",
                r"\frac{37}{x}+\frac{8}{3x+2}+\frac{15}{22x-23}",
                font_size=40,
            ),
        )
        self.play(FadeIn(f[0].shift(UP * 2.5)))
        self.wait()
        self.play(Circumscribe(f[0][1]))
        self.wait()
        self.play(Circumscribe(f[0][2]))
        self.wait()
        self.play(Circumscribe(f[0][3]))
        self.wait()
        self.play(
            TransformMatchingTex(
                f[0],
                f[1].move_to(f[0]),
                key_map={
                    r"(3x+2)(22x-23)": r"66x^{2}-25x-46",
                    r"(x)(22x-23)": r"22x^{2}-23x",
                    r"(x)(3x+2)": r"3x^{2}+2x",
                },
            )
        )
        self.wait()
        self.play(Circumscribe(f[1][0]))
        self.wait()
        self.play(Circumscribe(f[1][6]), Circumscribe(f[1][4]))
        self.wait()
        self.play(Circumscribe(f[1][13]), Circumscribe(f[1][11]))
        self.wait()
        self.play(Circumscribe(f[1][19]), Circumscribe(f[1][17]))
        self.wait()
        v0 = VGroup(f[2], f[3], f[4]).arrange(DOWN, aligned_edge=LEFT)
        self.play(
            TransformMatchingTex(
                f[1].copy(),
                f[2],
                key_map={
                    r"66x^{2}": "66A",
                    r"-22x^{2}": "22B",
                    r"3x^{2}": "3C",
                    r"2663x^{2}": "2663",
                },
            )
        )
        self.wait()
        self.play(Circumscribe(f[1][1]))
        self.wait()
        self.play(Circumscribe(f[1][7]), Circumscribe(f[1][4]))
        self.wait()
        self.play(Circumscribe(f[1][14]), Circumscribe(f[1][11]))
        self.wait()
        self.play(Circumscribe(f[1][20]), Circumscribe(f[1][17]))
        self.wait()
        self.play(
            TransformMatchingTex(
                f[1].copy(),
                f[3],
                key_map={
                    r"-25x": "-25A",
                    r"-23x": "-23B",
                    r"2x": "2C",
                    r"-1079x": "-1079",
                },
            )
        )
        self.wait()
        self.play(Circumscribe(f[1][2]))
        self.wait()
        self.play(Circumscribe(f[1][8]), Circumscribe(f[1][4]))
        self.wait()
        self.play(
            TransformMatchingTex(
                f[1].copy(),
                f[4],
                key_map={
                    r"-46": "-46A",
                    r"-1702": "-1702",
                },
            )
        )
        self.wait()
        v1 = VGroup(f[5], f[6], f[7]).arrange(buff=2).next_to(v0, DOWN)
        self.play(TransformFromCopy(v0, v1), FadeOut(f[1]))
        self.wait()
        self.play(FadeIn(f[8].move_to(f[1])))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(v1.copy(), f[8]), f[9].move_to(f[8])))
        self.wait()


class difp_20(Scene):
    def construct(self):
        f = VGroup(
            MathTex(
                r"\frac{64x^{2}+64x+18}{ {{512x^{3}+576x^{3}+216x+27} }}", font_size=40
            ),
            MathTex(r"x=-\frac{3}{8}", font_size=40),
            MathTex(r"8x=-3", font_size=40),
            MathTex(r"8x+3=0", font_size=40),
            # 4
            MathTex(r"(8x+3)=0", font_size=40),
            MathTex(r"{{(8x+3)^{3}}}=0", font_size=40),
            MathTex(r"\frac{64x^{2}+64x+18}{(8x+3)^{3}}", font_size=40),
            MathTex(
                r"\frac{64x^{2}+64x+18}{(8x+3)^{3}} = \frac{A}{8x+3} + \frac{B}{(8x+3)^{2}}+\frac{C}{(8x+3)^{3}}",
                font_size=40,
            ),
            # 8
            MathTex(
                r"64x^{2}+64x+18= \left( \frac{A}{8x+3} + \frac{B}{(8x+3)^{2}}+\frac{C}{(8x+3)^{3}} \right)(8x+3)^{3}",
                font_size=40,
            ),
            MathTex(r"64x^{2}+64x+18=  A(8x+3)^{2} + B(8x+3)+C ", font_size=40),
            MathTex(
                r"64 {{\left( -\frac{3}{8} \right)}} ^{2}+64{{\left( -\frac{3}{8} \right)}}+18",
                r"&=  A {{\left(8\left( -\frac{3}{8} \right)}}+3 \right)^{2}",
                r"+B {{\left(8\left( -\frac{3}{8} \right)}}+3  \right) \\ ",
                r"&+C ",
                font_size=40,
            ),
            MathTex(
                r"C=3",
                font_size=40,
            ),
            # 12
            MathTex(
                r"64x^{2}",
                r"+64x",
                r"+18 ",
                r"&=  ",
                r"A",
                r"(",
                r"64x^{2}",
                r"+48x",
                r"+9)\\ ",
                r"&+ ",
                r"B",
                r"(",
                r"8x",
                r"+3",
                r")\\ ",
                r"&+",
                r"C ",
                font_size=40,
            ),
            MathTex(
                r"64 = 64A",
                font_size=40,
            ),
            MathTex(
                r"64=  48A+8B",
                font_size=40,
            ),
            MathTex(
                r"18 = 9A+3B+C",
                font_size=40,
            ),
            # 16
            MathTex(
                r"A= 1",
                font_size=40,
            ),
            MathTex(
                r"B=2",
                font_size=40,
            ),
            MathTex(
                r"C=3",
                font_size=40,
            ),
            MathTex(
                r"\frac{64x^{2}+64x+18}{(8x+3)^{3}}",
                r"= \frac{1}{8x+3} + \frac{2}{(8x+3)^{2}}+\frac{3}{(8x+3)^{3}}",
                font_size=40,
            ),
        )
        self.play(FadeIn(f[0]))
        self.wait()
        self.play(f[0].animate.shift(UP * 2.5))
        self.wait()
        self.play(f[1].move_to(f[0]).animate.move_to(ORIGIN))
        self.wait()
        f1 = f[1].copy()
        self.play(f1.animate.next_to(f[1], DOWN))
        self.wait()
        self.play(TransformMatchingShapes(f1, f[2].move_to(f1), path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[2], f[3].move_to(f[2]), path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[3], f[4].move_to(f[3]), path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[4], f[5].move_to(f[4]), path_arc=PI / 2))
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(f[5], f[0]),
                f[6].move_to(f[0]),
                key_map={r"512x^{3}+576x^{3}+216x+27": r"(8x+3)^{3}"},
            )
        )
        self.wait()
        self.play(f[1].animate.next_to(f[6], LEFT, buff=2))
        self.wait()
        self.play(TransformFromCopy(f[6], f[7]))
        self.wait()
        self.play(TransformMatchingShapes(f[7], f[8], path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[8], f[9], path_arc=PI / 2))
        self.wait()
        self.play(
            f[9].animate.move_to(f[6]),
            FadeOut(f[6]),
            f[1].animate.shift(LEFT * 2),
        )
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(f[9], f[1]).copy(),
                f[10],
                key_map={r"x=-\frac{3}{8}": r"\left(8\left( -\frac{3}{8} \right)"},
            )
        )
        self.wait()

        self.play(TransformMatchingShapes(f[10], f[11]))
        self.wait()
        self.play(f[11].animate.next_to(f[1], DOWN, aligned_edge=LEFT))
        self.wait()
        self.play(TransformMatchingShapes(f[9], f[12].move_to(f[9])))
        self.wait()
        v0 = VGroup(f[13], f[14], f[15]).arrange(DOWN, aligned_edge=LEFT)

        self.play(Circumscribe(f[12][0]))
        self.wait()
        self.play(Circumscribe(f[12][4]), Circumscribe(f[12][6]))
        self.wait()
        self.play(TransformFromCopy(VGroup(f[12][0], f[12][6]), f[13]))
        self.wait()

        self.play(Circumscribe(f[12][1]))
        self.wait()
        self.play(Circumscribe(f[12][4]), Circumscribe(f[12][7]))
        self.wait()
        self.play(Circumscribe(f[12][10]), Circumscribe(f[12][12]))
        self.wait()
        self.play(TransformFromCopy(VGroup(f[12][1], f[12][7], f[12][12]), f[14]))
        self.wait()
        self.play(Circumscribe(f[12][2]))
        self.wait()
        self.play(Circumscribe(f[12][4]), Circumscribe(f[12][8]))
        self.wait()
        self.wait()
        self.play(Circumscribe(f[12][10]), Circumscribe(f[12][13]))
        self.wait()
        self.play(Circumscribe(f[12][16]))
        self.wait()
        self.play(
            TransformFromCopy(VGroup(f[12][2], f[12][8], f[12][13], f[12][16]), f[15])
        )
        self.wait()
        v1 = VGroup(f[16], f[17], f[18]).arrange(buff=2).next_to(f[15], DOWN, buff=2)
        self.play(
            TransformFromCopy(v0, v1), f[11].animate.move_to(f[18]), FadeOut(f[11])
        )
        self.wait()
        self.play(FadeOut(f[1], v0))
        self.wait()
        self.play(f[12].animate.move_to(ORIGIN))
        self.wait()
        self.play(TransformMatchingShapes(f[12], f[7].move_to(ORIGIN)))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(f[7], v1), f[19]))
        self.wait()
        self.play(Circumscribe(f[19][1]))
        self.wait()


class difp_30(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"\frac{x^{3}+25x^{2}-x+18}{3x^{4}+5x^{2}+2}", font_size=40),
            MathTex(r"3x^{4}+5x^{2}+2=0", font_size=40),
            MathTex(r"u = x^{2}", font_size=40),
            MathTex(r"{{3}}u^{2}+{{5}}u+{{2}}=0", font_size=40),
            # 4
            MathTex(
                r"u = \frac{-(5) \pm \sqrt{ (5)^{2}-4(3)(2) }}{2(3)}", font_size=40
            ),
            MathTex(r"u = -1", font_size=40),
            MathTex(r"u+1 =0", font_size=40),
            MathTex(r"(u+1) =0", font_size=40),
            # 8
            MathTex(r"u = -\frac{2}{3} ", font_size=40),
            MathTex(r"3u = -2 ", font_size=40),
            MathTex(r"3u+2 = 0 ", font_size=40),
            MathTex(r"(3u+2) = 0 ", font_size=40),
            # 12
            MathTex(r"(x^{2}+1)=0", font_size=40),
            MathTex(r"(3x^{2}+2)=0", font_size=40),
            MathTex(
                r"\frac{x^{3}+25x^{2}-x+18}{(3x^{2}+2)(x^{2}+1)} ",
                r"=",
                r"\frac{Ax+B}{3x^{2}+2}",
                r"+",
                r"\frac{Cx+D}{x^{2}+1}",
                font_size=40,
            ),
            MathTex(
                r"x^{3}+25x^{2}-x+18 = \left( \frac{Ax+B}{3x^{2}+2}+\frac{Cx+D}{x^{2}+1} \right)(3x^{2}+2)(x^{2}+1)",
                font_size=40,
            ),
            # 16
            MathTex(
                r"x^{3}+25x^{2}-x+18=(Ax+B)(x^{2}+1)+(Cx+D)(3x^{2}+2)", font_size=40
            ),
            MathTex(
                r"1x^{3}",
                r"+25x^{2}",
                r"-x",
                r"+18",
                r"&=",
                # 5
                r"A",
                r"(",
                # 7
                r"x^{3}",
                r"+x",
                r")",
                r"+",
                # 11
                r"B",
                "(",
                r"x^{2}",
                r"+1",
                r") \\",
                r"&+",
                # 17
                r"C",
                r"(",
                r"3x^{3}",
                r"+2x",
                r")",
                r"+",
                # 23
                r"D",
                r"(",
                r"3x^{2}",
                r"+2",
                r")",
                font_size=40,
            ),
            MathTex(r"1 = A+3C", font_size=40),
            MathTex(r"25 = B+3D", font_size=40),
            # 20
            MathTex(r"-1 = A+2C", font_size=40),
            MathTex(r"18 = B+2D", font_size=40),
            MathTex(r"A=-5 ", font_size=40),
            MathTex(r"B = 4", font_size=40),
            # 24
            MathTex(r"C=2 ", font_size=40),
            MathTex(r"D=7", font_size=40),
            MathTex(
                r"\frac{x^{3}+25x^{2}-x+18}{(3x^{2}+2)(x^{2}+1)} ",
                r"= \frac{-5x+4}{3x^{2}+1}+\frac{2x+7}{x^{2}+1}",
                font_size=40,
            ),
        )

        self.play(Write(f[0]), run_time=0.7)
        self.wait()
        self.play(f[0].animate.shift(UP * 3))
        self.wait()
        self.play(TransformFromCopy(f[0], f[1]))
        self.wait()
        self.play(f[2].animate.next_to(f[1], RIGHT, buff=2))
        self.wait()
        self.play(f[3].animate.next_to(f[1], DOWN))
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(f[2].copy(), f[3].copy()), f[4].next_to(f[3], DOWN)
            )
        )
        self.wait()
        v0 = VGroup(f[5], f[8]).arrange(buff=2).move_to(f[4])
        self.play(v0.animate.next_to(f[4], DOWN))
        self.wait()

        self.play(TransformMatchingShapes(f[5], f[6].move_to(f[5]), path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[6], f[7].move_to(f[6]), path_arc=PI / 2))
        self.wait()

        self.play(TransformMatchingShapes(f[8], f[9].move_to(f[8]), path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[9], f[10].move_to(f[9]), path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[10], f[11].move_to(f[10]), path_arc=PI / 2))
        self.wait()

        self.play(
            TransformMatchingShapes(
                VGroup(f[2].copy(), f[7]), f[12].move_to(f[7]), key_map={r"u": "x^{2}"}
            )
        )
        self.wait()

        self.play(
            TransformMatchingShapes(
                VGroup(f[2].copy(), f[11]),
                f[13].move_to(f[11]),
                key_map={r"u": "x^{2}"},
            )
        )
        self.wait()
        self.play(FadeOut(f[2], f[4], f[1], f[3]))
        self.wait()
        f[14].move_to(f[0])
        self.play(
            TransformMatchingShapes(
                VGroup(f[0], f[12], f[13]),
                f[14][0],
            )
        )
        self.wait()
        self.play(Write(f[14][1:3]), run_time=0.7)
        self.wait()
        self.play(Write(f[14][3:5]), run_time=0.7)
        self.wait()
        v1 = f[14].copy()
        self.play(v1.animate.move_to(ORIGIN))
        self.wait()
        self.play(TransformMatchingShapes(v1, f[15], path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[15], f[16], path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[16], f[17], path_arc=PI / 2))
        self.wait()
        self.play(f[17].animate.move_to(f[14]), FadeOut(f[14]))
        self.wait()

        v2 = VGroup(f[18], f[19], f[20], f[21]).arrange(DOWN, aligned_edge=LEFT)

        self.play(Circumscribe(f[17][0]))
        self.wait()
        self.play(Circumscribe(f[17][5]), Circumscribe(f[17][7]))
        self.wait()
        self.play(Circumscribe(f[17][17]), Circumscribe(f[17][19]))
        self.wait()
        self.play(TransformFromCopy(VGroup(f[17][0], f[17][7], f[17][20]), f[18]))
        self.wait()

        self.play(Circumscribe(f[17][1]))
        self.wait()
        self.play(Circumscribe(f[17][11]), Circumscribe(f[17][13]))
        self.wait()
        self.play(Circumscribe(f[17][23]), Circumscribe(f[17][25]))
        self.wait()

        self.play(TransformFromCopy(VGroup(f[17][1], f[17][13], f[17][25]), f[19]))
        self.wait()

        self.play(Circumscribe(f[17][2]))
        self.wait()
        self.play(Circumscribe(f[17][5]), Circumscribe(f[17][8]))
        self.wait()
        self.play(Circumscribe(f[17][17]), Circumscribe(f[17][20]))
        self.wait()

        self.play(TransformFromCopy(VGroup(f[17][2], f[17][11], f[17][20]), f[20]))
        self.wait()

        self.play(Circumscribe(f[17][3]))
        self.wait()
        self.play(Circumscribe(f[17][11]), Circumscribe(f[17][14]))
        self.wait()
        self.play(Circumscribe(f[17][23]), Circumscribe(f[17][26]))
        self.wait()

        self.play(TransformFromCopy(VGroup(f[17][3], f[17][14], f[17][26]), f[21]))
        self.wait()
        v3 = VGroup(f[22], f[23], f[24], f[25]).arrange(buff=1)
        self.wait()
        self.play(TransformFromCopy(v2, v3.next_to(v2, DOWN)))
        self.wait()
        self.play(FadeOut(v2, f[17]))
        self.wait()
        self.play(FadeIn(f[14].move_to(ORIGIN)))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(f[14], v3), f[26]))
        self.wait()
        self.play(Circumscribe(f[26][1]))
        self.wait()


class difp_40(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"\frac{18x^{2}+54x-4}{4x^{4}+20x^{2}+25}", font_size=40),
            MathTex(r"4x^{4}+20x^{2}+25=0", font_size=40),
            MathTex(r"u = x^{2}", font_size=40),
            MathTex(r"{{4}}u^{2}+{{20}}u+{{25}}=0", font_size=40),
            # 4
            MathTex(
                r"u = \frac{-(20) \pm \sqrt{ (-20)^{2}-4(4)(25) }}{2(4)}", font_size=40
            ),
            MathTex(r"u=-\frac{5}{2}", font_size=40),
            MathTex(r"2u=5", font_size=40),
            MathTex(r"2u-5=0", font_size=40),
            # 8
            MathTex(r"(2u-5)=0", font_size=40),
            MathTex(r"u=-\frac{5}{2}", font_size=40),
            MathTex(r"(2u-5)=0", font_size=40),
            MathTex(r"(2x^{2}+5)=0", font_size=40),
            # 12
            MathTex(r"(2x^{2}+5)=0", font_size=40),
            MathTex(r"(2x^{2}+5)^2=0", font_size=40),
            MathTex(
                r"\frac{18x^{2}+54x-4}{(2x^{2}+5)^{2}}",
                r"=",
                r"\frac{Ax+B}{2x^{2}+5} ",
                r"+ \frac{Cx+D}{(2x^{2}+5)^{2}}",
                font_size=40,
            ),
            MathTex(
                r"18x^{2}+54x-4 = \left( \frac{Ax+B}{2x^{2}+5}+ \frac{Cx+D}{(2x^{2}+5)^{2}} \right)(2x^{2}+5)^{2}",
                font_size=40,
            ),
            # 16
            MathTex(r"18x^{2}+54x-4 = (Ax+B)(2x^{2}+5)+(Cx+D)", font_size=40),
            MathTex(
                r"18x^{2}",
                r"+54x",
                "-4 ",
                r"= ",
                # 4
                r"A",
                r"(",
                r"2x^{3}",
                r"+5x",
                r")+",
                # 9
                r"B",
                r"(",
                r"2x^{2}",
                r"+5",
                r")+",
                # 14
                r"Cx",
                r"+D",
                font_size=40,
            ),
            MathTex(r"0 = 2A", font_size=40),
            MathTex(r"18 = 2B", font_size=40),
            # 20
            MathTex(r"54=5A+C", font_size=40),
            MathTex(r"-4 = 5B+D", font_size=40),
            MathTex(r"A=0 ", font_size=40),
            MathTex(r"B=9", font_size=40),
            # 24
            MathTex(r"C=54", font_size=40),
            MathTex(r"D=-49", font_size=40),
            MathTex(
                r"\frac{18x^{2}+54x-4}{(2x^{2}+5)^{2}} ",
                r"= \frac{0x+9}{2x^{2}+5}+ \frac{54x-49}{(2x^{2}+5)^{2}}",
                font_size=40,
            ),
            MathTex(
                r"\frac{18x^{2}+54x-4}{(2x^{2}+5)^{2}}",
                r"= \frac{9}{2x^{2}+5}+ \frac{54x-49}{(2x^{2}+5)^{2}}",
                font_size=40,
            ),
        )

        self.play(Write(f[0]), run_time=0.7)
        self.wait()
        self.play(f[0].animate.shift(UP * 3))
        self.wait()
        self.play(TransformFromCopy(f[0], f[1]))
        self.wait()
        self.play(f[2].animate.next_to(f[1], RIGHT, buff=2))
        self.wait()
        self.play(f[3].animate.next_to(f[1], DOWN))
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(f[2].copy(), f[3].copy()), f[4].next_to(f[3], DOWN)
            )
        )
        self.wait()
        v0 = VGroup(f[5], f[9]).arrange(buff=2).move_to(f[4])
        self.wait()
        self.play(v0.animate.next_to(f[4], DOWN))
        self.wait()

        self.play(TransformMatchingShapes(f[5], f[6].move_to(f[5]), path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[6], f[7].move_to(f[6]), path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[7], f[8].move_to(f[7]), path_arc=PI / 2))
        self.wait()

        self.play(TransformMatchingShapes(f[9], f[10].move_to(f[9]), path_arc=PI / 2))
        self.wait()

        self.play(
            TransformMatchingShapes(
                VGroup(f[2].copy(), f[8]), f[11].move_to(f[8]), key_map={r"u": "x^{2}"}
            )
        )
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(f[2].copy(), f[10]),
                f[12].move_to(f[10]),
                key_map={r"u": "x^{2}"},
            )
        )
        self.wait()

        self.play(
            TransformMatchingShapes(
                VGroup(f[11], f[12]), f[13].move_to(v0.get_center())
            )
        )
        self.wait()
        self.play(FadeOut(f[2], f[4], f[1], f[3]))
        self.wait()
        f[14].move_to(f[0])
        self.play(TransformMatchingShapes(VGroup(f[0], f[13]), f[14][0]))
        self.wait()
        self.play(Write(f[14][1:3]), run_time=0.7)
        self.wait()
        self.play(Write(f[14][3:4]), run_time=0.7)
        self.wait()

        v1 = f[14].copy()
        self.play(v1.animate.move_to(ORIGIN))
        self.wait()
        self.play(TransformMatchingShapes(v1, f[15], path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[15], f[16], path_arc=PI / 2))
        self.wait()
        self.play(TransformMatchingShapes(f[16], f[17], path_arc=PI / 2))
        self.wait()
        self.play(f[17].animate.move_to(f[14]), FadeOut(f[14]))
        self.wait()

        v2 = VGroup(f[18], f[19], f[20], f[21]).arrange(DOWN, aligned_edge=LEFT)

        self.play(Circumscribe(*VGroup(f[17][0:3])))
        self.wait()
        self.play(Circumscribe(f[17][4]), Circumscribe(f[17][6]))
        self.wait()
        self.play(TransformFromCopy(f[17][6], f[18]))
        self.wait()

        self.play(Circumscribe(f[17][0]))
        self.wait()
        self.play(Circumscribe(f[17][9]), Circumscribe(f[17][11]))
        self.wait()
        self.play(TransformFromCopy(VGroup(f[17][0], f[17][11]), f[19]))
        self.wait()

        self.play(Circumscribe(f[17][1]))
        self.wait()
        self.play(Circumscribe(f[17][4]), Circumscribe(f[17][7]))
        self.wait()
        self.play(Circumscribe(f[17][14]))
        self.wait()
        self.play(TransformFromCopy(VGroup(f[17][1], f[17][7], f[17][14]), f[20]))
        self.wait()

        self.play(Circumscribe(f[17][2]))
        self.wait()
        self.play(Circumscribe(f[17][9]), Circumscribe(f[17][12]))
        self.wait()
        self.play(Circumscribe(f[17][15]))
        self.wait()
        self.play(TransformFromCopy(VGroup(f[17][2], f[17][12], f[17][15]), f[21]))
        self.wait()

        v3 = VGroup(f[22], f[23], f[24], f[25]).arrange(buff=1)
        self.play(TransformFromCopy(v2, v3.next_to(v2, DOWN)))
        self.wait()
        self.play(FadeOut(v2, f[17]))
        self.wait()
        self.play(FadeIn(f[14].move_to(ORIGIN)))
        self.wait()

        self.play(TransformMatchingShapes(VGroup(f[14], v3), f[26]))
        self.wait()
        self.play(TransformMatchingShapes(f[26], f[27]))
        self.wait()
        self.play(Circumscribe(f[27][1]))
        self.wait()
        # que cosas, la animacion casi que fue la misma que difp_30 :D


class difp_50(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"\frac{3x^{2}+x+15}{x^{3}+3x^{2}+4x+12}"),
            MathTex(r"x^{3}+3x^{2}+4x+12=0"),
            MathTex(r"x^{2}(x+3) + 4x+12=0"),
            MathTex(r"x^{2}(x+3)+4(x+3)=0"),
            MathTex(r"(x^{2}+4)(x+3)=0"),
            MathTex(
                r"\frac{3x^{2}+x+15}{(x^{2}+4)(x+3)}",
                r"= \frac{Ax+B}{x^{2}+4}",
                r"+\frac{C}{x+3}",
            ),
            MathTex(r"A=0"),
            MathTex(r"B=1"),
            MathTex(r"C=3"),
            MathTex(
                r"\frac{3x^{2}+x+15}{(x^{2}+4)(x+3)}",
                r"=\frac{1}{x^{2}+4}+\frac{3}{x+3}",
            ),
        )

        self.play(Write(f[0]), run_time=0.7)
        self.wait()
        self.play(f[1].animate.next_to(f[0], DOWN, buff=1.5))
        self.wait()
        self.play(TransformMatchingShapes(f[1], f[2].move_to(f[1])))
        self.wait()
        self.play(TransformMatchingShapes(f[2], f[3].move_to(f[1])))
        self.wait()
        self.play(TransformMatchingShapes(f[3], f[4].move_to(f[1])))
        self.wait()

        self.play(TransformMatchingShapes(Group(f[0], f[4]), f[5][0].move_to(ORIGIN)))
        self.wait()
        self.play(f[5][0].animate.next_to(f[5][1], LEFT))
        self.wait()
        self.play(Write(f[5][1]), run_time=0.7)
        self.wait()
        self.play(Write(f[5][2]), run_time=0.7)
        self.wait()

        v0 = VGroup(f[6], f[7], f[8]).arrange(buff=2)
        self.wait()
        self.play(v0.animate.next_to(f[5], DOWN, buff=1.5))
        self.wait()
        self.play(TransformMatchingShapes(Group(f[5], v0), f[9]))
        self.wait()
        self.play(Circumscribe(f[9][1]))
        self.wait()
