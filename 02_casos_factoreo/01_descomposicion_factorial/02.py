from manim import *
import sys, os, math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from helpers import quickFormulas, quickWriteFormulas


# Imagen de introduccion
class fcat_00(Scene):
    def construct(self):
        img = ImageMobject('img/udb_logo_high.png')
        t1 = Text(r"Descomposición factorial")
        t2 = Text("(agrupación de términos)")
        t3 = Text("Caso de factoreo 2", font_size=32)
        v = Group(img, t1, t2, t3)
        self.add(img.scale(0.25), v.arrange(DOWN)) 


# Objetivo del metodo
class fcat_01(Scene):
    def construct(self):
        f1 = MathTex(r"12ab+7bc+12a^{2}+19ac+7c^{2}")
        f2 = MathTex(r"(a+b+c)(12a+7c)")
        self.play(Write(f1.shift(UP)))
        self.wait(2)
        self.play(
            TransformMatchingShapes(f1.copy(), f2, )
        )
        self.wait(2)

# Recordatorio para el método 
class fcat_02(Scene):
    def construct(self):
        f1 = MathTex(r"m^{a}\cdot m^{b}=m^{a+b}")
        self.play(Write(f1))
        self.wait(3)

        self.clear()
        f2 = [
            MathTex(r"m^{5}"),
            MathTex(r"m^{3}\cdot m^{2}"),
            MathTex(r"m^{3+2}"),
            MathTex(r"m^{5}"),
        ]
        fx = f2[0]
        self.play(Write(fx))
        self.wait(3)
        for f in f2[0:]:
            self.play(
                TransformMatchingShapes(fx, f, path_along_arc=PI/2)
            )
            fx = f
            self.wait(3)        

# Primer ejemplo
class fcat_03(Scene):
    def construct(self):
        f = [
            MathTex(r"jk-j+k^{2}-k"),
            MathTex(r"j(k-1)+k(k-1)"),
            MathTex(r"p=k-1"),
            MathTex(r"jp +kp"),
            MathTex(r"p(j+k)"),
            MathTex(r"(k-1)(j+k)"),
        ]

        self.play(Write(f[0]))
        self.wait(2)
        self.play(f[0].animate.shift(UP), 
                  TransformMatchingShapes(f[0].copy(), f[1]))
        self.wait(2)
        self.play(Write(f[2].shift(DOWN*3).shift(RIGHT*3)))
        self.wait(2)
        
        self.play(
            FadeOut(f[0]),
            f[1].animate.shift(UP), 
            TransformMatchingShapes(f[2].copy(), f[3])
        )
        self.wait(2)
        self.play(
            FadeOut(f[1]),
            f[3].animate.shift(UP), 
            TransformMatchingShapes(f[3].copy(), f[4])
        )
        self.wait(2)
        self.play(
            FadeOut(f[3]),
            f[4].animate.shift(UP), 
            TransformMatchingShapes(f[4].copy(), f[5])
            
        )
        self.wait(2)

# Segundo ejemplo
class fcat_04(Scene):
    def construct(self):
        f = [
            MathTex(r"l^{3}+l^{2}+l+1"),
            MathTex(r"(l^{3}+l^{2})+(l+1)"),
            MathTex(r"l^{2}(l+1)+(l+1)"),
            MathTex(r"l^{2}(l+1)+1(l+1)"),
            MathTex(r"(l^{2}+1)(l+1)"),
        ]

        self.play(Write(f[0]))
        self.wait(2)
        self.play(f[0].animate.shift(UP), 
                  TransformMatchingShapes(f[0].copy(), f[1]))
        self.wait(2)

        self.play(
            FadeOut(f[0]),
            f[1].animate.shift(UP), 
            TransformMatchingShapes(f[1].copy(), f[2]))
        self.wait(2)

        self.play(
            FadeOut(f[1]),
            # f[2].animate.shift(UP), 
                  TransformMatchingShapes(f[2], f[3]))
        self.wait(2)

        self.play(
            FadeOut(f[2]),
            f[3].animate.shift(UP), 
                  TransformMatchingShapes(f[3].copy(), f[4]))
        self.wait(2)


class fcat_05(Scene):
    def construct(self):
        f = [
            MathTex(r"140mp-270gn^{2}-180gm+210n^{2}p"),
            MathTex(r"(140mp-180gm)+(210n^{2}p-270gn^{2})"),
            MathTex(r"m(140p-180g)+n^{2}(210p-270g)"),
            MathTex(r"10m(14p-18g)+10n^{2}(21p-27g)"),
            MathTex(r"2\cdot 10m(7p-9g)+3 \cdot 10 n^{2}(7p-9g)"),
            MathTex(r"20m(7p-9g)+30n^{2}(7p-9g) "),
            MathTex(r"(7p-9g)(20m+30n^{2})"),
        ]

        self.play(Write(f[0]))
        self.wait(2)
        self.play(f[0].animate.shift(UP), 
                  TransformMatchingShapes(f[0].copy(), f[1]))
        self.wait(2)

        self.play(
            FadeOut(f[0]),
            f[1].animate.shift(UP), 
            TransformMatchingShapes(f[1].copy(), f[2]))
        self.wait(2)

        self.play(
            FadeOut(f[1]),
            f[2].animate.shift(UP), 
            TransformMatchingShapes(f[2].copy(), f[3]))
        self.wait(2)

        self.play(
            FadeOut(f[2]),
            f[3].animate.shift(UP), 
            TransformMatchingShapes(f[3].copy(), f[4]))
        self.wait(2)

        self.play(
            FadeOut(f[3]),
            f[4].animate.shift(UP), 
            TransformMatchingShapes(f[5].copy(), f[6]))
        self.wait(2)