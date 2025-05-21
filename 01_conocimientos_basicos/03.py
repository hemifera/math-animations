from manim import MathTex, Scene
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helpers import quickFormulas, quickWriteFormulas

class exponentes_01(Scene):
    def construct(self):
        f1 = [MathTex(r"a^{m}=a \times a\times a\times a\times \cdots \times a")]
        quickWriteFormulas(self, f1, 3)

        

        f2 = [
            MathTex(r"2^{3}"),
            MathTex(r"2\times2\times2"),
            MathTex(r"8"),
        ]
        quickFormulas(self, f2, 2)

        f22 = [MathTex(r"2^{3}=2\times2\times2=8")]
        quickWriteFormulas(self, f22, 3)

        f3 = [
            MathTex(r"580^{1}"),
            MathTex(r"580"),
        ]
        quickFormulas(self, f3, 2)

class propiedades_01(Scene):
    def construct(self):
        f1 = [
            MathTex(r"a^{m}\times a^{n}"),
            MathTex(r"a^{m+n}"),
            
            ]
        quickFormulas(self, f1, 3)

        quickWriteFormulas(self, [MathTex(r"a^{m}\times a^{n}=a^{m+n}"),], 5)

        f2 = [
            MathTex(r"3\times 3^{3}"),
            MathTex(r"3^{1}\times3^{3}"),
            MathTex(r"3^{1+3}"),
            MathTex(r"3^{4}"),
            MathTex(r"3 \times 3 \times 3 \times 3"),
            MathTex(r"81"),
        ]
        quickFormulas(self, f2, 2)


class propiedades_02(Scene):
    def construct(self):
        f1 = [MathTex(r"(a^{m})^{n}=a^{m\times n}")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"(2^{2})^{3}"),
            MathTex(r"2^{2\times 3}"),
            MathTex(r"2^{6}"),
            MathTex(r"2 \times 2 \times 2 \times 2 \times 2 \times 2"),
            MathTex(r"64"),
        ]
        quickFormulas(self, f2, 2)

class propiedades_03(Scene):
    def construct(self):
        f1 = [MathTex(r"(ab)^{m}=a^m \times b^{m}")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"6^{2}"),
            MathTex(r"6 \times 6 "),
            MathTex(r"36"),
            MathTex(r"6^{2}"),
            MathTex(r"(3\cdot 2)^2"),
            MathTex(r"3^2\times 2^2 "),
            MathTex(r"9\times4"),
            MathTex(r"36"),
        ]
        quickFormulas(self, f2, 2)


class propiedades_04(Scene):
    def construct(self):
        f1 = [MathTex(r"a^{-m}=\frac{1}{a^m}")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"2^{-3}"),
            MathTex(r"\frac{1}{2^3}"),
            MathTex(r"\frac{1}{8}"),
        ]
        quickFormulas(self, f2, 2)

class propiedades_05(Scene):
    def construct(self):
        f1 = [MathTex(r"\left( \frac{a}{b} \right)^{m}=\frac{a^{m}}{b^{m}}")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"\left( \frac{3}{5} \right)^{2}"),
            MathTex(r"\frac{3^{2}}{5^2}"),
            MathTex(r"\frac{9}{25}"),
        ]
        quickFormulas(self, f2, 2)


class propiedades_06(Scene):
    def construct(self):
        f1 = [MathTex(r"\frac{a^{m}}{a^{n}}=a^{m-n}")]
        quickWriteFormulas(self, f1, 3)

        f2 = [MathTex(r"\frac{8}{16}=\frac{1}{2}")]
        quickWriteFormulas(self, f2, 3)

        f22 = [
            MathTex(r"\frac{8}{16}"),
            MathTex(r"\frac{2^{3}}{2^{4}}"),
            MathTex(r"2^{3-4}"),
            MathTex(r"2^{-1}"),
            MathTex(r"\frac{1}{2}"),
        ]
        quickFormulas(self, f22, 2)

        f33 = [MathTex(r"\frac{8}{16}= \frac{2^{3}}{2^{4}} =\frac{1}{2}")]
        quickWriteFormulas(self, f33, 3)


class propiedades_07(Scene):
    def construct(self):
        f1 = [MathTex(r"a^{0}=1 \quad \{a\neq 0\}")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"\left( \frac{20+\pi}{2622\pi^{2}-1} \right)^{0}"),
            MathTex(r"1"),
            MathTex(r"\left( -\frac{1856}{3} \right)^{0}"),
            MathTex(r"1"),
        ]
        quickFormulas(self, f2, 2)

class propiedades_08(Scene):
    def construct(self):
        f1 = [MathTex(r"\sqrt[n]{a^{m}}=a^{\frac{m}{n}}")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"\sqrt{4}"),
            MathTex(r"\sqrt[2]{4}"),
            MathTex(r"4^{\frac{1}{2}}"),
            MathTex(r"(2^{2}){^\frac{1}{2}}"),
            MathTex(r"2^{\frac{2}{2}}"),
            MathTex(r"2^{1}"),
            MathTex(r"2"),
        ]
        quickFormulas(self, f2, 2)

        f3 = [
            MathTex(r"\sqrt[3] {8}"),
            MathTex(r"\sqrt[3]{2 \times 2 \times 2}"),
            MathTex(r"\sqrt[3]{2^3}"),
            MathTex(r"2^{\frac{3}{3} }"),
            MathTex(r"2^1"),
            MathTex(r"2"),
        ]
        quickFormulas(self, f3, 2)

class ejemplos_01(Scene):
    def construct(self):
        f1 = [
            MathTex(r"\sqrt[3]{ {\frac{8}{27}} }"),
            MathTex(r"\left( \frac{8}{27} \right)^{\frac{1}{3}}"),
            MathTex(r"\left( \frac{2^{3}}{3^{3}} \right)^{\frac{1}{3}}"),
            MathTex(r"\left[ \left( \frac{2}{3} \right)^{3} \right]^{\frac{1}{3}}"),
            MathTex(r"\left( \frac{2}{3} \right)^{\frac{3}{3}}"),
            MathTex(r"\frac{2}{3}"),
        ]

        quickFormulas(self, f1, 2)


class ejemplos_02(Scene):
    def construct(self):
        f1 = [
            MathTex(r"\sqrt{\frac{1}{16}}"),
            MathTex(r"\left( \frac{1}{2^{4}} \right)^{\frac{1}{2}}"),
            MathTex(r"(2^{-4}){^\frac{1}{2}}"),
            
            MathTex(r"2^{-\frac{4}{2}}"),
            MathTex(r"2^{-2}"),
            MathTex(r"\frac{1}{2^{2}}"),
            MathTex(r"\frac{1}{4}"),

        ]

        quickFormulas(self, f1, 2)

class ejemplos_021(Scene):
    def construct(self):
        f1 = [
            MathTex(r"\sqrt{ \frac{1}{16} }"),
            MathTex(r"\frac{\sqrt{ 1 }}{\sqrt{ 16 }}"),
            MathTex(r"\frac{1}{4}"),
            
        ]

        quickFormulas(self, f1, 2)