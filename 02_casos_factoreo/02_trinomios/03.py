from manim import *
import sys, os, math

class ebc_00(Scene):
    def construct(self):
        img = ImageMobject('img/udb_logo_high.png')
        t1 = Text(r"Trinomios")
        t2 = MathTex("(x^{2}+bx+c)", font_size=42)
        # t3 = Text("Caso de factoreo 5", font_size=32)
        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN)) 


class ebc_01(Scene):
    def construct(self):
        f = [
            MathTex(r"x^{2}+bx+c"),
            MathTex(r"(x-h)(x-m)"),

        ]
        self.play(Write(f[0]))
        self.wait(2)
        self.play(
            f[0].animate.shift(UP),
            TransformMatchingShapes(f[0].copy(), f[1])
        )
        self.wait(2)


class ebc_02(Scene):
    def construct(self):
        f = [
            MathTex(r"x^{2}-x-6"),
            MathTex(r"x^{2}-1x-6"),
            MathTex(r"(x-h)(x-m)"),
            MathTex(r"\begin{cases} b=-1 \\ c=-6 \end{cases}"),
            MathTex(r"""
                    \begin{cases}
                    hm=c=-6 \\
                    h+m = b = -1
                    \end{cases}
                    """),
            MathTex(r"""
                    \begin{cases}
                    (6)(-1) = -6 \\
                    6-1=5
                    \end{cases}
                    """),
            MathTex(r"""
                    \begin{cases}
                    (3)(-2)=-6 \\
                    3-2=1
                    \end{cases}"""),
            MathTex(r"""
                    \begin{cases}
                    (-3)(2)=-6 \\
                    -3+2=-1
                    \end{cases}
                    """),
        ]
        self.play(Write(f[0].shift(UP)))
        self.wait(2)
        self.play(TransformMatchingShapes(f[0], f[1].shift(UP)))
        self.wait(2)
        self.play(Write(f[2].next_to(f[1], DOWN)))
        self.play(TransformMatchingShapes(f[1].copy(), f[3].next_to(f[2], DOWN*2)))
        self.play(f[3].animate.shift(LEFT*2))
        self.play(f[4].animate.next_to(f[3], RIGHT*2))
        self.wait(2)
        self.remove(f[4])
        self.add(f[5].next_to(f[3], RIGHT*2))
        self.wait(2)
        self.remove(f[5])
        self.add(f[6].next_to(f[3], RIGHT*2))
        self.wait(2)
        self.remove(f[6])
        self.add(f[7].next_to(f[3], RIGHT*2))
        self.wait(2)
