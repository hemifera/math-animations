from manim import *  

class ax(Scene):
    def construct(self):
        ax = Axes(x_range = (-1, 12), y_range = (-1, 6), tips = False)
        ax.add_coordinates()

        x_lab = ax.get_x_axis_label("X axis")
        y_lab = ax.get_y_axis_label("Y axis") 

        self.play(Write(ax), Write(x_lab), Write(y_lab))  
        rec = Rectangle(height = 0.5, width = 0.5)
        rec.move_to(ax.c2p(4, 2)) 
        self.play(Write(rec))
        self.wait(2)

class ex(Scene):
    def construct(self):
        ax = Axes(x_range = (-5, 5), y_range = (0, 5), tips = True)
        ax.add_coordinates()

        x_lab = ax.get_x_axis_label(r"x")
        y_lab = ax.get_y_axis_label(r"y") 

        a = FunctionGraph(
            lambda t: abs(t),
            x_range=[-4, 4],
            color=GREEN,
        ).move_to(ORIGIN)

        self.play(Write(ax), Write(x_lab), Write(y_lab))  
        self.play(Create(a))
        # self.play()

class asas(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, r"x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)
        self.add(plot, labels)



class ArgMinExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(0)

        def func(x):
            return 2 * (x - 5) ** 2
        graph = ax.plot(func, color=MAROON)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()

        self.add(ax, labels, graph, dot)
        self.play(t.animate.set_value(x_space[minimum_index]))
        self.wait()
