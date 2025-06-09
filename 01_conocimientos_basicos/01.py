from manim import *
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helpers import quickFormulas


class introResumen(Scene):
    def construct(self):
        img = ImageMobject('img/udb_logo_high.png')
        # text = Text("Conocimientos básicos")
        text = Text("Ley de los signos")
        self.add(img.scale(0.25), text.shift(DOWN*2))
        # self.add()
        # self.add(text.shift(DOWN*2))
        # self.wait(1)
        # self.play(text.animate.scale(0.8).shift(UP*2.5),  img.animate.scale(0.7).shift(UP*2.3), run_time=1)
        # self.wait(1)



        # blist = BulletedList("Ley de los signos", "Operaciones con fracciones", "Propiedades de los exponentes", "Propiedades de los logaritmos")
        # blist.shift(DOWN*1.7).scale(0.8)

        # self.add(blist.shift(DOWN*1.5))
        # self.play(Create(blist), run_time=3)

        # self.wait(1)

class leySignos_00(Scene):
    def construct(self):
        t = MathTable(
            [
                ["A", "B", "A \cdot B"],
                ["+", "+", "+"],
                ["-", "-", "+"],
                ["+", "-", "-"],
                ["-", "+", "-"]
                
            ]
        )


        title = Text("Ley de los signos")
        tt = """Dos signos iguales dan positivo; signos diferentes, negativo."""
        enunciado = Text(tt, font_size=30)
        title.to_corner(UL)

        self.add(title)
        self.play(Write(enunciado), run_time=1)
        self.play(enunciado.animate.shift(UP*2), run_time=1)
        self.add(t.scale(0.7), t.shift(DOWN))
        self.wait(2)



class leySignos_01(Scene):
    def construct(self):
        

        t1 = MathTex(r"(-2)(3)=-6")
        t1_1 = MathTex(r"(-2)(3)=(2)(-3)=-6")
        t2 = MathTex(r"-2\cdot-2=4")
        t3 = MathTex(r"25(4)=100")
        t4 = MathTex(r"10\times-3=-30")


        t5_0 = MathTex(r"(-1)(-1)(-1)(-1)(-1)")
        t5_1 = MathTex(r"[(-1)(-1)]\cdot[(-1)(-1)]\cdot(-1)")
        t5_2 = MathTex(r"(1)(1)(-1)")
        t5_3 = MathTex(r"-1")
        t5 = VGroup(t5_0, t5_1, t5_2, t5_3).arrange(DOWN)

        t6_0 = MathTex(r"(1)(-2)\cdot4\times2(-1)")
        t6_1 = MathTex(r"(2)(2)(4)(-1)(-1)")
        t6_2 = MathTex(r"[(2)(2)(4)]\cdot(-1)(-1)")
        t6_3 = MathTex(r"(16)\cdot(1)")
        t6_4 = MathTex(r"16")
        t6 = VGroup(t6_0, t6_1, t6_2, t6_3, t6_4).arrange(DOWN)

        t7 = MathTex(r"-\frac{1}{1}=-1")
        t8 = MathTex(r"-\frac{1}{1}=\frac{-1}{1}=\frac{1}{-1}")
        t9 = MathTex(r"\frac{(-20)(-2)}{-40}=\frac{40}{-40}=1")

        self.play(ShowSubmobjectsOneByOne(VGroup(t1, t1_1, t2, t3, t4), run_time=7))
        self.clear()
        self.play(Succession(
            Write(t5_0, lag_ratio = 1, run_time = 0.3),
            Wait(1.0),
            Add(t5_1),
            Wait(1.0),
            Add(t5_2),
            Wait(1.0),
            Add(t5_3),
            Wait(1.0),
        ))
        self.clear()
        self.play(Succession(
            Write(t6_0, lag_ratio = 1, run_time = 0.3), Wait(1),
            Add(t6_1), Wait(1.0),
            Add(t6_2), Wait(1.0),
            Add(t6_3), Wait(1.0),
            Add(t6_4), Wait(1.0)
        ))
        self.clear()
        self.play(ShowSubmobjectsOneByOne(VGroup(t7, t8, t9), run_time=7))
        

        self.wait(1)





class leySignos_011(Scene):
    def construct(self):
        
        f1 = [
            MathTex(r"(-2)(3)=-6"),
            MathTex(r"(-2)(3)=(2)(-3)=-6"),
            MathTex(r"-2\cdot-2=4"),
            MathTex(r"25(4)=100"),
            MathTex(r"10\times-3=-30"),
        ]

        # quickFormulas(self, f1, 2)

        self.clear()

        f2 = [
            MathTex(r"(-1)(-1)(-1)(-1)(-1)"),
            MathTex(r"[(-1)(-1)]\cdot[(-1)(-1)]\cdot(-1)"),
            MathTex(r"(1)(1)(-1)"),
            MathTex(r"-1"),
        ]
        
        self.clear()

        quickFormulas(self, f2, 2)

    
        f3 = [
            MathTex(r"(1)(-2)\cdot4\times2(-1)"),        
            MathTex(r"(2)(2)(4)(-1)(-1)"),
            MathTex(r"[(2)(2)(4)]\cdot(-1)(-1)"),
            MathTex(r"(16)\cdot(1)"),
            MathTex(r"16"),
        ]
        
        self.clear()

        quickFormulas(self, f3, 2)
        
        self.clear()
        f4 = [
            MathTex(r"-\frac{1}{1}=-1"),
            MathTex(r"-\frac{1}{1}=\frac{-1}{1}=\frac{1}{-1}"),
            MathTex(r"\frac{(-20)(-2)}{-40}=\frac{40}{-40}=1"),
        ]

        self.clear()
        quickFormulas(self, f4, 2)
