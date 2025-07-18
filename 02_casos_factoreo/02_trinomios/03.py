from manim import *
import sys, os, math
import numpy as np


class ebc_00(Scene):
    def construct(self):
        img = ImageMobject("img/udb_logo_high.png")
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
        self.play(f[0].animate.shift(UP), TransformMatchingShapes(f[0].copy(), f[1]))
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
        self.play(TransformMatchingShapes(f[1].copy(), f[3].next_to(f[2], DOWN * 2)))
        self.play(f[3].animate.shift(LEFT * 2))
        self.play(f[4].animate.next_to(f[3], RIGHT * 2))
        self.wait(2)
        self.remove(f[4])
        self.add(f[5].next_to(f[3], RIGHT * 2))
        self.wait(2)
        self.remove(f[5])
        self.add(f[6].next_to(f[3], RIGHT * 2))
        self.wait(2)
        self.remove(f[6])
        self.add(f[7].next_to(f[3], RIGHT * 2))
        self.wait(2)


class ebc_03(Scene):
    def construct(self):
        f = [
            MathTex(r"j^{2}-32j+240"),
            MathTex(r"\begin{cases}h+m=32 \\ hm= 240 \end{cases}"),
            
            MathTex(r"2^{4}= 16"),
            MathTex(r"3\cdot 5 = 15"),
            MathTex(r"\begin{cases} 16+15 = 31 \\ 16 \cdot 15 = 240 \end{cases}"),
            
            
            MathTex(r"2 \cdot 5  = 10"),
            MathTex(r"2^{3} \cdot 3 = 24 "),
            MathTex(r"\begin{cases}10 + 24=34 \\ 10 \cdot 24 = 240 \end{cases}"),
            
            
            MathTex(r"2^{2} \cdot 3  = 12"),
            MathTex(r"2^{2} \cdot 5 = 20 "),
            MathTex(r"\begin{cases} 12 + 20 = 32 \\ 12 \cdot 20 = 240 \end{cases}"),
            
            MathTex(r"\begin{cases} (-12) + (-20) = -32 \\ (-12) (-20) = 240 \end{cases}"),
            
            MathTex(r"(x+h)(x+m)"),
            MathTex(r"(x-12)(x-20)"),
            
        ]

        self.play(Write(VGroup(f[0], f[12]).arrange(DOWN).shift(UP*2)))
        self.wait(2)
        f[1].move_to(f[0])
        self.play(f[1].animate.shift(DOWN * 2.5).shift(LEFT * 2))

        f1 = [
            r"240",
            r"2",
            r"120",
            r"2",
            r"60",
            r"2",
            r"30",
            r"2",
            r"15",
            r"3",
            r"5",
            r"5",
            r"1",
        ]
        v = VGroup()
        for val in f1:
            v.add(MathTex(val))

        v.shift(DOWN * 1.5).shift(RIGHT * 2).arrange_in_grid(cols=2, wbuff=2.0)

        self.wait(1)
        l = getline(v)
        self.add(l)
        for i, val in enumerate(f1):
            self.add(v[i])
            self.wait(1)

        self.wait(1)
        
        self.play(f[1].animate.shift(DOWN*2))
        VGroup(f[2], f[3]).arrange(DOWN).shift(DOWN*0.5).shift(LEFT*2)
        self.play(
            TransformMatchingShapes(Group(v[1], v[3] , v[5] , v[7]).copy(), f[2]),
            TransformMatchingShapes(Group(v[9], v[11]).copy(), f[3])
        )
        self.wait(1)
        self.play(
            
            ReplacementTransform(
                Group(f[2], f[3]).copy(), f[4].move_to(f[1])
            ),
            TransformMatchingShapes(f[1], f[4])
        )
        
        self.wait(2)
        
        self.remove(f[2], f[3], f[4])
        self.add(f[1])
        self.wait(1)
        
        
        VGroup(f[5], f[6]).arrange(DOWN).shift(DOWN*0.5).shift(LEFT*2)
        self.play(
            TransformMatchingShapes(Group(v[1], v[11]).copy(), f[5]),
            TransformMatchingShapes(Group(v[3], v[5], v[7] , v[9]).copy(), f[6])
        )
        self.wait(1)
        
        self.play(
            
            ReplacementTransform(
                Group(f[5], f[6]).copy(), f[7].move_to(f[1])
            ),
            TransformMatchingShapes(f[1], f[7])
        )
        self.wait(2)
        
        self.remove(f[5], f[6], f[7])
        self.add(f[1])
        self.wait(1)
        
        
        VGroup(f[8], f[9]).arrange(DOWN).shift(DOWN*0.5).shift(LEFT*2)
        self.play(
            TransformMatchingShapes(Group(v[1], v[3], v[9]).copy(), f[8]),
            TransformMatchingShapes(Group(v[11], v[5], v[7]).copy(), f[9])
        )
        self.wait(1)
        
        self.play(
            
            ReplacementTransform(
                Group(f[8], f[9]).copy(), f[10].move_to(f[1])
            ),
            TransformMatchingShapes(f[1], f[10])
        )
        self.wait(2)
    
        self.play(
            ReplacementTransform(f[10], f[11].move_to(f[10])),            
        )
        
        self.wait(1)
        
        self.add(v.set_opacity(0))
        self.remove(f[8], f[9])
        self.remove(l)
        self.remove(v)
        self.play(f[11].animate.move_to(ORIGIN).shift(DOWN))
        self.wait(1)
        
        
        f[13].move_to(f[12])
        k = VGroup(f[0], f[13])
        self.play(
            TransformMatchingShapes(f[12], f[13]),
            TransformMatchingShapes(f[11], k, run_time=0.8)
            
            # f[11].animate.set_opacity(0),


        )
        self.wait(0.5)
        self.play(
            
            k.animate.move_to(ORIGIN)
            )
        
        

        
        self.wait(1)


def getline(v: VGroup):
    v1 = v[0].get_right()
    v2 = v[1].get_left()
    vf = v[len(v) - 1].get_bottom()

    x1 = (v1[0] + v2[0]) / 2
    y1 = v[0].get_top()[1]
    y2 = vf[1]
    p1 = Point(np.array([x1, y1, 0]))
    p2 = Point(np.array([x1, y2, 0]))

    return Line(p1, p2)
