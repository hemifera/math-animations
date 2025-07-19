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
            MathTex(r"p=\frac{-53 \pm 67 {2}"),


            MathTex(r"\begin{cases} \frac{-53+67}{2} \\ \frac{-53-67}{2} \end{cases}"),
            MathTex(r"\begin{cases} \frac{14}{2} \\ \frac{-120}{2}\end{cases}"),
            MathTex(r"\begin{cases} 7 \\ -60\end{cases}"),
            
            MathTex(r"p=7"),
            MathTex(r"p=-60"),

            MathTex("(p-7)(p+60)")
        ]

        

        self.wait(1)