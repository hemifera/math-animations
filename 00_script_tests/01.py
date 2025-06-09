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



class PolynomialLongDivision(Scene):
    def construct(self):
        # Create the polynomials
        # Create the polynomials
        dividend = MathTex(r"x^3 + 2x^2 + 3x + 4")
        divisor = MathTex(r"x + 1")
        quotient = MathTex(r"x^2 + x + 2 \text{ (quotient)}")
        remainder = MathTex(r"2 \text{ (remainder)}")

        # Position the polynomials
        dividend.move_to(UP * 2)
        divisor.move_to(UP * 0.5)
        quotient.move_to(DOWN * 1.5)
        remainder.move_to(DOWN * 2.5)

        # Create a table for the long division
        table = MathTable(
            [["Step", "Operation", "Result"],
             ["1", r"$x^3 \div x$", r"$x^2$"],
             ["2", r"$x^2 \cdot (x + 1)$", r"$x^3 + x^2$"],
             ["3", r"$\text{Subtract: } (2x^2 - x^2)$", r"$x^2 + 3x + 4$"],
             ["4", r"$x^2 \div x$", r"$x$"],
             ["5", r"$x \cdot (x + 1)$", r"$x^2 + x$"],
             ["6", r"$\text{Subtract: } (3x - x)$", r"$2x + 4$"],
             ["7", r"$2x \div x$", r"$2$"],
             ["8", r"$2 \cdot (x + 1)$", r"$2x + 2$"],
             ["9", r"$\text{Subtract: } (4 - 2)$", r"$2$"]],
            col_labels=[Text("Step"), Text("Operation"), Text("Result")],
            include_outer_lines=True,
        )

        table.move_to(DOWN * 0.5)

        # Display the dividend and divisor
        self.play(Write(dividend))
        self.play(Write(divisor))

        # Show the long division table
        self.wait(1)
        self.play(Create(table))
        self.wait(1)

        # Show the quotient and remainder
        self.play(Write(quotient))
        self.wait(1)
        self.play(Write(remainder))
        self.wait(2)

        # Final message
        final_message = Tex("Thus, the result is: $x^2 + x + 2$ with a remainder of $2$")
        final_message.move_to(DOWN * 3.5)
        self.play(Write(final_message))
        self.wait(2)


# To run this, save it as a .py file and run it using the Manim command:
# manim -pql your_script_name.py PolynomialLongDivision
