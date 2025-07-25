from manim import *
import numpy as np

class sdpb_00(Scene):
    def construct(self):
        img = ImageMobject("img/udb_logo_high.png")
        t1 = Text(r"Polinomios de mayor orden")
        t2 = Text(r"Suma o diferencia de cubos", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))

class sdpb_01(Scene):
    def construct(self):
        f = [
            MathTex(r"\begin{cases} a^{3}+b^{3}=(a+b)(a^{2}-ab+b^{2}) \\ a^{3}-b^{3}=(a-b)(a^{2}+ab+b^{2}) \end{cases}"),
            MathTex(r"a^{3}\pm b^{3}=(a \pm b)(a^{2}\mp ab+b^{2})"),
        ]
        self.play(Write(f[0], run_time=1))
        self.wait(3)
        self.play(TransformMatchingShapes(f[0], f[1]))
        self.wait(2)
        
        
class sdpb_02(Scene):
    def construct(self):
        f = [
            MathTex(r"125k^{3} + 8p^{9}"),
            MathTex(r"a^{3}+b^{3}=(a+b)(a^{2}-ab+b^{2})"),
            MathTex(r"\begin{cases} a^{3}=125k^{3} \\ b^{3} = 8p^{9}  \end{cases}"),
            MathTex(r"\begin{cases} \sqrt[3]{ a^{3} }=\sqrt[3]{ 125k^{3} } \\ \sqrt[3]{ b^{3} } = \sqrt[3]{ 8p^{9} }  \end{cases}"),
            MathTex(r"\begin{cases} a = 5k^{3/3} \\ b = 2p^{9/3} \end{cases}"),
            MathTex(r"\begin{cases} a = 5k \\ b = 2p^{3} \end{cases}"),
            MathTex(r"(5k+2p^{3})[(5k)^{2}-(5k)(2p^{3})+(2p^{3})^{2}]"),
            MathTex(r"(5k+2p^{3})[25k^{2}-10kp^{3}+4p^{5}]"),
        ]
        
        self.play(Write(f[0], run_time=0.7))
        self.wait(2)
        
        self.play(f[0].animate.shift(UP*2))
        self.play(f[1].animate.next_to(f[0], DOWN))
        self.wait(1)
        self.play(
            TransformMatchingShapes(
                f[0].copy(), f[2].next_to(f[1], DOWN*1.5)
            )
        )
        for i in range(2, 5):
            self.play( TransformMatchingShapes( f[i], f[i+1].move_to(f[i]) )) 
            self.wait(1)
           
        self.wait(1)
        self.play(
            TransformMatchingShapes(VGroup(f[0], f[5]), f[6].move_to(f[0]), run_time=0.7),
        )
        self.wait(1)
        self.play(
            VGroup(f[6], f[1]).animate.move_to(ORIGIN)
        )
        self.play(TransformMatchingShapes(f[6], f[7].move_to(f[6])))
        self.remove(f[1])
        self.wait(1)
        self.play(f[7].animate.move_to(ORIGIN))
        self.wait(2)
        
        
class sdpb_03(Scene):
    def construct(self):
        
        f = [
            MathTex(r"3p^{2}-u"),
            MathTex(r"a^{3}-b^{3}=(a-b)(a^{2}+ab+b^{2})"),
            MathTex(r"\begin{cases} a^{3}=3p^{2} \\ b^{3}=u \end{cases}"),
            MathTex(r"\begin{cases} \sqrt[3]{ a^{3} }=\sqrt[3]{ 3p^{2} } \\ \sqrt[3]{ b^{3} }=\sqrt[3]{ u } \end{cases}"),
            MathTex(r"\begin{cases} a=3^{1/3}p^{2/3} \\ b=u^{1/3} \end{cases}"),
            
            MathTex(r"(3^{1/3}p^{2/3}-u^{1/3})[(\sqrt[3]{ 3 }p^{2/3})^{2}+(\sqrt[3]{ 3 }p^{2/3})(\sqrt[3]{ u })+(\sqrt[3]{ u })^{2}]"),
            MathTex(r"(3^{1/3}p^{2/3}-u^{1/3}) [3^{2/3}p^{4/3}+3^{1/3}p^{2/3}u^{1/3}+u^{2/3}]"),
            MathTex(r"(\sqrt[3]{ 3p^{2} }-\sqrt[3]{ u })[\sqrt[3]{ 3^{2} p^{4}}+\sqrt[3]{ 3p^{2} u} +\sqrt[3]{ u^{2} }]"),
        ]
        
        self.play(Write(f[0], run_time=0.7))
        self.wait(2)
        
        self.play(f[0].animate.shift(UP*2))
        self.play(f[1].animate.next_to(f[0], DOWN))
        self.wait(1)
        self.play(
            TransformMatchingShapes(
                f[0].copy(), f[2].next_to(f[1], DOWN*1.5)
            )
        )
        for i in range(2, 4):
            self.play( TransformMatchingShapes( f[i], f[i+1].move_to(f[i]) )) 
            self.wait(1)
           
        self.wait(1)
        self.play(
            TransformMatchingShapes(VGroup(f[0], f[4].copy()), f[5].move_to(f[0]), run_time=0.7),
        )
        self.wait(1)
        self.remove(f[4])
        self.play(
            VGroup(f[5], f[1]).animate.move_to(ORIGIN)
        )
        self.play(TransformMatchingShapes(f[5], f[6].move_to(f[5])))
        self.remove(f[1])
        self.wait(1)
        
        self.play(f[6].animate.move_to(ORIGIN))
        self.play(TransformMatchingShapes(f[6], f[7].move_to(f[6])))
        self.wait(2)
        
        
        self.wait(1)