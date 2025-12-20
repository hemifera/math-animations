from manim import *
from manim.utils.rate_functions import (
    ease_in_out_cubic,
    ease_in_out_quint,
    ease_in_out_sine,
    smoothererstep,
)


class trig_00(Scene):
    def construct(self):
        img = ImageMobject("../img/udb_logo_high.png")
        t1 = Text(r"Trigonometría")
        t2 = Text(r"Teoría", font_size=32)

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))


class trig_10(Scene):
    def construct(self):
        radius = ValueTracker(1)
        theta = ValueTracker(10)
        scale_tracker = ValueTracker(10)

        ax = always_redraw(
            lambda: Axes(
                x_range=[-3, 3, 1],
                y_range=[-3, 3, 1],
                x_length=scale_tracker.get_value(),
                y_length=scale_tracker.get_value(),
                axis_config={"include_numbers": False},
                tips=False,
            )
        )
        pln = always_redraw(
            lambda: NumberPlane(
                x_range=ax.get_x_range(),
                y_range=ax.get_y_range(),
                x_length=scale_tracker.get_value(),
                y_length=scale_tracker.get_value(),
                background_line_style={"stroke_opacity": 0.4},
            )
        )

        circle = always_redraw(
            lambda: Circle(
                radius=np.linalg.norm(ax.c2p(radius.get_value(), 0) - ax.c2p(0, 0))
            ).move_to(ax.c2p(0, 0))
        )

        line0 = Line(ax.c2p(*ORIGIN), ax.c2p(*RIGHT))
        line1 = always_redraw(
            lambda: Line(
                ax.c2p(0, 0),
                ax.c2p(
                    radius.get_value() * np.cos(theta.get_value() * DEGREES),
                    radius.get_value() * np.sin(theta.get_value() * DEGREES),
                ),
                color=YELLOW,
            )
        )

        dot0 = Dot(ax.c2p(*ORIGIN))
        dot1 = always_redraw(
            lambda: Dot(
                point=ax.c2p(
                    radius.get_value() * np.cos(theta.get_value() * DEGREES),
                    radius.get_value() * np.sin(theta.get_value() * DEGREES),
                )
            )
        )

        def one_unit_scale() -> float:
            return np.linalg.norm(ax.c2p(radius.get_value(), 0) - ax.c2p(0, 0))

        def safe_angle(l0, l1, radius):
            v0 = l0.get_unit_vector()
            v1 = l1.get_unit_vector()

            dot = np.dot(v0, v1)
            if abs(dot) > 0.999:
                return VGroup()
            else:
                return Angle(l0, l1, radius=radius)

        radText = always_redraw(
            lambda: MathTex(rf"\text{{radio: }}{round(radius.get_value(), 2)}")
            .shift(DOWN)
            .shift(LEFT * 4.5)
        )
        brh = always_redraw(
            lambda: Brace(
                line1,
                sharpness=1,
                direction=line1.copy().rotate(PI / 2).get_unit_vector(),
            )
        )
        brhTex = always_redraw(lambda: brh.get_tex(r"\text{radio}"))

        theta_label = always_redraw(
            lambda: MathTex(rf"\theta: {round(theta.get_value(), 1)}^\circ").next_to(
                radText, DOWN
            )
        )

        self.wait()
        self.play(FadeIn(ax, pln))
        self.wait()
        self.play(FadeIn(circle))
        self.wait()
        self.play(FadeIn(brh, brhTex))
        self.wait()

        self.play(FadeIn(dot0, dot1, line1))
        self.wait()

        self.play(TransformMatchingShapes(brhTex, radText), FadeOut(brh))

        self.wait()

        self.play(radius.animate.set_value(2), rate_func=smooth, run_time=1)
        self.wait()
        self.play(radius.animate.set_value(1), rate_func=smooth, run_time=1)
        self.wait()

        self.play(scale_tracker.animate.set_value(20), rate_func=smooth, run_time=1)
        self.wait()

        angle = always_redraw(
            lambda: safe_angle(line0, line1, radius=one_unit_scale() * 0.25)
        )

        def angle_label_condition(angle_value):
            return ax.c2p(
                0.5 * radius.get_value() * np.cos((angle_value / 2) * PI / 180),
                0.5 * radius.get_value() * np.sin((angle_value / 2) * PI / 180),
            )

        angle_label = always_redraw(
            lambda: MathTex(
                rf"{round(theta.get_value(), 1)}^\circ",
            ).move_to(angle_label_condition(theta.get_value()))
        )

        self.play(FadeIn(angle, angle_label))
        self.wait()

        self.play(theta.animate.set_value(120), rate_func=smooth, run_time=1)
        self.wait(0.5)
        self.play(theta.animate.set_value(60), rate_func=smooth, run_time=1)
        self.wait(0.2)
        self.play(theta.animate.set_value(359.9999), rate_func=smooth, run_time=1)
        self.wait(0.3)
        self.play(theta.animate.set_value(45), rate_func=smooth, run_time=1)
        self.wait(0.5)

        self.wait()
        self.play(TransformFromCopy(angle, theta_label))

        self.wait()
        self.play(Circumscribe(dot1, Circle))
        self.wait()
        dot2 = always_redraw(
            lambda: Dot(
                point=ax.c2p(
                    radius.get_value() * np.cos(theta.get_value() * DEGREES), 0
                )
            )
        )
        ly = always_redraw(
            lambda: Line(
                np.array([dot1.get_x(), 0, 0]), dot1.get_center(), color=YELLOW
            )
        )
        self.play(FadeIn(dot2, ly))
        self.wait()

        bry = always_redraw(
            lambda: Brace(
                ly, sharpness=1, direction=ly.copy().rotate(-PI / 2).get_unit_vector()
            )
        )
        bryTex = always_redraw(
            lambda: brh.get_tex(r"\text{distancia}\\ \text{vertical}").next_to(
                bry, ax.c2p(*RIGHT)
            )
        )
        self.play(FadeIn(bry, bryTex))
        self.wait()
        self.play(Circumscribe(dot0, Circle), Circumscribe(dot2, Circle))
        self.wait()
        lx = always_redraw(
            lambda: Line(ax.c2p(*ORIGIN), np.array([dot1.get_x(), 0, 0]), color=YELLOW)
        )
        self.play(FadeIn(lx))

        brx = always_redraw(
            lambda: Brace(
                lx, sharpness=1, direction=lx.copy().rotate(-PI / 2).get_unit_vector()
            )
        )
        brxTex = always_redraw(
            lambda: brh.get_tex(r"\text{distancia horizontal}").next_to(brx, DOWN)
        )

        self.play(FadeIn(brx, brxTex))
        self.wait()

        x_label = always_redraw(
            lambda: MathTex(
                r"{}",
                round(radius.get_value() * np.cos(theta.get_value() * (PI / 180)), 3),
            ).move_to(np.array([dot1.get_x() / 2, ax.c2p(0, -0.3)[1], 0]))
        )

        y_label = always_redraw(
            lambda: MathTex(
                r"{}",
                round(radius.get_value() * np.sin(theta.get_value() * (PI / 180)), 3),
            ).move_to(np.array([dot1.get_x() + ax.c2p(0.4, 0)[0], dot1.get_y() / 2, 0]))
        )
        radY = always_redraw(
            lambda: MathTex(
                rf"\text{{d. V: }}{round(radius.get_value() * np.sin(theta.get_value() * (PI / 180)), 3)}"
            ).next_to(theta_label, DOWN)
        )
        radX = always_redraw(
            lambda: MathTex(
                rf"\text{{d. H: }}{round(radius.get_value() * np.cos(theta.get_value() * (PI / 180)), 3)}"
            ).next_to(radY, DOWN)
        )
        self.play(
            FadeOut(bry, brx),
            TransformMatchingShapes(bryTex, radY),
            TransformMatchingShapes(brxTex, radX),
            FadeIn(y_label, x_label),
        )
        item_labels = VGroup(radText, theta_label, radY, radX)
        # self.play(VGroup())
        self.play(item_labels.animate.arrange(DOWN).move_to(item_labels.get_center()))
        print(f"item labels center: {item_labels.get_center()}")

        self.play(theta.animate.set_value(0), rate_func=smooth, run_time=1.5)
        self.wait()

        self.play(theta.animate.set_value(90), rate_func=smooth, run_time=1.5)
        self.wait()

        self.play(theta.animate.set_value(180), rate_func=smooth, run_time=1.5)
        self.wait()

        self.play(theta.animate.set_value(270), rate_func=smooth, run_time=1.5)
        self.wait()

        self.play(theta.animate.set_value(360), rate_func=smooth, run_time=1.5)
        self.wait(2)

        self.play(theta.animate.set_value(30), rate_func=smooth, run_time=2)
        self.wait()

        self.play(scale_tracker.animate.set_value(12), rate_func=smooth, run_time=1)
        self.wait()

        # self.play(VGroup(ax, pln).animate.shift(RIGHT))
        self.wait()
        self.play(radius.animate.set_value(2), rate_func=smooth, run_time=1)
        self.wait()
        self.play(radius.animate.set_value(1), rate_func=smooth, run_time=1)
        self.wait()
        self.play(radius.animate.set_value(0.5), rate_func=smooth, run_time=1)
        self.wait()
        self.play(scale_tracker.animate.set_value(20))
        self.wait()
        self.play(radius.animate.set_value(1), rate_func=smooth, run_time=1)
        self.wait()

        # self.play(theta.animate.set_value(0), rate_func=smooth, run_time = 1)
        # self.wait()

        # self.play(theta.animate.set_value(360), rate_func=smooth, run_time = 8)
        # self.wait()

        # self.play(theta.animate.set_value(0), rate_func=smooth, run_time = 3)
        # self.wait()


radius = ValueTracker(1)
theta = ValueTracker(10)
scale_tracker = ValueTracker(10)

ax = always_redraw(
    lambda: Axes(
        x_range=[-3, 3, 1],
        y_range=[-3, 3, 1],
        x_length=scale_tracker.get_value(),
        y_length=scale_tracker.get_value(),
        axis_config={"include_numbers": False},
        tips=False,
    )
)
pln = always_redraw(
    lambda: NumberPlane(
        x_range=ax.get_x_range(),
        y_range=ax.get_y_range(),
        x_length=scale_tracker.get_value(),
        y_length=scale_tracker.get_value(),
        background_line_style={"stroke_opacity": 0.4},
    )
)

circle = always_redraw(
    lambda: Circle(
        radius=np.linalg.norm(ax.c2p(radius.get_value(), 0) - ax.c2p(0, 0))
    ).move_to(ax.c2p(0, 0))
)
line0 = Line(ax.c2p(*ORIGIN), ax.c2p(*RIGHT))
line1 = always_redraw(
    lambda: Line(
        ax.c2p(0, 0),
        ax.c2p(
            radius.get_value() * np.cos(theta.get_value() * DEGREES),
            radius.get_value() * np.sin(theta.get_value() * DEGREES),
        ),
        color=YELLOW,
    )
)

dot0 = Dot(ax.c2p(*ORIGIN))
dot1 = always_redraw(
    lambda: Dot(
        point=ax.c2p(
            radius.get_value() * np.cos(theta.get_value() * DEGREES),
            radius.get_value() * np.sin(theta.get_value() * DEGREES),
        )
    )
)


def one_unit_scale() -> float:
    return np.linalg.norm(ax.c2p(radius.get_value(), 0) - ax.c2p(0, 0))


def safe_angle(l0, l1, radius):
    v0 = l0.get_unit_vector()
    v1 = l1.get_unit_vector()

    dot = np.dot(v0, v1)
    if abs(dot) > 0.999:
        return VGroup()
    else:
        return Angle(l0, l1, radius=radius)


radText = always_redraw(
    lambda: MathTex(rf"\text{{radio: }}{round(radius.get_value(), 2)}")
    .shift(DOWN)
    .shift(LEFT * 5)
)
brh = always_redraw(
    lambda: Brace(
        line1, sharpness=1, direction=line1.copy().rotate(PI / 2).get_unit_vector()
    )
)
brhTex = always_redraw(lambda: brh.get_tex(r"\text{radio}"))

theta_label = always_redraw(
    lambda: MathTex(rf"\theta: {round(theta.get_value(), 1)}^\circ").next_to(
        radText, DOWN
    )
)

angle = always_redraw(lambda: safe_angle(line0, line1, radius=one_unit_scale() * 0.25))


def angle_label_condition(angle_value):
    return ax.c2p(
        0.5 * radius.get_value() * np.cos((angle_value / 2) * PI / 180),
        0.5 * radius.get_value() * np.sin((angle_value / 2) * PI / 180),
    )


angle_label = always_redraw(
    lambda: MathTex(
        rf"{round(theta.get_value(), 1)}^\circ",
    ).move_to(angle_label_condition(theta.get_value()))
)

dot2 = always_redraw(
    lambda: Dot(
        point=ax.c2p(radius.get_value() * np.cos(theta.get_value() * DEGREES), 0)
    )
)
ly = always_redraw(
    lambda: Line(np.array([dot1.get_x(), 0, 0]), dot1.get_center(), color=YELLOW)
)

bry = always_redraw(
    lambda: Brace(
        ly, sharpness=1, direction=ly.copy().rotate(-PI / 2).get_unit_vector()
    )
)
bryTex = always_redraw(
    lambda: brh.get_tex(r"\text{distancia}\\ \text{vertical}").next_to(
        bry, ax.c2p(*RIGHT)
    )
)

lx = always_redraw(
    lambda: Line(ax.c2p(*ORIGIN), np.array([dot1.get_x(), 0, 0]), color=YELLOW)
)

brx = always_redraw(
    lambda: Brace(
        lx, sharpness=1, direction=lx.copy().rotate(-PI / 2).get_unit_vector()
    )
)
brxTex = always_redraw(
    lambda: brh.get_tex(r"\text{distancia horizontal}").next_to(brx, DOWN)
)

x_label = always_redraw(
    lambda: MathTex(
        r"{}", round(radius.get_value() * np.cos(theta.get_value() * (PI / 180)), 3)
    ).move_to(np.array([dot1.get_x() / 2, ax.c2p(0, -0.3)[1], 0]))
)

y_label = always_redraw(
    lambda: MathTex(
        r"{}", round(radius.get_value() * np.sin(theta.get_value() * (PI / 180)), 3)
    ).move_to(np.array([dot1.get_x() + ax.c2p(0.4, 0)[0], dot1.get_y() / 2, 0]))
)
radY = always_redraw(
    lambda: MathTex(
        rf"\text{{d. v: }}{round(radius.get_value() * np.sin(theta.get_value() * (PI / 180)), 3)}"
    ).next_to(theta_label, DOWN)
)
radX = always_redraw(
    lambda: MathTex(
        rf"\text{{d. h: }}{round(radius.get_value() * np.cos(theta.get_value() * (PI / 180)), 3)}"
    ).next_to(radY, DOWN)
)

item_labels = VGroup(radText, theta_label, radY, radX)


class trig_11(Scene):
    def construct(self):
        self.wait()
        radius.set_value(1)
        theta.set_value(30)
        scale_tracker.set_value(20)

        self.add(ax, pln, circle)
        self.add(dot0, dot1, dot2, line1, lx, ly, angle)
        self.add(radText, theta_label, radY, radX)
        # self.add(item_labels.arrange(DOWN).move_to(np.array([-5, -1.92105032,0])))
        self.add(x_label, y_label, angle_label)

        self.play(theta.animate.set_value(30), rate_func=smooth, run_time=1)
        self.wait(1)

        self.play(FadeOut(ax, pln, circle), FadeOut(y_label, x_label))
        self.remove(y_label, x_label)
        self.wait()

        rect = Rectangle(height=one_unit_scale() * 0.1, width=one_unit_scale() * 0.1)
        rect.add_updater(lambda k: k.move_to(dot2.get_center() + ax.c2p(-0.05, 0.05)))

        self.play(GrowFromEdge(rect, UL))

        self.wait()
        brh1 = always_redraw(
            lambda: Brace(
                line1,
                sharpness=1,
                direction=line1.copy().rotate(PI / 2).get_unit_vector(),
            )
        )
        brhTex1 = always_redraw(lambda: brh1.get_tex(r"\text{hipotenusa}"))

        self.play(FadeIn(brh1, brhTex1))

        self.wait()
        radText1 = always_redraw(
            lambda: MathTex(
                rf"\text{{hipotenusa: }}{round(radius.get_value(), 2)}"
            ).move_to(radText)
        )

        self.play(ReplacementTransform(radText, radText1))
        self.wait()
        self.play(theta_label.animate.next_to(radText1, DOWN))
        self.wait()
        self.theta_label = always_redraw(
            lambda: MathTex(rf"\theta: {round(theta.get_value(), 1)}^\circ").next_to(
                radText1, DOWN
            )
        )

        bry1 = always_redraw(
            lambda: Brace(
                ly, sharpness=1, direction=ly.copy().rotate(-PI / 2).get_unit_vector()
            )
        )
        bryTex1 = bry1.get_tex(r"\text{cateto}\\ \text{opuesto}").next_to(
            bry1, RIGHT, buff=0.5
        )

        radY1 = always_redraw(
            lambda: MathTex(
                rf"\text{{c. opuesto: }}{round(radius.get_value() * np.sin(theta.get_value() * (PI / 180)), 3)}"
            ).next_to(theta_label, DOWN)
        )
        self.play(
            FadeIn(bry1, bryTex1),
        )
        self.wait()
        self.play(ReplacementTransform(radY, radY1))
        self.wait()

        brx1 = always_redraw(
            lambda: Brace(
                lx, sharpness=1, direction=lx.copy().rotate(-PI / 2).get_unit_vector()
            )
        )
        brxTex1 = brx1.get_tex(r"\text{cateto adyacente}").next_to(brx1, DOWN)

        radX1 = always_redraw(
            lambda: MathTex(
                rf"\text{{c. adyacente: }}{round(radius.get_value() * np.cos(theta.get_value() * (PI / 180)), 3)}"
            ).next_to(radY, DOWN)
        )
        self.play(FadeIn(brx1, brxTex1))
        self.wait()
        self.play(ReplacementTransform(radX, radX1))
        self.wait()

        self.y_label = always_redraw(
            lambda: MathTex(
                r"{}",
                round(radius.get_value() * np.sin(theta.get_value() * (PI / 180)), 3),
            ).move_to(np.array([dot1.get_x() + ax.c2p(0.2, 0)[0], dot1.get_y() / 2, 0]))
        )

        self.play(
            FadeOut(brh1, brhTex1),
            ReplacementTransform(VGroup(bry1, bryTex1), y_label),
            ReplacementTransform(VGroup(brx1, brxTex1), x_label),
        )
        # self.remove(brh1, brhTex1)
        self.remove(brh1, brhTex1)
        self.wait()

        t00 = always_redraw(
            lambda: MathTex(rf"\tan ({round(theta.get_value(), 1)}^\circ)")
            .shift(UP)
            .shift(LEFT * 5)
        )

        self.play(TransformFromCopy(angle_label, t00))
        # self.play(FadeIn(t00))
        self.wait(1)
        t01 = always_redraw(
            lambda: MathTex(
                rf"=\frac{{{round(radius.get_value() * np.sin(theta.get_value() * (PI / 180)), 3)}}}{{{round(radius.get_value() * np.cos(theta.get_value() * (PI / 180)), 3)}}}"
            ).next_to(t00, RIGHT, buff=0.25)
        )
        self.play(TransformFromCopy(VGroup(y_label, x_label), t01))
        self.wait(1)

        t1 = always_redraw(
            lambda: MathTex(
                rf"={round(np.tan(theta.get_value() * (PI / 180)), 3)}"
            ).next_to(t01, DOWN)
        )
        self.play(FadeIn(t1))
        self.wait()

        self.play(theta.animate.set_value(45), rate_func=smooth, run_time=2)
        self.wait(2)

        self.play(theta.animate.set_value(60), rate_func=smooth, run_time=2)
        self.wait(2)

        self.play(theta.animate.set_value(75), rate_func=smooth, run_time=2)
        self.wait(2)

        self.play(theta.animate.set_value(30), rate_func=smooth, run_time=2)
        self.wait(1)

        self.play(radius.animate.set_value(1.5), rate_func=smooth, run_time=1)
        self.wait(1)

        self.play(radius.animate.set_value(1), rate_func=smooth, run_time=1)
        self.wait(1)

        t100 = always_redraw(
            lambda: MathTex(
                rf"\arctan \left( \frac{{{round(radius.get_value() * np.sin(theta.get_value() * (PI / 180)), 3)}}}{{{round(radius.get_value() * np.cos(theta.get_value() * (PI / 180)), 3)}}} \right)"
            ).next_to(t00, UP * 2.5)
        )
        self.play(TransformFromCopy(t01, t100))
        self.wait()

        t12 = always_redraw(
            lambda: MathTex(rf"={round(theta.get_value(), 1)}^\circ").next_to(
                t100, RIGHT, buff=0.25
            )
        )
        self.play(TransformFromCopy(angle_label, t12))
        self.wait()

        self.play(theta.animate.set_value(70), rate_func=ease_in_out_cubic, run_time=2)
        self.wait()
        self.play(radius.animate.set_value(1.5), rate_func=ease_in_out_sine, run_time=1)
        self.wait()
        # self.play(theta.animate.set_value(15), rate_func=ease_in_out_cubic, run_time=2)
        # self.wait()
        self.play(theta.animate.set_value(25), rate_func=smoothererstep, run_time=2)
        self.wait()
        # self.play(radius.animate.set_value(1.5), rate_func=ease_in_out_sine, run_time=1)
        # self.wait()
        self.play(radius.animate.set_value(1), rate_func=ease_in_out_sine, run_time=1)
        self.wait()

        fu10 = MathTex(
            r"\tan (\theta) = \frac{\text{c. opuesto}}{\text{c. adyacente}}"
        ).next_to(x_label, DOWN)
        fu11 = MathTex(
            r"\arctan \left( \frac{\text{c. opuesto}}{\text{c. adyacente}}\right) = \theta"
        ).next_to(fu10, DOWN)

        self.play(Write(fu10), run_time=0.8)
        self.wait()
        self.play(Write(fu11), run_time=0.8)

        self.wait()

        self.play(FadeOut(t00, t01, t1, t100, t12, fu10, fu11))
        self.remove(t00, t01, t1, t100, t12, fu10, fu11)
        self.wait()

        # self.play()

        def calc_hipotenuse_position(phi: float, mobject_reference):
            return ax.c2p(
                mobject_reference.get_center()[0]
                + (radius.get_value() / 2) * np.cos((phi + 20) * (PI / 180)),
                mobject_reference.get_center()[1]
                + (radius.get_value() / 2) * np.sin((phi + 20) * (PI / 180)),
            )

        h_label = always_redraw(
            lambda: MathTex(rf"{round(radius.get_value(), 2)}").move_to(
                calc_hipotenuse_position(theta.get_value(), circle)
            )
        )

        self.play(TransformFromCopy(radText1, h_label))
        self.wait(1)

        t20 = always_redraw(
            lambda: MathTex(rf"\sin ({round(theta.get_value(), 1)}^\circ)")
            .shift(UP)
            .shift(LEFT * 5)
        )
        self.play(TransformFromCopy(theta_label, t20))
        self.wait()

        t21 = always_redraw(
            lambda: MathTex(
                rf"=\frac{{{round(radius.get_value() * np.sin(theta.get_value() * (PI / 180)), 3)}}}{{{round(radius.get_value(), 2)}}}"
            ).next_to(t20, RIGHT, buff=0.25)
        )
        self.play(TransformFromCopy(VGroup(h_label, y_label), t21))
        self.wait()
        t22 = always_redraw(
            lambda: MathTex(
                rf"={round(np.sin(theta.get_value() * (PI / 180)), 3)}"
            ).next_to(t21, DOWN)
        )
        self.play(Write(t22))

        self.wait()

        t23 = always_redraw(
            lambda: MathTex(
                rf"\arcsin \left( \frac{{{round(radius.get_value() * np.sin(theta.get_value() * (PI / 180)), 3)}}}{{{round(radius.get_value(), 2)}}} \right)"
            ).next_to(t20, UP * 2.5)
        )
        self.play(TransformFromCopy(VGroup(h_label, y_label), t23))
        self.wait()
        t24 = always_redraw(
            lambda: MathTex(rf"={round(theta.get_value(), 1)}^\circ").next_to(
                t23, RIGHT, buff=0.25
            )
        )
        self.play(TransformFromCopy(theta_label, t24))
        self.wait()

        self.play(theta.animate.set_value(45), rate_func=smooth, run_time=2)
        self.wait(2)

        self.play(theta.animate.set_value(60), rate_func=smooth, run_time=2)
        self.wait(2)

        self.play(
            radius.animate.set_value(1.5), rate_func=ease_in_out_cubic, run_time=1
        )
        self.wait(1)

        self.play(theta.animate.set_value(75), rate_func=smooth, run_time=2)
        self.wait(2)

        self.play(theta.animate.set_value(30), rate_func=smooth, run_time=2)
        self.wait(1)

        self.play(radius.animate.set_value(1), rate_func=ease_in_out_cubic, run_time=1)
        self.wait(1)

        fu20 = MathTex(
            r"\sin (\theta) = \frac{\text{c. opuesto}}{\text{hipotenusa}}"
        ).next_to(x_label, DOWN)
        fu21 = MathTex(
            r"\arcsin \left(\frac{\text{c. opuesto}}{\text{hipotenusa}}\right) = \theta"
        ).next_to(fu20, DOWN)

        self.play(Write(fu20), run_time=0.8)
        self.wait()
        self.play(Write(fu21), run_time=0.8)

        self.wait()

        self.play(FadeOut(t20, t21, t22, t23, t24, fu20, fu21))
        self.remove(t20, t21, t22, t23, t20, fu20, fu21)

        # asasa

        t30 = always_redraw(
            lambda: MathTex(rf"\cos ({round(theta.get_value(), 1)}^\circ)")
            .shift(UP)
            .shift(LEFT * 5)
        )
        self.play(TransformFromCopy(theta_label, t30))
        self.wait()

        t31 = always_redraw(
            lambda: MathTex(
                rf"=\frac{{{round(radius.get_value() * np.cos(theta.get_value() * (PI / 180)), 3)}}}{{{round(radius.get_value(), 2)}}}"
            ).next_to(t30, RIGHT, buff=0.25)
        )
        self.play(TransformFromCopy(VGroup(h_label, x_label), t31))
        self.wait()
        t32 = always_redraw(
            lambda: MathTex(
                rf"={round(np.cos(theta.get_value() * (PI / 180)), 3)}"
            ).next_to(t31, DOWN)
        )
        self.play(Write(t32))

        self.wait()

        t33 = always_redraw(
            lambda: MathTex(
                rf"\arccos \left( \frac{{{round(radius.get_value() * np.cos(theta.get_value() * (PI / 180)), 3)}}}{{{round(radius.get_value(), 2)}}} \right)"
            ).next_to(t30, UP * 2.5)
        )
        self.play(TransformFromCopy(VGroup(h_label, y_label), t33))
        self.wait()
        t34 = always_redraw(
            lambda: MathTex(rf"={round(theta.get_value(), 1)}^\circ").next_to(
                t33, RIGHT, buff=0.25
            )
        )
        self.play(TransformFromCopy(theta_label, t34))
        self.wait()

        self.play(theta.animate.set_value(45), rate_func=smooth, run_time=2)
        self.wait(2)

        self.play(
            radius.animate.set_value(1.5), rate_func=ease_in_out_cubic, run_time=1
        )
        self.wait(1)

        self.play(theta.animate.set_value(60), rate_func=smooth, run_time=2)
        self.wait(2)

        self.play(theta.animate.set_value(30), rate_func=smooth, run_time=2)
        self.wait(1)

        self.play(theta.animate.set_value(75), rate_func=smooth, run_time=2)
        self.wait(2)

        self.play(theta.animate.set_value(45), rate_func=smooth, run_time=2)
        self.wait(1)

        self.play(radius.animate.set_value(1), rate_func=ease_in_out_cubic, run_time=1)
        self.wait(1)

        fu30 = MathTex(
            r"\cos (\theta) = \frac{\text{c. adyacente}}{\text{hipotenusa}}"
        ).next_to(x_label, DOWN)
        fu31 = MathTex(
            r"\arccos \left(\frac{\text{c. adyacente}}{\text{hipotenusa}}\right) = \theta"
        ).next_to(fu30, DOWN)

        self.play(Write(fu30), run_time=0.8)
        self.wait()
        self.play(Write(fu31), run_time=0.8)

        self.wait()


class trig_12(Scene):
    def construct(self):
        rec = Rectangle(width=3.0, height=1.5)

        a0 = Arrow(start=rec.get_left() + LEFT * 2, end=rec.get_left(), buff=0)
        a1 = Arrow(end=rec.get_right() + RIGHT * 2, start=rec.get_right(), buff=0)

        f0 = MathTex(r"\theta").next_to(a0, LEFT)
        f1 = MathTex(r"f(\theta)")

        f2 = Text("resultado\ndeterminista", font_size=32).next_to(a1, RIGHT)

        self.play(Create(rec))
        self.wait()
        self.play(FadeIn(f0, a0))
        self.wait()
        self.play(Write(f1))
        self.wait()
        self.play(FadeIn(a1))
        self.wait()
        self.play(Write(f2))
        self.wait()


class trig_13(Scene):
    def construct(self):
        f = [
            MathTex(r"\sin \theta = \frac{\text{c. opuesto}}{\text{hipotenusa}}"),
            MathTex(
                r"\arcsin \left(\frac{\text{c. opuesto}}{\text{hipotenusa}}\right) = \theta "
            ),
            MathTex(r"\cos \theta = \frac{\text{c. adyacente}}{\text{hipotenusa}}"),
            MathTex(
                r"\arccos \left(\frac{\text{c. adyacente}}{\text{hipotenusa}}\right) = \theta "
            ),
            MathTex(
                r"\tan \theta = \frac{\text{c. opuesto}}{\text{c. adyacente}} = \frac{\sin \theta}{\cos \theta}"
            ),
            MathTex(
                r"\arctan \left(\frac{\text{c. opuesto}}{\text{c. adyacente}}\right) = \theta "
            ),
            MathTex(
                r"\csc \theta = \frac{\text{hipotenusa}}{\text{c. opuesto}} = \frac{1}{\sin \theta}"
            ),
            MathTex(
                r"\operatorname{arccsc} \left(\frac{\text{hipotenusa}}{\text{c. opuesto}}\right) = \theta "
            ),
            MathTex(
                r"\sec \theta = \frac{\text{hipotenusa}}{\text{c. adyacente}} = \frac{1}{\cos \theta}"
            ),
            MathTex(
                r"\operatorname{arcsec} \left(\frac{\text{hipotenusa}}{\text{c. adyacente}}\right) = \theta "
            ),
            MathTex(
                r"\cot \theta = \frac{\text{c. adyacente}}{\text{c. opuesto}} = \frac{1}{\tan \theta}"
            ),
            MathTex(
                r"\operatorname{arccot} \left(\frac{\text{c. adyacente}}{\text{c. opuesto}}\right) = \theta "
            ),
        ]

        items1 = VGroup(*[f[i] for i in range(6)])
        items1.arrange_in_grid(rows=6, cols=2, buff=(1.5, 1))

        items2 = VGroup(*[f[i] for i in range(6, 12)])
        items2.arrange_in_grid(rows=6, cols=2, buff=(1.5, 1))

        # for row in range(6):
        #     if row % 2 == 1:
        #         items[row].shift(DOWN * 0.4)
        t = Text(r"SOH-CAH-TOA")
        self.play(Write(t.next_to(items1, UP)))

        self.wait()

        self.play(Write(items1), run_time=1)
        self.wait(2)
        self.play(FadeOut(items1, t))
        self.wait()

        self.play(Write(items2), run_time=1)
        self.wait(2)
        self.play(FadeOut(items2))
        self.wait()


class trig_14(Scene):
    def construct(self):
        theta = ValueTracker(27)
        radius = ValueTracker(5)

        dot0 = Dot(LEFT * 0.5)
        dot1 = Dot()
        dot1.add_updater(
            lambda m: m.move_to(
                [
                    dot0.get_center()[0]
                    + radius.get_value() * np.cos(theta.get_value() * DEGREES),
                    dot0.get_center()[1],
                    0,
                ]
            )
        )

        dot2 = Dot()
        dot2.add_updater(
            lambda m: m.move_to(
                [
                    dot0.get_center()[0]
                    + radius.get_value() * np.cos(theta.get_value() * DEGREES),
                    dot0.get_center()[1]
                    + radius.get_value() * np.sin(theta.get_value() * DEGREES),
                    0,
                ]
            )
        )

        self.play(FadeIn(dot0, dot1, dot2), run_time=1)
        # self.wait()

        lh = always_redraw(
            lambda: Line(start=dot0.get_center(), end=dot2.get_center(), color=YELLOW)
        )
        lx = always_redraw(
            lambda: Line(start=dot0.get_center(), end=dot1.get_center(), color=YELLOW)
        )
        ly = always_redraw(
            lambda: Line(start=dot1.get_center(), end=dot2.get_center(), color=YELLOW)
        )

        self.play(FadeIn(lh, lx, ly), run_time=1)
        self.wait()

        a0 = always_redraw(lambda: Angle(lx, lh, radius=0.2 * radius.get_value()))

        a0T = always_redraw(
            lambda: DecimalNumber(
                Angle(lx, lh).get_value(degrees=True),  # <— calcular sobre la marcha
                unit=r"^{\circ}",
            ).move_to(
                [
                    dot0.get_center()[0]
                    + 0.4
                    * radius.get_value()
                    * np.cos((theta.get_value() / 2) * DEGREES),
                    dot0.get_center()[1]
                    + 0.4
                    * radius.get_value()
                    * np.sin((theta.get_value() / 2) * DEGREES),
                    0,
                ]
            )
        )

        a1 = always_redraw(
            lambda: Angle(
                lh.copy().reverse_points(),
                ly.copy().reverse_points(),
                radius=0.2 * radius.get_value(),
                other_angle=False,
            )
        )

        a1T = always_redraw(
            lambda: DecimalNumber(
                Angle(
                    lh.copy().reverse_points(),
                    ly.copy().reverse_points(),
                    other_angle=False,
                ).get_value(degrees=True),  # <— calcular sobre la marcha
                unit=r"^{\circ}",
            ).move_to(
                [
                    dot2.get_center()[0]
                    - 0.3
                    * radius.get_value()
                    * np.sin(((90 - theta.get_value()) / 2) * DEGREES),
                    dot2.get_center()[1]
                    - 0.3
                    * radius.get_value()
                    * np.cos(((90 - theta.get_value()) / 2) * DEGREES),
                    0,
                ]
            )
        )

        def calc_post(phi: float, radius: float, mobjectA: Mobject, mobjectB: Mobject):
            return np.array(
                [
                    mobjectA.get_center()[0]
                    - np.linalg.norm(mobjectB.get_center() - mobjectB.get_right())
                    + (radius / 2) * np.cos((phi + 20) * DEGREES),
                    mobjectA.get_center()[1]
                    + (radius / 2) * np.sin((phi + 20) * DEGREES),
                    0,
                ]
            )

        brx = always_redraw(
            lambda: Brace(
                lx, sharpness=1, direction=lx.copy().rotate(-PI / 2).get_unit_vector()
            )
        )
        brxTex = always_redraw(
            lambda: MathTex(r"\text{c. adyacente}").next_to(brx, DOWN)
        )

        bry = always_redraw(
            lambda: Brace(
                ly, sharpness=1, direction=ly.copy().rotate(-PI / 2).get_unit_vector()
            )
        )
        bryTex = always_redraw(
            lambda: MathTex(r"\text{c. opuesto}").next_to(bry, RIGHT)
        )

        brh = always_redraw(
            lambda: Brace(
                lh, sharpness=1, direction=lh.copy().rotate(PI / 2).get_unit_vector()
            )
        )
        brhTex = MathTex(r"5.28")
        brhTex.add_updater(
            lambda k: k.move_to(
                calc_post(theta.get_value(), radius.get_value(), dot0, brhTex)
            )
        )

        rect = Rectangle(height=0.4, width=0.4)
        rect.add_updater(lambda k: k.move_to(dot1.get_center() + [-0.2, 0.2, 0]))

        self.play(FadeIn(a0, a0T, brx, brxTex, bry, bryTex, brh, brhTex, a1, rect))
        self.wait()

        self.play(FadeOut(brx, brh, bry, brxTex, bryTex))
        self.remove(brx, brh, bry, brxTex, bryTex)
        self.wait()

        self.play(dot2.animate.shift(RIGHT))
        self.wait()

        f = [
            MathTex(r"\sin \theta = \frac{\text{c. opuesto}}{\text{hipotenusa}}"),
            MathTex(r"\cos \theta = \frac{\text{c. adyacente}}{\text{hipotenusa}}"),
            MathTex(r"\tan \theta = \frac{\text{c. opuesto}}{\text{c. adyacente}}"),
        ]

        v0 = VGroup(f[0], f[1], f[2]).arrange(DOWN, buff=1).shift(LEFT * 4)

        self.play(Write(v0), run_time=1)
        self.wait()
        self.play(Circumscribe(f[0]))
        self.wait()

        self.play(Circumscribe(f[1]))
        self.wait()

        self.play(FadeOut(f[2]))

        self.wait()

        self.play(
            VGroup(f[0], f[1])
            .animate.arrange(DOWN, buff=0.5)
            .shift(UP * 2)
            .shift(LEFT * 4),
            dot0.animate.shift(RIGHT).shift(DOWN),
        )
        self.wait()
        t0 = [
            MathTex(r"\sin (27 ^\circ) = \frac{\text{c. opuesto}}{5.28}"),
            MathTex(r"(5.28) \sin (27 ^\circ) = \text{c. opuesto}"),
            MathTex(r" \text{c. opuesto} = (5.28) \sin (27 ^\circ)"),
            MathTex(r" \text{c. opuesto} = 2.397"),
            MathTex(r" \text{c. opuesto} = 2.4"),
        ]

        v1 = VGroup(t0[0], t0[1], t0[2], t0[3], t0[4]).shift(LEFT * 4)

        self.play(
            TransformMatchingShapes(
                VGroup(f[0], a0, brhTex).copy(),
                t0[0],
            )
        )
        self.wait()
        for i in range(4):
            self.play(TransformMatchingShapes(t0[i], t0[i + 1], path_arc=PI / 2))
            self.wait()

        bryTex1 = always_redraw(lambda: MathTex(r"2.4").next_to(ly, RIGHT))
        self.play(TransformMatchingShapes(t0[4], bryTex1))

        self.wait()

        t1 = [
            MathTex(r"\cos (27 ^\circ) = \frac{\text{c. adyacente}}{5.28}"),
            MathTex(r"(5.28) \cos (27 ^\circ) = \text{c. adyacente}"),
            MathTex(r" \text{c. adyacente} = (5.28) \cos (27 ^\circ)"),
            MathTex(r" \text{c. adyacente} = 4.7"),
        ]

        v2 = VGroup(t1[0], t1[1], t1[2], t1[3]).shift(LEFT * 3.5)
        self.play(
            TransformMatchingShapes(
                VGroup(f[1], a0, brhTex).copy(),
                t1[0],
            )
        )
        self.wait()

        for i in range(3):
            self.play(TransformMatchingShapes(t1[i], t1[i + 1], path_arc=PI / 2))
            self.wait()

        brxTex1 = always_redraw(lambda: MathTex(r"4.7").next_to(lx, DOWN))
        self.play(TransformMatchingShapes(t1[3], brxTex1))

        self.wait()
        t90 = MathTex(r"90^\circ").next_to(rect, DR * 0.7)
        self.play(Write(t90))

        self.wait()
        t2 = [
            MathTex(r"\alpha + \beta + \theta = 180^\circ"),
            MathTex(r"27^\circ + 90^\circ + \theta = 180 ^\circ"),
            MathTex(r"\theta = 180^\circ -  27^\circ - 90^\circ"),
            MathTex(r"\theta = 63 ^\circ "),
        ]

        v3 = VGroup(t2[0], t2[1], t2[2], t2[3]).shift(LEFT * 3.5)

        self.play(Write(t2[0]))
        self.wait()

        self.play(
            TransformMatchingShapes(
                VGroup(t2[0], a0T.copy(), t90.copy()),
                t2[1],
            )
        )
        self.wait()

        for i in range(1, 3):
            self.play(TransformMatchingShapes(t2[i], t2[i + 1], path_arc=PI / 2))
            self.wait()

        t63 = MathTex(r"63 ^\circ").move_to(dot2.get_center()).shift(DL)
        self.play(TransformMatchingShapes(t2[3], t63))

        self.wait()

        self.play(FadeOut(brxTex1, bryTex1, brhTex, a0T, t63, t90, f[0], f[1]))
        self.wait()

        self.play(
            theta.animate.set_value(53.13), rate_func=ease_in_out_quint, run_time=2
        )
        self.wait()

        brxTex2 = always_redraw(lambda: MathTex(r"6").next_to(lx, DOWN))
        bryTex2 = always_redraw(lambda: MathTex(r"8").next_to(ly, RIGHT))
        self.play(FadeIn(brxTex2, bryTex2))
        self.wait()

        f = [
            MathTex(r"\sin \theta = \frac{\text{c. opuesto}}{\text{hipotenusa}}"),
            MathTex(r"\cos \theta = \frac{\text{c. adyacente}}{\text{hipotenusa}}"),
            MathTex(r"\tan \theta = \frac{\text{c. opuesto}}{\text{c. adyacente}}"),
        ]

        v0 = VGroup(f[0], f[1], f[2]).arrange(DOWN, buff=1).shift(LEFT * 4)

        self.play(Write(v0), run_time=1)
        self.wait()
        self.play(Circumscribe(f[2]))
        self.wait()
        self.play(FadeOut(f[0], f[1]))
        self.wait()

        t3 = [
            MathTex(r"\tan \theta = \frac{8}{6}"),
            MathTex(r"\arctan (\tan \theta ) = \arctan \left(\frac{8}{6} \right)"),
            MathTex(r"\theta = \arctan \left(\frac{8}{6}\right)"),
            MathTex(r"\theta = 53.13 ^\circ"),
        ]

        t53 = MathTex(r"53.13 ^\circ").move_to(dot0).shift(UP * 0.5 + RIGHT * 1.7)

        v4 = VGroup(t3[0], t3[1], t3[2], t3[3]).shift(LEFT * 3.5)
        self.play(
            TransformMatchingShapes(
                VGroup(f[2], brxTex2, bryTex2).copy(),
                t3[0],
            )
        )
        self.wait()

        for i in range(3):
            self.play(TransformMatchingShapes(t3[i], t3[i + 1], path_arc=PI / 2))
            self.wait()

        self.play(TransformMatchingShapes(t3[3], t53))

        self.wait()

        t4 = [
            MathTex(r"\alpha + \beta + \theta = 180^\circ"),
            MathTex(r"53.13^\circ + 90^\circ + \theta = 180 ^\circ"),
            MathTex(r"\theta = 180^\circ -  53.13^\circ - 90^\circ"),
            MathTex(r"\theta = 36.87 ^\circ "),
        ]
        t36 = (
            MathTex(r"36.87 ^\circ")
            .move_to(dot2.get_center())
            .shift(DOWN * 2 + LEFT * 0.7)
        )
        v5 = VGroup(t4[0], t4[1], t4[2], t4[3]).shift(LEFT * 3.5)
        self.play(Write(t4[0]))
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(t4[0], t53.copy()),
                t4[1],
            )
        )
        self.wait()

        for i in range(1, 3):
            self.play(TransformMatchingShapes(t4[i], t4[i + 1], path_arc=PI / 2))
            self.wait()

        self.play(TransformMatchingShapes(t4[3], t36))

        self.wait()
        self.play(FadeOut(f[2]))
        self.wait()

        f1 = [
            MathTex(r"\text{hipotenusa}^{2}=a^{2} + b^{2}"),
            MathTex(r"\sqrt{\text{hipotenusa}^{2}}=\sqrt{ a ^{2} + b ^{2} }"),
            MathTex(r"\text{hipotenusa} = \sqrt{ 8^{2}+6^{2} }"),
            MathTex(r"\text{hipotenusa}=\sqrt{ 100 }"),
            MathTex(r"\text{hipotenusa}=10"),
        ]

        v6 = VGroup(f1[0], f1[1], f1[2], f1[3], f1[4]).shift(LEFT * 3.5)
        self.play(Write(f1[0]))
        self.wait()

        for i in range(4):
            if i == 1:
                self.play(
                    TransformMatchingShapes(
                        VGroup(f1[i], brxTex2.copy(), bryTex2.copy()),
                        f1[i + 1],
                        path_arc=PI / 2,
                    )
                )

            else:
                self.play(TransformMatchingShapes(f1[i], f1[i + 1], path_arc=PI / 2))
            self.wait()

        brh10 = MathTex(r"10").move_to(lh.get_center()).shift(LEFT)
        self.play(TransformMatchingShapes(f1[4], brh10))

        self.wait()

        self.play(FadeOut(brh10, brxTex2, bryTex2, t36, t53))
        self.wait()

        # self.play()

        self.play(theta.animate.set_value(65), rate_func=ease_in_out_quint, run_time=2)
        self.play(dot0.animate.shift(RIGHT).shift(DOWN))
        self.wait()

        t25 = (
            MathTex(r"25 ^\circ")
            .move_to(dot2.get_center())
            .shift(DOWN * 2 + LEFT * 0.7)
        )
        t65 = MathTex(r"65 ^\circ").move_to(dot0).shift(UP * 0.5 + RIGHT * 1.7)

        brh3 = Brace(
            lh, sharpness=1, direction=lh.copy().rotate(PI / 2).get_unit_vector()
        )
        brhT = Tex(r"hipotenusa").move_to(brh3.get_center()).shift(LEFT * 2).shift(UP)

        brx3 = Brace(
            lx, sharpness=1, direction=lx.copy().rotate(-PI / 2).get_unit_vector()
        )
        brxT = Tex(r"c. opuesto").move_to(brx3.get_center()).shift(DOWN)

        bry3 = Brace(
            ly, sharpness=1, direction=ly.copy().rotate(-PI / 2).get_unit_vector()
        )
        bry3T = Tex(r"c. adyacente").move_to(bry3.get_center()).shift(RIGHT * 1.5)

        yyyy = MathTex(r"12.25").move_to(bry3.get_center()).shift(RIGHT)

        t25 = (
            MathTex(r"25 ^\circ")
            .move_to(dot2.get_center())
            .shift(DOWN * 1.5 + LEFT * 0.25)
        )

        self.play(FadeIn(yyyy), FadeIn(t25))
        self.wait()
        self.play(FadeOut(yyyy))
        self.wait()

        self.play(FadeIn(brh3))
        self.wait()
        self.play(FadeIn(brhT))
        self.wait()

        self.play(FadeIn(brx3))
        self.wait()
        self.play(FadeIn(brxT))
        self.wait()

        self.play(FadeIn(bry3))
        self.wait()
        self.play(FadeIn(bry3T))
        self.wait()

        self.play(FadeOut(brh3, brx3, bry3, brhT, brxT, bry3T))
        self.wait()
        self.play(FadeIn(yyyy))
        self.wait()

        f = [
            MathTex(r"\sin \theta = \frac{\text{c. opuesto}}{\text{hipotenusa}}"),
            MathTex(r"\cos \theta = \frac{\text{c. adyacente}}{\text{hipotenusa}}"),
            MathTex(r"\tan \theta = \frac{\text{c. opuesto}}{\text{c. adyacente}}"),
        ]

        v0 = VGroup(f[0], f[1], f[2]).arrange(DOWN, buff=1).shift(LEFT * 4)

        self.play(Write(v0), run_time=1)
        self.wait()
        self.play(Circumscribe(f[1]))
        self.wait()

        self.play(Circumscribe(f[0]))
        self.wait()

        self.play(FadeOut(f[2]))
        self.wait()

        self.play(
            VGroup(f[1], f[0])
            .animate.arrange(DOWN, buff=0.5)
            .shift(UP * 2)
            .shift(LEFT * 4),
        )
        self.wait()
        # self.play()

        f1 = [
            MathTex(r"\cos (25 ^\circ) = \frac{12.25}{\text{hipotenusa}}"),
            MathTex(r"\text{hipotenusa} = \frac{12.25}{\cos (25 ^\circ) }"),
            MathTex(r"\text{hipotenusa} = 13.51"),
        ]

        v6 = VGroup(f1[0], f1[1], f1[2]).shift(LEFT * 3.5)
        self.play(TransformFromCopy(VGroup(f[1], t25, yyyy), f1[0]))
        self.wait()

        for i in range(2):
            self.play(TransformMatchingShapes(f1[i], f1[i + 1], path_arc=PI / 2))
            self.wait()

        hhhh = MathTex(r"13.51").move_to(lh.get_center()).shift(LEFT)

        self.play(TransformMatchingShapes(f1[2], hhhh))
        self.wait()

        f2 = [
            MathTex(r"\sin (25 ^\circ) = \frac{\text{c. opuesto}}{13.51}"),
            MathTex(r"(13.51) \sin ( 25 ^\circ ) = \text{c. opuesto}"),
            MathTex(r"\text{c. opuesto} = (13.51) \sin ( 25 ^\circ )"),
            MathTex(r"\text{c. opuesto} = 5.7"),
        ]

        v6 = VGroup(f2[0], f2[1], f2[2], f2[3]).shift(LEFT * 3.5)
        self.play(TransformFromCopy(VGroup(f2[0], t25, hhhh), f2[0]))
        self.wait()

        for i in range(3):
            self.play(TransformMatchingShapes(f2[i], f2[i + 1], path_arc=PI / 2))
            self.wait()

        xxxx = MathTex(r"5.7").move_to(lx.get_center()).shift(DOWN)

        self.play(TransformMatchingShapes(f2[3], xxxx), FadeOut(f[0], f[1]))
        self.wait()

        t4 = [
            MathTex(r"\alpha + \beta + \theta = 180^\circ"),
            MathTex(r"25^\circ + 90^\circ + \theta = 180 ^\circ"),
            MathTex(r"\theta = 180^\circ -  25^\circ - 90^\circ"),
            MathTex(r"\theta = 65 ^\circ "),
        ]

        t65 = MathTex(r"65 ^\circ").move_to(dot0).shift(UP + RIGHT * 1.5)
        v5 = VGroup(t4[0], t4[1], t4[2], t4[3]).shift(LEFT * 3.5)
        self.play(Write(t4[0]))
        self.wait()
        self.play(
            TransformMatchingShapes(
                VGroup(t4[0], t25.copy()),
                t4[1],
            )
        )
        self.wait()

        for i in range(1, 3):
            self.play(TransformMatchingShapes(t4[i], t4[i + 1], path_arc=PI / 2))
            self.wait()

        self.play(TransformMatchingShapes(t4[3], t65))
        self.wait()

        # self.play()
