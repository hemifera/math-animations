from manim import *
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helpers import quickFormulas

class homogenea_01(Scene):
    def construct(self):
        f1 = [
            MathTex(r"\frac{a}{c}+ \frac{b}{c}"),
            MathTex(r"\frac{a+ b}{c}"),
        ]

        quickFormulas(self, f1, 2)

        self.clear()

        f2 = [
            MathTex(r"\frac{a}{c}- \frac{b}{c}"),
            MathTex(r"\frac{a- b}{c}"),
        ]

        quickFormulas(self, f2, 2)

        self.clear()

        f3 = [
            MathTex(r"\frac{a}{c}\pm \frac{b}{c}"),
            MathTex(r"\frac{a\pm b}{c}"),
        ]

        quickFormulas(self, f3, 2)

        self.clear()


class eje_homogenea_01(Scene):
    def construct(self):
        f1 = [
            MathTex(r"\frac{3}{4}+\frac{5}{4}"),
            MathTex(r"\frac{3+5}{4}"),
            MathTex(r"\frac{8}{4}"),
            MathTex(r"2"),
        ]

        quickFormulas(self, f1, 2)

        self.clear()

        f2 = [
            MathTex(r"\frac{25}{100}+\frac{25}{100}+\frac{25}{100}+\frac{25}{100}"),
            MathTex(r"\frac{25+25+25+25}{100}"),
            MathTex(r"\frac{100}{100}"),
            MathTex(r"1"),
        ]

        quickFormulas(self, f2, 2)

        self.clear()

        f3 = [
            MathTex(r"\frac{23}{17}+\frac{15}{17}+\frac{13}{17}"),
            MathTex(r"\frac{51}{17}"),
            MathTex(r"3"),
        ]

        quickFormulas(self, f3, 2)

        self.clear()


class heterogenea_01(Scene):
    def construct(self):
        f1 = [
            MathTex(r"\frac{a}{b}+\frac{c}{d}"),
            MathTex(r"\frac{ad+bc}{bd}"),
        ]

        quickFormulas(self, f1, 2)

        self.clear()

        f2 = [
            MathTex(r"\frac{a}{b}-\frac{c}{d}"),
            MathTex(r"\frac{ad-bc}{bd}"),
        ]

        quickFormulas(self, f2, 2)

        self.clear()

        f3 = [
            MathTex(r"\frac{a}{b}\pm\frac{c}{d}"),
            MathTex(r"\frac{ad\pm bc}{bd}"),
        ]

        quickFormulas(self, f3, 2)

        self.clear()


class eje_heterogenea_01(Scene):
    def construct(self):
        f1 = [
            MathTex(r"\frac{3}{4}+\frac{5}{7}"),
            MathTex(r"\frac{3\cdot 7 + 4\cdot 5}{4\cdot 7}"),
            MathTex(r"\frac{21+20}{28}"),
            MathTex(r"\frac{41}{28}"),
        ]

        quickFormulas(self, f1, 2)

        self.clear()

        f2 = [
            MathTex(r"\frac{4}{9}-\frac{12}{6}"),
            MathTex(r"\frac{4}{9}-2"),
            MathTex(r"\frac{4}{9}-\frac{2}{1}"),
            MathTex(r"\frac{4 \cdot 1 - 9\cdot 2}{9\cdot 1}"),
            MathTex(r"\frac{-14}{9}"),
            MathTex(r"-\frac{14}{9}"),
        ]

        quickFormulas(self, f2, 2)

        self.clear()

        f3 = [
            MathTex(r"-\frac{1}{3}-\frac{7}{8}"),
            MathTex(r"\frac{-1}{3}-\frac{7}{8}"),
            MathTex(r"\frac{-1 \cdot 8 - 3\cdot 7}{24}"),
            MathTex(r"-\frac{14}{24}"),
            MathTex(r"-\frac{7}{12}"),
        ]

        quickFormulas(self, f3, 2)

        self.clear()

class eje_heterogenea_02(Scene):
    def construct(self):
        f1 = [
            MathTex(r"\frac{-4}{3}+\frac{5}{2}+\frac{2}{3}+\frac{7}{14}"),
            MathTex(r"\left[ \frac{-4}{3} +\frac{2}{3} \right]+\left[ \frac{5}{2}+\frac{1}{2} \right]"),
            MathTex(r"\frac{-4+2}{3}+\frac{5+1}{2}"),
            MathTex(r"\frac{-2}{3}+\frac{6}{2}"),
            
            MathTex(r"\frac{-2\cdot2+6\cdot3}{3\cdot2}"),
            MathTex(r"\frac{-4+18}{6}"),
            MathTex(r"\frac{14}{6}"),
            MathTex(r"\frac{7}{3}"),
        ]

        quickFormulas(self, f1, 2)

        self.clear()

        f2 = [
            MathTex(r"\frac{\frac{25}{5}}{\frac{10}{20}}"),
            MathTex(r"\frac{25}{5} \div \frac{10}{20}"),
            MathTex(r"\frac{5}{1}\div \frac{1}{2}"),
            MathTex(r"\frac{5\cdot 2}{1\cdot 1}"),
            MathTex(r"\frac{10}{1}"),
            MathTex(r"10"),
        ]

        quickFormulas(self, f2, 2)

        self.clear()

        f3 = [
            MathTex(r"\frac{\frac{5}{3}}{9}\cdot -\frac{3}{5}"),
            MathTex(r"\frac{5}{3}\div \frac{9}{1}\cdot \frac{-3}{5}"),
            MathTex(r"\frac{5\cdot 1}{3 \cdot9}\left( \frac{-3}{5} \right) "),
            MathTex(r"\frac{\not 5}{27}\times \frac{-3}{\not 5}"),
            MathTex(r"-\frac{1}{9}"),
        ]

        quickFormulas(self, f3, 2)

        self.clear()




