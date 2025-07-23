from manim import *
import numpy as np


class cpb_00(Scene):
    def construct(self):
        img = ImageMobject("img/udb_logo_high.png")
        t1 = Text(r"Polinomios de mayor orden")
        t2 = Text(r"Cubo perfecto de binomios", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))

class cpb_01(Scene):
    def construct(self):
        f = [
            MathTex(r"\begin{cases} (a+b)^{3}=a^{3}+3a^{2}b+3ab^{2}+b^{3} \\ (a-b)^{3}=a^{3}-3a^{2}b+3ab^{2}-b^{3} \end{cases}"),
        ]
        self.play(Write(f[0], run_time = 0.5))
        self.wait(2)

class cpb_02(Scene):
    def construct(self):
        f = [
            MathTex(r"(9u-2v)^{3}"),
            MathTex(r"(a-b)^{3}=a^{3}-3a^{2}b+3ab^{2}-b^{3}"),
            MathTex(r"\begin{cases} a=9u \\ b=2v \end{cases}"),
            MathTex(r"(9u)^{3}-3(9u)^{2}(2v)+3(9u)(2v)^{2}-(2v)^{2}"),
            
            MathTex(r"729u^{3}-18v(81u^{2})+29u(4v^{2})-8v^{3}"),
            MathTex(r"729u^{3}-1458u^{2}v+29uv^{2}-8v^{3}"),

        ]
        self.play(Write(f[0], run_time = 0.5))
        self.wait(1)
        self.play(
            f[0].animate.shift(UP*2),
            TransformMatchingShapes(f[0].copy(), f[2])
        )
        self.wait(1)
        self.play(
            Write(f[1].next_to(f[2], DOWN*2))
        )
        self.wait(1)

        self.play(
            TransformMatchingShapes(f[2], f[3].move_to(f[2]))
        )
        self.remove(f[2])
        self.play(f[3].animate.move_to(ORIGIN))
        self.wait(1)
        self.remove(f[1])
        for i in range(3, 5):
            self.play(
                ReplacementTransform(f[i], f[i+1].move_to(f[i]))
            )
            self.wait(1)
        self.wait(2)

class cpb_03(Scene):
    def construct(self):
        f = [
            MathTex(r"(5j^{9}+13k^{4})^{3}"),
            MathTex(r"(a-b)^{3}=a^{3}-3a^{2}b+3ab^{2}-b^{3}"),
            MathTex(r"\begin{cases} a = 5j^{9} \\ b=13k^{4} \end{cases}"),
            MathTex(r"(5j^{9})^{3}+3(5j^{9})^{2}(13k^{4})+3(5j^{9})(13k^{4})^{2}+(13k^{4})^{3}"),
            MathTex(r"125j^{27}+3(25j^{18})(13k^{4})+3(5j^{9})(169k^{8})+2197k^{12}"),

            MathTex(r"125j^{27}+975j^{18}k^{4}+2535j^{9}k^{8}+2197k^{12}"),
        ]

        self.play(Write(f[0], run_time = 0.5))
        self.wait(1)
        self.play(
            f[0].animate.shift(UP*2),
            TransformMatchingShapes(f[0].copy(), f[2])
        )
        self.wait(1)
        self.play(
            Write(f[1].next_to(f[2], DOWN*2))
        )
        self.wait(1)

        self.play(
            TransformMatchingShapes(f[2], f[3].move_to(f[2]))
        )
        self.remove(f[2])
        self.play(f[3].animate.move_to(ORIGIN))
        self.wait(1)
        self.remove(f[1])
        for i in range(3, 5):
            self.play(
                ReplacementTransform(f[i], f[i+1].move_to(f[i]))
            )
            self.wait(1)
        self.wait(2)

class cpb_04(Scene):
    def construct(self):
        f = [
            MathTex(r"8u^{15}+108mp^{2}u^{10}+729m^{3}p^{6}+ 486m^{2}p^{4}u^{5}"),
            MathTex(r"a^{3}+3a^{2}b+3ab^{2}+b^{3}"),
            MathTex(r"8u^{15}+108mp^{2}u^{10}+ 486m^{2}p^{4}u^{5} +729m^{3}p^{6}"),

            MathTex(r"\begin{cases} a^{3} = 8u^{15}  \\ b^{3} =729 m^{3}p^{6} \end{cases}"),
            MathTex(r"\begin{cases} \sqrt[3]{ a^{3} } = \sqrt[3]{ 8u^{15} }  \\ \sqrt[3]{ b^{3} } =\sqrt[3]{ 729 m^{3}p^{6} } \end{cases}"),
            MathTex(r"\begin{cases} a = 2u^{15/3} \\ b = 9 m^{3/3} p^{6/3} \end{cases}"),

            MathTex(r"\begin{cases} a = 2u^{5} \\ b = 9 mp^{2}  \end{cases}"),
            MathTex(r"(a+b)^{3} = (2u^{5}+9mp^{2})^{3} \to ?"),
            MathTex(r"3a^{2}b = 3(2u^{5})^{2}(9mp^{2}) "),
            
            MathTex(r"3a^{2}b = 3(4u^{10})(9mp^{2})"),
            MathTex(r"3a^{2}b = 108mp^{2}u^{10}"),
            MathTex(r"3ab^{2} = 3(2u^{5})(9mp^{2})^{2}"),

            MathTex(r"3ab^{2} = 3(2u^{5})(81m^{2}p^{4})"),
            MathTex(r"3ab^{2} = 486m^{2}p^{4}u^{5}"),

            MathTex(r"(2u^{5}+9mp^{2})^{3}"),

        ]

        self.play(
            Write(f[0], run_time = 0.7)
        )
        self.wait(1)
        self.play(
            f[0].animate.shift(UP*2),
            Write(f[1].shift(DOWN*2))
        )
        self.wait(2)
        self.play(TransformMatchingShapes(f[0], f[2].move_to(f[0])))
        self.wait(1)

        self.play(
            Write(f[3], run_time = 0.7)
        )
        self.wait(1)
        for i in range(3, 6):
            self.play(
                ReplacementTransform(f[i], f[i+1].move_to(f[i]))
            )
            self.wait(1)
        self.remove(f[1])
        self.play(f[6].animate.shift(DOWN*2))
        self.wait(1)
        self.play(Write((f[7]), run_time=0.7))
        self.wait(1)
        self.remove(f[7])
        self.play(
            Write(f[8])
        )
        for i in range(8, 10):

            self.play(
                ReplacementTransform(f[i], f[i+1].move_to(f[i]))
            )
            self.wait(1)
            
        self.wait(2)
        self.remove(f[10])
        self.play(Write(f[11]))
        self.wait(1)
        for i in range(11, 13):

            self.play(
                ReplacementTransform(f[i], f[i+1].move_to(f[i]))
            )
            self.wait(1)
        self.wait(2)
        self.remove(f[1], f[13])
        self.wait(1)
        # self.play(Write(f[6], run_time=0.7))
        self.wait(1)
        self.play(VGroup(f[6], f[14]).animate.arrange(UP*1.5), run_time=0.7)
        self.wait(2)
        
