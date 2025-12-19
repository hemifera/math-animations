from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    PI,
    RIGHT,
    UP,
    Circumscribe,
    FadeOut,
    Group,
    ImageMobject,
    MathTex,
    Scene,
    Text,
    TransformFromCopy,
    TransformMatchingShapes,
    VGroup,
    Write,
)

# RLSC: Reducion lineal del seno y coseno


class rlsc_00(Scene):
    def construct(self):
        img = ImageMobject("../img/udb_logo_high.png")
        t1 = Text(r"Reducción lineal del", font_size=40)
        t2 = Text(r"seno y coseno", font_size=40)

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))


class rlsc_10(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"\cos ^{2} x ", r"= [\cos (x)]^{2}"),
            MathTex(r"\cos x^{2} ", r"= \cos (x^{2})"),
            MathTex(r"\cos ^{2} x ", r"\neq \cos x^{2}"),
            MathTex(r"\cos ^{3} 10x ", r"= [\cos (10x)]^3"),
            # 4
            MathTex(r"\cos(-\theta) = \cos(\theta)"),
            MathTex(r"\cos(-\pi)  = \cos \pi"),
            MathTex(r"\sin(-\theta) = -\sin \theta"),
            MathTex(
                r"\sin\left( -\frac{\pi}{4} \right) = -\sin\left( \frac{\pi}{4} \right)"
            ),
            # 8
            MathTex(
                r"\cos ^2{\theta}",
                r"=\frac{1}{2}+\frac{1}{2}\cos(2\theta)",
                r"= \frac{1}{2} (1+\cos 2\theta)",
            ),
            MathTex(
                r"\sin ^2{\theta}",
                r"=\frac{1}{2}-\frac{1}{2}\cos(2\theta)",
                r"= \frac{1}{2} (1-\cos 2 \theta)",
            ),
            MathTex(
                r"\sin \alpha \sin \beta",
                r"=\frac{1}{2}[\cos(\alpha-\beta)-\cos(\alpha+\beta)]",
            ),
            MathTex(
                r"\cos \alpha \cos \beta",
                r"=\frac{1}{2}[\cos (\alpha-\beta)+\cos(\alpha+\beta)]",
            ),
            # 12
            MathTex(
                r"\sin \alpha \cos \beta",
                r"=\frac{1}{2}[\sin(\alpha-\beta)+\sin(\alpha+\beta)]",
            ),
        )
        v0 = VGroup(*[f.submobjects[0:4]]).arrange(DOWN, aligned_edge=LEFT, buff=1)
        v1 = VGroup(*[f.submobjects[4:8]]).arrange_in_grid(rows=2, cols=2, buff=(1, 1))
        v2 = VGroup(*[f.submobjects[8:10]]).arrange(DOWN, aligned_edge=LEFT, buff=1)
        v3 = VGroup(*[f.submobjects[10:13]]).arrange(DOWN, aligned_edge=LEFT, buff=1)
        for m in v0:
            self.play(Write(m), run_time=0.7)
            self.wait()
        self.play(FadeOut(v0))
        self.wait()
        for m in v1:
            self.play(Write(m), run_time=0.7)
            self.wait()
        self.play(FadeOut(v1))
        self.wait()

        for m in v2:
            for sm in m:
                self.play(Write(sm), run_time=0.7)
                self.wait()
        self.play(Circumscribe(f.submobjects[8][2]))
        self.wait()
        self.play(Circumscribe(f.submobjects[9][2]))
        self.wait()
        self.play(FadeOut(v2))
        self.wait()

        for m in v3:
            for sm in m:
                self.play(Write(sm), run_time=0.7)
                self.wait()
        self.wait()
        self.wait()


class rlsc_20(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"36 \sin ^3(x)"),
            MathTex(r"=27\sin (x) -9\sin(3x)"),
            MathTex(r"36 \sin ^3(x)"),
            MathTex(r"36\sin x \sin ^{2}x"),
            # 4
            MathTex(r"36\sin x \left( \frac{1}{2}  [1-\cos(2\cdot x)] \right)"),
            MathTex(r"\frac{36}{2} \sin x (1-\cos 2x)"),
            MathTex(r"18 \sin x - 18 \sin x \cos 2x"),
            MathTex(
                r"18\sin x -18 \left( \frac{1}{2} [\sin(x-2x) + \sin(x+2x)] \right)"
            ),
            # 8
            MathTex(r"18 \sin x - 9(\sin(-x)+\sin(3x))"),
            MathTex(r"18\sin x - 9(-\sin x +\sin 3x)"),
            MathTex(r"27\sin x-9\sin 3x"),
        )

        g = VGroup(
            MathTex(
                r"\sin ^2{\theta}",
                r"= \frac{1}{2} (1-\cos 2 \theta)",
                font_size=40,
            ),
            MathTex(r"\sin(-\theta) = -\sin \theta", font_size=40),
            MathTex(
                r"\sin \alpha \cos \beta",
                r"=\frac{1}{2}[\sin(\alpha-\beta)+\sin(\alpha+\beta)]",
                font_size=40,
            ),
        ).shift(DOWN * 2)
        self.play(Write(f.submobjects[0]), run_time=0.7)
        self.wait()
        self.play(f.submobjects[0].animate.shift(LEFT * 2))
        self.wait()
        self.play(
            Write(f.submobjects[1].next_to(f.submobjects[0], RIGHT)), run_time=0.8
        )
        self.wait()
        self.play(
            FadeOut(f[1]),
            f[0].animate.move_to(ORIGIN).shift(UP * 3),
            TransformFromCopy(f[0], f[2].shift(UP)),
        )
        self.wait()

        self.play(TransformFromCopy(f[2], f[3].next_to(f[2], DOWN)))
        self.wait()
        self.play(f[3].animate.move_to(f[2]), FadeOut(f[2]))
        self.wait()

        self.play(Write(g.submobjects[0]), run_time=0.7)
        self.wait()
        self.play(TransformFromCopy(f[3], f[4].next_to(f[3], DOWN)))
        self.wait()

        self.play(f[4].animate.move_to(f[3]), FadeOut(f[3], g[0]))
        self.wait()

        self.play(TransformFromCopy(f[4], f[5].next_to(f[4], DOWN)))
        self.wait()
        self.play(f[5].animate.move_to(f[4]), FadeOut(f[4]))
        self.wait()

        self.play(TransformFromCopy(f[5], f[6].next_to(f[5], DOWN)))
        self.wait()
        self.play(Write(g.submobjects[2]), run_time=0.7)
        self.wait()

        self.play(f[6].animate.move_to(f[5]), FadeOut(f[5]))
        self.wait()

        self.play(TransformFromCopy(f[6], f[7].next_to(f[6], DOWN)))
        self.wait()
        self.play(f[7].animate.move_to(f[6]), FadeOut(f[6], g[2]))
        self.wait()

        self.play(TransformFromCopy(f[7], f[8].next_to(f[7], DOWN)))
        self.wait()
        self.play(Write(g.submobjects[1]), run_time=0.7)
        self.wait()
        self.play(f[8].animate.move_to(f[7]), FadeOut(f[7]))
        self.wait()

        self.play(TransformFromCopy(f[8], f[9].next_to(f[8], DOWN)))
        self.wait()
        self.play(f[9].animate.move_to(f[8]), FadeOut(f[8], g[1]))
        self.wait()

        self.play(TransformFromCopy(f[9], f[10].next_to(f[9], DOWN)))
        self.wait()
        self.play(f[0].animate.next_to(f[10], UP), FadeOut(f[9]))
        self.wait()

        self.wait()


class rlsc_30(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"12\cos ^3(8x)"),
            MathTex(r"=9\cos(8x)+3\cos(24x)"),
            MathTex(r"12\cos ^3(8x)"),
            MathTex(r"12\cos8x \cos ^{2}8x"),
            MathTex(r"12\cos 8x \left(  \frac{1+\cos(2 \cdot 8x)}{2}  \right)"),
            MathTex(r"6 \cos 8x (1+\cos 16x)"),
            MathTex(r"6\cos 8x + 6\cos 8x \cos 16x"),
            MathTex(
                r"6\cos 8x + 6 \left( \frac{1}{2} [\cos (8x-16x) + \cos(8x+16x)] \right)"
            ),
            MathTex(r"6 \cos 8x + 3 (\cos (-8x) + \cos 24x)"),
            MathTex(r"6\cos 8x + 3 (\cos 8x + \cos 24x)"),
            MathTex(r"6\cos 8x + 3\cos 8x + 3 \cos 24x "),
            MathTex(r"9 \cos 8x + 3 \cos 24x"),
        )
        g = VGroup(
            MathTex(r"\cos ^2{\theta}=\frac{1+\cos(2\theta)}{2}"),
            MathTex(
                r"\cos \alpha \cos \beta=\frac{1}{2}[\cos (\alpha-\beta)+\cos(\alpha+\beta)]"
            ),
        ).shift(DOWN * 3)

        self.play(Write(f.submobjects[0]), run_time=0.7)
        self.wait()
        self.play(f[0].animate.shift(LEFT * 3))
        self.wait()
        self.play(Write(f.submobjects[1].next_to(f[0], RIGHT)), run_time=0.7)
        self.wait()
        self.play(
            f[0].animate.move_to(ORIGIN).shift(UP * 3),
            FadeOut(f[1]),
            TransformFromCopy(f[0], f[2]),
        )
        self.wait()

        self.play(TransformFromCopy(f[2], f[3].next_to(f[2], DOWN)))
        self.wait()
        self.play(FadeOut(f[2]), f[3].animate.move_to(f[2]))
        self.wait()

        self.play(Write(g.submobjects[0]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[3], f[4].next_to(f[3], DOWN)))
        self.wait()
        self.play(FadeOut(f[3]), f[4].animate.move_to(f[3]))
        self.wait()

        self.play(TransformFromCopy(f[4], f[5].next_to(f[4], DOWN)), FadeOut(g[0]))
        self.wait()
        self.play(FadeOut(f[4]), f[5].animate.move_to(f[4]))
        self.wait()

        self.play(TransformFromCopy(f[5], f[6].next_to(f[5], DOWN)))
        self.wait()
        self.play(FadeOut(f[5]), f[6].animate.move_to(f[5]))
        self.wait()
        self.play(Write(g.submobjects[1]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[6], f[7].next_to(f[6], DOWN)))
        self.wait()
        self.play(FadeOut(f[6]), f[7].animate.move_to(f[6]))
        self.wait()

        for i in range(7, 11):
            if i == 7:
                self.play(
                    TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)), FadeOut(g[1])
                )
                self.wait()
            else:
                self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
                self.wait()
            self.play(FadeOut(f[i]), f[i + 1].animate.move_to(f[i]))
            self.wait()

        self.play(Group(f[0], f[11]).animate.arrange(DOWN))
        self.wait()


class rlsc_40(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"80\cos^5(22x)"),
            MathTex(r"=50\cos(22x)+25\cos(66x)+5\cos(110x)"),
            MathTex(r"80 \cos ^{5} 22x", font_size=40),
            MathTex(r"80 \cos 22 x \cos ^{4} 22x", font_size=40),
            # 4
            MathTex(r"80 \cos 22x  (\cos ^{2}22x) ^{2}", font_size=40),
            MathTex(
                r"80 \cos 22x \left( \frac{1+\cos (2 \cdot 22x)}{2} \right)^{2}",
                font_size=40,
            ),
            MathTex(r"\frac{80}{4} \cos 22x (1+ \cos 44x)^{2}", font_size=40),
            MathTex(r"20 \cos 22x (1+ 2 \cos 44x + \cos ^{2} 44x)", font_size=40),
            # 8
            MathTex(
                r"20\cos 22x + 40 \cos 22x \cos 44x + 20 \cos 22x  \cos ^{2} 44x",
                font_size=40,
            ),
            MathTex(
                r"20\cos 22x ",
                r"+ (40 \cos 22x \cos 44x) ",
                r"+ (20 \cos 22x  \cos ^{2} 44x)",
                font_size=40,
            ),
            MathTex(r"40 \cos 22x \cos 44x ", font_size=40),
            MathTex(r"\frac{40}{2} (\cos (22x-44x)+\cos (22x+44))", font_size=40),
            # 12
            MathTex(r"20  \cos 22x + 20 \cos 66x", font_size=40),
            MathTex(
                r"20\cos 22x + (20  \cos 22x + 20 \cos 66x) + (20 \cos 22x  \cos ^{2} 44x)",
                font_size=40,
            ),
            MathTex(
                r"40\cos 22x + 20 \cos 66x + ",
                r"(20 \cos 22x  \cos ^{2} 44x)",
                font_size=40,
            ),
            MathTex(r"20 \cos 22x  \cos ^{2} 44x", font_size=40),
            # 16
            MathTex(r"10 \cos 22x (1+\cos (88x))", font_size=40),
            MathTex(r"10 \cos 22x + 10 \cos 22x \cos 88x", font_size=40),
            MathTex(
                r"10 \cos 22x + 5 (\cos ( 22x -88x)+ \cos (22x+88x))", font_size=40
            ),
            MathTex(r"10 \cos 22x + 5 \cos 66x + 5 \cos 110x", font_size=40),
            # 20
            MathTex(
                r"40\cos 22x + 20 \cos 66x + (10 \cos 22x + 5 \cos 66x + 5 \cos 110x)",
                font_size=40,
            ),
            MathTex(r"50 \cos 22x + 25 \cos 66 x + 5 \cos 110x", font_size=40),
        )
        g = VGroup(
            MathTex(
                r"\cos ^2{\theta}",
                r"= \frac{1}{2} (1+\cos 2\theta)",
                font_size=40,
            ),
            MathTex(
                r"\cos \alpha \cos \beta=\frac{1}{2}[\cos (\alpha-\beta)+\cos(\alpha+\beta)]",
                font_size=40,
            ),
        ).shift(DOWN * 2)
        self.play(Write(f.submobjects[0]), run_time=0.7)

        self.play(f.submobjects[0].animate.shift(LEFT * 4))

        self.play(
            Write(f.submobjects[1].next_to(f.submobjects[0], RIGHT)), run_time=0.8
        )

        self.play(
            FadeOut(f[1]),
            f[0].animate.move_to(ORIGIN).shift(UP * 3),
            TransformFromCopy(f[0], f[2].shift(UP)),
        )

        for i in range(2, 4):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))

        self.play(Write(g.submobjects[0]), run_time=0.7)
        self.play(TransformFromCopy(f[4], f[5].next_to(f[4], DOWN)))
        self.play(f[5].animate.move_to(f[4]), FadeOut(f[4]))
        self.play(FadeOut(g.submobjects[0]))

        for i in range(5, 9):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            if i == 8:
                self.play(f[i + 1].animate.next_to(f[0], DOWN), FadeOut(f[i]))
            else:
                self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))

        self.play(Circumscribe(f[9][1]))
        self.play(TransformFromCopy(f[9][1], f[10]))

        self.play(Write(g.submobjects[1]), run_time=0.7)

        self.play(TransformFromCopy(f[10], f[11].next_to(f[10], DOWN)))
        self.play(f[11].animate.move_to(f[10]), FadeOut(f[10]))

        self.play(TransformFromCopy(f[11], f[12].next_to(f[11], DOWN)))
        self.play(f[12].animate.move_to(f[11]), FadeOut(f[11], g[1]))

        self.play(TransformMatchingShapes(Group(f[12], f[9]), f[13].move_to(f[9])))

        self.play(TransformMatchingShapes(f[13], f[14].move_to(f[13])))
        self.play(Circumscribe(f[14][1]))

        self.play(TransformFromCopy(f[14][1], f[15]))

        self.play(Write(g.submobjects[0]), run_time=0.7)

        self.play(TransformFromCopy(f[15], f[16].next_to(f[15], DOWN)))
        self.play(f[16].animate.move_to(f[15]), FadeOut(f[15]))
        self.play(FadeOut(g[0]))

        self.play(
            TransformFromCopy(
                f[16],
                f[17].next_to(f[16], DOWN),
            )
        )
        self.play(f[17].animate.move_to(f[16]), FadeOut(f[16]))

        self.play(TransformFromCopy(f[17], f[18].next_to(f[17], DOWN)))
        self.play(Write(g.submobjects[1]), run_time=0.7)
        self.play(f[18].animate.move_to(f[17]), FadeOut(f[17]))

        self.play(TransformFromCopy(f[18], f[19].next_to(f[18], DOWN)))
        self.play(f[19].animate.move_to(f[18]), FadeOut(f[18], g[1]))

        self.play(TransformMatchingShapes(Group(f[14], f[19]), f[20].move_to(f[14])))

        self.play(TransformMatchingShapes(f[20], f[21].move_to(f[20]), path_arc=PI / 2))
        self.play(Group(f[0], f[21]).animate.arrange(DOWN))

        self.wait()


class rlsc_50(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"64\cos^6(5x)", font_size=40),
            MathTex(r"=20+30\cos(10x)+12\cos(20x)+2\cos(30x)", font_size=40),
            MathTex(r"64\cos^6 5x", font_size=40),
            MathTex(r"64 (\cos ^{2}5x) ^{3}", font_size=40),
            # 4
            MathTex(r"64 \left( \frac{1 + \cos (10x)}{2} \right)^{3}", font_size=40),
            MathTex(r"8(1  + 3\cos 10x + 3\cos ^{2}10x+ \cos ^{3}10x)", font_size=40),
            MathTex(
                r"8+24\cos 10 x + 24\cos ^{2}10x + 8 \cos 10x \cos ^{2}10x",
                font_size=40,
            ),
            MathTex(
                r"8 + 24\cos 10 x + \frac{24}{2} (1+\cos 20x) + \frac{8}{2} \cos 10x (1+\cos 20 x)",
                font_size=40,
            ),
            # 8
            MathTex(
                r"8 +24 \cos 10x + (12 + 12 \cos 20x) + (4 \cos 10x + 4 \cos 10x \cos 20 x)",
                font_size=40,
            ),
            MathTex(
                r"20 + 28 \cos 10 x + 12 \cos 20 x + 4 \cos 10x \cos 20x", font_size=40
            ),
            MathTex(
                r"20 + 28 \cos 10x + 12\cos 20x + 2 (\cos (10x-20x)+ \cos(10x+20x))",
                font_size=40,
            ),
            MathTex(
                r"20 + 28 \cos 10x + 12 \cos 20x + 2\cos 10x + 2 \cos 30x", font_size=40
            ),
            MathTex(r"20 + 30 \cos 10x + 12\cos 20x +2 \cos 30x", font_size=40),
        )

        g = VGroup(
            MathTex(
                r"\cos ^2{\theta}",
                r"= \frac{1}{2} (1+\cos 2\theta)",
                font_size=40,
            ),
            MathTex(
                r"(a+b)^{3}=a^{3}+3a^{2}b+3ab^{2}+b^{3}",
                font_size=40,
            ),
            MathTex(
                r"\cos \alpha \cos \beta=\frac{1}{2}[\cos (\alpha-\beta)+\cos(\alpha+\beta)]",
                font_size=40,
            ),
        ).shift(DOWN * 3)

        self.play(Write(f.submobjects[0]), run_time=0.7)
        self.wait()

        self.play(f.submobjects[0].animate.shift(LEFT * 4))
        self.wait()

        self.play(
            Write(f.submobjects[1].next_to(f.submobjects[0], RIGHT)),
            run_time=0.8,
        )
        self.wait()

        self.play(
            FadeOut(f[1]),
            f[0].animate.move_to(ORIGIN).shift(UP * 3),
            TransformFromCopy(f[0], f[2]),
        )
        self.wait()

        self.play(TransformFromCopy(f[2], f[3].next_to(f[2], DOWN)))
        self.wait()

        self.play(f[3].animate.move_to(f[2]), FadeOut(f[2]))
        self.wait()

        self.play(Write(g.submobjects[0]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[3], f[4].next_to(f[3], DOWN)))
        self.wait()
        self.play(f[4].animate.move_to(f[3]), FadeOut(f[3]), FadeOut(g[0]))
        self.wait()
        self.play(Write(g.submobjects[1]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[4], f[5].next_to(f[4], DOWN)))
        self.wait()
        self.play(f[5].animate.move_to(f[4]), FadeOut(f[4], g[1]))
        self.wait()

        self.play(TransformFromCopy(f[5], f[6].next_to(f[5], DOWN)))
        self.wait()
        self.play(f[6].animate.move_to(f[5]), FadeOut(f[5]))
        self.wait()

        self.play(Write(g.submobjects[0]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[6], f[7].next_to(f[6], DOWN)))
        self.wait()
        self.play(f[7].animate.move_to(f[6]), FadeOut(f[6], g[0]))
        self.wait()

        for i in range(7, 9):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(Write(g.submobjects[2]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[9], f[10].next_to(f[9], DOWN)))
        self.wait()
        self.play(f[10].animate.move_to(f[9]), FadeOut(f[9], g[2]))
        self.wait()

        for i in range(10, 12):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(Group(f[0], f[12]).animate.arrange(DOWN))

        self.wait()


class rlsc_60(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"64\sin^7(x)"),
            MathTex(r"=35\sin (x)-21\sin(3x)+7\sin(5x)-\sin(7x)"),
            MathTex(r"64\sin x \sin ^{6} x"),
            MathTex(r"64 \sin x (\sin ^{2} x) ^{3}"),
            # 4
            MathTex(r"64 \sin x\left( \frac{1-\cos 2x}{2} \right)^{3}"),
            MathTex(r"\frac{64}{8} \sin x (1-\cos 2x)^{3}"),
            MathTex(r"8 \sin x (1-3\cos 2x +3\cos ^{2} 2x - \cos ^{3}2x)"),
            MathTex(
                r"8\sin x ",
                r"- 24\sin x\cos 2x",
                r"+ 24 \sin x\cos ^{2}2x ",
                r"- 8 \sin x \cos ^{3} 2x ",
            ),
            # 8 y parte 1
            MathTex(r"-24 \sin x \cos 2 x"),
            MathTex(r"12 (\sin (x-2x)+\sin(x+2x))"),
            MathTex(r"-12 (-\sin(x)+ \sin 3x)"),
            MathTex(r"12\sin x -12 \sin 3x"),
            # 12
            MathTex(
                r"20 \sin x- 12 \sin 3x ",
                r"+ 24 \sin x\cos ^{2}2x ",
                r"- 8 \sin x \cos ^{3} 2x ",
            ),
            # parte 2
            MathTex(r"24 \sin x \cos ^{2} 2x"),
            MathTex(r"12 \sin x (1+ \cos 4x)"),
            MathTex(r"12 \sin x+ 12\sin x \cos 4x"),
            # 16
            MathTex(r"12 \sin x + 6 (\sin (x-4x)+\sin(x+4x))"),
            MathTex(r"12\sin x +6 (-\sin 3x + \sin 5x)"),
            MathTex(r"12 \sin x -6 \sin 3x + 6\sin 5x"),
            MathTex(r"32 \sin x - 18 \sin 3x + 6\sin 5x ", r"- 8 \sin x \cos ^{3} 2x "),
            # 20 y parte 3
            MathTex(r"-8 \sin x \cos ^{3} 2x "),
            MathTex(r"-8 \sin x \cos 2x \cos ^{2} 2x"),
            MathTex(r"-\frac{8}{2} \sin x  \cos 2x (1+ \cos 4x)"),
            MathTex(r"-\frac{4}{2} (\sin (x-2x)+ \sin(x+2x))(1+\cos 4x)"),
            # 24
            MathTex(r"-2 (-\sin x+\sin 3x)(1 + \cos 4x)"),
            MathTex(r"-2 (-\sin x  - \sin x \cos 4x + \sin 3x + \sin 3x \cos 4x)"),
            MathTex(r"2 \sin x - 2\sin 3x + 2(\sin x\cos 4x) - 2(\sin 3x \cos 4x)"),
            # 28
            MathTex(
                r"2 \sin x - 2\sin 3x + (-\sin 3x+ \sin 5x) - (-\sin x + \sin 7x )"
            ),
            MathTex(r"3 \sin x  -3 \sin 3x + \sin 5x - \sin 7x"),
            MathTex(r"35 \sin x - 21 \sin 3x + 7 \sin 5x - \sin 7x"),
        ).set_font_size(40)
        g = VGroup(
            MathTex(r"\sin ^2{\theta} = \left(  \frac{1-\cos(2\theta)}{2}  \right)"),
            MathTex(
                r"(a-b)^{3}=a^{3}-3a^{2}b+3ab^{2}-b^{3}",
            ),
            MathTex(
                r"\sin \alpha \cos \beta=\frac{1}{2}[\sin(\alpha-\beta)+\sin(\alpha+\beta)]"
            ),
            MathTex(
                r"\sin \alpha \sin \beta=\frac{1}{2}[\cos(\alpha-\beta)-\cos(\alpha+\beta)]"
            ),
            MathTex(r"\cos^2 \theta = \frac{1 + \cos 2 \theta}{2}"),
            MathTex(r""),
        ).shift(DOWN * 3)

        self.play(Write(f.submobjects[0]), run_time=0.7)
        self.wait()
        self.play(f.submobjects[0].animate.shift(LEFT * 4.5))
        self.wait()
        self.play(
            Write(f.submobjects[1].next_to(f.submobjects[0], RIGHT)),
            run_time=0.8,
        )
        self.wait()
        self.play(
            FadeOut(f[1]),
            f[0].animate.move_to(ORIGIN).shift(UP * 3),
            TransformFromCopy(f[0], f[2]),
        )
        self.wait()

        self.play(TransformFromCopy(f[2], f[3].next_to(f[2], DOWN)))
        self.wait()
        self.play(f[3].animate.move_to(f[2]), FadeOut(f[2]))
        self.wait()

        self.play(Write(g.submobjects[0]), run_time=0.7)
        self.wait()
        self.play(TransformFromCopy(f[3], f[4].next_to(f[3], DOWN)))
        self.wait()
        self.play(f[4].animate.move_to(f[3]), FadeOut(f[3], g[0]))
        self.wait()

        self.play(TransformFromCopy(f[4], f[5].next_to(f[4], DOWN)))
        self.wait()
        self.play(f[5].animate.move_to(f[4]), FadeOut(f[4]))
        self.wait()

        self.play(Write(g.submobjects[1]), run_time=0.7)
        self.wait()
        self.play(TransformFromCopy(f[5], f[6].next_to(f[5], DOWN)))
        self.wait()
        self.play(f[6].animate.move_to(f[5]), FadeOut(f[5], g[1]))
        self.wait()

        self.play(TransformFromCopy(f[6], f[7].next_to(f[6], DOWN)))
        self.wait()
        self.play(f[7].animate.next_to(f[0], DOWN), FadeOut(f[6]))
        self.wait()

        self.play(Circumscribe(f[7][1]))
        self.wait()
        self.play(TransformFromCopy(f[7], f[8]))
        self.wait()

        self.play(Write(g.submobjects[2]), run_time=0.7)
        self.wait()
        self.play(TransformFromCopy(f[8], f[9].next_to(f[8], DOWN)))
        self.wait()
        self.play(f[9].animate.move_to(f[8]), FadeOut(f[8], g[2]))
        self.wait()

        for i in range(9, 11):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(Circumscribe(f[7]))
        self.wait()
        self.play(Circumscribe(f[7][1]))
        self.wait()
        self.play(TransformMatchingShapes(Group(f[7], f[11]), f[12].move_to(f[7])))
        self.wait()

        self.play(Circumscribe(f[12][1]))
        self.wait()
        self.play(TransformFromCopy(f[12], f[13]))
        self.wait()

        self.play(Write(g.submobjects[4]), run_time=0.7)
        self.wait()
        self.play(TransformFromCopy(f[13], f[14].next_to(f[13], DOWN)))
        self.wait()
        self.play(f[14].animate.move_to(f[13]), FadeOut(f[13], g[4]))
        self.wait()

        self.play(TransformFromCopy(f[14], f[15].next_to(f[14], DOWN)))
        self.wait()
        self.play(f[15].animate.move_to(f[14]), FadeOut(f[14]))
        self.wait()

        self.play(Write(g.submobjects[2]), run_time=0.7)
        self.wait()
        self.play(TransformFromCopy(f[15], f[16].next_to(f[15], DOWN)))
        self.wait()
        self.play(f[16].animate.move_to(f[15]), FadeOut(f[15], g[2]))
        self.wait()

        for i in range(16, 18):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(Circumscribe(f[12][1]))
        self.wait()
        self.play(TransformMatchingShapes(Group(f[12], f[18]), f[19].move_to(f[12])))
        self.wait()

        self.play(Circumscribe(f[19][1]))
        self.wait()
        self.play(TransformFromCopy(f[19], f[20]))
        self.wait()

        for i in range(20, 28):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(Circumscribe(f[19][1]))
        self.wait()

        self.play(TransformMatchingShapes(Group(f[19], f[28]), f[29]))
        self.wait()
        self.play(Group(f[0], f[29]).animate.arrange(DOWN))
        self.wait()


class rlsc_70(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"32\sin^3(6x)\cos^2(8x)"),
            MathTex(
                r"-2\sin(2x)+12\sin(6x)-6\sin(10x)-4\sin(18x)+6\sin(22x)-2\sin(34x)"
            ),
            MathTex(r"32\sin^3 6x \cos^2 8x "),
            MathTex(r"32 \sin 6x \sin ^{2} 6x \cos ^{2} 8x"),
            # 4
            MathTex(
                r"32 \sin 6x \left( \frac{1-\cos 12x}{2} \right)\left( \frac{1+\cos 16x}{2} \right)"
            ),
            MathTex(r"8 \sin 6x (1-\cos 12x) (1+\cos 16x)"),
            MathTex(r"8\sin 6x (1+\cos 16x -\cos 12x - \cos 12x \cos 16x)"),
            MathTex(
                r" 8 \sin 6x + ",
                r"8\sin 6x \cos 16x ",
                r"- 8 \sin 6x \cos 12x",
                r" -8\sin 6x \cos 12x \cos 16x ",
            ),
            # parte 1 y 8
            MathTex(r"8 \sin 6x \cos 16x"),
            MathTex(r"4 (\sin (6x-16x)+\sin(6x+16x))"),
            MathTex(r"-4 \sin 10x + 4 \sin 22x "),
            MathTex(
                r"8 \sin 6x - 4 \sin 10 x + 4 \sin 22x ",
                r"- 8 \sin 6x \cos 12x ",
                r" -8\sin 6x \cos 12x \cos 16x ",
            ),
            # parte 2 y 12
            MathTex(r"-8\sin 6x \cos 12x"),
            MathTex(r"- \frac{8}{2} (\sin(6x-12x)+\sin(6x+12x))"),
            MathTex(r"4\sin 6x - 4 \sin 18x"),
            MathTex(
                r"12 \sin 6x - 4 \sin 10 x - 4 \sin 18x + 4 \sin 22x ",
                r"-8\sin 6x \cos 12x \cos 16x ",
            ),
            # parte 3 y 16
            MathTex(r"-8\sin 6x \cos 12 x \cos 16 x"),
            MathTex(r"-\frac{8}{2} \sin 6x (\cos (12x-16x)+\cos(12x+16x)) "),
            MathTex(r"-4\sin 6x (\cos 4x + \cos 28x)"),
            MathTex(r" -4\sin 6x \cos 4x - 4 \sin 6x \cos 28 x"),
            # 20
            MathTex(r" -2 (\sin (6x-4x)+\sin(6x+4x)) -2(\sin (6x-28x)+ \sin(6x+28x))"),
            MathTex(r" -2\sin 2x - 2 \sin 10x +2 \sin 22x - 2\sin 34x"),
            MathTex(
                r"-2 \sin 2x + 12 \sin 6x - 6 \sin 10 x -4 \sin 18 x + 6 \sin 22x - 2 \sin 34x"
            ),
        )
        g = VGroup(
            MathTex(r"\cos ^2{\theta} = \frac{1 + \cos 2 \theta}{2}"),
            MathTex(r"\sin ^2{\theta} = \frac{1 - \cos 2 \theta}{2}"),
            MathTex(
                r"\cos \alpha \cos \beta=\frac{1}{2}[\cos (\alpha-\beta)+\cos(\alpha+\beta)]"
            ),
            MathTex(
                r"\sin \alpha \cos \beta=\frac{1}{2}[\sin(\alpha-\beta)+\sin(\alpha+\beta)]"
            ),
            MathTex(
                r"\cos \alpha \cos \beta=\frac{1}{2}[\cos (\alpha-\beta)+\cos(\alpha+\beta)]"
            ),
        ).shift(DOWN * 3)

        for m in f:
            m.set_font_size(40)
        for m in g:
            m.set_font_size(40)

        self.play(Write(f.submobjects[0]), run_time=0.7)
        self.wait()
        # self.play(f.submobjects[0].animate.shift(LEFT * 4.5))
        self.play(
            Write(f.submobjects[1].next_to(f.submobjects[0], DOWN)),
            run_time=0.8,
        )
        self.wait()
        self.play(
            FadeOut(f[1]),
            f[0].animate.move_to(ORIGIN).shift(UP * 3),
            TransformFromCopy(f[0], f[2]),
        )
        self.wait()

        self.play(TransformFromCopy(f[2], f[3].next_to(f[2], DOWN)))
        self.wait()
        self.play(f[3].animate.move_to(f[2]), FadeOut(f[2]))
        self.wait()

        k = Group(g[0], g[1]).arrange(DOWN).shift(DOWN * 2.5)
        self.play(Write(g.submobjects[0]), Write(g.submobjects[1]), run_time=0.7)
        self.wait()
        self.play(TransformFromCopy(f[3], f[4].next_to(f[3], DOWN)))
        self.wait()
        self.play(f[4].animate.move_to(f[3]), FadeOut(f[3], k))
        self.wait()

        for i in range(4, 7):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(f[7].animate.next_to(f[0], DOWN))
        self.wait()
        self.play(Circumscribe(f[7][1]))
        self.wait()
        self.play(TransformFromCopy(f[7][1], f[8]))
        self.wait()

        self.play(Write(g.submobjects[3]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[8], f[9].next_to(f[3], DOWN)))
        self.wait()
        self.play(f[9].animate.move_to(f[8]), FadeOut(f[8], g[3]))
        self.wait()

        self.play(TransformFromCopy(f[9], f[10].next_to(f[9], DOWN)))
        self.wait()
        self.play(f[10].animate.move_to(f[9]), FadeOut(f[9]))
        self.wait()

        self.play(Circumscribe(f[7][1]))
        self.wait()
        self.play(TransformMatchingShapes(Group(f[7], f[10]), f[11].move_to(f[7])))
        self.wait()

        self.play(Circumscribe(f[11][1]))
        self.wait()

        self.play(TransformFromCopy(f[11][1], f[12]))
        self.wait()

        self.play(Write(g.submobjects[3]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[12], f[13].next_to(f[12], DOWN)))
        self.wait()
        self.play(f[13].animate.move_to(f[12]), FadeOut(f[12], g[3]))
        self.wait()

        self.play(TransformFromCopy(f[13], f[14].next_to(f[13], DOWN)))
        self.wait()
        self.play(f[14].animate.move_to(f[13]), FadeOut(f[13]))
        self.wait()

        self.play(Circumscribe(f[11][1]))
        self.wait()
        self.play(TransformMatchingShapes(Group(f[11], f[14]), f[15].move_to(f[11])))
        self.wait()

        self.play(TransformFromCopy(f[15][1], f[16]))
        self.wait()
        g[0].move_to(g[3])
        g[1].move_to(g[3])

        self.play(Write(g.submobjects[2]), run_time=0.7)
        self.wait()
        self.play(TransformFromCopy(f[16], f[17].next_to(f[16], DOWN)))
        self.wait()
        self.play(f[17].animate.move_to(f[16]), FadeOut(f[16], g[2]))
        self.wait()

        for i in range(17, 19):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(Write(g.submobjects[3]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[19], f[20].next_to(f[19], DOWN)))
        self.wait()
        self.play(f[20].animate.move_to(f[19]), FadeOut(f[19], g[3]))
        self.wait()

        self.play(TransformFromCopy(f[20], f[21].next_to(f[20], DOWN)))
        self.wait()
        self.play(f[21].animate.move_to(f[20]), FadeOut(f[20]))
        self.wait()
        self.play(Circumscribe(f[15][1]))
        self.wait()
        self.play(TransformMatchingShapes(Group(f[15], f[21]), f[22].move_to(f[15])))
        self.wait()
        self.play(Group(f[0], f[22]).animate.arrange(DOWN))
        self.wait()


class rlsc_80(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"16\sin^4(6x)\sin(8x)"),
            MathTex(r"4\sin(4x) + 6\sin(8x)-\sin(16x)-4\sin(20x)+\sin(32x)"),
            MathTex(r"16\sin^4 6x \sin 8x"),
            MathTex(r"16 \sin 8x (\sin ^{2}6x) ^{2}"),
            # 4
            MathTex(r"16 \sin 8x \left( \frac{1-\cos 12x}{2} \right)^{2}"),
            MathTex(r"\frac{16}{4} \sin 8x (1- \cos 12x)^{2}"),
            MathTex(r"4 \sin 8x ( 1- 2\cos 12 x + \cos ^{2} 12x)"),
            MathTex(
                r"4 \sin 8x ", r"- 8 \sin 8x \cos 12x ", r"+ 4 \sin 8x \cos ^{2} 12x"
            ),
            # 8
            # Parte 1
            MathTex(r"-8\sin 8x \cos 12x"),
            MathTex(r" -4 (\sin (8x -12x)+\sin (8x+12x))"),
            MathTex(r"-4 (-\sin 4x + \sin 20 x)"),
            MathTex(r"4 \sin 4x - 4 \sin 20x"),
            # 12
            MathTex(
                r"4 \sin 4x + 4 \sin 8x - 4\sin 20x ", r"+ 4 \sin 8x \cos ^{2} 12x "
            ),
            # Parte 2
            MathTex(r"4 \sin 8x \cos ^{2} 12x "),
            MathTex(r"2 \sin 8x (1+\cos 24x)"),
            MathTex(r"2 \sin 8x + 2 \sin 8x \cos 24x"),
            # 16
            MathTex(r"2 \sin 8x + \sin (8x-24x) + \sin (8x+24x)"),
            MathTex(r"2\sin 8x -\sin 16x + \sin 32 x"),
            MathTex(r"4 \sin 4x + 6 \sin 8x  - \sin 16x - 4 \sin 20x + \sin 32x "),
        )
        g = VGroup(
            MathTex(r"\sin ^2{\theta} = \frac{1 - \cos 2 \theta}{2}"),
            MathTex(
                r"\sin \alpha \cos \beta=\frac{1}{2}[\sin(\alpha-\beta)+\sin(\alpha+\beta)]"
            ),
            MathTex(r"\cos ^2{\theta} = \frac{1 + \cos 2 \theta}{2}"),
        ).shift(DOWN * 3)

        self.play(Write(f.submobjects[0]), run_time=0.7)
        self.play(
            Write(f.submobjects[1].next_to(f.submobjects[0], DOWN)),
            run_time=0.8,
        )
        self.play(
            FadeOut(f[1]),
            f[0].animate.move_to(ORIGIN).shift(UP * 3),
            TransformFromCopy(f[0], f[2]),
        )

        for i in range(2, 3):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))

        self.play(Write(g.submobjects[0]), run_time=0.7)

        self.play(TransformFromCopy(f[3], f[4].next_to(f[3], DOWN)))
        self.play(f[4].animate.move_to(f[3]), FadeOut(f[3], g[0]))

        for i in range(4, 7):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))

        self.play(f[7].animate.next_to(f[0], DOWN))
        self.play(Circumscribe(f[7][1]))
        self.play(TransformFromCopy(f[7][1], f[8]))

        self.play(Write(g.submobjects[1]), run_time=0.7)

        self.play(TransformFromCopy(f[8], f[9].next_to(f[8], DOWN)))
        self.play(f[9].animate.move_to(f[8]), FadeOut(f[8], g[1]))

        for i in range(9, 11):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))

        self.play(Circumscribe(f[7][1]))
        self.play(TransformMatchingShapes(Group(f[7], f[11]), f[12].move_to(f[7])))
        self.play(TransformFromCopy(f[12][1], f[13]))

        self.play(Write(g.submobjects[2]), run_time=0.7)

        self.play(TransformFromCopy(f[13], f[14].next_to(f[13], DOWN)))
        self.play(f[14].animate.move_to(f[13]), FadeOut(f[13], g[2]))

        for i in range(14, 15):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))

        self.play(Write(g.submobjects[1]), run_time=0.7)
        self.play(TransformFromCopy(f[15], f[16].next_to(f[15], DOWN)))
        self.play(f[16].animate.move_to(f[15]), FadeOut(f[15], g[1]))

        for i in range(16, 17):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))

        self.play(Circumscribe(f[12][1]))
        self.play(TransformMatchingShapes(Group(f[12], f[17]), f[18].move_to(f[12])))
        self.play(Group(f[0], f[18]).animate.arrange(DOWN))

        self.wait()


class rlsc_90(Scene):
    def construct(self):
        f = VGroup(
            MathTex(r"16\cos^3(7x)\cos^2(20x)"),
            MathTex(r"6\cos(7x)+\cos(19x)+2\cos(21x)+3\cos(33x)+3\cos(47x)+\cos(61x)"),
            MathTex(r"16\cos^3 7x\cos^2 20x"),
            MathTex(r"16 \cos 7x (\cos ^{2} 7x) (\cos ^{2} 20x)"),
            # 4
            MathTex(
                r"16 \cos 7x \left(  \frac{1+ \cos 14x}{2} \right)\left( \frac{1+\cos 40 x}{2} \right)"
            ),
            MathTex(r"4 \cos 7x (1+ \cos 14x) ( 1+\cos 40x)"),
            MathTex(r"4 \cos 7x (1 +\cos 40x + \cos 14x + \cos 14x \cos 40x)"),
            MathTex(
                r"4 \cos 7x + ",
                r" 4 \cos 7x \cos 40x ",
                r"+ 4 \cos 7x \cos 14x ",
                r"+ 4 \cos 7x \cos 14x \cos40x",
            ),
            # Parte 1 y 8
            MathTex(r"4 \cos 7x \cos 40x"),
            MathTex(r"2 (\cos (7x-40x)+ \cos (7x+40x))"),
            MathTex(r"2 \cos 33x + 2 \cos 47x"),
            MathTex(
                r"4 \cos 7x + 2 \cos 33x + 2\cos 47x  + ",
                r"4 \cos 7x \cos 14x ",
                r" + 4 \cos 7x \cos 14x \cos 40x ",
            ),
            # PArte 2 y 12
            MathTex(r"4 \cos 7x \cos 14x"),
            MathTex(r"2 (\cos (7x-14x)+ \cos (7x + 14x))"),
            MathTex(r"2 \cos 7x + 2 \cos 21x"),
            MathTex(
                r"6 \cos 7x + 2 \cos 21x + 2 \cos 33x + 2 \cos 47x ",
                r"+ 4 \cos 7x \cos 14x \cos 40x",
            ),
            # Parte 3 y 16
            MathTex(r"4 \cos 7x \cos 14x \cos 40x "),
            MathTex(r"2 \cos 7x (\cos (14x-40x)+ \cos (14x+40x))"),
            MathTex(r"2 \cos 7x (\cos 26x + \cos 54x)"),
            MathTex(r"2 \cos 7x \cos 26x + 2 \cos 7x \cos 54x "),
            # 20
            MathTex(r"(\cos (7x-26x)+\cos (7x+26x))+ (\cos (7x-54x)+ \cos (7x +54x))"),
            MathTex(r"\cos 19x + \cos 33x + \cos 47x + \cos 61x"),
            MathTex(
                r"6 \cos 7x + \cos 19x + 2 \cos 21x + 3 \cos 33 x + 3 \cos 47x + \cos 61x "
            ),
        )
        g = VGroup(
            MathTex(r"\cos ^2{\theta} = \frac{1 + \cos 2 \theta}{2}"),
            MathTex(
                r"\cos \alpha \cos \beta=\frac{1}{2}[\cos (\alpha-\beta)+\cos(\alpha+\beta)]"
            ),
        ).shift(DOWN * 3)

        for m in f:
            m.set_font_size(40)
        for m in g:
            m.set_font_size(40)

        self.play(Write(f.submobjects[0]), run_time=0.7)
        self.wait()
        self.play(
            Write(f.submobjects[1].next_to(f.submobjects[0], DOWN)),
            run_time=0.8,
        )
        self.wait()
        self.play(
            FadeOut(f[1]),
            f[0].animate.move_to(ORIGIN).shift(UP * 3),
            TransformFromCopy(f[0], f[2]),
        )
        self.wait()

        for i in range(2, 3):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(Write(g.submobjects[0]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[3], f[4].next_to(f[3], DOWN)))
        self.wait()
        self.play(f[4].animate.move_to(f[3]), FadeOut(f[3], g[0]))
        self.wait()

        for i in range(4, 7):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(f[7].animate.next_to(f[0], DOWN))
        self.wait()
        self.play(Circumscribe(f[7][1]))
        self.wait()
        self.play(TransformFromCopy(f[7][1], f[8]))
        self.wait()

        self.play(Write(g.submobjects[1]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[8], f[9].next_to(f[8], DOWN)))
        self.wait()
        self.play(f[9].animate.move_to(f[8]), FadeOut(f[8], g[1]))
        self.wait()

        for i in range(9, 10):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(Circumscribe(f[7][1]))
        self.wait()
        self.play(TransformMatchingShapes(Group(f[7], f[10]), f[11].move_to(f[7])))
        self.wait()

        self.play(TransformFromCopy(f[11], f[12]))
        self.wait()

        self.play(Write(g.submobjects[1]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[12], f[13].next_to(f[12], DOWN)))
        self.wait()
        self.play(f[13].animate.move_to(f[12]), FadeOut(f[12], g[1]))
        self.wait()

        for i in range(13, 14):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(Circumscribe(f[11][1]))
        self.wait()
        self.play(TransformMatchingShapes(Group(f[11], f[14]), f[15].move_to(f[11])))
        self.wait()

        self.play(TransformFromCopy(f[15], f[16]))
        self.wait()

        self.play(Write(g.submobjects[1]), run_time=0.7)
        self.wait()

        self.play(TransformFromCopy(f[16], f[17].next_to(f[16], DOWN)))
        self.wait()
        self.play(f[17].animate.move_to(f[16]), FadeOut(f[16], g[1]))
        self.wait()

        for i in range(17, 21):
            self.play(TransformFromCopy(f[i], f[i + 1].next_to(f[i], DOWN)))
            self.wait()
            self.play(f[i + 1].animate.move_to(f[i]), FadeOut(f[i]))
            self.wait()

        self.play(Circumscribe(f[15][1]))
        self.wait()
        self.play(TransformMatchingShapes(Group(f[15], f[21]), f[22].move_to(f[21])))
        self.wait()
        self.play(Group(f[0], f[22]).animate.arrange(DOWN))

        self.wait()
