from manim import *

class migg_00(Scene):
    def construct(self):
        img = ImageMobject("../../img/udb_logo_high.png")
        t1 = Text(r"Ecuaciones lineales")
        t2 = Text(r"Método de igualación", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))

class migg_01(Scene):
    def construct(self):
        f = [
            MathTex(r"2", r"x", r"+12", r"y",  r"=38 "),
            MathTex(r"8", r"x", r"-5", r"y", r"=46"),
            t(r"es una ecuación"),
            t(r"es otra ecuación"),

            MathTex(r"x", r"\quad \text{es una variable}"),
            MathTex(r"y", r"\quad \text{es otra variable}"),
            t("Sistema de ecuaciones"),
            Paragraph("Un sistema de ecuaciones tiene que tener", "al menos la misma cantidad de variables ", "que la cantidad de ecuaciones"),

            mt(r"\text{tiene dos variables} \quad (x,y)"),
            t(r"\text{son dos ecuaciones}"),
            MathTex(r"x=", r"7"),
            MathTex(r"y=", r"2"),
            # MathTex(r"\begin{cases} x=", r"7",  r"\\ y=", r"2", r"\end{cases}"),
            MathTex(r"2", r"(7)", r"+12", r"(2)",  r"=38 "),
            MathTex(r"8", r"(7)", r"-5", r"(2)", r"=46"),

        ]

        ec = VGroup(f[0], f[1]).arrange(DOWN)
        self.play(Write(ec), run_time = 0.5)
        self.wait(1)
        self.play(
            ec.animate.shift(LEFT*2),
            Write(f[2].next_to(f[0], RIGHT), run_time = 0.5),
            Write(f[3].next_to(f[1], RIGHT), run_time = 0.5),
            run_time = 0.5
            )
        self.wait(1)
        ac = VGroup(f[4], f[5]).arrange(DOWN).shift(DOWN*2)
        self.play(Write(ac))
        self.play(Indicate(f[0][1]),  Indicate(f[1][1]), Indicate(f[4][0]), run_time = 2)
        self.wait(1)
        self.play(Indicate(f[0][3]), Indicate(f[1][3]), Indicate(f[5][0]), run_time = 2)
        self.wait(1)
        self.play(Write(f[6].shift(UP*2)), run_time = 0.5)
        self.wait(1)
        self.clear()
        self.play(Write(f[7]), run_time=1)
        self.wait(3)
        self.clear()
        self.play(Write(ec.move_to(ORIGIN)), run_time = 0.5)
        self.wait(1)
        VGroup(f[8], f[9]).arrange(DOWN).next_to(ec, DOWN)
        self.play(Write(f[8]), run_time = 0.5)
        self.wait(1)
        self.play(Write(f[9]), run_time = 0.5)
        self.wait(2)
        self.remove(f[8], f[9])
        self.wait(1)
        ac0 = VGroup(f[10], f[11]).arrange(DOWN)
        self.play(Write(ac0.next_to(ec, DOWN*1.5)), run_time=0.5)
        self.wait(1)
        ec0 = VGroup(f[12], f[13]).arrange(DOWN)
        self.play(TransformMatchingShapes(VGroup(ec, f[10][1].copy(), f[11][1].copy()) , ec0))
        self.wait(2)


class migg_02(Scene):
    def construct(self):
        f= [
            MathTex(r"2", r"x", r"+12", r"y",  r"=38 "),
            MathTex(r"8", r"x", r"-5", r"y", r"=46"),


            mt(r"2x+12y=38"),
            mt(r"2x=38-12y"),
            mt(r"x=\frac{38-12y}{2}"),

            # 5
            mt(r"x=19-6y \quad \text{(1)}"),

            # 6
            mt(r"8x-5y=46"),
            mt(r"8x=46+5y"),
            mt(r"x=\frac{46+5y}{8}"),
            mt(r"x=\frac{23}{4}+\frac{5}{8}y \quad \text{(2)}"),

            # 10
            mt(r"x=x"),
            mt(r"{{19-6y}}={{\frac{23}{4}+\frac{5}{8}y}}"),
            mt(r"-6y-\frac{5}{8}y=\frac{23}{4}-19"),
            mt(r"-\frac{53}{8}y=-\frac{53}{4}"),
            mt(r"y=\frac{-\frac{53}{4}}{-\frac{53}{8}}"),
            mt(r"y=2"),
            # 15


            mt(r"x=19-6({{2}})"),
            
            # 17
            mt(r"x=7"),


        ]

        ec = VGroup(f[0], f[1]).arrange(DOWN)
        self.play(Write(ec), run_time = 0.5)
        self.wait(1)
        self.play(ec.animate.shift(UP*3))
        self.wait(1)
        self.play(TransformFromCopy(f[0], f[2]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[2], f[3], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[3], f[4], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[4], f[5], path_arc = PI/2))
        self.wait(1)
        self.play(
            ec.animate.shift(LEFT*4),
            f[5].animate.shift(UP*3.5).shift(RIGHT*2),
        )
        # self.wait(1)

        self.play(TransformFromCopy(f[1], f[6]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[6], f[7], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[7], f[8], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[8], f[9], path_arc = PI/2))
        self.wait(1)
        self.play(
            f[9].animate.next_to(f[5], DOWN),
        )
        self.wait(1)
        self.play(Write(f[10]), run_time = 0.5)
        self.wait(1)
        self.play(ReplacementTransform(VGroup(f[5].copy(), f[9].copy(), f[10]), f[11]))
        self.wait(1)

        self.play(TransformMatchingShapes(f[11], f[12], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[12], f[13]))
        self.wait(1)
        self.play(TransformMatchingShapes(f[13], f[14], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[14], f[15], path_arc = PI/2))
        self.wait(1)

        self.play(f[15].animate.next_to(ec, DOWN))
        self.wait(1)
        e = f[5].copy()
        self.play(e.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(e, f[15].copy()), f[16], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[16], f[17], path_arc = PI/2))
        self.wait(1)
        ae = VGroup(f[17], f[15]).arrange(DOWN)
        self.remove(f[5], f[9])
        self.play(VGroup(ec, ae).animate.move_to(ORIGIN).arrange(DOWN, buff=1))
        self.wait(1)
        

class migg_03(Scene):
    def construct(self):
        f = [
            mt(r"8u+4v+2w=67"),
            mt(r"-3u+\frac{2}{3} v -\frac{1}{3}w=-9"),
            mt(r"7v-\frac{1}{3}w=\frac{27}{4}"),
            mt(r"7v=\frac{27}{4}+\frac{1}{3}w"), # repetir la 2 antes

            mt(r"v=\frac{\frac{27}{4}+\frac{1}{3}w}{7}"),
            mt(r"v=\frac{\frac{27}{4}}{7}+\frac{\frac{1}{3}w}{7}"),
            mt(r"v=\frac{27}{28}+\frac{1}{21}w \quad \text{(1)}"),
            mt(r"8u = 67-4v-2w"), #repetir la 0 antes

            mt(r"u=\frac{67-4v-2w}{8}"),
            mt(r"u=\frac{67}{8}-\frac{1}{2}v-\frac{1}{4}w \quad \text{(2)}"),
            mt(r"-3u=-9-\frac{2}{3}v+\frac{1}{3}w"),
            mt(r"u=\frac{-9-\frac{2}{3}v+\frac{1}{3}w}{-3}"),

            mt(r"u=3+\frac{2}{9}v-\frac{1}{9}w \quad \text{(3)}"),
            mt(r"u=u"),
            mt(r"\frac{67}{8}-\frac{1}{2}v-\frac{1}{4}w = 3+\frac{2}{9}v-\frac{1}{9}w"),
            mt(r"\left( -\frac{1}{2}v-\frac{2}{9}v \right)+\left( -\frac{1}{4}w+\frac{1}{9}w \right)=3-\frac{67}{8}"),

            # 16
            mt(r"-\frac{13}{18}v-\frac{5}{36}w=-\frac{43}{8}"),
            mt(r"-\frac{13}{18}v=-\frac{43}{8}+\frac{5}{36}w"),
            mt(r"v=\frac{-\frac{48}{8}+\frac{5}{36}w}{-\frac{13}{18}}"),
            mt(r"v=\frac{387}{52}-\frac{5}{26}w \quad \text{(4)}"),
            # 20
            mt(r"v=v"),
            mt(r"\frac{27}{28}+\frac{1}{21}w = \frac{387}{52}-\frac{5}{26}w"),
            mt(r"\frac{1}{21}w+\frac{5}{26}w=\frac{387}{52}-\frac{27}{28}"),
            mt(r"\frac{131}{546}w=\frac{1179}{182}"),
            # 24
            mt(r"w=\frac{\frac{1179}{182}}{\frac{131}{546}}"),
            mt(r"w=27"),
            mt(r"v=\frac{387}{52}-\frac{5}{26}(27)"), # repetir 19 antes
            mt(r"v=\frac{9}{4}"),

            mt(r"u=\frac{67}{8}-\frac{1}{2}\left( \frac{9}{4} \right)-\frac{1}{4}(27) "), # repetir 9 antes
            mt(r"u=\frac{1}{2}"),
            mt(r""),
            mt(r""),

            mt(r""),
            mt(r""),
            mt(r""),
            
        ]

        ec = VGroup(f[0], f[1], f[2]).arrange(DOWN, buff=0.1)
        self.play(Write(ec), run_time = 0.5)
        self.wait(1)
        self.play(ec.animate.shift(UP*2).shift(LEFT*4.5).scale(0.9))
        self.wait(1)

        a = f[2].copy()
        self.play(a.animate.move_to(ORIGIN))
        self.wait(1)
        
        self.play(TransformMatchingShapes(a, f[3], path_arc = PI/2), run_time=0.8)
        self.wait(1)
        for ix in range(3, 6):
            if ix in []:
                self.play(TransformMatchingShapes(f[ix], f[ix+1]), run_time=0.8)
            else:
                self.play(TransformMatchingShapes(f[ix], f[ix+1], path_arc = PI/2), run_time=0.8)
            self.wait(1)

        self.play(f[6].animate.shift(UP*3).shift(RIGHT*4).scale(0.8))
        self.wait(1)

        a1 = f[0].copy()
        self.play(a1.animate.move_to(ORIGIN))
        self.wait(1)

        self.play(TransformMatchingShapes(a1, f[7], path_arc = PI/2), run_time=0.8)
        self.wait(1)
        for ix in range(7, 9):
            if ix in []:
                self.play(TransformMatchingShapes(f[ix], f[ix+1]), run_time=0.8)
            else:
                self.play(TransformMatchingShapes(f[ix], f[ix+1], path_arc = PI/2), run_time=0.8)
            self.wait(2)
        self.play(f[9].animate.next_to(f[6], DOWN).scale(0.8))
        self.wait(1)


        a2 = f[1].copy()
        self.play(a2.animate.move_to(ORIGIN))
        self.wait(1)

        self.play(TransformMatchingShapes(a2, f[10], path_arc = PI/2))
        self.wait(1)
        for ix in range(10, 12):
            if ix in []:
                self.play(TransformMatchingShapes(f[ix], f[ix+1]), run_time=0.8)
            else:
                self.play(TransformMatchingShapes(f[ix], f[ix+1], path_arc = PI/2), run_time=0.8)
            self.wait(1)
        self.play(f[12].animate.next_to(f[9], DOWN).scale(0.8))
        self.wait(1)

        self.play(Write(f[13].shift(DOWN)), run_time=0.8)
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[9].copy(), f[12].copy(), f[13]), f[14].move_to(f[13])))
        self.wait(1)

        for ix in range(14, 19):
            if ix in [15, ]:
                self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix])), run_time=0.8)
            else:
                self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)
        
        self.play(f[19].animate.shift(DOWN*2).shift(LEFT*4).scale(0.8))
        self.wait(1)
        self.play(Write(f[20].shift(DOWN)), run_time=0.8)
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[6].copy(), f[19].copy(), f[20]), f[21].move_to(f[20])))
        self.wait(1)
        for ix in range(21, 25):
            if ix in []:
                self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix])), run_time=0.8)
            else:
                self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)

        self.play(f[25].animate.next_to(ec, DOWN))
        self.wait(1)

        a3 = f[19].copy()
        self.play(a3.animate.move_to(ORIGIN).shift(DOWN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a3, f[25].copy()), f[26].move_to(a3)))
        self.wait(1)
        self.play(TransformMatchingShapes(f[26], f[27].move_to(f[26]), path_arc = PI/2), run_time=0.8)
        self.wait(1)
        self.play(f[27].animate.next_to(f[25], DOWN))
        self.wait(1)
        a4 = f[9].copy()
        self.play(a4.animate.move_to(ORIGIN).shift(DOWN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a4, f[27].copy(), f[25].copy()), f[28].move_to(a4)))
        self.wait(1)
        self.play(TransformMatchingShapes(f[28], f[29].move_to(f[28]), path_arc = PI/2), run_time=0.8)
        self.wait(1)
        self.remove(f[6], f[9], f[12], f[19])
        self.wait(1)
        ee = VGroup(f[29], f[27], f[25])
        self.play(ee.animate.arrange(DOWN).move_to(ORIGIN).scale(0.8))
        self.play(VGroup(ec, ee).animate.arrange(DOWN, buff=1))
        self.wait(1)


class migg_04(Scene):
    def construct(self):
        f = [
            mt(r"a+b+c=9"),
            mt(r"2a-3b+5c=18"),
            mt(r"5a+2b-7c=-24"),
            mt(r"a=9-b-c \quad \text{(1)}"), #llamar 0 primero
            
            mt(r"2a=18+3b-5c"),
            mt(r"a=\frac{18+3b-5c}{2} \quad \text{(2)}"), #llamar 1 primero
            mt(r"a=a"),
            mt(r"9-b-c = \frac{18+3b-5c}{2}"),

            mt(r"2(9-b-c)=18+3b-5c"),
            mt(r"18-2b-2c=18+3b-5c"),
            mt(r"-2b-3b=(18-18) + (-5c+2c)"),
            mt(r"-5b=-3c"),

            mt(r"b=\frac{3}{5}c \quad \text{(3)}"),
            mt(r"5a=-2b+7c-24"), # llamar 2 primero
            mt(r"a=\frac{-2b+7c-24}{5} \quad \text{(4)}"),
            mt(r"a=a"),

            mt(r"\frac{18+3b-5c}{2}=\frac{-2b+7c-24}{5}"),
            mt(r"(5)(18+3b-5c)=(2)(-2b+7c-24)"),
            mt(r"90+15b-25c=-4b+14c-48"),
            mt(r"(15b+4b) +(-14c-25c)=-48-90"),
            # 20
            mt(r"19b=39c-138"),
            mt(r"b=\frac{39c-138}{19} \quad \text{(5)}"),
            mt(r"b=b"),
            mt(r"\frac{3}{5}c=\frac{39c-138}{19}"),

            mt(r"\frac{3}{5}c=\frac{39}{19}c-\frac{138}{19}"),
            mt(r"\frac{3}{5}c-\frac{39}{19}c=-\frac{138}{19}"),
            mt(r"-\frac{138}{95}c=-\frac{138}{19}"),
            mt(r"c=\frac{-\frac{138}{19}}{-\frac{138}{95}}"),

            mt(r"c=5"),
            mt(r"b=\frac{3}{5}(5)"), #llamar la otra 
            mt(r"b=3"),
            mt(r"a=9-3-5"),

            mt(r"a=1"),
        ]

        ec = VGroup(f[0], f[1], f[2]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(ec), run_time = 0.5)
        self.wait(1)
        self.play(ec.animate.shift(UP*3).shift(LEFT*4.5).scale(0.9))
        self.wait(1)

        a = f[0].copy()
        self.play(a.animate.move_to(ORIGIN))
        self.wait(1)
        
        self.play(TransformMatchingShapes(a, f[3], path_arc = PI/2), run_time=0.8)
        self.wait(1)
        self.play(f[3].animate.shift(UP*3.5).shift(RIGHT*4.5).scale(0.9))
        self.wait(1)
        a0 = f[1].copy()
        self.play(a0.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(a0, f[4], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[4], f[5], path_arc=PI/2))
        self.wait(1)
        # self.play(TransformMatchingShapes(f[5], f[6], path_arc=PI/2))
        self.wait(1)
        self.play(f[5].animate.next_to(f[3], DOWN).scale(0.9))
        self.wait(1)
        self.play(Write(f[6]))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[3].copy(), f[5].copy(), f[6]), f[7], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[7], f[8], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[8], f[9], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[9], f[10], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[10], f[11], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[11], f[12], path_arc=PI/2))
        self.wait(1)
        self.play(f[12].animate.next_to(f[5], DOWN).scale(0.9))
        self.wait(1)
        a1 = f[2].copy()
        self.play(a1.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(a1, f[13], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[13], f[14], path_arc=PI/2))
        self.wait(1)
        self.play(f[14].animate.shift(DOWN*3).shift(LEFT*4.5).scale(0.9))
        self.wait(1)
        self.play(Write(f[15]))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[15], f[5].copy(), f[14].copy()), f[16], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[16], f[17], path_arc=PI/2))
        self.wait(1)

        for ix in range(17, 21):
            if ix in [18, ]:
                self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix])), run_time=0.8)
            else:
                self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)

        self.play(f[21].animate.shift(DOWN*3).shift(RIGHT*4.5).scale(0.9))
        self.wait(1)
        self.play(Write(f[22]))
        self.play(TransformMatchingShapes(VGroup(f[22], f[12].copy(), f[21].copy()), f[23], path_arc = PI/2), run_time=0.8)
        self.wait(1)
        
        for ix in range(23, 28):
            if ix in [18, ]:
                self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix])), run_time=0.8)
            else:
                self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)
        self.play(f[28].animate.next_to(ec, DOWN))
        self.wait(1)
        a2 = f[12].copy()
        self.play(a2.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a2, f[28].copy()), f[29], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[29], f[30], path_arc=PI/2))
        self.wait(1)
        self.play(f[30].animate.next_to(f[28], DOWN))
        self.wait(1)
        a3 = f[0].copy()
        self.play(a3.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a3, f[28].copy(), f[30].copy()), f[31], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[31], f[32], path_arc=PI/2))
        self.wait(1)


        v0 = VGroup(f[32], f[30], f[28])
        self.remove(f[3], f[5], f[12], f[14], f[21])
        self.play(v0.animate.arrange(DOWN))
        self.play(VGroup(ec, v0).animate.arrange(DOWN, buff=1))
        self.wait(1)

        # hasta 27
        # self.play(TransformMatchingShapes(f[23], f[24], path_arc=PI/2))


# Returns the mathtex equivalent of the string
def mt(t: str):
    return MathTex(t)

def t(t: str):
    return Tex(t)

def h_line(a_0: Mobject, a_1: Mobject, b_0: Mobject, b_1: Mobject):
    x0 = (a_0.get_left()[0] + a_1.get_left()[0])/2
    y0 = (a_0.get_bottom()[1] + a_1.get_top()[1])/2
    initial = Point(np.array([x0*1.1, y0, 0]))

    x1 = (b_0.get_right()[0] + b_1.get_right()[0])/2
    # y1 = (b_0.get_bottom()[1] + b_1.get_top()[1])/2
    final = Point(np.array([x1*1.1, y0, 0]))
    
    return Line(initial, final)



def v_line(a_0: Mobject, a_1: Mobject, b_0: Mobject, b_1: Mobject):
    x0 = (a_0.get_right()[0] + a_1.get_left()[0])/2
    y0 = (a_0.get_top()[1] + a_1.get_top()[1])/2
    initial = Point(np.array([x0*1.1, y0*1.1, 0]))

    # x1 = (b_0.get_right()[0] + b_1.get_left()[0])/2
    y1 = (b_0.get_bottom()[1] + b_1.get_top()[1])/2
    final = Point(np.array([x0*1.1, y1, 0]))
    
    return Line(initial, final)


def l_to_vgroup(l: list) -> VGroup:
    vg = VGroup()
    for i in l:
        for x in i:
            vg.add(x)
    return vg
