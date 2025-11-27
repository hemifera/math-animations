from manim import *

class mred_00(Scene):
    def construct(self):
        img = ImageMobject("../../img/udb_logo_high.png")
        t1 = Text(r"Ecuaciones lineales")
        t2 = Text(r"Método de reducción", font_size=32) 


        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))

class mred_01(Scene):
    def construct(self):

        f = [
            mt(r"{{2x}}+{{12y}}={{38}}"),
            mt(r"{{8x}}{{-5y}}={{46}}"),
            mt(r"(5)"),
            mt(r"(12)"),

            mt(r"106x=742"),
            mt(r"x=\frac{742}{106}"),
            mt(r"x=7"),
            mt(r"2(7)+12y=38"),

            mt(r"y=\frac{38-2(7)}{12}"),
            mt(r"y=2"),
        ]
        v0 = [
                [[mt(r"2x")], [mt(r"12y")], [mt(r"=")], [t(r"38")], ],
                [[mt(r"8x")], [mt(r"-5y")], [mt(r"=")], [mt(r"46")], ],
                [[mt(r"106x")], [mt(r"0y")], [mt(r"=")], [mt(r"742")], ],
            ]
        v1 = [
                [[mt(r"10x")], [mt(r"60y")], [mt(r"=")], [t(r"190")], ],
                [[mt(r"96x")], [mt(r"-60y")], [mt(r"=")], [mt(r"552")], ],
            ]
        vv0 = l_to_vgroup(v0).arrange_in_grid(cols=4, rows=4, buff=(1.5, 0.75), )
        vv1 = l_to_vgroup(v1)
        
        for i in range(8):
            vv1[i].move_to(vv0[i])

        lh0 = h_line(vv0[4], vv0[8], vv0[7], vv0[11])

        VGroup(vv0[8], vv0[9], vv0[10],  vv0[11]).set_opacity(0)
        ec = VGroup(f[0], f[1]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        self.play(Write(ec), run_time = 0.5)
        self.wait(1)
        self.play(TransformMatchingShapes(ec, VGroup(*[vv0[i] for i in range(8)])))
        self.play(Create(lh0))
        self.wait(1)

        b0 = (VGroup(vv0[1], vv0[5]))
        b1 = (VGroup(*[vv0[i] for i in range(4)]))
        b2 = (VGroup(*[vv0[i] for i in range(4, 8)]))

        self.play(Circumscribe(b0))
        self.wait(1)
        self.play(Circumscribe(b1))
        # self.wait(1)
        # self.play(FadeOut(b1))
        self.wait(1)
        self.play(TransformFromCopy(vv0[5], f[2].next_to(vv0[3], RIGHT)))
        self.wait(1)

        self.play(Circumscribe(b2))
        self.wait(1)
        self.play(TransformFromCopy(vv0[1], f[3].next_to(vv0[7], RIGHT)))
        self.wait(1)
        
        self.play(TransformMatchingShapes(VGroup(f[2], b1), VGroup(*[vv1[i] for i in range(4)]), path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[3], b2), VGroup(*[vv1[i] for i in range(4, 8)]), path_arc = PI/2))
        self.wait(1)
        # self.play(FadeOut(Group(*[vv1[i] for i in range(8)])), FadeOut(lh0))
        self.play(FadeIn(vv0[10]))
        for i in range(4):
            if i != 2:
                self.play(Circumscribe(VGroup(vv1[i], vv1[i+4])))
                self.play(TransformFromCopy(VGroup(vv1[i], vv1[i+4]), vv0[8+i].set_opacity(1)))
                self.wait(1)
        
        e = VGroup(*[vv0[8+i] for i in range(4)])
        self.play(TransformMatchingShapes(e, f[4].move_to(e)))
        self.wait(1)
        self.play(FadeOut(VGroup(*[vv1[i] for i in range(8)])), FadeOut(lh0), f[4].animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(f[4], f[5], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[5], f[6], path_arc = PI/2))
        self.wait(1)

        self.play(ec.animate.shift(LEFT*3).shift(UP*3))
        self.play(f[6].animate.next_to(ec, DOWN))
        self.wait(1)

        ae = f[0].copy()
        self.play(ae.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(ae, f[6].copy()), f[7], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[7], f[8], path_arc = PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(f[8], f[9], path_arc = PI/2))
        self.wait(1)

        v3 = VGroup(f[6], f[9])
        # self.remove(f[3], f[10])
        self.play(v3.animate.arrange(DOWN))
        self.play(VGroup(ec, v3).animate.arrange(DOWN, buff=1))
        self.wait(1)


class mred_02(Scene):
    def construct(self):
        f= [
            mt(r"8u+4v+2w=67 "),
            mt(r"-3u+\frac{2}{3} v -\frac{1}{3}w=-9"),
            mt(r"7v-\frac{1}{3}w=\frac{27}{4}"),
            mt(r"(3)"),

            mt(r"(8)"),
            mt(r"\frac{52}{3}v +\frac{10}{3}w =129 \quad \text{(a)}"),
            mt(r"\left( \frac{52}{3} \right)"),
            mt(r"(-7)"),

            mt(r"-\frac{262}{9} w= -786"),
            mt(r"w=27"),
            mt(r"\frac{52}{3}v=129-\frac{10}{3}w"),
            mt(r"v=\frac{129-\frac{10}{3}w}{\frac{52}{3}}"),

            mt(r"v=\frac{129-\frac{10}{3}(27)}{\frac{52}{3}}"),
            mt(r"v=\frac{9}{4}"),
            mt(r"u=\frac{-9-\frac{2}{3}v+\frac{1}{3}w}{-3}"),
            mt(r"u=\frac{-9-\frac{2}{3}\left( \frac{9}{4} \right)+\frac{1}{3}(27)}{-3}"),
           
            mt(r"u=\frac{1}{2}"),
            mt(r""),
            mt(r""),

        ]

        v00 = [
                [[mt(r"8u")], [mt(r"4v")], [mt(r"2w")], [mt(r"=")], [mt(r"67")], ],
                [[mt(r"-3u")], [mt(r"\frac{2}{3} v")], [mt(r"-\frac{1}{3}w")], [mt(r"=")], [mt(r"-9")], ],
                [[mt(r"0u")], [mt(r"\frac{52}{3}v")], [mt(r"-\frac{1}{3}w")], [mt(r"=")], [mt(r"129")], ],
            ]
        v01 = [
                [[mt(r"24u")], [mt(r"12v")],[mt(r"6w")],  [mt(r"=")], [t(r"201")], ],
                [[mt(r"-24u")], [mt(r"\frac{16}{3} v")], [mt(r"-\frac{8}{3} w")], [mt(r"=")], [mt(r"-72")], ],
            ]
        

        vv00 = l_to_vgroup(v00).arrange_in_grid(cols=5, rows=4, buff=(0.5, 0.5), )
        vv01 = l_to_vgroup(v01)
        
        for i in range(10):
            vv01[i].move_to(vv00[i])

        for i in range(10, 15):
            vv00[i].set_opacity(0) 

        lh0 = h_line(vv00[5], vv00[10], vv00[9], vv00[14])
        v10 = [
                [[mt(r"7v")], [mt(r"-\frac{1}{3}w")], [mt(r"=")], [mt(r"\frac{27}{4}")], ],
                [[mt(r"\frac{52}{3}v")], [mt(r"\frac{10}{3}w")], [mt(r"=")], [mt(r"129")], ],
                [[mt(r"0v")], [mt(r"-\frac{262}{9} w")], [mt(r"=")], [mt(r"-786")], ],
            ]
        v11 = [
                [[mt(r"\frac{364}{3}v")], [mt(r"-\frac{52}{9}w")], [mt(r"=")], [t(r"117")], ],
                [[mt(r"-\frac{364}{3}v")], [mt(r"-\frac{70}{3}w")], [mt(r"=")], [mt(r"-903")], ],
            ]
        
        vv10 = l_to_vgroup(v10).arrange_in_grid(cols=4, rows=4, buff=(0.5, 0.5), )
        vv11 = l_to_vgroup(v11)
        
        for i in range(8):
            vv11[i].move_to(vv10[i])

        for i in range(8, 12):
            vv10[i].set_opacity(0) 

        lh1 = h_line(vv10[4], vv10[8], vv10[7], vv10[11])
        

        

        ec = VGroup(f[0], f[1], f[2]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        ec1 = VGroup(*[vv00[i] for i in range(5)])
        ec2 = VGroup(*[vv00[i] for i in range(5, 10)])
        ec3 = VGroup(*[vv00[i] for i in range(10, 15)])
        self.play(Write(ec), run_time = 0.5)
        self.wait(1)
        self.play(Circumscribe(VGroup(*[vv00[i] for i in range(10)])))
        self.wait(1)
        self.play(TransformMatchingShapes(
                ec.copy(), VGroup(ec1, ec2)
            ),
            ec.animate.shift(UP*2.5).shift(LEFT*5).scale(0.8)
            )
        self.play(Create(lh0))
        self.wait(1)

        self.play(Circumscribe(vv00[5]))
        self.wait(1)
        self.play(Circumscribe(ec1))
        self.wait(1)
        self.play(TransformFromCopy(vv00[5], f[3].next_to(vv00[4], RIGHT)))
        self.wait(1)

        self.play(Circumscribe(vv00[0]))
        self.wait(1)
        self.play(Circumscribe(ec2))
        self.wait(1)
        self.play(TransformFromCopy(vv00[0], f[4].next_to(vv00[9], RIGHT)))
        self.wait(1)

        # self.play(TransformMatchingShapes(VGroup(f[3]), ))
        self.play(TransformMatchingShapes(VGroup(ec1, f[3]), VGroup(*[vv01[i] for i in range(5)]), path_arc = PI/2))
        self.wait(1)    
        self.play(TransformMatchingShapes(VGroup(ec2, f[4]), VGroup(*[vv01[i] for i in range(5, 10)]), path_arc = PI/2))
        self.wait(1)      


        for i in range(5):
            if i != 3:
                self.play(Circumscribe(VGroup(vv01[i], vv01[i+5])))
                self.play(TransformFromCopy(VGroup(vv01[i], vv01[i+5]), vv00[10+i].set_opacity(1)))
                self.wait(1)


        self.play(TransformMatchingShapes(ec3, f[5].move_to(ec3)))
        self.play(FadeOut(VGroup(*[vv01[i] for i in range(10)])), FadeOut(lh0), f[5].animate.move_to(ORIGIN))
        self.wait(1)
        self.play(f[5].animate.shift(RIGHT*3).shift(UP*3).scale(0.8))
        self.wait(1)
        


        ec11 = VGroup(*[vv10[i] for i in range(4)])
        ec12 = VGroup(*[vv10[i] for i in range(4, 8)])
        ec13 = VGroup(*[vv10[i] for i in range(8, 12)])
        self.play(Circumscribe(f[2]), run_time=1)
        self.wait(1)
        self.play(TransformMatchingShapes(f[2].copy(), ec11))
        self.wait(1)
        
        self.play(Circumscribe(f[5]), run_time=1)
        self.wait(1)
        self.play(TransformMatchingShapes(f[5].copy(), ec12))
        self.play(Create(lh1))
        self.wait(1)
        self.play(Circumscribe(VGroup(vv10[0], vv10[4])))
        self.wait(1)
        self.play(Circumscribe(vv10[4]))
        self.play(TransformMatchingShapes(vv10[4].copy(), f[6].next_to(vv10[3], RIGHT)))
        self.wait(1)

        self.play(Circumscribe(vv10[0]))
        self.play(TransformMatchingShapes(vv10[0].copy(), f[7].next_to(vv10[7], RIGHT)))
        self.wait(1)

        self.play(
            TransformMatchingShapes(VGroup(ec11, f[6]), VGroup(*[vv11[i] for i in range(4)]), path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(ec12, f[7]), VGroup(*[vv11[i] for i in range(4,8)]), path_arc=PI/2))
        self.wait(1)

        for i in range(4):
            if i != 2:
                self.play(Circumscribe(VGroup(vv11[i], vv11[i+4])))
                self.play(TransformFromCopy(VGroup(vv11[i], vv11[i+4]), vv10[8+i].set_opacity(1)))
                self.wait(1)

        self.play(TransformMatchingShapes(ec13, f[8].move_to(ec13)))
        self.play(FadeOut(VGroup(*[vv11[i] for i in range(8)])), FadeOut(lh1), f[8].animate.move_to(ORIGIN), )
        self.wait(1)
        self.play(TransformMatchingShapes(f[8], f[9], path_arc=PI/2))
        self.wait(1)

        self.play(f[9].animate.next_to(ec, DOWN))
        self.wait(1)
        a=f[5].scale(1).copy()
        self.play(a.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(a, f[10], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[10], f[11], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(f[11], f[9].copy()), f[12], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[12], f[13], path_arc=PI/2))
        self.wait(1)

        self.play(f[13].animate.next_to(f[9], DOWN))
        self.wait(1)


        e=f[2].scale(1).copy()
        self.play(e.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(TransformMatchingShapes(e, f[14], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(f[14], f[9].copy(), f[13].copy()), f[15], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[15], f[16], path_arc=PI/2))
        self.wait(1)

        v3 = VGroup(f[16], f[13], f[9])
        # self.remove(f[3], f[10])
        self.play(v3.animate.arrange(DOWN), FadeOut(f[5]))
        self.play(VGroup(ec, v3).animate.arrange(DOWN, buff=1))
        self.wait(1)

class mred_03(Scene):
    def construct(self):
        f = [
            mt(r"a+b+c=9"),
            mt(r"2a-3b+5c=18"),
            mt(r"5a+2b-7c=-24"),
            mt(r"(5)"),

            mt(r"(-1)"),
            mt(r"3a+8b=27 \quad \text{(a)}"),
            mt(r"(7)"),
            mt(r"(1)"),

            mt(r"12a+9b=39 \quad \text{(b)}"),
            mt(r"(-12)"),
            mt(r"(3)"),
            mt(r"-69b=-207"),
            # 12
            mt(r"b=\frac{-207}{-69}"),
            mt(r"b=3"),
            mt(r"3a+8(3)=27"),
            mt(r"a=\frac{27-8(3)}{3}"),
            # 16
            mt(r"a=1"),
            mt(r"(1)+(3)+c=9 "),
            mt(r"c=9-1-3"),
            mt(r"c=5"),
            mt(r""),


        ]

        v00 = [
                [[mt(r"a")], [mt(r"b")], [mt(r"c")], [mt(r"=")], [mt(r"9")], ],
                [[mt(r"2a")], [mt(r"-3b")], [mt(r"5c")], [mt(r"=")], [mt(r"18")], ],
                [[mt(r"3a")], [mt(r"8b")], [mt(r"0c")], [mt(r"=")], [mt(r"27")], ],
            ]
        v01 = [
                [[mt(r"5a")], [mt(r"5b")],[mt(r"5c")],  [mt(r"=")], [mt(r"45")], ],
                [[mt(r"-2a")], [mt(r"3b")], [mt(r"-5c")], [mt(r"=")], [mt(r"-18")], ],
            ]
        vv00 = l_to_vgroup(v00).arrange_in_grid(cols=5, rows=4, buff=(0.5, 0.5), )
        vv01 = l_to_vgroup(v01)

        lh0 = h_line(vv00[5], vv00[10], vv00[9], vv00[14])
        
        for i in range(10):
            vv01[i].move_to(vv00[i])

        for i in range(10, 15):
            vv00[i].set_opacity(0) 

    
        v10 = [
                [[mt(r"a")], [mt(r"b")], [mt(r"c")], [mt(r"=")], [mt(r"9")], ],
                [[mt(r"5a")], [mt(r"2b")], [mt(r"-7c")], [mt(r"=")], [mt(r"-24")], ],
                [[mt(r"12a")], [mt(r"9b")], [mt(r"0c")], [mt(r"=")], [mt(r"39")], ],
            ]
        v11 = [
                [[mt(r"7a")], [mt(r"7b")],[mt(r"7c")],  [mt(r"=")], [mt(r"63")], ],
                [[mt(r"5a")], [mt(r"2b")], [mt(r"-7c")], [mt(r"=")], [mt(r"-24")], ],
            ]
        vv10 = l_to_vgroup(v10).arrange_in_grid(cols=5, rows=4, buff=(0.5, 0.5), )
        vv11 = l_to_vgroup(v11)

        lh1 = h_line(vv10[5], vv10[10], vv10[9], vv10[14])
        
        for i in range(10):
            vv11[i].move_to(vv10[i])

        for i in range(10, 15):
            vv10[i].set_opacity(0) 


        v20 = [
                [[mt(r"3a")], [mt(r"8b")], [mt(r"=")], [mt(r"27")], ],
                [[mt(r"12a")], [mt(r"9b")], [mt(r"=")], [mt(r"39")], ],
                [[mt(r"0a")], [mt(r"-69b")], [mt(r"=")], [mt(r"-207")], ],
            ]
        v21 = [
                [[mt(r"-36a")], [mt(r"-96b")], [mt(r"=")], [mt(r"-324")], ],
                [[mt(r"36a")], [mt(r"27b")], [mt(r"=")], [mt(r"117")], ],
            ]
        vv20 = l_to_vgroup(v20).arrange_in_grid(cols=4, rows=4, buff=(0.75, 0.75), )
        vv21 = l_to_vgroup(v21)

        lh2 = h_line(vv20[4], vv20[8], vv20[7], vv20[11])
        
        for i in range(8):
            vv21[i].move_to(vv20[i])

        for i in range(8, 12):
            vv20[i].set_opacity(0) 



        ec00 = VGroup(f[0], f[1], f[2]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        ec01 = VGroup(*[vv00[i] for i in range(5)])
        ec02 = VGroup(*[vv00[i] for i in range(5, 10)])
        ec03 = VGroup(*[vv00[i] for i in range(10, 15)])

        self.play(Write(ec00), run_time = 0.5)
        self.wait(1)
        self.play(Circumscribe(VGroup(f[0], f[1])))
        self.wait(1)
        self.play(TransformMatchingShapes(
                ec00.copy(), VGroup(ec01, ec02)
            ),
            ec00.animate.shift(UP*2.5).shift(LEFT*5).scale(0.8)
            )
        self.play(Create(lh0))
        self.wait(1)
        
        self.play(Circumscribe(VGroup(vv00[2], vv00[7])))
        self.wait(1)
        self.play(Circumscribe(vv00[7]))
        self.play(Circumscribe(ec01))
        self.wait(1)
        self.play(TransformMatchingShapes(vv00[7].copy(), f[3].next_to(vv00[4])))
        self.wait(1)

        self.play(Circumscribe(vv00[2]))
        self.play(Circumscribe(ec02))
        self.wait(1)
        self.play(TransformMatchingShapes(vv00[2].copy(), f[4].next_to(vv00[9])))
        self.wait(1)

        self.play(TransformMatchingShapes(
            VGroup(*[vv00[i] for i in range(5)], f[3]), 
            VGroup(*[vv01[i] for i in range(5)]), 
            path_arc = PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(
            VGroup(*[vv00[i] for i in range(5, 10)], f[4]), 
            VGroup(*[vv01[i] for i in range(5, 10)]), 
            path_arc = PI/2))

        self.wait(1)

        for i in range(5):
            if i != 3:
                self.play(Circumscribe(VGroup(vv01[i], vv01[i+5])))
                self.play(TransformFromCopy(VGroup(vv01[i], vv01[i+5]), vv00[10+i].set_opacity(1)))
                self.wait(1)
        
        self.play(TransformMatchingShapes(ec03, f[5].move_to(ec03)))
        self.wait(1)

        
        self.play(
            FadeOut(*[vv01[i] for i in range(10)]),
            FadeOut(lh0),
            f[5].animate.move_to(ORIGIN)
        )
        self.wait(1)
        self.play(f[5].animate.shift(RIGHT*3).shift(UP*3).scale(0.8))
        self.wait(1)
        
        

        # asasas

        # ec00 = VGroup(f[0], f[1], f[2]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        ec11 = VGroup(*[vv10[i] for i in range(5)])
        ec12 = VGroup(*[vv10[i] for i in range(5, 10)])
        ec13 = VGroup(*[vv10[i] for i in range(10, 15)])


        self.play(Circumscribe(f[0]), Circumscribe(f[2]))
        self.wait(1)
        self.play(TransformMatchingShapes(ec00.copy(), VGroup(ec11, ec12)),)
        self.play(Create(lh1))
        self.wait(1)
        
        self.play(Circumscribe(VGroup(vv10[2], vv10[7])))
        self.wait(1)
        self.play(Circumscribe(vv10[7]))
        self.play(Circumscribe(ec11))
        self.wait(1)
        self.play(TransformMatchingShapes(vv10[7].copy(), f[6].next_to(vv10[4])))
        self.wait(1)

        self.play(Circumscribe(vv10[2]))
        self.play(Circumscribe(ec12))
        self.wait(1)
        self.play(TransformMatchingShapes(vv10[2].copy(), f[7].next_to(vv10[9])))
        self.wait(1)

        self.play(TransformMatchingShapes(
            VGroup(*[vv10[i] for i in range(5)], f[6]), 
            VGroup(*[vv11[i] for i in range(5)]), 
            path_arc = PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(
            VGroup(*[vv10[i] for i in range(5, 10)], f[7]), 
            VGroup(*[vv11[i] for i in range(5, 10)]), 
            path_arc = PI/2))

        self.wait(1)

        for i in range(5):
            if i != 3:
                self.play(Circumscribe(VGroup(vv11[i], vv11[i+5])))
                self.play(TransformFromCopy(VGroup(vv11[i], vv11[i+5]), vv10[10+i].set_opacity(1)))
                self.wait(1)

        self.play(TransformMatchingShapes(ec13, f[8].move_to(ec13)))
        self.wait(1)

        self.play(
            FadeOut(*[vv11[i] for i in range(10)]),
            FadeOut(lh1),
            f[8].animate.move_to(ORIGIN)
        )
        self.wait(1)
        self.play(f[8].animate.next_to(f[5], DOWN).scale(0.8))
        self.wait(1)



        ec21 = VGroup(*[vv20[i] for i in range(4)])
        ec22 = VGroup(*[vv20[i] for i in range(4, 8)])
        ec23 = VGroup(*[vv20[i] for i in range(8, 12)])


        self.play(Circumscribe(f[5]), Circumscribe(f[8]))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[5], f[8]).copy(), VGroup(ec21, ec22)),)
        self.play(Create(lh2))
        self.wait(1)
        
        self.play(Circumscribe(VGroup(vv20[0], vv20[4])))
        self.wait(1)

        self.play(Circumscribe(vv20[4]))
        self.play(Circumscribe(ec21))
        self.wait(1)
        self.play(TransformMatchingShapes(vv20[4].copy(), f[9].next_to(vv20[3])))
        self.wait(1)

        self.play(Circumscribe(vv20[0]))
        self.play(Circumscribe(ec22))
        self.wait(1)
        self.play(TransformMatchingShapes(vv20[0].copy(), f[10].next_to(vv20[7])))
        self.wait(1)

        self.play(TransformMatchingShapes(
            VGroup(*[vv20[i] for i in range(4)], f[9]), 
            VGroup(*[vv21[i] for i in range(4)]), 
            path_arc = PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(
            VGroup(*[vv20[i] for i in range(4, 8)], f[10]), 
            VGroup(*[vv21[i] for i in range(4, 8)]), 
            path_arc = PI/2))

        self.wait(1)

        for i in range(4):
            if i != 2:
                self.play(Circumscribe(VGroup(vv21[i], vv21[i+4])))
                self.play(TransformFromCopy(VGroup(vv21[i], vv21[i+4]), vv20[8+i].set_opacity(1)))
                self.wait(1)

        self.wait(1)

        self.play(TransformMatchingShapes(ec23, f[11].move_to(ec23)))
        self.wait(1)

        self.wait(1)

        self.play(
            FadeOut(*[vv21[i] for i in range(8)]),
            FadeOut(lh2),
            f[11].animate.move_to(ORIGIN)
        )

        self.wait(1)

        self.play(TransformMatchingShapes(f[11], f[12], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[12], f[13], path_arc=PI/2))
        self.wait(1)

        self.play(f[13].animate.next_to(ec00, DOWN).scale(0.8))

        self.wait(1)

        ae = f[5].copy()
        self.play(Circumscribe(f[5]))
        self.wait(1)
        self.play(ae.animate.move_to(ORIGIN).scale(1.2))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[13].copy(), ae), f[14], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[14], f[15], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[15], f[16], path_arc=PI/2))
        self.wait(1)

        self.play(f[16].animate.next_to(f[13], DOWN).scale(0.8))
        self.wait(1)


        aee = f[0].copy()
        self.play(Circumscribe(f[0]))
        self.wait(1)
        self.play(aee.animate.move_to(ORIGIN).scale(1.2))
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(f[13].copy(), f[16].copy(), aee), f[17], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[17], f[18], path_arc=PI/2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[18], f[19].scale(0.8), path_arc=PI/2))
        self.wait(1)

        v3 = VGroup(f[16], f[13], f[19])
        # self.remove(f[3], f[10])
        self.play(v3.animate.arrange(DOWN), FadeOut(f[5], f[8]))
        self.play(VGroup(ec00, v3).animate.arrange(DOWN, buff=1))
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
