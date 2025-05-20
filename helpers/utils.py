from manim import *


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