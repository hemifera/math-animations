from manim import *
import sys, os, math


class tcp_00(Scene):
    def construct(self):
        img = ImageMobject("img/udb_logo_high.png")
        t1 = Text(r"Trinomios")
        t2 = Text("(trinomio cuadrado perfecto)", font_size=38)
        # t3 = Text("Caso de factoreo 3", font_size=32)
        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))


class tcp_01(Scene):
    def construct(self):
        f1 = MathTex(r"a^{2} + 2ab+b^{2}")
        f2 = MathTex(r"(a + b)^{2}")
        self.play(Write(f1.shift(UP)))
        self.wait(2)
        self.play(
            TransformMatchingShapes(
                f1.copy(),
                f2,
            )
        )
        self.wait(2)


class tcp_02(Scene):
    def construct(self):
        f = [
            MathTex(r"(a+b)^{2}"),
            MathTex(r"(a+b)(a+b)"),
            MathTex(r"a\cdot a + a\cdot b + b\cdot a + b\cdot b"),
            MathTex(r"a^{2} + 2ab + b^{2}"),
        ]
        self.play(Create(f[0]))
        self.wait(2)

        self.play(
            f[0].animate.shift(UP),
            TransformMatchingShapes(
                f[0].copy(),
                f[1],
            ),
        )
        self.wait(2)
        self.play(
            TransformMatchingShapes(
                f[1],
                f[2],
                path_along_arc=PI / 2,
            )
        )
        self.wait(2)
        self.play(
            FadeOut(f[0]),
            f[2].animate.shift(UP),
            TransformMatchingShapes(
                f[2].copy(),
                f[3],
                path_along_arc=PI / 2,
            ),
        )
        self.wait(2)


class tcp_03(Scene):
    def construct(self):
        f = [
            MathTex(r"{{9x^{2}}}+{{12xy}}+{{4y^{2}}}"),
            MathTex(r"9x^{2}"),
            MathTex(r"12xy"),
            MathTex(r"4y^{2}"),
            MathTex(r"a^{2}"),
            MathTex(r"2ab"),
            MathTex(r"b^{2}"),
            MathTex(r"a"),
            MathTex(r"b"),
            MathTex(r"\sqrt{ 9x^{2} }"),
            MathTex(r"\sqrt{ 4y^{2} } "),
            MathTex(r"3x"),
            MathTex(r"2y "),
            MathTex(r"2({{3x}})({{2y}})"),
            MathTex(r"({{3x}}+{{2y}})^{2}"),
        ]

        self.play(Create(f[0].shift(UP * 1.5)))
        self.wait(2)
        v0 = VGroup(f[1], f[2], f[3]).arrange(RIGHT, buff=1)
        v1 = VGroup(f[4], f[5], f[6]).arrange(RIGHT, buff=1)
        v2 = VGroup(v1, v0).arrange(DOWN, buff=0.3)

        self.play(TransformMatchingTex(f[0].copy(), v0), Wait(2), FadeIn(v1))
        self.wait(2)
        f[7].move_to(f[4])
        f[8].move_to(f[6])

        f[9].move_to(f[1])
        f[11].move_to(f[1])

        f[10].move_to(f[3])
        f[12].move_to(f[3])
        self.play(
            TransformMatchingShapes(
                Group(f[4], f[6]),
                Group(f[7], f[8]),
                key_map={r"a^{2}": r"a", r"b^{2}": r"b"},
            ),
            TransformMatchingShapes(
                Group(f[1], f[3]),
                Group(f[9], f[10]),
                key_map={
                    f[9].tex_string: f[1].tex_string,
                    f[3].tex_string: f[10].tex_string,
                },
            ),
        )
        self.wait(2)
        self.play(
            TransformMatchingShapes(f[9], f[11], fade_transform_mismatches=True),
            TransformMatchingShapes(f[10], f[12], fade_transform_mismatches=True),
        )
        self.wait(2)

        self.play(
            # Write(f[13].shift(DOWN*2.5)),
            TransformMatchingTex(
                Group(f[11].copy(), f[12].copy()), f[13].shift(DOWN * 2)
            )
        )
        self.wait(2)
        self.play(TransformMatchingShapes(f[13], f[2], path_along_arc=PI / 2))
        self.wait(2)

        self.play(
            TransformMatchingTex(
                Group(f[11].copy(), f[12].copy()), f[14].shift(DOWN * 2)
            )
        )
        self.wait(2)
        self.play(
            VGroup(f[0], f[14]).animate.arrange(DOWN),
            # f[0].animate.move_to(ORIGIN),
            FadeOut(Group(f[7], f[8], f[11], f[12], f[2], f[5])),
        )
        self.wait(2)


class tcp_04(Scene):
    def construct(self):
        f = [
            MathTex(r"{{3j^{2}}}-{{2jk\sqrt{ 15 }}} + {{5k^{2}}}"),
            MathTex(r"3j^{2}"),
            MathTex(r"2jk\sqrt{ 15 }"),
            MathTex(r"5k^{2}"),
            MathTex(r"a^{2}"),
            MathTex(r"2ab"),
            MathTex(r"b^{2}"),
            MathTex(r"a"),
            MathTex(r"b"),
            MathTex(r"\sqrt{ 3j^{2} }"),
            MathTex(r"\sqrt{ 5k^{2} } "),
            MathTex(r"j \sqrt{3}"),
            MathTex(r"k \sqrt{5} "),
            MathTex(r"2({{j \sqrt{3}}})({{k \sqrt{5}}})"),
            MathTex(r"({{j \sqrt{3}}}-{{k \sqrt{5}}})^{2}"),
        ]

        f1 = [
            MathTex(r"(k \sqrt{5}-j\sqrt{3})^{2}"),
            MathTex(r"k\sqrt{ 5 } - j\sqrt{ 3 }"),
            MathTex(r"(k\sqrt{ 5 } - j\sqrt{ 3 })"),
            MathTex(r"-1(j\sqrt{ 3 }-k\sqrt{ 5 })"),
            MathTex(r"[(-1)(j\sqrt{ 3 }-k\sqrt{ 5 })]^{2}"),
            MathTex(r"(-1)^{2}(j\sqrt{ 3 }-k\sqrt{ 5 })^{2} "),
            MathTex(r"(j\sqrt{ 3 }-k\sqrt{ 5 })^{2}"),
        ]

        self.play(Create(f[0].shift(UP * 1.5)))
        self.wait(2)
        v0 = VGroup(f[1], f[2], f[3]).arrange(RIGHT, buff=1)
        v1 = VGroup(f[4], f[5], f[6]).arrange(RIGHT, buff=1)
        v2 = VGroup(v1, v0).arrange(DOWN, buff=0.3)

        self.play(TransformMatchingTex(f[0].copy(), v0), Wait(2), FadeIn(v1))
        self.wait(2)
        f[7].move_to(f[4])
        f[8].move_to(f[6])

        f[9].move_to(f[1])
        f[11].move_to(f[1])

        f[10].move_to(f[3])
        f[12].move_to(f[3])
        self.play(
            TransformMatchingShapes(
                Group(f[4], f[6]),
                Group(f[7], f[8]),
                key_map={r"a^{2}": r"a", r"b^{2}": r"b"},
            ),
            TransformMatchingShapes(
                Group(f[1], f[3]),
                Group(f[9], f[10]),
                key_map={
                    f[9].tex_string: f[1].tex_string,
                    f[3].tex_string: f[10].tex_string,
                },
            ),
        )
        self.wait(2)
        self.play(
            TransformMatchingShapes(f[9], f[11], fade_transform_mismatches=True),
            TransformMatchingShapes(f[10], f[12], fade_transform_mismatches=True),
        )
        self.wait(2)

        self.play(
            # Write(f[13].shift(DOWN*2.5)),
            TransformMatchingTex(
                Group(f[11].copy(), f[12].copy()), f[13].shift(DOWN * 2)
            )
        )
        self.wait(2)
        self.play(TransformMatchingShapes(f[13], f[2], path_along_arc=PI / 2))
        self.wait(2)

        self.play(
            TransformMatchingTex(
                Group(f[11].copy(), f[12].copy()), f[14].shift(DOWN * 2)
            )
        )
        self.wait(2)
        self.play(
            VGroup(f[0], f[14]).animate.arrange(DOWN),
            # f[0].animate.move_to(ORIGIN),
            FadeOut(Group(f[7], f[8], f[11], f[12], f[2], f[5])),
        )
        self.wait(2)
        j = VGroup(f[14], f1[0])
        self.play(FadeOut(f[0]), j.animate.arrange(DOWN))
        self.wait(2)

        # f1[1].shift(DOWN*1.5)
        self.play(
            j.animate.shift(UP),
            TransformMatchingTex(f1[1].copy(), f1[2].shift(DOWN * 1.5)),
        )
        self.wait(2)
        self.play(TransformMatchingShapes(f1[2], f1[3].move_to(f1[2])))

        self.wait(2)
        self.play(TransformMatchingShapes(f1[3], f1[4].move_to(f1[3])))

        self.wait(2)
        self.play(TransformMatchingShapes(f1[4], f1[5].move_to(f1[4])))

        self.wait(2)
        self.play(TransformMatchingShapes(f1[5], f1[6].move_to(f1[5])))

        self.wait(2)


class tcp_05(Scene):
    def construct(self):
        f = [
            MathTex(r"-25bm^{2}+4an^{2} + 25am^{2} -4bn^{2} -20amn + 20bmn"),
            MathTex(r"(-25bm^{2}-4bn^{2}+20bmn)+(4an^{2}+25am^{2}-20amn)"),
            MathTex(r"b(-25m^{2}-4n^{2}+20mn)+a(4n^{2}+25m^{2}-20mn)"),
            MathTex(r"-b(25m^{2}-20mn +4n^{2})+a(25m^{2}-20mn+4n^{2})"),
            MathTex(r"(-b+a)(25m^{2}-20mn+4n^{2})"),
            MathTex(r"(a-b)(5m-2n)^{2}"),
        ]

        self.play(Write(f[0]))
        self.wait(2)

        self.play(
            f[0].animate.shift(UP),
            TransformMatchingShapes(f[0].copy(), f[1], path_along_arc=PI / 2),
        )
        self.wait(2)

        for i, eq in enumerate(f[1:-1]):
            self.play(
                FadeOut(f[i]),
                f[i + 1].animate.shift(UP),
                TransformMatchingShapes(
                    f[i + 1].copy(), f[i + 2], path_along_arc=PI / 2
                ),
            )
            self.wait(2)

        self.wait(2)
