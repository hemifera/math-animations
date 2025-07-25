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
        self.play( Write(cv[0][0]), )
        self.wait(1)
        self.play( Write(fv[0]), )
        self.wait(1)
        # fila 1
        self.play( Write(cv[1][0]),  Write(cv[1][1]),)
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
        
        
        
    
def mt(t: str):
    return MathTex(t)
