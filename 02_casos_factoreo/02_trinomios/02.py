from manim import *

class ddp_00(Scene):
    def construct(self):
        img = ImageMobject("img/udb_logo_high.png")
        t1 = Text(r"Trinomios")
        t2 = Text("(diferencia de cuadrados perfectos)", font_size=38)
        t3 = Text("Caso de factoreo 4", font_size=32)
        v = Group(img, t1, t2, t3)
        self.add(img.scale(0.25), v.arrange(DOWN))


# Objetivo del metodo
class ddp_01(Scene):
    def construct(self):
        f = [
            MathTex(r"x^{2}-y^{2}"),
            MathTex(r"(x+y)(x-y)"),
            MathTex(r"x\cdot x + x\cdot y - y\cdot x - y\cdot y"),
            MathTex(r"x^{2}+xy-xy-y^{2}"),
            MathTex(r"x^{2}-y^{2}"),
        ]

        self.play(Write(f[0].shift(UP)))
        self.wait(2)
        self.play(
            # f[0].animate.shift(UP),
            TransformMatchingShapes(f[0].copy(), f[1]),
        )
        self.wait(2)

        self.play(
            FadeOut(f[0]),
            f[1].animate.shift(UP),
            TransformMatchingShapes(f[1].copy(), f[2]),
        )
        self.wait(2)

        self.play(
            FadeOut(f[1]),
            f[2].animate.shift(UP),
            TransformMatchingShapes(f[2].copy(), f[3]),
        )
        self.wait(2)

        self.play(
            FadeOut(f[2]),
            f[3].animate.shift(UP),
            TransformMatchingShapes(f[3].copy(), f[4]),
        )
        self.wait(2)

        self.wait(2)


class ddp_02(Scene):
    def construct(self):
        f = [
            MathTex(r"x-y"),
            MathTex(r"(\sqrt{ x }-\sqrt{ y })(\sqrt{ x }+\sqrt{ y })"),
            MathTex(
                r"(\sqrt{ x }\sqrt{ x }+\sqrt{ x }\sqrt{ y } -\sqrt{ x }\sqrt{ y }-\sqrt{ y }\sqrt{ y })"
            ),
            MathTex(r"x^{1/2}x^{1/2}- y^{1/2}y^{1/2}"),
            MathTex(r"x^{ \frac{1}{2}+\frac{1}{2} } - y^{ \frac{1}{2}+\frac{1}{2} }"),
            MathTex(r"x^{1}-y^{1}"),
            MathTex(r"x-y"),
        ]
        self.play(Write(f[0]))
        self.wait(2)
        self.play(f[0].animate.shift(UP), TransformMatchingShapes(f[0].copy(), f[1]))
        self.wait(2)

        for i in range(1, 5):
            self.play(
                FadeOut(f[i - 1]),
                f[i].animate.shift(UP),
                TransformMatchingShapes(f[i].copy(), f[i + 1]),
            )
            self.wait(2)


class ddp_03(Scene):
    def construct(self):
        f = [
            MathTex(r"81x^{8}-169"),
            MathTex(r"((81x^{8})^{1/2} + (196)^{1/2})((81x^{8})^{1/2} - (196)^{1/2})"),
            MathTex(r"(9x^{4}+13)(9x^{4}-13)"),
        ]

        self.play(Write(f[0]))
        self.wait(2)
        self.play(f[0].animate.shift(UP), TransformMatchingShapes(f[0].copy(), f[1]))
        self.wait(2)

        self.play(
            FadeOut(f[0]),
            f[1].animate.shift(UP),
            TransformMatchingShapes(f[1].copy(), f[2]),
        )

        self.wait(2)
        pass


class ddp_04(Scene):
    def construct(self):
        f = [
            MathTex(r"a^{2}+2ab+b^{2}-16"),
            MathTex(r"(a+b)^{2}-16"),
            MathTex(r"u^{2}-16"),
            MathTex(r"(u+16)(u-16)"),
            MathTex(r"(a+b+16)(a+b-16)"),
        ]
        f1 = [
            MathTex(r"u = (a+b)"),
        ]

        self.play(Write(f[0]))
        self.wait(2)
        self.play(f[0].animate.shift(UP), TransformMatchingShapes(f[0].copy(), f[1]))
        self.wait(2)
        self.play(Write(f1[0].next_to(f[1], LEFT * 3)))
        self.wait(2)

        self.play(
            f1[0].animate.shift(UP),
        )
        for i in range(1, 4):
            self.play(
                FadeOut(f[i - 1]),
                f[i].animate.shift(UP),
                TransformMatchingShapes(f[i].copy(), f[i + 1]),
            )
            self.wait(2)

        self.wait(2)


class ddp_05(Scene):
    def construct(self):
        f = [
            MathTex(r"343j^{9}+245j^{6}k-175j^{3}k^{2}-125k^{3}"),
            MathTex(r"j^{6}(343j^{3}+245k)-k^{2}(175j^{3}+125k)"),
            MathTex(r"7j^{6}(49j^{3}+35k)-5k^{2}(35j^{3}+25k)"),
            MathTex(r"7\cdot 7j^{6}(7j^{3}+5k)-5\cdot 5 k^{2}(7j^{3}+5k)"),
            MathTex(r"49j^{6}(7j^{3}+5k)-25k^{2}(7j^{3}+5k)"),
            MathTex(r"(7j^{3}+5k)(49j^{6}-25k^{2})"),
            MathTex(r"(7j^{3}+5k) \cdot (7j^{3}-5k)(7j^{3}+5k)"),
            MathTex(r"(7j^{3}+5k)^{2}(7j^{3}-5k)"),
        ]

        self.play(Write(f[0]))
        self.wait(2)
        self.play(f[0].animate.shift(UP), TransformMatchingShapes(f[0].copy(), f[1]))
        self.wait(2)

        for i in range(1, 7):
            self.play(
                FadeOut(f[i - 1]),
                f[i].animate.shift(UP),
                TransformMatchingShapes(f[i].copy(), f[i + 1]),
            )
            self.wait(2)

        self.wait(2)
