from manim import *
from manim.utils.rate_functions import ease_in_out_cubic, smoothererstep, ease_in_out_sine, ease_in_out_quint

# cambios de codigo
# renderizar desde la direccion actual del archivo 

class divl_00(Scene):
    def construct(self):
        img = ImageMobject("../img/udb_logo_high.png")
        t1 = Text(r"División de polinómios")
        t2 = Text(r"División larga", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))

class divl_10(Scene):
    def construct(self): 
        # setup general de todo el ejercicio
        f0 = [
            MathTex(r"\frac{x^{5}+x^{2}+3x+2}{x^{2}+2}"),
            MathTex(r"= x^{3}-2x+1+\frac{7x}{x^{2}+2}"),
            MathTex(r"x^{3}", r"-2x", r"+1"),
            MathTex(r"x^{3}-2x+1", r"+\frac{7x}{x^{2}+2}"),
            MathTex(r"x^2 \cdot x^3 = x^{2+3}=x^5"),
        ]

        v0 = VGroup(
            mt(r"x^{5}"), mt(r"0x^{4}"), mt(r"0x^{3}"), mt(r"x^{2}"), mt(r"3x"), mt(r"2"), t(r"NO"), MathTex(r"x^{2}", r"+", r"2"),
            mt(r"-x^{5}"), mt(r"0"), mt(r"-2x^{3}"), mt(r"0"), mt(r"0"), mt(r"0"),t(r"NO"), mt(r"0"),
            mt(r"0"), mt(r"0"), mt(r"-2x^{3}"), mt(r"x^{2}"), mt(r"3x"), mt(r"2"), t(r"NO"), mt(r"0"),
            mt(r"0"), mt(r"0"), mt(r"+2x^{3}"), mt(r"0"), mt(r"4x"), mt(r"0"), t(r"NO"), mt(r"0"),
            mt(r"0"), mt(r"0"), mt(r"0"), mt(r"x^{2}"), mt(r"7x"), mt(r"2"), t(r"NO"), mt(r"0"),
            mt(r"0"), mt(r"0"), mt(r"0"), mt(r"-x^{2}"), mt(r"0"), mt(r"-2"), t(r"NO"), mt(r"0"),
            mt(r"0"), mt(r"0"), mt(r"0"), mt(r"0"), mt(r"7x"), mt(r"0"), t(r"NO"), mt(r"0"),
        ).arrange_in_grid(rows= 7, cols = 8, )

        v0a = VGroup()

        for m in v0:
            if isinstance(m, MathTex) and (m.tex_string == "0" or m.tex_string == "NO" ):
                m.set_opacity(0)
            else:
                print(m.get_opacity())
                v0a.add(m)
            
        for i, m in enumerate(v0a):
            if i > 6:
                m.set_opacity(0)

        f0[2].next_to(v0[7], UP, buff=0.5, aligned_edge=LEFT)

        
        l01, l02 = div_line(v0[7])
        l1 = horizontal_line(v0[8], v0[16], v0[13], v0[21])
        l2 = horizontal_line(v0[8+2+16], v0[16+2+16], v0[13+16], v0[21+16])
        l3 = horizontal_line(v0[8+3+16*2], v0[16+3+16*2], v0[13+16*2], v0[21+16*2])


        self.play(Write(f0[0]), run_time=0.7)
        self.wait()
        self.play(f0[0].animate.shift(LEFT*3), run_time=0.5)
        self.play(Write(f0[1].next_to(f0[0], RIGHT)), run_time=0.8)
        self.wait()
        self.play(f0[0].animate.move_to(ORIGIN), FadeOut(f0[1]), run_time=0.6)
        self.wait()
        self.play(TransformMatchingShapes(f0[0].copy(), VGroup(*v0a[:7])))
        self.wait()
        self.play(FadeOut(f0[0]))
        self.wait()
        self.play(FadeIn(l01, l02))
        self.wait()
        self.play(Circumscribe(v0a[0]))
        self.wait()
        self.play(Circumscribe(v0a[6][0]))
        self.wait()

        self.play(Write(f0[4]))
        self.wait()
        self.play(FadeOut(f0[4]))
        self.wait()

        self.play(Write(f0[2][0]))
        self.wait()
        self.play(Circumscribe(f0[2][0]), Circumscribe(v0a[6].get_part_by_tex(r"x^{2}")))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(f0[2][0], v0[7][0]).copy(), v0a[7].set_opacity(1)))
        self.wait()

        self.play(Circumscribe(f0[2][0]), Circumscribe(v0[7][2]))
        self.wait()
        # v0a[8].set_opacity(1)
        self.play(TransformMatchingShapes(VGroup(f0[2][0], v0[7][2]).copy(), v0a[8].set_opacity(1)))
        self.wait()
        self.play(FadeIn(l1))
        self.wait()

        self.play(TransformMatchingShapes(v0a[8].copy(), v0a[9].set_opacity(1)))
        self.wait()
        self.play(TransformMatchingShapes(v0a[3].copy(), v0a[10].set_opacity(1)))
        self.play(TransformMatchingShapes(v0a[4].copy(), v0a[11].set_opacity(1)))
        self.play(TransformMatchingShapes(v0a[5].copy(), v0a[12].set_opacity(1)))
        self.wait()
        self.play(Circumscribe(v0a[9]))
        self.wait()
        self.play(Circumscribe(v0[7][0]))
        self.wait()
        self.play(Write(f0[2][1]))
        self.wait()

        self.play(Circumscribe(f0[2][1]), Circumscribe(v0[7][0]))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(f0[2][1], v0[7][0]).copy(), v0a[13].set_opacity(1)))
        self.wait()

        self.play(Circumscribe(f0[2][1]), Circumscribe(v0[7][2]))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(f0[2][1], v0[7][2]).copy(), v0a[14].set_opacity(1)))
        self.wait()

        self.play(FadeIn(l2))
        self.wait()

        self.play(TransformMatchingShapes(v0a[10].copy(), v0a[15].set_opacity(1)))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(v0a[11], v0a[14]).copy(), v0a[16].set_opacity(1)))
        self.wait()
        self.play(TransformMatchingShapes(v0a[12].copy(), v0a[17].set_opacity(1)))
        self.wait()


        self.play(Circumscribe(v0[7][0]))
        self.wait()
        self.play(Circumscribe(v0a[15]))
        self.wait()
        self.play(Write(f0[2][2]))
        self.wait()


        self.play(Circumscribe(f0[2][2]), Circumscribe(v0[7][0]))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(f0[2][2], v0[7][0]).copy(), v0a[18].set_opacity(1)))
        self.wait()

        self.play(Circumscribe(f0[2][2]), Circumscribe(v0[7][2]))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(f0[2][2], v0[7][2]).copy(), v0a[19].set_opacity(1)))
        self.wait()
        self.play(FadeIn(l3))
        self.wait()
        self.play(TransformMatchingShapes(v0a[16].copy(), v0a[20].set_opacity(1)))
        self.wait()

        self.play(
            FadeOut(VGroup(*v0a[:6], *v0a[7:20], l1, l2, l3))
        )
        self.wait()

        self.play(TransformMatchingShapes(f0[2].copy(), f0[3][0]))
        self.wait()

        self.play(TransformMatchingShapes(VGroup(v0a[20], v0a[6]).copy(), f0[3][1]))
        self.wait()
        self.play(FadeOut(f0[2], v0a[20], v0a[6], l01, l02))
        self.wait()

        


class divl_20(Scene):
    def construct(self): 
        # setup general de todo el ejercicio
        f0 = [
            MathTex(r"\frac{-20h^{7}+15h^{6}-10h^{5}}{-3h{^2}+h{^6}-h^{7}}"),
            MathTex(r"\frac{h^{5} (-20h^{2}+15h-10)}{h^{2}(-3+h^{3}-h^{5})}"),
            MathTex(r"\frac{h^{3} (-20h^{2}+15h-10)}{(-3+h^{4}-h^{5})}"),
            MathTex(r"\frac{h^{3} (-20h^{2}+15h-10)}{(-3+h^{4}-h^{5})}"),
            MathTex(r"\frac{-20h^{5}+15h^{4}-10h^{3}}{-3+h^{4}-h^{5}}"),
            MathTex(r"\frac{-20h^{5}+15h^{4}-10h^{3}}{-h^{5}+h^{4}-3}"),
            MathTex(r"20"),
            MathTex(r"20", r"+ \frac{-5h^{4}-10h^{3}+60}{-h^{5}+h^{4}-3}"),
        ]

        v0 = VGroup(
            mt(r"-20h^{5}"), mt(r"+15h^{4}"), mt(r"-10h^{3}"), mt(r"0"), t(r"NO"), MathTex(r"-h^{5}", r"+h^{4}", r"-3"),
            mt(r"+20h^{5}"), mt(r"-20h^{4}"), mt(r"0"), mt(r"60"), t(r"NO"), MathTex(r"0"),
            mt(r"0"), mt(r"-5h^{4}"), mt(r"-10h^{3}"), mt(r"60"), t(r"NO"), MathTex(r"0"),
            
        ).arrange_in_grid(rows= 3, cols = 6, )

        v0a = VGroup()

        for m in v0:
            if isinstance(m, MathTex) and (m.tex_string == "0" or m.tex_string == "NO" ):
                m.set_opacity(0)
            else:
                v0a.add(m)
        
        
        for i, m in enumerate(v0a):
            if i > 3:
                m.set_opacity(0)

        f0[6].next_to(v0[5], UP, buff=0.5, aligned_edge=LEFT)

        
        l01, l02 = div_line(v0[5])
        l1 = horizontal_line(v0[6], v0[12], v0[9], v0[15])
        # self.add(f0[6], l01, l02, l1)
        # l2 = horizontal_line(v0[8+2+16], v0[16+2+16], v0[13+16], v0[21+16])
        # l3 = horizontal_line(v0[8+3+16*2], v0[16+3+16*2], v0[13+16*2], v0[21+16*2])
        # self.add(v0a)
        self.play(Write(f0[0]), run_time=0.7)
        self.wait()
        for i in range(5):
            self.play(TransformMatchingShapes(f0[i], f0[i+1], path_arc=PI/2))
            self.wait()
        
        self.play(f0[5].animate.shift(DOWN), run_time=0.7)
        self.wait()
        self.play(TransformMatchingShapes(f0[5].copy(), VGroup(*v0a[:4])))
        
        self.wait()
        self.play(FadeOut(f0[5]), run_time=0.7)
        self.wait()
        
        self.play(FadeIn(l01, l02), run_time=0.7)
        self.wait()

        self.play(Circumscribe(v0a[3][0]))
        self.wait()


        self.play(Circumscribe(v0a[0]))
        self.wait()

        self.play(Write(f0[6]))
        self.wait()

        self.play(Circumscribe(v0a[3][0]), Circumscribe(f0[6]))
        self.wait()

        self.play(TransformMatchingShapes(VGroup(f0[6], v0a[3][0]).copy(), v0a[4].set_opacity(1)))
        self.wait()

        self.play(Circumscribe(v0a[3][1]), Circumscribe(f0[6]))
        self.wait()

        self.play(TransformMatchingShapes(VGroup(f0[6], v0a[3][1]).copy(), v0a[5].set_opacity(1)))
        self.wait()

        self.play(Circumscribe(v0a[3][2]), Circumscribe(f0[6]))
        self.wait()

        self.play(TransformMatchingShapes(VGroup(f0[6], v0a[3][2]).copy(), v0a[6].set_opacity(1)))
        self.wait()

        self.play(FadeIn(l1))
        self.wait()

        self.play(TransformMatchingShapes(VGroup(v0a[1], v0a[5]).copy(), v0a[7].set_opacity(1)))
        self.wait()

        self.play(TransformMatchingShapes(v0a[2].copy(), v0a[8].set_opacity(1)))
        self.wait()

        self.play(TransformMatchingShapes(v0a[6].copy(), v0a[9].set_opacity(1)))
        self.wait()


        self.play(Circumscribe(v0a[7]))
        self.wait()
        self.play(Circumscribe(v0a[3][0]))
        self.wait()
        self.play(
            FadeOut(VGroup(*v0a[:3], *v0a[4:7], l1))
        )
        self.wait()
        self.play(VGroup(v0a[3], f0[6],  l01, l02).animate.shift(UP), VGroup(v0a[7], v0a[8], v0a[9]).animate.shift(DOWN))
        self.play(TransformMatchingShapes(f0[6].copy(), f0[7][0]))
        self.wait()

        self.play(TransformMatchingShapes(VGroup(v0a[9], v0a[3]).copy(), f0[7][1]))
        self.wait()

        self.play(FadeOut(f0[6], v0a[7], v0a[8], v0a[9], v0a[3], l01, l02))
        self.wait()
        






def mt(t: str):
    return MathTex(t)

def t(t: str):
    return Tex(t)

def div_line(mobject: Mobject):
    l01 = Line(
            start=[mobject.get_left()[0]+0.5*LEFT[0], mobject.get_bottom()[1] + 0.3*DOWN[1], 0], 
            end=[mobject.get_left()[0]+0.5*LEFT[0], mobject.get_top()[1]+ 0.3*UP[1], 0], color=WHITE)
    l02 = Line(
        start=[mobject.get_left()[0]+0.5*LEFT[0], mobject.get_top()[1]+ 0.3*UP[1], 0], 
        end=[mobject.get_right()[0]+0.5*RIGHT[0], mobject.get_top()[1]+ 0.3*UP[1], 0], color=WHITE)

    return l01, l02

def horizontal_line(start_top: Mobject, start_bottom: Mobject , end_top: Mobject, end_bottom: Mobject):
    c0 = [
        (start_top.get_left()[0] + start_bottom.get_left()[0])/2,
        (start_top.get_bottom()[1] + start_bottom.get_top()[1])/2,
        0,
    ]

    c1 = [
        (end_top.get_right()[0] + end_bottom.get_right()[0])/2,
        (end_top.get_bottom()[1] + end_bottom.get_top()[1])/2,
        0,
    ]

    return Line(start=c0, end=c1, color=WHITE)
