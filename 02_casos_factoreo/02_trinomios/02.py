from manim import *
import sys, os, math

class ddp_00(Scene):
    def construct(self):
        img = ImageMobject('img/udb_logo_high.png')
        t1 = Text(r"Trinomios")
        t2 = Text("(diferencia de cuadrados perfectos)", font_size=38)
        t3 = Text("Caso de factoreo 4", font_size=32)
        v = Group(img, t1, t2, t3)
        self.add(img.scale(0.25), v.arrange(DOWN)) 

# Objetivo del metodo
class ddp_01(Scene):
    def construct(self):
        f = [
            MathTex(r"x^{2}-y^{2} "),
            MathTex(r"(x+y)(x-y)"),
            MathTex(r"x\cdot x + x\cdot y - y\cdot x + y\cdot y"),
            MathTex(r"x^{2}+xy-xy+y^{2}"),
            MathTex(r"x^{2}+y^{2}"),            
        ]

        self.play(Write(f[0].shift(UP)))
        self.wait(2)
        self.play(
            # f[0].animate.shift(UP),
            TransformMatchingShapes(f[0].copy(), f[1]),
            )
        self.wait(2)
        pass