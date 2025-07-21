from manim import *
import numpy as np


class fcc_00(Scene):
    def construct(self):
        img = ImageMobject("img/udb_logo_high.png")
        t1 = Text(r"Trinomios")
        t2 = Text(r"Fórmula cuadrática", font_size=32) 
        t3 = MathTex("(ax^{2}+bx+c)", font_size=42)


        v = Group(img, t1, t2, t3)
        self.add(img.scale(0.25), v.arrange(DOWN))


class fcc_01(Scene):
    def construct(self):
        f = [
            MathTex(r"ax^{2}+bx+c =0"),
            MathTex(r"x=\frac{-b\pm \sqrt{ b^{2}-4ac }}{2a}"),
            MathTex(r"(x+h)(x+m)"),
        ]
        
        self.play(Write(f[0]))
        self.wait(1)
        
        self.play(Group(f[0], f[1]).animate.arrange(DOWN, buff = 1.2))

        self.wait(1)

        self.play(
            Write(f[2].next_to(f[1], DOWN))
        )


        self.wait(1)

class fcc_02(Scene):
    def construct(self):

        f = [
            MathTex(r"p^{2}+53p-420"),
            MathTex(r"1p^{2}+53p-420"),
            MathTex(r"\begin{cases} a = 1 \\ b = +53 \\ c = -420 \end{cases}"),
            MathTex(r"p=\frac{-b\pm \sqrt{ b^{2}-4ac }}{2a}"),
            
            MathTex(r"p=\frac{-(+53)\pm \sqrt{ (+53)^{2}-4(1)(-420) }}{2(1)}"),
            MathTex(r"p=\frac{-53 \pm \sqrt{ 2809+1680 }}{2}"),
            MathTex(r"p=\frac{-53 \pm \sqrt{ 4489 }}{2}"),
            MathTex(r"p=\frac{-53 \pm 67 }{2}"),


            MathTex(r"p=\begin{cases} \frac{-53+67}{2} \\ \frac{-53-67}{2} \end{cases}"),
            MathTex(r"p=\begin{cases} \frac{14}{2} \\ \frac{-120}{2}\end{cases}"),
            MathTex(r"p=\begin{cases} 7 \\ -60\end{cases}"),
            
            MathTex(r"p=7"),
            MathTex(r"p=-60"),

            MathTex(r"(p-7)(p+60)")
        ]
        
        self.play(Write(f[0]))
        self.wait(1)    
        self.play(TransformMatchingShapes(f[0], f[1]), path = PI/2)
        self.wait(1)
        self.play(f[1].animate.shift(UP), TransformMatchingShapes(f[1].copy(), f[2].shift(DOWN*1.5)))
        self.wait(1)
        self.play(f[2].animate.shift(LEFT*2), Write(f[3].shift(DOWN*1.5).shift(RIGHT*2)))
        self.wait(1)
        self.play(TransformMatchingShapes(Group(f[2], f[3]), f[4].shift(ORIGIN).shift(DOWN)))
        self.wait(1)
        self.remove(f[2])
        
        for i in range(4, 10):
            self.play(TransformMatchingShapes(f[i], f[i+1].move_to(f[i])))
            self.wait(1)

        self.play(TransformMatchingShapes(f[10], Group(f[11], f[12]).arrange(UP).move_to(f[10])))
        self.wait(1)
        self.play(TransformMatchingShapes(Group(f[11], f[12]).copy(), f[13]))

        
        self.wait(1)
        
class fcc_03(Scene):
    def construct(self):
        f = [
            MathTex(r"x=\frac{-b\pm \sqrt{ b^{2}-4ac }}{2a}"),
            MathTex(r"\sqrt{ b^{2}-4ac }"),
            MathTex(r"\sqrt{ \mathbb{R} }"),
            MathTex(r"\mathbb{R} < 0"),
            MathTex(r"\mathbb{C}"),
            MathTex(r"\mathbb{C}=u \pm vi"),
            MathTex(r"i=\sqrt{-1}"),
            
            MathTex(r"x = u\pm vi"),
            MathTex(r"(x - u - vi)(x - u + vi)"),
        ]
        
        self.play(Write(f[0]))
        self.wait(1)
        self.play(
            f[0].animate.shift(UP*2),
            TransformMatchingShapes(f[0].copy(), f[1])
        )
        self.wait(1)
        self.play(TransformMatchingShapes(f[1], f[2]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[2].copy(), f[3].shift(DOWN)))
        self.wait(1)
        self.play(TransformMatchingShapes(f[3], f[4].move_to(f[3])))
        self.wait(1)
        self.play(TransformMatchingShapes(f[4], f[5].move_to(f[4])))
        self.wait(1)
        self.play(
            TransformMatchingShapes(f[5].copy(), f[6].next_to(f[5], RIGHT*2))
        )
        self.wait(1)
        self.play(
            f[0].animate.move_to(ORIGIN),
            TransformMatchingShapes(Group(f[5], f[2]), f[7]), 
            VGroup(f[0], f[7]).animate.arrange(DOWN),
            f[6].animate.move_to(ORIGIN).shift(RIGHT*4),
            
            
        )
        self.wait(1)
        self.play(
            ReplacementTransform(f[7], f[8].next_to(f[0], DOWN*1.5)), 
        )
        self.wait(1)
        
class fcc_04(Scene):
    def construct(self):
        f = [
            
            MathTex(r"9x{2}+12x+5"),
            MathTex(r"x=\frac{-b\pm \sqrt{ b^{2}-4ac }}{2a}"),
            MathTex(r"\begin{cases} a = 9 \\ b = 12 \\ c = 5 \end{cases}"),
            MathTex(r"x=\frac{-(12)\pm \sqrt{ (12)^{2}-4(9)(5) }}{2(9)}"),
            
            MathTex(r"x=\frac{-(12)\pm \sqrt{ (12)^{2}-4(9)(5) }}{2(9)}"),
            MathTex(r"x=\frac{-12\pm \sqrt{ 144-180 }}{18}"),
            MathTex(r"x=\frac{-12\pm \sqrt{ -36 }}{18}"),
            MathTex(r"x=\frac{-12\pm \sqrt{ 36 }\sqrt{ -1 }}{18}"),
            MathTex(r"x=\frac{-12\pm 6i}{18}"),
            MathTex(r"x=-\frac{12}{18}\pm \frac{6i}{18}"),
            MathTex(r"x=-\frac{2}{3}\pm \frac{1}{3}"),
            MathTex(r"x=\frac{-2\pm 1i}{3} "),
            MathTex(r"3x=-2\pm i"),
            MathTex(r"3x +2 \mp i = 0"),
            MathTex(r"(3x +2 - i)(3x +2 + i) = 0"),
        ]
        
        self.play(
            Write(f[0])
        )
        
        self.play(
            f[0].animate.shift(UP),
            TransformMatchingShapes(f[0].copy(), f[1].shift(RIGHT*2)),
            TransformMatchingShapes(f[0].copy(), f[2].shift(LEFT*2)),
        )
        self.wait(1)