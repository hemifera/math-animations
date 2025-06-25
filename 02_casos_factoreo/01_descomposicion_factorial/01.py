from manim import *
import sys, os, math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from helpers import quickFormulas, quickWriteFormulas

class LinePoints:
    def __init__(self, table: MathTable, row_size, col_size):
        
        top = (table.get_entries((1, row_size-1)).get_top() + table.get_entries((1, row_size)).get_top())/2

        if row_size == 1:
            bottom = np.array([

                top[0], 
                table.get_entries((col_size, row_size)).get_bottom()[1], 
                0])
        else:
            bottom = np.array([
                top[0], 
                table.get_entries((col_size, row_size-1)).get_bottom()[1], 
                0])
        
        self.line = Line(top, bottom, color=WHITE)

# Imagen de introduccion
class fc_00(Scene):
    def construct(self):
        img = ImageMobject('img/udb_logo_high.png')
        t1 = Text("Descomposición factorial")
        t2 = Text("Caso de factoreo 1", font_size=32)
        v = VGroup(t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN).shift(DOWN*2.5))


class fc_01(Scene):
    def construct(self):

        f111 = MathTex(r"2 ({{1}} + {{3}} + {{5}})", substrings_to_isolate="2")
        f12 = MathTex(r"2(9)")
        f13 = MathTex(r"18")


        f21 = MathTex(r"2 \cdot {{1}} + 2 \cdot {{3}} + 2 \cdot {{5}}", substrings_to_isolate="2")
        f22 = MathTex(r"2+6+10")
        f23 = MathTex(r"18")

        ft1 = VGroup(f111,f12,f13).arrange(DOWN)
        ft2 = VGroup(f21,f22,f23).arrange(DOWN).shift(RIGHT*2)

        for component in ft1:
            self.play(Write(component))
            self.wait(1)

        self.play(ft1.animate.shift(LEFT*2))
        self.wait(1)

        for component in ft2:
            self.play(Write(component))
            self.wait(1)
        

        f31 = f22.copy()
        f32 = f21.copy()
        f33 = f111.copy()
        
        ft3 = VGroup(ft1, ft2)
        
        self.wait(1)
        self.play(ft3.animate.shift(UP))
 
        self.play(f31.animate.move_to(ORIGIN).move_to(DOWN))
        self.wait(1)
        self.play(f32.animate.move_to(ORIGIN).move_to(DOWN*2))
        self.wait(1)
        self.play(f33.animate.move_to(ORIGIN).move_to(DOWN*3))
        

        # self.remove(ft3)
        self.wait(1)

        ft4 = VGroup(f31, f32, f33)
        self.play(
            FadeOut(ft3),
            ft4.animate.arrange(DOWN, buff=0.3).move_to(ORIGIN))
        self.wait(1)

        self.play(
            f32.animate.set_color_by_tex("2", YELLOW),
            f33.animate.set_color_by_tex("2", YELLOW)
        )
        self.wait(1)

        variables = VGroup(
            MathTex("a").set_color(RED), 
            MathTex("b").set_color(RED), 
            MathTex("c").set_color(RED)
            ).arrange_submobjects().shift(UP*2)
        
        
        f41 = MathTex(r"2\cdot {{a}} + 2 \cdot {{b}} + 2 \cdot {{c}}", substrings_to_isolate="2").move_to(f32.get_center()).set_color_by_tex("a", RED).set_color_by_tex("b", RED).set_color_by_tex("c", RED)
        f42 = MathTex(r" 2 ( {{a}} + {{b}} + {{c}} )", substrings_to_isolate="2").move_to(f33.get_center()).set_color_by_tex("a", RED).set_color_by_tex("b", RED).set_color_by_tex("c", RED)
        
        
        self.wait(2)
        self.add(variables)

        self.wait(2)
        
        self.play(
            TransformMatchingTex(Group(f32, variables), f41)
            )
        self.wait(1)
        self.play(
            TransformMatchingTex(Group(f33, variables), f42)
            )
        self.wait(1)
        

        self.wait(2)

        self.play(FadeOut(Group(f31, f41, f42)))
        self.wait(1)
        self.play(f42.animate.move_to(ORIGIN).set_color(WHITE))
        self.wait(2)

        


class ejemplo_uno(Scene):
    def construct(self):
        self.play(AddTextWordByWord(Text("Máximo común divisor (MCD)").shift(UP*3)))
        t0 = MathTable(
            [[2, 6, 10, 2]], 
            line_config={"stroke_width": 0})
        t1 = MathTable(
            [[2, 6, 10, 2], [1, 3, 5, 0]], 
            line_config={"stroke_width": 0})
        
        lp0 = LinePoints(t0, 4 , 1)
        lp1 = LinePoints(t1, 4 , 2)
        self.add(
            t0.get_entries()[3].set_opacity(0), 
            t1.get_entries()[7].set_opacity(0)
            )
        self.play(
            Create(lp0.line),
            Create(t0)
            )
        
        self.wait(1)
        self.play(t0.get_entries()[3].animate.set_opacity(1))
        self.wait(1)
        
        self.play(
            TransformMatchingShapes(lp0.line, lp1.line), 
            FadeOut(t0, run_time=0.0), 
            Add(t1)
            )

        self.wait(1)
        
            
        v = Group()
        for i in range(3, 7):
            v.add(t1.get_entries()[i].copy())

        t = MathTex(r"{{2}}({{1}}+{{3}}+{{5}})").shift(DOWN*2)
        self.play(TransformMatchingTex(v, t))
        self.wait(1)


class ejemplo_dos(Scene):
    def construct(self):
        t0 =[[15, 3], [5, 5], [1, 0]]
        t00 = MathTable(t0, line_config={"stroke_width": 0})

        t1 = [[45, 5], [9, 3], [3, 3], [1,0]]
        # t11 = MathTable([], line_config={"stroke_width": 0})
        
        t2 = [[90, 2], [45, 5], [9, 3], [3, 3], [1,0]]
        # t22 = MathTable([], line_config={"stroke_width": 0})
        self.wait(1)
        
        ct = []
        r_size = len(t0)
        c_size = len(t0[len(t0)-1])

        print([t0[0]])
        t00 = MathTable([t0[0]], line_config={"stroke_width": 0})
        l = LinePoints(t00, 2, 1)

        # self.add(t00.get_entries((2, 1)).set_opacity(0))
        self.play(Create(l.line), Create(t00))

        self.wait(1)
        self.remove(t00)
        t00 = MathTable([t0[0], t0[1]], line_config={"stroke_width": 0})
        l01 = LinePoints(t00, 2, 2)
        self.play(TransformMatchingShapes(l.line, l01.line), Add(t00))
        self.wait(1)

        self.remove(t00)
        t00 = MathTable([t0[0], t0[1], t0[2]], line_config={"stroke_width": 0})
        l02 = LinePoints(t00, 2, 3)

        self.play(TransformMatchingShapes(l01.line, l02.line), Add(t00))
        self.wait(1)
        
        pass



class ejemplo_tres(Scene):
    def construct(self):
        t0 =[[15, 3], [5, 5], [1, 0]]
        t1 = [[45, 5], [9, 3], [3, 3], [1,0]]
        t2 = [[90, 2], [45, 5], [9, 3], [3, 3], [1,0]]
        t3 = [[15, 45, 90, 3], [5, 15, 30, 5], [1, 3, 6, 0]]

        t4 = [[30, 40, 80, 2], [15, 20, 40, 5], [3, 4, 8, 0]]


        



        tabla = t4
        table = MathTable(
            tabla, 
            line_config={"stroke_width": 0},
            v_buff = 0.5
        )

        filas = table.get_rows()
        columnas = table.get_columns()

        tf1 = VGroup()    
        [tf1.add(element) for element in filas[0][0: -1]]

            # print(element)
            

        f0 = MathTex(r"{{30}}a+{{40}}b+{{80}}c", substrings_to_isolate=["30", "40", "80"])
        self.play(Write(f0))
        self.wait(1)
        self.play(f0.animate.shift(UP*3))
        self.wait(1)
        self.play(
            TransformMatchingTex(f0.copy(), tf1)
        )
        self.wait(1)
        
        
        [fila.set_opacity(0) for fila in filas[1:]]
        self.add(table)
        self.wait(2)
        # [col.set_opacity(0) for col in columnas]

        self.add(table.get_vertical_lines()[-1].set_color(WHITE).set_stroke_width(3))
        for i, fila in enumerate(filas[1:]):
            f_non_zero = VGroup()
            for element in fila:
                if element.tex_string != "0":
                    f_non_zero.add(element)
            # l = LinePoints(table, i+1, 3)
            
            if i+1 != len(filas[1:]):
                self.play(f_non_zero[0: -1].animate.set_opacity(1))
                self.wait(2)
            else:
                self.play(f_non_zero.animate.set_opacity(1))
                self.wait(2)
            self.wait(2)

            if i+1 != len(filas[1:]):
                self.play(f_non_zero[-1].animate.set_opacity(1),)
                self.wait(2)
            self.wait(2)


        tc1 = VGroup()    
        [tc1.add(element.copy()) for element in columnas[-1][0: -1]]
        [tc1.add(element.copy()) for element in filas[-1][0: -1]]
        f2 = MathTex(r" {{2}}\times {{5}} ({{3}}a+{{4}}b+{{8}}c) ").shift(DOWN*2.5)
        f3 = MathTex(r"10(3a+4b+8c) ").shift(DOWN*2.5)
        self.play(
            TransformMatchingTex(tc1, f2)
        )
        
        self.wait(1)
        self.play(TransformMatchingShapes(f2, f3, key_map={"{{2}}\times {{5}} ": "10"}, path_arc=PI/2) )
        self.wait(1)

class recordatorio_potenciacion(Scene):
    def construct(self):
        f1 = MathTex(r"m^{a}\cdot m^{b}=m^{a+b}")
        self.play(Write(f1))
        self.wait(3)

        self.clear()
        f2 = [
            MathTex(r"m^{5}"),
            MathTex(r"m^{3}\cdot m^{2}"),
            MathTex(r"m^{3+2}"),
            MathTex(r"m^{5}"),
        ]
        fx = f2[0]
        self.play(Write(fx))
        self.wait(3)
        for f in f2[0:]:
            self.play(
                TransformMatchingShapes(fx, f, path_along_arc=PI/2)
            )
            fx = f
            self.wait(3)        


class ejemplo_cuatro(Scene):
    def construct(self):

        t4 = [[42, 105, 168, 3], [14, 35, 56, 7], [2, 5, 8, 0]]

        tabla = t4
        table = MathTable(
            tabla, 
            line_config={"stroke_width": 0},
            v_buff = 0.5
        )

        filas = table.get_rows()
        columnas = table.get_columns()

        tf1 = VGroup()    
        [tf1.add(element) for element in filas[0][0: -1]]

            # print(element)
            

        f0 = MathTex(r"{{42}}m^{3}+{{105}}m^{4}+{{168}}m^{5}", substrings_to_isolate=["42", "105", "147"])
        f1 = MathTex(r"{{42}}m^{3}+{{105}}m^{3} \cdot m^{1} +{{168}}m^{3} \cdot m^{2}", substrings_to_isolate=["42", "105", "147"])
        f2 = MathTex(r"m^{3}({{42}}+{{105}}m^{1} + {{168}}m^{2})", substrings_to_isolate=["42", "105", "147"])
        f3 = MathTex(r"m^{3}({{42}}+{{105}}m + {{168}}m^{2})", substrings_to_isolate=["42", "105", "147"])
        self.play(Write(f0))
        self.wait(1)
        self.play(TransformMatchingShapes(f0, f1, key_map={"m^{3}":"m^{3}"}))
        self.wait(1)
        self.play(TransformMatchingShapes(f1, f2, path_arc=PI/2, key_map={"m^{3}":"m^{3}"}))
        self.wait(1)
        self.play(TransformMatchingShapes(f2, f3))
        self.wait(1)
        self.play(f3.animate.shift(UP*3))

        self.wait(1)
        self.play(
            TransformMatchingTex(f3.copy(), tf1)
        )
        self.wait(1)
        
        
        [fila.set_opacity(0) for fila in filas[1:]]
        self.add(table)
        self.wait(2)
        # [col.set_opacity(0) for col in columnas]

        self.add(table.get_vertical_lines()[-1].set_color(WHITE).set_stroke_width(3))
        for i, fila in enumerate(filas[1:]):
            f_non_zero = VGroup()
            for element in fila:
                if element.tex_string != "0":
                    f_non_zero.add(element)
            # l = LinePoints(table, i+1, 3)
            
            if i+1 != len(filas[1:]):
                self.play(f_non_zero[0: -1].animate.set_opacity(1))
                self.wait(2)
            else:
                self.play(f_non_zero.animate.set_opacity(1))
                self.wait(2)
            self.wait(2)

            if i+1 != len(filas[1:]):
                self.play(f_non_zero[-1].animate.set_opacity(1),)
                self.wait(2)
            self.wait(2)


        tc1 = VGroup()    
        [tc1.add(element.copy()) for element in columnas[-1][0: -1]]
        [tc1.add(element.copy()) for element in filas[-1][0: -1]]
        f4 = MathTex(r" {{3}}\cdot {{7}} \cdot m^{3} ({{2}}+{{5}}m+{{8}}m^{2}) ").shift(DOWN*2.5)
        f5 = MathTex(r"21m^{3}(2+5m+8m^{2}) ").shift(DOWN*2.5)
        self.play(
            TransformMatchingTex(tc1, f4)
        )
        
        self.wait(1)
        self.play(TransformMatchingShapes(f4, f5, key_map={"{{3}}\times {{7}} ": "21"}, path_arc=PI/2) )
        self.wait(1)


class ejemplo_cinco(Scene):
    def construct(self):

        t4 = [[150, 210, 270, 2], [75, 105, 135, 3], [25, 35, 45, 5], [5, 7, 9, 0]]

        tabla = t4
        table = MathTable(
            tabla, 
            line_config={"stroke_width": 0},
            v_buff = 0.5
        )

        filas = table.get_rows()
        columnas = table.get_columns()

        tf1 = VGroup()    
        [tf1.add(element) for element in filas[0][0: -1]]

            # print(element)
            

        f0 = MathTex(r"{{150}}a^{2} b^{2}+{{210}}a^{2}b^{4}+{{270}} a^{2} b^{6}")
        f1 = MathTex(r"{{150}}a^{2} b^{2} +{{210}}a^{2} b^{2} \cdot b^{2} + {{270}}a^{2} b^{2} \cdot b^{4}")
        f2 = MathTex(r"a^{2} b^{2}({{150}}+{{210}}b^{2} + {{270}}b^{4})")
        f3 = MathTex(r"a^{2} b^{2}({{150}}+{{210}}b^{2} + {{270}}b^{4})", substrings_to_isolate=["42", "105", "147"])
        self.play(Write(f0))
        self.wait(1)
        self.play(TransformMatchingShapes(f0, f1,path_arc=PI, key_map={r"a^{2} b^{2}":r"a^{2} b^{2}"}))
        self.wait(1)
        self.play(TransformMatchingShapes(f1, f2, path_arc=PI, key_map={r"a^{2} b^{2}":r"a^{2} b^{2}"}))
        self.wait(1)
        self.play(TransformMatchingShapes(f2, f3))
        self.wait(1)
        self.play(f3.animate.shift(UP*3))

        self.wait(1)
        self.play(
            TransformMatchingTex(f3.copy(), tf1)
        )
        self.wait(1)
        
        
        [fila.set_opacity(0) for fila in filas[1:]]
        self.add(table)
        self.wait(2)
        # [col.set_opacity(0) for col in columnas]

        self.add(table.get_vertical_lines()[-1].set_color(WHITE).set_stroke_width(3))
        for i, fila in enumerate(filas[1:]):
            f_non_zero = VGroup()
            for element in fila:
                if element.tex_string != "0":
                    f_non_zero.add(element)
            # l = LinePoints(table, i+1, 3)
            
            if i+1 != len(filas[1:]):
                self.play(f_non_zero[0: -1].animate.set_opacity(1))
                self.wait(2)
            else:
                self.play(f_non_zero.animate.set_opacity(1))
                self.wait(2)
            self.wait(2)

            if i+1 != len(filas[1:]):
                self.play(f_non_zero[-1].animate.set_opacity(1),)
                self.wait(2)
            self.wait(2)


        tc1 = VGroup()    
        [tc1.add(element.copy()) for element in columnas[-1][0: -1]]
        [tc1.add(element.copy()) for element in filas[-1][0: -1]]
        f4 = MathTex(r" {{2}}\cdot {{3}}\cdot {{5}} \cdot a^{2} b^{2}({{5}}+{{7}}b^{2} + {{9}}b^{4})").shift(DOWN*2.5)
        f5 = MathTex(r"30a^{2} b^{2}(5+7b^{2}+9b^{4}) ").shift(DOWN*2.5)
        self.play(
            TransformMatchingTex(tc1, f4)
        )
        
        self.wait(1)
        self.play(TransformMatchingShapes(f4, f5, key_map={r"{{2}}\cdot {{3}}\cdot {{5}}": r"30"}, path_arc=PI/2) )
        self.wait(1)

