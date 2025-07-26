from manim import *

class tdpp_00(Scene):
    def construct(self):
        img = ImageMobject("img/udb_logo_high.png")
        t1 = Text(r"Polinomios de mayor orden")
        t2 = Text(r"Triángulo de pascal", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))
        
class tdpp_010(Scene):
    def construct(self):
        g = [
                MathTex(r"(a\pm b)^{n}"),
                MathTex(r"(a\pm b)^{2} = a^{2} \pm 2ab+b^{2}"),
                MathTex(r"(a\pm b)^{2} = \begin{cases} a^{3}+3a^{2}b+3ab^{2}+b^{3} \\ a^{3}-3a^{2}b+3ab^{2}-b^{3} \end{cases}"),
            ]
        
        
        self.play(Write(g[0], run_time = 0.7))
        self.wait(1)
        self.play(g[0].animate.shift(UP))
        self.play(
            TransformMatchingShapes(g[0].copy(), g[1].next_to(g[0], DOWN), run_time = 1)
        )
        self.wait(2)
        self.play(VGroup(g[0], g[1]).animate.shift(UP))
        self.play(
            TransformMatchingShapes(g[0].copy(), g[2].next_to(g[1], DOWN), run_time = 1.3)
        )
        self.wait(3)
        
class tdpp_011(Scene):
    def construct(self):
        c = [
            MathTex(r"f_{0}"),
            MathTex(r"f_{1}"),
            MathTex(r"f_{2}"),
            MathTex(r"f_{3}"),
            MathTex(r"f_{4}"),
            MathTex(r"f_{5}"),
            MathTex(r"f_{6}"),
            MathTex(r"f_{7}"),

        ]
        fv = VGroup()
        for i, j in enumerate(c):
            fv.add(j)
        fv.arrange(DOWN, buff=0.3)
        b = [
            [[mt(r"1")]],
            [[mt(r"1")], [mt(r"1")]],
            [[mt(r"1")], [mt(r"2")], [mt(r"1")],], 
            [[mt(r"1")], [mt(r"3")], [mt(r"3")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"4")], [mt(r"6")], [mt(r"4")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"5")], [mt(r"10")], [mt(r"10")], [mt(r"5")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"6")], [mt(r"15")], [mt(r"20")], [mt(r"15")], [mt(r"6")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"7")], [mt(r"21")], [mt(r"35")], [mt(r"35")], [mt(r"21")], [mt(r"7")], [mt(r"1")],],

        ]
        
        cv = VGroup()
        
        # ordena todos los textos en diferentes subobjects
        for bi, bv in enumerate(b):
            v = VGroup()
            for li, lv in enumerate(bv):
                v.add(lv)
            v.arrange(RIGHT)
            v.next_to(cv, DOWN, buff=0.4)
            cv.add(v)
        cv.move_to(ORIGIN)

        keke = VGroup(cv, fv)
        fv.next_to(cv, RIGHT, 1)

        # self.add(keke)
        # print(cv[7][3])

        # fila 0 
        self.play( Write(cv[0][0]), ) # type: ignore
        self.wait(1)
        self.play( Write(fv[0]), ) # pyright: ignore[reportArgumentType]
        self.wait(1)
        # fila 1
        self.play( Write(cv[1][0]),  Write(cv[1][1]),) # pyright: ignore[reportArgumentType]
        self.wait(1)
        self.play( Write(fv[1]), )
        self.wait(1)
        
        
        # fila 2
        self.play( Write(cv[2][0]),  Write(cv[2][2]),)
        self.wait(1)
        
        self.play(Group(cv[1][0], cv[1][1]).animate.scale(1.2))
        self.play(
            Group(cv[1][0], cv[1][1]).animate.scale(1/1.2),
            TransformMatchingShapes(Group(cv[1][0], cv[1][1]).copy(), cv[2][1])
        )
        self.wait(2)
        self.play( Write(fv[2]), )
        self.wait(1)
        
        
        # fila 3
        self.play( Write(cv[3][0]),  Write(cv[3][3]),)
        self.wait(1)
        
        self.play(Group(cv[2][0], cv[2][1]).animate.scale(1.2))
        self.play(
            Group(cv[2][0], cv[2][1]).animate.scale(1/1.2),
            TransformMatchingShapes(Group(cv[2][0], cv[2][1]).copy(), cv[3][1])
        )
        self.wait(1)
        self.play(Group(cv[2][1], cv[2][2]).animate.scale(1.2))
        self.play(
            Group(cv[2][1], cv[2][2]).animate.scale(1/1.2),
            TransformMatchingShapes(Group(cv[2][1], cv[2][2]).copy(), cv[3][2])
        )
        self.wait(1)
        
        
        self.wait(1)
        self.play( Write(fv[3]), )
        self.wait(1)
        
        
        
        # fila 4 
        self.play( Write(cv[4][0]),  Write(cv[4][4]),)
        self.wait(1)
        
        self.play(Group(cv[3][0], cv[3][1]).animate.scale(1.2))
        self.play(
            Group(cv[3][0], cv[3][1]).animate.scale(1/1.2),
            TransformMatchingShapes(Group(cv[3][0], cv[3][1]).copy(), cv[4][1])
        )
        self.wait(1)
        
        self.play(Group(cv[3][1], cv[3][2]).animate.scale(1.2))
        self.play(
            Group(cv[3][1], cv[3][2]).animate.scale(1/1.2),
            TransformMatchingShapes(Group(cv[3][1], cv[3][2]).copy(), cv[4][2])
        )
        self.wait(1)
        
        self.play(Group(cv[3][2], cv[3][3]).animate.scale(1.2))
        self.play(
            Group(cv[3][2], cv[3][3]).animate.scale(1/1.2),
            TransformMatchingShapes(Group(cv[3][2], cv[3][3]).copy(), cv[4][3])
        )
        self.wait(1)
        
        self.play( Write(fv[4]), )
        self.wait(1)
        
        self.wait(3)
        for i in range(5, 8):
            self.play(FadeIn(cv[i]), FadeIn(fv[i]))
            self.wait(0.5)
            
        
        # self.remove(cv)
        
        # self.add(cv)
        
        self.wait(3)
        
        
class tdpp_012(Scene):
    def construct(self):
        p = Paragraph(
            "1. Los terminos a multiplicar para un",
            "exponente n corresponden a la n fila"
        )
        self.play(
            Write(p, run_time=1)
        )
        self.wait(3)
        self.play(Unwrite(p, run_time=0.5))
        self.wait(1)

        c = [
            MathTex(r"f_{0}"),
            MathTex(r"f_{1}"),
            MathTex(r"f_{2}"),
            MathTex(r"f_{3}"),
            MathTex(r"f_{4}"),
            MathTex(r"f_{5}"),
            MathTex(r"f_{6}"),
            MathTex(r"f_{7}"),

        ]
        fv = VGroup()
        for i, j in enumerate(c):
            fv.add(j)
        fv.arrange(DOWN, buff=0.3)
        b = [
            [[mt(r"1")]],
            [[mt(r"1")], [mt(r"1")]],
            [[mt(r"1")], [mt(r"2")], [mt(r"1")],], 
            [[mt(r"1")], [mt(r"3")], [mt(r"3")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"4")], [mt(r"6")], [mt(r"4")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"5")], [mt(r"10")], [mt(r"10")], [mt(r"5")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"6")], [mt(r"15")], [mt(r"20")], [mt(r"15")], [mt(r"6")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"7")], [mt(r"21")], [mt(r"35")], [mt(r"35")], [mt(r"21")], [mt(r"7")], [mt(r"1")],],

        ]
        
        cv = VGroup()
        
        # ordena todos los textos en diferentes subobjects
        for bi, bv in enumerate(b):
            v = VGroup()
            for li, lv in enumerate(bv):
                v.add(lv)
            v.arrange(RIGHT)
            v.next_to(cv, DOWN, buff=0.4)
            cv.add(v)
        cv.move_to(ORIGIN)

        keke = VGroup(cv, fv)
        fv.next_to(cv, RIGHT, 1)
        h = [
            MathTex(r"(a \pm b)^{2}="),
            MathTex(r"1a^{2} \quad 2ab \quad 1b^2"),

            MathTex(r"(a \pm b)^{3}="),
            MathTex(r"1a^{3} \quad 3a^2b \quad 3ab^2 \quad 1b^2"),

        ]
        self.play(FadeIn(keke))
        self.wait(2)
        self.play(
            FadeOut(cv[0]), FadeOut(fv[0]),
            FadeOut(cv[1]), FadeOut(fv[1]),
            FadeOut(fv[2]),
            FadeOut(cv[3]), FadeOut(fv[3]),
            FadeOut(cv[4]), FadeOut(fv[4]),
            FadeOut(cv[5]), FadeOut(fv[5]),
            FadeOut(cv[6]), FadeOut(fv[6]),
            FadeOut(cv[7]), FadeOut(fv[7]),
        )
        self.wait(1)
        self.play(cv[2].animate.move_to(ORIGIN).shift(RIGHT*2))
        self.play(h[0].animate.next_to(cv[2], LEFT))
        self.wait(1)
        self.play(
            TransformMatchingShapes(cv[2], h[1].next_to(h[0], RIGHT))
        )
        self.play(VGroup(h[0], h[1]).animate.move_to(ORIGIN))
        self.wait(3)

        # transicion
        cv = VGroup()
        
        # ordena todos los textos en diferentes subobjects
        for bi, bv in enumerate(b):
            v = VGroup()
            for li, lv in enumerate(bv):
                v.add(lv)
            v.arrange(RIGHT)
            v.next_to(cv, DOWN, buff=0.4)
            cv.add(v)
        cv.move_to(ORIGIN)

        keke = VGroup(cv, fv)
        fv.next_to(cv, RIGHT, 1)


        # hue hue hue 


        self.remove(h[0], h[1], fv[2])
        self.play(FadeIn(cv), FadeIn(fv))
        self.wait(1)
        self.play(Write(h[2].next_to(cv, LEFT)))
        self.wait(2)
        self.play(
            FadeOut(cv[0]), FadeOut(fv[0]),
            FadeOut(cv[1]), FadeOut(fv[1]),
            FadeOut(cv[2]), FadeOut(fv[2]),
            # FadeOut(cv[3]), FadeOut(fv[3]),
            FadeOut(cv[4]), FadeOut(fv[4]),
            FadeOut(cv[5]), FadeOut(fv[5]),
            FadeOut(cv[6]), FadeOut(fv[6]),
            FadeOut(cv[7]), FadeOut(fv[7]),
        )
        self.wait(1)
        self.play(
            cv[3].animate.next_to(h[2], RIGHT)
            )
        
        self.play(
            VGroup(h[2], cv[3]).animate.move_to(ORIGIN),
            FadeOut(fv[3])
            )
        self.wait(1)
        self.play(TransformMatchingShapes(cv[3], h[3].next_to(h[2], RIGHT)))
        self.play(VGroup(h[2], h[3]).animate.move_to(ORIGIN))
        self.wait(3)

class tdpp_013(Scene):
    def construct(self):
        p = Paragraph(
            "2. Los exponentes en a decrecen, ",
            "empezando con el exponente n, ",
            "y los exponentes en b aumentan",
            "hasta alcanzar n"
        )
        self.play(
            Write(p, run_time=1)
        )
        self.wait(3)
        self.play(Unwrite(p, run_time=0.5))
        self.wait(1)



        c = [
            MathTex(r"f_{0}"),
            MathTex(r"f_{1}"),
            MathTex(r"f_{2}"),
            MathTex(r"f_{3}"),
            MathTex(r"f_{4}"),
            MathTex(r"f_{5}"),
            MathTex(r"f_{6}"),
            MathTex(r"f_{7}"),

        ]
        fv = VGroup()
        for i, j in enumerate(c):
            fv.add(j)
        fv.arrange(DOWN, buff=0.3)
        b = [
            [[mt(r"1")]],
            [[mt(r"1")], [mt(r"1")]],
            [[mt(r"1")], [mt(r"2")], [mt(r"1")],], 
            [[mt(r"1")], [mt(r"3")], [mt(r"3")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"4")], [mt(r"6")], [mt(r"4")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"5")], [mt(r"10")], [mt(r"10")], [mt(r"5")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"6")], [mt(r"15")], [mt(r"20")], [mt(r"15")], [mt(r"6")], [mt(r"1")],],
            [[mt(r"1")], [mt(r"7")], [mt(r"21")], [mt(r"35")], [mt(r"35")], [mt(r"21")], [mt(r"7")], [mt(r"1")],],

        ]
        
        cv = VGroup()
        
        # ordena todos los textos en diferentes subobjects
        for bi, bv in enumerate(b):
            v = VGroup()
            for li, lv in enumerate(bv):
                v.add(lv)
            v.arrange(RIGHT)
            v.next_to(cv, DOWN, buff=0.4)
            cv.add(v)
        cv.move_to(ORIGIN)

        keke = VGroup(cv, fv)
        fv.next_to(cv, RIGHT, 1)
        self.play(FadeIn(cv, fv))
        self.wait(1)

        h = [
            MathTex(r"(a \pm b )^{4}="),
            MathTex(r"1a^{4}b^{0} \quad 4 \quad 6 \quad 4 \quad 1"),
            MathTex(r"1a^{4}b^{0} \quad 4a^{3}b^{1} \quad 6 \quad 4 \quad 1"),
            MathTex(r"1a^{4}b^{0} \quad 4a^{3}b^{1} \quad 6a^{2}b^{2} \quad 4 \quad 1"),
            MathTex(r"1a^{4}b^{0} \quad 4a^{3}b^{1} \quad 6a^{2}b^{2} \quad 4a^{1}b^{3} \quad 1"),
            MathTex(r"1a^{4}b^{0} \quad 4a^{3}b^{1} \quad 6a^{2}b^{2} \quad 4a^{1}b^{3} \quad 1a^{0}b^{4}"),
            
            
            MathTex(r"a^{4} \quad 4a^{3}b^{1} \quad 6a^{2}b^{2} \quad 4a^{1}b^{3} \quad b^{4}"),
            MathTex(r""),
            MathTex(r""),
        ]
        self.play(
            Write(h[0].next_to(cv, LEFT))
        )
        self.wait(2)
        self.play(
            FadeOut(cv[0]), FadeOut(fv[0]),
            FadeOut(cv[1]), FadeOut(fv[1]),
            FadeOut(cv[2]), FadeOut(fv[2]),
            FadeOut(cv[3]), FadeOut(fv[3]),
            # FadeOut(cv[4]), FadeOut(fv[4]),
            FadeOut(cv[5]), FadeOut(fv[5]),
            FadeOut(cv[6]), FadeOut(fv[6]),
            FadeOut(cv[7]), FadeOut(fv[7]),
        )
        self.wait(1)

        self.play(cv[4].animate.next_to(h[0], RIGHT))
        self.play(FadeOut(fv[4]))
        self.wait(1)
        
        self.play(ReplacementTransform(cv[4], h[1].next_to(h[0], RIGHT)))
        self.play(VGroup(h[0], h[1]).animate.move_to(ORIGIN))
        self.wait(1)
        for i in range(1, 6 ):
            self.play(ReplacementTransform(h[i], h[i+1].next_to(h[0], RIGHT)))
            self.play(VGroup(h[0], h[i+1]).animate.move_to(ORIGIN))
            self.wait(1)
        self.wait(2)
    

class tdpp_014(Scene):
    def construct(self):
        p = Paragraph(
            "3.1 Si entre a y b, ambos son positivos, ",
            "todos los coeficientes son positivos., ",
            "3.2 Si sólo uno es negativo, los signos",
            "se intercambian."
        )

        f = [
            MathTex(r"(a+b)^{3}=1 \quad 3 \quad 3 \quad 1"),
            MathTex(r"(a+b)^{3}=1a^3b^{0} \quad 3a^{2}b \quad 3ab^{2} \quad 1a^{0}b^{3}"),
            MathTex(r"(a+b)^{3}=a^3 \quad 3a^{2}b \quad 3ab^{2} \quad b^{3}"),
            MathTex(r"(a+b)^{3}=a^3 + 3a^{2}b +  3ab^{2} + b^{3}"),


            MathTex(r"(a-b)^6= 1 \quad 6 \quad 15 \quad 20 \quad 15 \quad 6 \quad 1"),
            MathTex(r"(a-b)^6= 1a^{6}b^{0} \quad 6a^{5}b^{1} \quad 15a^{4}b^{2} \quad 20a^{3}b^{3} \quad 15a^{2}b^{4} \quad 6a^{1}b^{5} \quad 1a^{0}b^{6}"),
            MathTex(r"(a-b)^6= a^{6} \quad 6a^{5}b \quad 15a^{4}b^{2} \quad 20a^{3}b^{3} \quad 15a^{2}b^{4} \quad 6ab^{5} \quad b^{6}"),
            MathTex(r"(a-b)^6= a^{6} - 6a^{5}b + 15a^{4}b^{2} - 20a^{3}b^{3} + 15a^{2}b^{4} - 6ab^{5} + b^{6}"),
        ]

        self.play(
            Write(p, run_time=1)
        )
        self.wait(3)
        self.play(Unwrite(p, run_time=0.5))
        self.wait(1)

        self.play(Write(f[0]))
        self.wait(1)
        for i in range(0, 3):
            self.play(ReplacementTransform(f[i], f[i+1]))
            self.wait(1)
        self.wait(3)
        self.remove(f[3])
        self.wait(1)
        self.play(Write(f[4]))
        self.wait(1)
        for i in range(4, 7):
            self.play(ReplacementTransform(f[i], f[i+1]))
            self.wait(1)

        self.wait(3)
        
class tdpp_015(Scene):
    def construct(self):
        p = Paragraph(
            "3.3 Si entre a y b, ambos son negativos, ",
            "si n es par, todos los terminos son positivos. ",
            "si n es impar, todos los terminos son negativos",
        )

        f = [
            MathTex(r"(-a-b)^{3} = 1 \quad 3 \quad 3 \quad 1"),
            MathTex(r"(-a-b)^{3} = a^3 \quad 3a^{2}b \quad 3ab^{2} \quad b^{3}"),
            MathTex(r"n=3"),
            MathTex(r"\frac{3}{2} = 1.5 \quad \text{Es impar}"),
            MathTex(r"(-a-b)^{3} = -a^3 - 3a^{2}b - 3ab^{2} - b^{3}"),

            MathTex(r"(-a-b)^{6} = a^{6} \quad 6a^{5}b \quad 15a^{4}b^{2} \quad 20a^{3}b^{3} \quad 15a^{2}b^{4} \quad 6ab^{5} \quad b^{6}"),
            MathTex(r"n=6"),
            MathTex(r"\frac{6}{2} = 3 \quad \text{Es par}"),
            MathTex(r"(-a-b)^{6} = a^{6} + 6a^{5}b + 15a^{4}b^{2} + 20a^{3}b^{3} + 15a^{2}b^{4} + 6ab^{5} + b^{6}"),
        ]

        self.play(
            Write(p, run_time=1)
        )
        self.wait(3)
        self.play(Unwrite(p, run_time=0.5))
        self.wait(1)


        self.play(Write(f[0]))
        self.wait(1)
        for i in range(0, 1):
            self.play(ReplacementTransform(f[i], f[i+1]))
            self.wait(1)
        self.wait(1)
        self.play(f[2].animate.next_to(f[1], DOWN*2))
        self.wait(1)
        self.play(f[2].animate.shift(LEFT*2))
        self.play(f[3].animate.next_to(f[2], RIGHT, 2))
        self.play(VGroup(f[2], f[3]).animate.move_to(ORIGIN).shift(DOWN*2))

        self.wait(1)

        self.play(
            TransformMatchingShapes(f[1], f[4].move_to(f[1]))
        )
        self.wait(3)

        self.remove(f[2], f[3], f[4])
        self.wait(1)
        self.play(Write(f[5]))
        self.wait(1)
        self.play(f[6].animate.next_to(f[5], DOWN*2))
        self.wait(1)
        self.play(f[6].animate.shift(LEFT*2))
        self.play(f[7].animate.next_to(f[6], RIGHT, 2))
        self.wait(1)
        self.play(VGroup(f[6], f[7]).animate.move_to(ORIGIN).shift(DOWN*2))
        self.wait(1)

        self.play(
            TransformMatchingShapes(f[5], f[8].move_to(f[1]))
        )
        self.wait(3)

class tdpp_016(Scene):
    def construct(self):
        f = [
            MathTex(r"(-a-b)^{3}"),
            MathTex(r"(-1)^{3}(a+b)^{3}"),
            MathTex(r"(-1)(-1)(-1)(a+b)^{3}"),
            MathTex(r"(-1)(a+b)^{3}"),
            MathTex(r"-(a+b)^{3}"),
            MathTex(r"(-a-b)^{3}= -(a+b)^{3} "),
            MathTex(r"(-a-b)^{3}= -(a^{3}+3a^{2}b+3ab^{2}+b^{3}) "),
            MathTex(r"(-a-b)^{3}= -a^{3}-3a^{2}b-3ab^{2}-b^{3} "),


            MathTex(r"(-a-b)^{6} "),

            MathTex(r"(-1)^{6}(a+b)^{6}"),
            MathTex(r"(-1)(-1)(-1) \cdot (-1)(-1)(-1)\cdot(a+b)^{6}"),

            MathTex(r"(-1)(-1)(a+b)^{6}"),
            MathTex(r"(a+b)^{6}"),
            MathTex(r"(-a-b)^{6} = (a+b)^{6}"),
            MathTex(r"(-a-b)^{6} = a^{6}+6a^{5}b+15a^{4}b^{2}+20a^{3}b^{3}+15a^{2}b^{4}+6ab^{5}+b^{6}"),


        ]
        self.play(Write(f[0]))
        self.wait(1)
        for i in range(0, 7):
            self.play(ReplacementTransform(f[i], f[i+1]))
            self.wait(1)
        self.wait(3)
        self.remove(f[7])

        self.wait(2)
        self.play(Write(f[8]))
        self.wait(1)
        for i in range(8, 14):
            self.play(ReplacementTransform(f[i], f[i+1]))
            self.wait(1)
        self.wait(3)


class tdpp_02(Scene):
    def construct(self):
        f= [
            MathTex(r"(-7m^{3}-2k^{5})^{4} "),
            MathTex(r"(-a-b)^{4}=1 \quad 4 \quad 6 \quad 4\quad 1"),
            MathTex(r"(-a-b)^{4}=a^{4}\quad  4a^{3}b \quad 6a^{2}b^{2} \quad  4ab^{3} \quad b^{4}"),
            MathTex(r"\frac{4}{2}=2 \quad \text{Es par}"),

            MathTex(r"(-a-b)^{4}=a^{4}+4a^{3}b+6a^{2}b^{2}+4ab^{3}+b^{4}"),
            MathTex(r"\begin{cases} a = 7m^{3} \\ b= 2k^{5} \end{cases}"),
            MathTex(r"a^{4}+4a^{3}b+6a^{2}b^{2}+4ab^{3}+b^{4}"),
            MathTex(r"(7m^{3})^{4}+4(7m^{3})^{3}(2k^{5})+6(7m^{3})^{2}(2k^{5})^{2}+4(7m^{3})(2k^{5})^{3}+(2k^{5})^{4}"),
            MathTex(r"2401m^{12}+2744m^{9}k^{5}+1176m^{6}k^{10}+224m^{3}k^{15}+16k^{20}"),
        ]
        self.play(Write(f[0]))
        self.wait(1)
        self.play(f[0].animate.shift(UP*2))
        self.play(f[1].animate.next_to(f[0], DOWN))
        self.wait(1)
        self.play(ReplacementTransform(f[1], f[2].move_to(f[1])))
        self.wait(1)
        self.play(Write(f[3].next_to(f[2], DOWN)))
        self.wait(1)

        self.play(ReplacementTransform(f[2], f[4].move_to(f[2])))
        self.play(FadeOut(f[3]))
        self.wait(1)
        self.play(f[5].animate.next_to(f[1], DOWN))
        self.wait(1)
        self.play(
            TransformMatchingShapes(f[4], f[6].next_to(f[0], DOWN), run_time=0.7),
            
            )
        # self.play()
        self.wait(1)
        self.play(
            TransformMatchingShapes(f[6], f[7].next_to(f[0], DOWN)),
            TransformMatchingTex(f[5].copy(), f[7], key_map={"a":"7m^{3}", "b":"2k^{5}"})
        )
        self.wait(2)
        
        self.play(FadeOut(f[5]))
        self.play(VGroup(f[0], f[7]).animate.move_to(ORIGIN))
        self.wait(1)
        self.play(ReplacementTransform(f[7], f[8].move_to(f[7])))
        self.wait(3)



def mt(t: str):
    return MathTex(t)
