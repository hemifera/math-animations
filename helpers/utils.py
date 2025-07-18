from manim import Write, Scene, TransformMatchingShapes, MathTex, MathTable, VGroup, Point, Line
from numpy import array


def quickFormulas(self_parameter, formula_array: list[MathTex], wait_interval: float):
    formulas = formula_array
    current = formulas[0]
    self_parameter.play(Write(current))
    self_parameter.wait(wait_interval)

    # Transformar paso a paso
    for next_formula in formulas[1:]:
        next_formula.move_to(current)  # Asegura que esté en la misma posición
        self_parameter.play(TransformMatchingShapes(current, next_formula))
        self_parameter.wait(1)
        current = next_formula

    self_parameter.wait(wait_interval)
    self_parameter.clear()

def quickWriteFormulas(self_parameter, formula_array: list[MathTex], wait_interval: float):
    for formula in formula_array:
        self_parameter.play(Write(formula))
        self_parameter.wait(wait_interval)
        self_parameter.clear()


def getline(v: VGroup):
    v1 = v[0].get_right()
    v2 = v[1].get_left()
    vf = v[len(v)-1].get_bottom()
    
    
    x1 = (v1[0]+v2[0])/2
    y1 = v[0].get_top()[1]
    y2 = vf[1]
    p1 = Point(array([x1, y1, 0]))
    p2 = Point(array([x1, y2, 0]))
    
    return Line(p1, p2)