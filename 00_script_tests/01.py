from manim import *


class LogDerivationWithShapes(Scene):
    def construct(self):
        # Lista de fórmulas
        formulas = [
            MathTex(r"q = q_{0}(1 - e^{t/\tau})"),
            MathTex(r"\frac{q}{q_{0}} = 1 - e^{t/\tau}"),
            MathTex(r"e^{t/\tau} = 1 - \frac{q}{q_{0}}"),
            MathTex(r"\ln(e^{t/\tau}) = \ln\left(1 - \frac{q}{q_{0}}\right)"),
            MathTex(r"\frac{t}{\tau} \ln e = \ln\left(1 - \frac{q}{q_{0}}\right)"),
            MathTex(r"t = \tau \ln\left(1 - \frac{q}{q_{0}}\right)")
        ]

        quickFormulas(self, formulas, 1)


class PPEPEPE(Scene):
    def construct(self):
        # Lista de fórmulas
        formulas = [
            # MathTex(r"left( \frac{22+e{^3}}{2+\pi} \right)^{\log_{\frac{22+e{^3}}{2+\pi} }(9)}=9"),
            MathTex(r"e^{\ln (4+\pi)}"),
            MathTex(r"e^{\log_{e}(4+\pi)}"),
            MathTex(r"1 \times (4+\pi)"),
            # MathTex(r"(4+\pi) \cdot 1"),
            MathTex(r"4+\pi"),
            # MathTex(r"e^{t/\tau} = 1 - \frac{q}{q_{0}}"),
            # MathTex(r"\ln(e^{t/\tau}) = \ln\left(1 - \frac{q}{q_{0}}\right)"),
            # MathTex(r"\frac{t}{\tau} \ln e = \ln\left(1 - \frac{q}{q_{0}}\right)"),
            # MathTex(r"t = \tau \ln\left(1 - \frac{q}{q_{0}}\right)")
        ]

        quickFormulas(self, formulas, 1)
        # # Mostrar la primera fórmula
        # current = formulas[0]
        # self.play(Write(current))
        # self.wait(1)

        # # Transformar paso a paso
        # for next_formula in formulas[1:]:
        #     next_formula.move_to(current)  # Asegura que esté en la misma posición
        #     self.play(TransformMatchingShapes(current, next_formula))
        #     self.wait(1)
        #     current = next_formula

        # self.wait(2)



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
    


class niceTest(Scene):
    def construct(self):
        formulas = [
            MathTex(r"\frac{\ln (F)}{\ln 10}"),
            MathTex(r"\log_{10}F"),
            MathTex(r"\log F"),
        ]

        quickFormulas(self, formulas, 1)