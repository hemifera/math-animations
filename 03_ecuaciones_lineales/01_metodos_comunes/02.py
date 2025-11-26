from manim import *

class msus_00(Scene):
    def construct(self):
        img = ImageMobject("../../img/udb_logo_high.png")
        t1 = Text(r"Ecuaciones lineales")
        t2 = Text(r"Método de sustución", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))

class msus_01(Scene):
    def construct(self):
        f= [
            mt(r"2x+12y=38"),
            MathTex(r"8", r"x", r"-5y=46"),
            mt(r"x=\frac{38-12y}{2}"),
            mt(r"x=\frac{38}{2}-\frac{12}{2}y"),

            mt(r"x=19-6y \quad \text{(1)}"),
            mt(r"8(19-6y)-5y=46"),
            mt(r"(152-48y)-5y=46"),
            mt(r"152-48y-5y=46"),
            
            mt(r"-48y-5y=46-152"),
            mt(r"-53y=-106"),
            mt(r"y=\frac{-106}{-53}"),
            mt(r"y=2"),

            mt(r"x=19-6(2)"),
            mt(r"x=7"),
        ]

        ec = VGroup(f[0], f[1]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(ec), run_time = 0.5)
        self.wait(1)
        self.play(ec.animate.shift(UP*3).shift(LEFT*4.5).scale(0.9))
        self.wait(1)

        a0 = f[0].copy()
        self.play(a0.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(a0, f[2], path_arc=PI/2))
        self.wait(1)
        
        for ix in range(2, 4):
            self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)
        self.play(f[4].animate.shift(UP*3).shift(RIGHT*4.5))
        self.wait(1)

        a1 = f[1].copy()
        self.play(a1.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a1, f[4].copy()), f[5], path_arc=PI/2))
        self.wait(1)
        for ix in range(5, 11):
            self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)
        # self.play(f[11].animate.next_to(f[4], DOWN))
        # self.wait(1)

        self.play(f[11].animate.next_to(ec, DOWN))
        self.wait(1)
        a2 = f[4].copy()
        self.play(a2.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[11].copy(), a2), f[12], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[12], f[13], path_arc=PI/2))
        self.wait(1)
        v0 = VGroup(f[13], f[11])
        self.remove(f[4])
        self.play(v0.animate.arrange(DOWN))
        self.play(VGroup(ec, v0).animate.arrange(DOWN, buff=1))
        self.wait(1)


class msus_02(Scene):
    def construct(self):
        f = [
            mt(r"8u+4v+2w=67"),
            mt(r"-3u+\frac{2}{3} v -\frac{1}{3}w=-9"),
            mt(r"7v-\frac{1}{3}w=\frac{27}{4}"),
            mt(r"u=\frac{67-4v-2w}{8} \quad \text{(1)}"),

            mt(r"u=\frac{67}{8}-\frac{1}{2}v-\frac{1}{4}w"),
            mt(r"-3\left( \frac{67}{8}-\frac{1}{2}v-\frac{1}{4}w \right)+\frac{2}{3} v -\frac{1}{3}w=-9"),
            mt(r"\left( -\frac{201}{8}+\frac{3}{2}v+\frac{3}{4}w \right)+\frac{2}{3}v-\frac{1}{3}w=-9"),
            mt(r"-\frac{201}{8}+\frac{3}{2}v+\frac{3}{4}w +\frac{2}{3}v-\frac{1}{3}w=-9"),

            mt(r"-\frac{201}{8}+\left( \frac{3}{2}v +\frac{2}{3}v  \right)+ \left( \frac{3}{4}w -\frac{1}{3}w \right)=-9"),
            mt(r"\frac{13}{6}v+\frac{5}{12}w =-9 +\frac{201}{8}"),
            mt(r"\frac{13}{6}v+\frac{5}{12}w=\frac{129}{8}"),
            mt(r"\frac{13}{6}v=\frac{129}{8}-\frac{5}{12}w"),

            mt(r"v=\frac{6}{13}\left( \frac{129}{8} -\frac{5}{12}w \right)"),
            mt(r"v=\frac{387}{52}-\frac{5}{26}w \quad \text{(2)}"),
            mt(r"7\left( \frac{387}{52} -\frac{5}{26} w \right)-\frac{1}{3}w=\frac{27}{4}"),
            mt(r"\left( \frac{2709}{52}-\frac{35}{26}w \right)-\frac{1}{3}w=\frac{27}{4}"),

            mt(r"-\frac{35}{26}w-\frac{1}{3}w=\frac{27}{4}-\frac{2709}{52}"),
            mt(r"-\frac{131}{78}w=-\frac{1179}{26}"),
            mt(r"w= \frac{-\frac{1179}{26}}{-\frac{131}{78}}"),
            mt(r"w=27"),

            mt(r"v=\frac{387}{52}-\frac{5}{26}(27)"),
            mt(r"v=\frac{9}{4}"),
            mt(r"u=\frac{67-4\left( \frac{9}{4} \right)-2(27)}{8}"),
            mt(r"u=\frac{1}{2}"),

        ]

        ec = VGroup(f[0], f[1], f[2]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        self.play(Write(ec), run_time = 0.5)
        self.wait(1)
        self.play(ec.animate.shift(UP*2).shift(LEFT*4.5).scale(0.8))
        self.wait(1)

        a0 = f[0].copy()
        self.play(a0.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(a0, f[3], path_arc=PI/2))
        self.wait(1)
        self.play(f[3].animate.shift(UP*3).shift(RIGHT*4.5).scale(0.9))
        self.wait(1)

        self.play(TransformFromCopy(f[3], f[4].scale(0.8)))
        self.wait(1)

        self.play(f[4].animate.shift(DOWN*1.5))
        self.wait(1)
        # self.play
        a1 = f[1].copy()
        self.play(a1.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a1, f[4]), f[5], path_arc=PI/2))
        self.wait(1)

        for ix in range(5, 13):
            self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)

        self.play(f[13].animate.next_to(f[3], DOWN).scale(0.8))
        a2 = f[2].copy()
        self.play(a2.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a2, f[13].copy()), f[14], path_arc=PI/2))
        self.wait(1)

        for ix in range(14, 19):
            self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)

        self.play(f[19].animate.next_to(ec, DOWN, buff=1).scale(0.8))
        self.wait(1)
        a3 = f[13].copy()
        self.play(a3.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a3, f[19].copy()), f[20], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[20], f[21], path_arc=PI/2))
        self.wait(1)
        self.play(f[21].animate.next_to(f[19], DOWN).scale(0.8))
        self.wait(1)

        a4 = f[3].copy()
        self.play(a4.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a4, f[21].copy(), f[19].copy()), f[22], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[22], f[23].scale(0.8), path_arc=PI/2))
        self.wait(1)

        v0 = VGroup(f[23], f[21], f[19])
        self.remove(f[3], f[13])
        self.play(v0.animate.arrange(DOWN))
        self.play(VGroup(ec, v0).animate.arrange(DOWN, buff=1))
        self.wait(1)


class msus_03(Scene):
    def construct(self):
        f = [
            mt(r"a+b+c=9"),
            mt(r"2a-3b+5c=18"),
            mt(r"5a+2b-7c=-24"),
            mt(r"a=9-b-c \quad \text{(1)}"),

            mt(r"2(9-b-c)-3b+5c=18"),
            mt(r"(18-2b-2c)-3b+5c=18"),
            mt(r"(-2b-3b)+(-2c+5c)=18-18"),
            mt(r"-5b+3c=0"),

            mt(r"-5b=-3c"),
            mt(r"b=\frac{-3c}{-5}"),
            mt(r"b=\frac{3}{5}c \quad \text{(2)}"),
            mt(r"5(9-b-c)+2b-7c=-24"),

            mt(r"(45-5b-5c)+2b-7c=-24"),
            mt(r"(-5b+2b)+(-5c-7c)=-24-45"),
            mt(r"-3b-12c=-69"),
            mt(r"-3\left( \frac{3}{5}c \right)-12c=-69"),

            mt(r"-\frac{9}{5}c-12c=-69"),
            mt(r"-\frac{69}{5}c=-69"),
            mt(r"c=\frac{-69}{-\frac{69}{5}}"),
            mt(r"c=5"),

            mt(r"b=\frac{3}{5}(5)"),
            mt(r"b=3"),
            mt(r"a=9-3-5"),
            mt(r"a=1"),
        ]


        ec = VGroup(f[0], f[1], f[2]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        self.play(Write(ec), run_time = 0.5)
        self.wait(1)
        self.play(ec.animate.shift(UP*2).shift(LEFT*4.5))
        self.wait(1)

        a0 = f[0].copy()
        self.play(a0.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(a0, f[3], path_arc=PI/2))
        self.wait(1)
        self.play(f[3].animate.shift(UP*3).shift(RIGHT*4.5))
        self.wait(1)

        a1 = f[1].copy()
        self.play(a1.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a1, f[3].copy()), f[4], path_arc=PI/2))
        self.wait(1)

        for ix in range(4, 10):
            self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)

        self.play(f[10].animate.next_to(f[3], DOWN))
        a2 = f[2].copy()
        self.play(a2.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a2, f[3].copy()), f[11], path_arc=PI/2))
        self.wait(1)

        for ix in range(11, 14):
            self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)

        self.play(TransformMatchingShapes(VGroup(f[10].copy(), f[14]), f[15]))
        self.wait(1)

        for ix in range(15, 19):
            self.play(TransformMatchingShapes(f[ix], f[ix+1].move_to(f[ix]), path_arc = PI/2), run_time=0.8)
            self.wait(1)

        self.play(f[19].animate.next_to(ec, DOWN, buff=1))
        self.wait(1)
        a3 = f[10].copy()
        self.play(a3.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a3, f[19].copy()), f[20], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[20], f[21], path_arc=PI/2))
        self.wait(1)
        self.play(f[21].animate.next_to(f[19], DOWN))
        self.wait(1)
        
        a5 = f[3].copy() 
        self.play(a5.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(a5, f[19].copy(), f[21].copy()), f[22], path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[22], f[23], path_arc=PI/2))
        self.wait(1)

        v0 = VGroup(f[23], f[21], f[19])
        self.remove(f[3], f[10])
        self.play(v0.animate.arrange(DOWN))
        self.play(VGroup(ec, v0).animate.arrange(DOWN, buff=1))
        self.wait(1)

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
