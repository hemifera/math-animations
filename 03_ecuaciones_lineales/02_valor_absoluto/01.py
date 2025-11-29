from manim import *

class vabs_00(Scene):
    def construct(self):
        img = ImageMobject("../../img/udb_logo_high.png")
        t1 = Text(r"Valor absoluto")
        t2 = Text(r"Teoría", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))

class vabs_10(Scene):
    def construct(self):
        f = [
            mt(r"|x|"),
            mt(r"|-1|=1"),
            mt(r"|20+3-50-12|"),
            mt(r"|-39|"),
            mt(r"39"),

            mt(r"|0|=0"),
            mt(r"|20|=20"),
            mt(r"|-20|=-(-20)=20"),
            mt(r"|x| \geq 0"),
            mt(r"|x|=\begin{cases} +x  & x> 0 \\ +x  &  x=0 \\ -x  & x < 0\end{cases}"),

            mt(r"|x+3|=0"),
            mt(r"x+3=0"),
            mt(r"x=-3"),
            mt(r"|x+3|"),
            mt(r"|-3+3|"),

            # 15
            mt(r"|0|"),
            mt(r"0"),
            mt(r"|x-2|=1"),
            mt(r"x=1"),
            mt(r"|1-2|"),

            mt(r"|-1|"),
            mt(r"1"),
            mt(r"x=3"),
            mt(r"|3-2|"),
            mt(r"|1|"),

            mt(r"1"),
        ]

        self.play(Write(f[0].scale(2)), run_time=0.8)
        self.wait(1)
        self.add(f[0].set_opacity(0))
        self.play(Write(f[1].scale(2)), run_time=0.8)
        self.wait(1)

        self.add(f[1].set_opacity(0))
        self.play(Write(f[2].scale(2)), run_time=0.8)
        self.wait(1)

        self.play(TransformMatchingShapes(f[2], f[3].scale(2)), run_time=0.8)
        self.wait(1)

        self.play(TransformMatchingShapes(f[3], f[4].scale(2) ), )
        self.wait(1)

        for i in range(4, 8):
            self.add(f[i].set_opacity(0))
            self.play(Write(f[i+1].scale(2)))
            self.wait(1)

        # self.add(f[5].set_opacity(0))
        # self.play(Write(f[6].scale(2)))
        # self.wait(1)

        # self.add(f[6].set_opacity(0))
        # self.play(Write(f[7].scale(2)))
        # self.wait(1)

        # self.add(f[7].set_opacity(0))
        # self.play(Write(f[8].scale(2)))
        # self.wait(1)

        # self.add(f[8].set_opacity(0))
        self.play(f[8].animate.scale(0.5).shift(UP))
        # self.play(Write(f[9]), run_time=0.8)
        # self.wait(1)
        self.play(f[9].animate.next_to(f[8], DOWN))
        self.wait(1)

        self.add(VGroup(f[8], f[9]).set_opacity(0))
        # self.play(Write(f[10]), run_time = 0.8)
        # self.wait(1)
        # self.play(TransformMatchingShapes(f[10], f[11], path_arc=PI/2))
        # self.wait(1)
        # self.play(TransformMatchingShapes(f[11], f[12], path_arc=PI/2))
        # self.wait(1)

        # self.play(f[10].animate.shift(UP*1.5))
        # self.play(f[12].animate.next_to(f[13], LEFT, buff=2))
        # self.wait(1)
        # self.play(TransformMatchingShapes(VGroup(f[12], f[13]).copy(), f[14]))
        # self.wait(1)
        # # self.play(TransformMatchingShapes(f[13], f[14],))
        # # self.wait(1)
        # self.play(TransformMatchingShapes(f[14], f[15],))
        # self.wait(1)
        # self.play(TransformMatchingShapes(f[15], f[16],))
        # self.wait(1)

        # self.add(VGroup(f[10], f[12], f[16]).set_opacity(0))
        self.wait(1)

        self.play(Write(f[17]), run_time = 0.8)
        self.wait(1)
        self.play(f[17].animate.shift(UP*1.5))
        self.wait(1)
        self.play(Write(f[18].next_to(f[19], LEFT, buff=2)), run_time = 0.8)
        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(f[18], f[17]).copy(), f[19]))
        self.wait(1)

        self.play(TransformMatchingShapes(f[19], f[20], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[20], f[21], path_arc=PI/2))
        self.wait(1)

        self.add(f[21].set_opacity(0))
        self.play(Write(f[22].next_to(f[18], DOWN)), run_time = 0.8)
        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(f[22], f[17]).copy(), f[23]))
        self.wait(1)

        self.play(TransformMatchingShapes(f[23], f[24], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[24], f[25], path_arc=PI/2))
        self.wait(1)




class vabs_20(Scene):
    def construct(self):
        f = [
            MathTex(r"\left|x-5\right|=", r"-3"),
            t(r"el resultado NO puede ser negativo"),
            MathTex(r"\left|x-5\right|=", r"3"),
            mt(r"|u|=u"),
            mt(r"u=x-5"),
            
            mt(r"|u|=3"),
            mt(r"x-5=+3"),
            mt(r"x=3+5"),
            mt(r"x=8"),
            mt(r"|8-5|"),

            mt(r"|3|"),
            mt(r"3"),
            mt(r"|u|=-u"),
            mt(r"-u = -(x-5)"),
            mt(r"u=-x+5"),

            

            # 15
            mt(r"|u|=3"),
            mt(r"-x+5=3"),
            mt(r"-x=3-5"),
            mt(r"-x=-2"),
            mt(r"x=2"),

            mt(r"|2-5|"),
            mt(r"|-3|"),
            mt(r"3"),
        ]

        self.play(Write(f[0]))
        self.wait(1)
        self.play(Write(f[1].next_to(f[0], DOWN)), run_time=0.8)
        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(f[1], f[0]), f[2]))
        self.wait(1)
        self.play(f[2].animate.shift(UP*3).shift(LEFT*3))
        # self.play(f[3].animate.next_to(f[2], RIGHT, buff=1))
        # self.wait(1)
        # self.play(f[4].animate.next_to(f[3], DOWN))
        # self.wait(1)
        # self.play(f[5].animate.next_to(f[4], DOWN))
        # self.wait(1)
        self.play(
            VGroup(f[3], f[4], f[5]).animate.arrange(DOWN, aligned_edge = LEFT).next_to(f[2], buff=3)
        )        
        self.wait(1)

        self.play(TransformFromCopy(VGroup(f[4], f[5]), f[6]))
        self.wait(1)
        for i in range (6, 8):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)
        self.play(f[8].animate.next_to(f[2], DOWN))
        self.wait(1)
        self.play(TransformFromCopy(VGroup(f[2], f[8]), f[9]))
        self.wait(1)
        for i in range (9, 11):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)

        self.play(Circumscribe(VGroup(f[3], f[4], f[5])))
        self.wait(1)
        self.play(FadeOut(f[11]), 
                  TransformMatchingShapes(f[3], f[12].move_to(f[3])),
                  
                )
                
        self.wait(1)
        self.play(TransformMatchingShapes(f[4], f[13].move_to(f[4])), )
        self.wait(1)
        self.play(TransformMatchingShapes(f[13], f[14].move_to(f[13])))
        self.wait(1)
        # self.play(TransformMatchingShapes(f[5], f[15].move_to(f[5])))
        # self.wait(1)

        self.play(TransformFromCopy(VGroup(f[14], f[15]), f[16]))
        self.wait(1)
        for i in range (16, 19):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)
        self.play(f[19].animate.next_to(f[8], DOWN))
        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(f[19], f[2]).copy(), f[20]))
        self.wait(1)

        for i in range (20, 22):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)
        
        self.play(
            FadeOut(f[5], f[12], f[14], f[22]),
            VGroup(f[2], f[19], f[8]).animate.arrange(DOWN)
        )
        self.wait(1)



class vabs_30(Scene):
    def construct(self):
        f = [

            mt(r"|ab|=|a||b|"),
            mt(r"|4 \cdot 2|"),
            mt(r"|8|"),
            mt(r"8"),
            mt(r"|4| \cdot|2|"),

            mt(r"4 \cdot 2 "),
            mt(r"8"),
            mt(r"|-5 \cdot 10|"),
            mt(r"|-50|"),
            mt(r"50"),

            mt(r"|-5| \cdot |10|"),
            mt(r"5\cdot 10"),
            mt(r"50"),
        ]

        self.play(Write(f[0]))
        self.wait(1)

        self.add(f[0].set_opacity(0))
        self.play(Write(f[1]))
        self.wait(1)
        self.play(f[1].animate.shift(UP*2))

        self.play(Write(f[2]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[2], f[3], path_arc=PI/2))
        self.wait(1)
        self.play(FadeOut(f[3]))
        self.wait(1)
        self.play(Write(f[4]))

        for i in range (4, 6):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)

        self.play(FadeOut(f[2], f[6], f[1]))
        self.wait(1)

        self.play(Write(f[7]))
        self.wait(1)
        self.play(f[7].animate.shift(UP*2))
        self.play(TransformFromCopy(f[7], f[8]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[8], f[9], path_arc=PI/2))
        self.wait(1)
        self.play(FadeOut(f[9]))
        self.wait(1)
        self.play(TransformFromCopy(f[7], f[10]))

        for i in range (10, 12):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)

        self.play(FadeOut(f[12], f[7]))
        self.wait(1)




# inicio de intervalos
class vabs_40(Scene):
    def construct(self):
        f = [
            mt(r"\begin{cases} >  & \text{mayor que} \\ <  & \text{menor que} \\ \geq  & \text{mayor o igual que} \\ \leq  & \text{menor o igual que} \end{cases}"),
            mt(r"x>2"),
            mt(r"x=2"),
            mt(r"2>2"),
            t(r"no es válido"),

            mt(r"x=3"),
            mt(r"3>2 "),
            t(r"es válido"),
            mt(r"x=1000"),
            mt(r"1000 > 2"),
            
            

            # 10
            t(r"es válido"),
            mt(r"x=2.0000001"),
            mt(r"2.0000001 > 2"),
            t(r"es válido"),
            mt(r"(2, \infty^{+})"),
            

            # 15
            mt(r"]2, \infty^{+} ["),
            mt(r"x\geq 2"),
            mt(r"2\geq 2"),
            t(r"es válido"),
            mt(r"[2, \infty^{+})"),
            

            # 20
            mt(r"[2, \infty^{+}["),
            mt(r"|x| >2"),
            mt(r"|-3| >2"),
            mt(r"3 > 2"),
            t(r"es válido"),
            
            # 25
            mt(r"|-10000| >2"),
            mt(r"10000 > 2"),
            t(r"es válido"),
            mt(r"(\infty^{-}, -2)"),
            mt(r"(\infty^{-}, -2) \cup (2, \infty^{+})"),
            

            # 30
            mt(r"x \in (\infty^{-}, -2) \cup (2, \infty^{+})"),
            mt(r"\cup"),
            t(r'implica "unión" '),
            mt(r"x \notin [-2, 2]"),
            mt(r"|x|\geq2"),
            

            mt(r"x \in (\infty^{-}, -2] \cup [2, \infty^{+})"),
            mt(r"x \notin (-2, 2)"),
        ]

        self.play(Write(f[0]), run_time=0.7)
        self.wait(1)
        self.play(FadeOut(f[0]), run_time=0.3)
        self.play(Write(f[1]))
        self.wait(1)
        self.play(f[1].animate.shift(UP))
        self.wait(1)
        self.play(Write(f[2].next_to(f[3], LEFT, buff = 2)))
        self.wait(1)
        self.play(Write(f[3]))
        self.wait(1)
        self.play(Write(f[4].next_to(f[3], DOWN)), run_time=0.7)
        self.wait(1)


        self.play(FadeOut(f[2], f[3], f[4]))
        self.wait(1)
        self.play(Write(f[5].next_to(f[6], LEFT, buff = 2)))
        self.wait(1)
        self.play(Write(f[6]))
        self.wait(1)
        self.play(Write(f[7].next_to(f[6], DOWN)))
        self.wait(1)

        self.play(FadeOut(f[5], f[6], f[7]))
        self.wait(1)
        
        self.play(Write(f[8].next_to(f[9], LEFT, buff = 2)))
        self.wait(1)
        self.play(Write(f[9]))
        self.wait(1)
        self.play(Write(f[10].next_to(f[9], DOWN)), run_time=0.7)
        self.wait(1)

        self.play(FadeOut(f[8], f[9], f[10]))
        self.wait(1)
        
        self.play(Write(f[11].next_to(f[12], LEFT, buff = 2)))
        self.wait(1)
        self.play(Write(f[12]))
        self.wait(1)
        self.play(Write(f[13].next_to(f[12], DOWN)), run_time=0.7)
        self.wait(1)

        self.play(FadeOut(f[11], f[12], f[13]))
        self.wait(1)

        self.play(Write(f[14]))
        self.wait(1)
        self.play(Write(f[15].next_to(f[14], DOWN)))
        self.wait(1)
        self.play(FadeOut(f[15], f[14]))

        self.play(TransformMatchingShapes(f[1], f[16].move_to(f[1])))
        self.wait(1)

        self.play(Write(f[2].next_to(f[3], LEFT, buff = 2)))
        self.wait(1)
        self.play(Write(f[17]))
        self.play(Write(f[18].next_to(f[17], DOWN)), run_time=0.7)
        self.wait(1)

        self.play(FadeOut(f[2], f[17], f[18]))
        self.wait(1)

        self.play(Write(f[19]))
        self.wait(1)
        self.play(Write(f[20].next_to(f[19], DOWN)))
        self.wait(1)

        self.play(FadeOut(f[19], f[20]))
        self.wait(1)

        self.play(TransformMatchingShapes(f[16], f[21].move_to(f[16])))

        self.wait(1)

        self.play(Write(f[22]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[22], f[23]))
        self.wait(1)
        self.play(Write(f[24].next_to(f[23], DOWN)))

        self.play(FadeOut(f[23], f[24]))

        self.play(Write(f[25]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[25], f[26]))
        self.wait(1)
        self.play(Write(f[27].next_to(f[26], DOWN)))
        self.wait(1)
        self.play(FadeOut(f[26], f[27]))
        self.wait(1)
        self.play(Write(f[28]))
        self.wait(1)
        self.play(Write(f[29].next_to(f[28], DOWN)))
        self.wait(1)

        self.play(Write(f[30].next_to(f[29], DOWN)))
        self.wait(1)

        self.play(FadeOut(f[28], f[29]), f[30].animate.next_to(f[21], DOWN))
        self.wait(1)

        a = VGroup(f[31], f[32]).arrange()
        self.play(Write(a.shift(UP*3).shift(RIGHT*3)))
        self.wait(1)
        self.play(Write(f[33].next_to(f[30], DOWN)))
        self.wait(1)
        self.play(FadeOut(f[33], a, f[30]),)
        self.wait(1)

        self.play(TransformMatchingShapes(f[21], f[34].move_to(f[21])))
        self.wait(1)

        self.play(Write(f[35]))
        self.wait(1)
        self.play(Write(f[36].next_to(f[35], DOWN)))
        self.wait(1)


class vabs_50(Scene):
    def construct(self):
        f= [
            mt(r"|x|\leq 5"),
            mt(r"+x\leq 5"),
            mt(r"x \in (\infty^{-}, 5]"),
            mt(r"-x\leq 5"),
            mt(r"x \geq -5"),

            mt(r"x\leq 5"),
            mt(r"x \in (-5, \infty^{+}]"),
            mt(r"x \in (\infty^{-}, 5] \cap (\infty^{-}, 5]"),
            mt(r"\cap"),
            t(r'implica "intersección" '),

            mt(r"[-5, 5]"),
            mt(r"x \in [-5, 5]"),
            mt(r"-5\leq x\leq 5"),

        ]
        self.play(Write(f[0]))
        self.wait(1)
        self.play(f[0].animate.shift(UP*3))
        self.wait(1)
        self.play(Write(f[1]))
        self.wait(1)
        self.play(Write(f[2].next_to(f[1], DOWN)))
        self.wait(1)

        self.play(FadeOut(f[1]), f[2].animate.next_to(f[0], DOWN, ))
        self.wait(1)
        self.play(Write(f[3]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[3], f[4]))
        self.wait(1)

        self.play(Write(f[6].next_to(f[4], DOWN)))
        self.wait(1)
        self.play(FadeOut(f[4]))
        self.wait(1)

        self.play(VGroup(f[2], f[6]).animate.arrange(DOWN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[2], f[6]).copy(), f[7].next_to(f[6], DOWN)))
        self.wait(1)
        self.play(FadeOut(f[2], f[6]))

        a = VGroup(f[8], f[9]).arrange()
        self.play(Write(a.shift(UP*2).shift(RIGHT*3)))
        self.wait(1)
        self.play(FadeOut(a))
        self.play(Write(f[10].next_to(f[7], DOWN)))
        self.wait(1)

        self.play(TransformMatchingShapes(f[10], f[11].move_to(f[10])))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[11] , f[7]), f[12]))
        self.wait(1)


    
class vabs_60(Scene):
    def construct(self):
        f= [
            mt(r"|x+3|<7"),
            mt(r"x+3<7"),
            mt(r"x<7-3"),
            mt(r"x<4"),
            mt(r"-(x+3)<7"),

            mt(r"-x+3 < -7"),
            mt(r"-x < -7-3"),
            mt(r"x> -10"),
            mt(r"-10<x<4"),
            mt(r"x \in ]-10, 4["),

            mt(r"x \in (-10, 4)"),

        ]

        self.play(Write(f[0]))
        self.wait(1)
        self.play(f[0].animate.shift(UP*3))
        self.wait(1)
        self.play(Write(f[1]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[1], f[2], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[2], f[3], path_arc = PI/2))
        self.wait(1)

        self.play(f[3].animate.next_to(f[0], DOWN))
        self.wait(1)

        self.play(Write(f[4]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[4], f[5], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[5], f[6], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[6], f[7], path_arc = PI/2))
        self.wait(1)

        self.play(f[7].animate.next_to(f[3], DOWN))
        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(f[3], f[7]).copy(), f[8], path_arc = PI/2))
        self.wait(1)

        self.play(f[9].animate.next_to(f[8], DOWN))
        self.wait(1)

        self.play(f[10].animate.next_to(f[9], DOWN))
        self.wait(1)

        self.play(
            FadeOut(f[3], f[7], f[9]),
            VGroup(f[0], f[8], f[10]).animate.arrange(DOWN),
        )
        self.wait(1)





    
class vabs_70(Scene):
    def construct(self):
        f= [

            mt(r"8\leq |-4x - 12| < 20 "),
            mt(r"8\leq |(-4)(x+3)|<20"),
            mt(r"8\leq|-4| \cdot |x+3| < 20"),
            mt(r"8\leq 4 |x+3| <20"),
            mt(r"\frac{8}{4}\leq |x+3| < \frac{20}{4}"),

            mt(r"2\leq |x+3| < 5"),
            mt(r"2\leq x+3<5"),
            mt(r"2-3\leq x<5-3"),
            mt(r"-1\leq x<2"),
            mt(r"x \in [-1, 2)"),

            mt(r"2\leq (-1)(x+3)<5"),
            mt(r"-2\geq x+3>-5"),
            mt(r"-2-3\geq x>-5-3"),
            mt(r"-5\geq x>-8"),
            mt(r"-8<x\leq-5"),


            # 15
            mt(r"x \in (-8, -5]"),
            mt(r"x=0"),
            mt(r"8\leq |-4(0) - 12| < 20 "),
            mt(r"8\leq|-12|<20"),
            mt(r"8\leq 12 < 20 "),

            t(r"si cumple"),
            mt(r"x=-7"),
            mt(r"8\leq |-4(-7) - 12| < 20 "),
            mt(r"8\leq|28-12|<20"),
            mt(r"8\leq|16|<20"),

            mt(r"8\leq 16 < 20"),
            t(r"si cumple"),
            mt(r"x \in (-8, -5] \cup [-1, 2)"),

        ]

        self.play(Write(f[0]))
        self.wait(1)
        a = f[0].copy()
        self.play(a.animate.shift(DOWN*3).shift(RIGHT*3))
        self.wait(1)
        for i in range(5):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)

        self.play(f[5].animate.shift(UP*3))
        self.wait(1)

        self.play(Write(f[6]))
        self.wait(1)
        for i in range(6, 8):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)
        
        self.play(f[9].animate.next_to(f[8], DOWN))
        self.wait(1)
        self.play(FadeOut(f[8]), f[9].animate.next_to(f[5], DOWN))
        self.wait(1)
        self.play(Write(f[10]))

        for i in range(10, 14):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)

        self.play(f[15].animate.next_to(f[14], DOWN))
        self.wait(1)
        self.play(FadeOut(f[14]), f[15].animate.next_to(f[9], DOWN))

        self.play(
            a.animate.move_to(f[5]),
            FadeOut(f[5]))
        self.wait(1)


        self.play(Circumscribe(f[9]))
        self.wait(1)

        self.play(Write(f[16].next_to(f[7], LEFT, buff=2)))
        self.wait(1)

        self.play(TransformFromCopy(VGroup(f[16], a), f[17]))
        self.wait(1)

        for i in range(17, 19):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)

        self.play(f[20].animate.next_to(f[19], DOWN))
        self.wait(1)
        self.play(FadeOut(f[19], f[20], f[16]))
        self.wait(1)


        self.play(Circumscribe(f[15]))
        self.wait(1)

        self.play(Write(f[21].next_to(f[22], LEFT, buff=2)))
        self.wait(1)

        self.play(TransformFromCopy(VGroup(f[21], a), f[22]))
        self.wait(1)

        for i in range(22, 25):
            self.play(TransformMatchingShapes(f[i], f[i+1], path_arc=PI/2))
            self.wait(1)

        self.play(f[26].animate.next_to(f[25], DOWN))
        self.wait(1)

        self.play(FadeOut(f[25], f[21], f[26]))
        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(f[9], f[15]), f[27]))
        self.wait(1)

        self.play(VGroup(a, f[27]).animate.arrange(DOWN))
        self.wait(1)
        


        

        

        



def mt(t: str):
    return MathTex(t)

def t(t: str):
    return Tex(t)