from manim import *
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helpers import quickFormulas, quickWriteFormulas


class logaritmos_01(Scene):
    def construct(self):

        f1 = MathTex(r"\log_{\text{base}}{(\text{argumento})}=\text{resultado}").shift(UP)
        f2 = MathTex(r" \text{argumento}=\text{resultado}^\text{base}")
        self.add(f1)
        self.add(f2)

        self.wait(2)

class logaritmos_02(Scene):
    def construct(self):
        
        f1 = MathTex(r"\log_{3}{81}=?").shift(UP)
        f2 = MathTex(r"3^{4}=81")
        f3 = MathTex(r"\log_{3}{81}=4").shift(UP)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f1))
        
        self.play(TransformMatchingShapes(f1, f3))
        self.wait(2)

class logaritmos_03(Scene):
    def construct(self):
        
        f1 = [
            MathTex(r"\log_{2}{16}=?"),
        ]

        quickWriteFormulas(self, f1, 2)


        f2 = [
            MathTex(r"2^1=2"),
            MathTex(r"2^2 = 4"),
            MathTex(r"2^3 = 8"),
            MathTex(r"2^{4} = 16"),
        ]

        quickFormulas(self, f2, 2)

        f2 = [
            MathTex(r"\log_{2}{16}=?"),
            MathTex(r"\log_{2}{16}=4"),
        ]

        quickFormulas(self, f2, 2)
        
        
        self.wait(2)


class logaritmos_04(Scene):
    def construct(self):
        

        f1 = MathTex(r"\log_{5}{25}=?")
        f11 = MathTex(r"5^{?}=25")

        f2 = MathTex(r"\log_{5}{25}=2")
        f22 = MathTex(r"5^{2}=25")

        self.play(
            Write(f1),
        )

        self.wait(1)
        self.play(
            f1.animate.shift(UP),
            Write(f11)
        )

        self.wait(2)

        self.clear()
        self.add(
            f2.shift(UP), f22
        )

        self.wait(2)


class equivalencias_01(Scene):
    def construct(self):
        
        f1 = [
            MathTex(r"\ln x=\log_{e}{x} \quad\{e=2.71828\dots\}")
        ]

        quickWriteFormulas(self, f1, 2)

        f2 = [
            MathTex(r"\log x=\log_{10}x")
        ]

        quickWriteFormulas(self, f2, 2)


class propiedades_01(Scene):
    def construct(self):
        f1 = [MathTex(r"\log_{a}{(mn)}=\log_{a}(m)+\log_{a}(n)")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"\log_{3}(9)"),
            MathTex(r"\log_{3}(3\times 3)"),
            MathTex(r"\log_{3}3+\log_{3}3"),
            MathTex(r"1+1"),
            MathTex(r"2"),
        ]
        quickFormulas(self, f2, 2)


class propiedades_02(Scene):
    def construct(self):
        f1 = [MathTex(r"\log_{a}{\left( \frac{m}{n} \right)}=\log_{a}{m}-\log_{a}{n}")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"\log_{4}\left( \frac{2}{3} \right)"),
            MathTex(r"\log_{4}2-\log_{4}{3}"),
        ]
        quickFormulas(self, f2, 2)

class propiedades_03(Scene):
    def construct(self):
        f1 = [MathTex(r"\log_{a}(x^{n})=n\log_{a}x")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"\log_{2}{9}"),
            MathTex(r"\log_{2}{3^{2}}"),
            MathTex(r"2\log_{2}{3}"),
        ]
        quickFormulas(self, f2, 2)

class propiedades_04(Scene):
    def construct(self):
        f1 = [MathTex(r"\log_{a}(\sqrt[n]{x^{m}})=\log_{a}\left( x^{\frac{m}{n}} \right)=\frac{m}{n}\log_{a}{x}")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"\log_{4}(\sqrt{ 16 })"),
            MathTex(r"\log_{4}(16^{1/2})"),
            MathTex(r"\frac{1}{2}\log_{4}(16)"),
            MathTex(r"\frac{1}{2}\cdot2=1"),
        ]
        quickFormulas(self, f2, 2)



class propiedades_05(Scene):
    def construct(self):
        

        f1 = MathTex(r"\log_{a}1=?")
        f11 = MathTex(r"a^{?}=1")

        f2 = MathTex(r"\log_{a}1=0")
        f22 = MathTex(r"a^{0}=1")

        f3 = MathTex(r"\{a>0 \cap a\neq1\}")

        self.play(
            Write(f1),
        )

        self.wait(1)
        self.play(
            f1.animate.shift(UP),
            Write(f11)
        )

        self.wait(2)

        self.clear()
        self.add(
            f2.shift(UP), f22
        )
        self.wait(2)
        self.play(Write(f3.shift(DOWN)))

        self.wait(2)
        self.clear()
        f4 = MathTex(r"{log_{-2}{5}}", color=RED)
        f5 = MathTex(r"{log_{0}{10}}", color=RED)
        f6 = MathTex(r"{log_{1}{80}}", color=RED)



        self.play(
            Write(f4.shift(UP)),
            Write(f5),
            Write(f6.shift(DOWN)),
        )

        self.wait(2)
        self.clear()
        f7 = [MathTex(r"\log_{a}1=0 \quad\{a>0 \cap a\neq1\}")]
        quickWriteFormulas(self, f7, 3)

        # self.wait(2)

        f8 = [
            MathTex(r"\log_{\frac{\pi^{2}}{6}}(1)=0")
            ]
        quickWriteFormulas(self, f8, 3)


class propiedades_06(Scene):
    def construct(self):
        

        f1 = MathTex(r"\log_{a}a=?")
        f11 = MathTex(r"a^{?}=a")

        f2 = MathTex(r"\log_{a}a=1")
        f22 = MathTex(r"a^{1}=a")

        self.play(
            Write(f1),
        )

        self.wait(1)
        self.play(
            f1.animate.shift(UP),
            Write(f11)
        )

        self.wait(2)

        self.clear()
        self.add(
            f2.shift(UP), f22
        )
        self.wait(2)
        self.clear()


        f8 = [
            MathTex(r"\log_{102}{102}=1")
            ]
        quickWriteFormulas(self, f8, 3)




class propiedades_07(Scene):
    def construct(self):

        f1 = MathTex(r"\log_{a}{m}=\frac{\log_{b}{m}}{\log_{b}{a}}")
        f2 = MathTex(r"\{b\text{ es arbitario} \cap b>0\cap b\neq 1\}")

        formulas = VGroup(f1, f2).arrange(DOWN)

        
        self.play(Create(formulas))



        self.wait(2)

        self.clear()

        f3 = [
            MathTex(r"\log_{3}{5}"),
            MathTex(r"\frac{\log_{5}5}{\log_{5}3}"),
            MathTex(r"\frac{1}{\log_{5}3}"),
        
        ]
        quickFormulas(self, f3, 3)

        f4 = [
            MathTex(r"\frac{\ln (F)}{\ln 10}"),
            MathTex(r"\frac{\log_{e}(F)}{\log_{e} 10}"),
            MathTex(r"\log_{10}F"),
            MathTex(r"\log F"),
        
        ]
        quickFormulas(self, f4, 3)
        

class propiedades_08(Scene):
    def construct(self):
        f1 = [MathTex(r"a^{\log_{a}{x}}=x")]
        quickWriteFormulas(self, f1, 3)

        f2 = [
            MathTex(r"\left( \frac{22+e{^3}}{2+\pi} \right)^{\log_{\frac{22+e{^3}}{2+\pi} }(9)}"),
            MathTex(r"9"),
        ]
        quickFormulas(self, f2, 2)

        f3 = [
            MathTex(r"e^{\ln (4+\pi)}"),
            MathTex(r"e^{\log_{e}(4+\pi)}"),
            MathTex(r"4+\pi"),
        ]
        quickFormulas(self, f3, 2)


class ejemplos_01(Scene):
    def construct(self):
        f1 = MathTex(r"\frac{\log10+\ln \sqrt{ e{^4} }+20^{\log_{20}(\sqrt{ 16 }-1)}}{\log_{525}(525)\times \ln e^{2}}")
        self.play(Write(f1))
        self.wait(2)
        
        
        self.play(f1.animate.shift(UP*2))
        f2 = [
            MathTex(r"\log10"),
            MathTex(r"\log_{10}10"),
            MathTex(r"1"),
        ]
        quickFormulas(self, f2, 2)
        self.add(MathTex(r"\frac{1+\ln \sqrt{ e{^4} }+20^{\log_{20}(\sqrt{ 16 }-1)}}{\log_{525}(525)\times \ln e^{2}}").shift(UP*2))
        
        f3 = [
            MathTex(r"\ln \sqrt{ e{^4} }"),
            MathTex(r"\ln  ( (e{^4}) ^ {\frac{1}{2} })"),
            MathTex(r"\ln e^ {\frac{4}{2}} "),
            MathTex(r"\ln  e{^2} "),
            MathTex(r"2\ln  e "),
            MathTex(r"2\log_{e} e"),
            MathTex(r"2 \cdot 1"),
            MathTex(r"2"),
        ]
        quickFormulas(self, f3, 2)
        self.add(MathTex(r"\frac{1+2+20^{\log_{20}(\sqrt{ 16 }-1)}}{\log_{525}(525)\times \ln e^{2}}").shift(UP*2))
        self.wait(2)



        f4 = [
            MathTex(r"20^{\log_{20}\sqrt{ 16 }-1}"),
            MathTex(r"20^{\log_{20} {4 -1}}"),
            MathTex(r"20^{\log_{20} {3}}"),
            MathTex(r"3"),
        ]
        quickFormulas(self, f4, 2)
        self.add(MathTex(r"\frac{1+2+3}{\log_{525}(525)\times \ln e^{2}}").shift(UP*2))
        self.wait(2)

        f5 = [
            MathTex(r"\log_{525}(525)"),
            MathTex(r"1"),
        ]
        quickFormulas(self, f5, 2)
        self.add(MathTex(r"\frac{1+2+3}{1 \times \ln e^{2}}").shift(UP*2))
        self.wait(2)

        f6 = [
            MathTex(r"\ln e^{2}"),
            MathTex(r"2\ln e"),
            MathTex(r"2\log_{e} e"),
            MathTex(r"2 \cdot 1"),
            MathTex(r"2"),
        ]
        quickFormulas(self, f6, 2)

        f7 = MathTex(r"\frac{1+2+3}{1 \times 2 }").shift(UP*2)
        self.add(f7)
        self.wait(1)

        self.play(f7.animate.shift(DOWN*2))
        self.wait(1)
        self.clear()
        f8 = [
            MathTex(r"\frac{6}{2}"),
            MathTex(r"3"),
        ]

        quickFormulas(self, f8, 2)




        