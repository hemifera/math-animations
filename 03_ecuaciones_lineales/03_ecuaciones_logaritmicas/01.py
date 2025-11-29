from manim import *

class elog_00(Scene):
    def construct(self):
        img = ImageMobject("../../img/udb_logo_high.png")
        t1 = Text(r"Ecuaciones logarítmicas")
        t2 = Text(r"Ejercicios", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))


class elog_10(Scene):
    def construct(self):
        props = VGroup(
                    MathTex(r"\log_{a}{(mn)}=\log_{a}(m)+\log_{a}(n)", font_size=40),
                    MathTex(r"\log_{a}{\left( \frac{m}{n} \right)}=\log_{a}{m}-\log_{a}{n}", font_size=40),
                    MathTex(r"\log_{a}(x^{n})=n\log_{a}x", font_size=40),
                    MathTex(r"\log_{a}(\sqrt[n]{x^{m}})=\frac{m}{n}\log_{a}{x}", font_size=40),
                    MathTex(r"\log_{a}1=0 \quad\{a>0\}", font_size=40),
                    MathTex(r"\log_{a}a=1", font_size=40),
                    MathTex(r"\log_{a}{m}=\frac{\log_{b}{m}}{\log_{b}{a}}", font_size=40),
                    MathTex(r"a^{\log_{a}{x}}=x", font_size=40),
                ).arrange_in_grid(rows=4, cols=2, buff=(1.0, 0.5))
        f = [
            t(r"Recordar propiedades de los exponentes y  \\logaritmos..."),
            t(r"")
        ]
        self.play(Write(f[0]), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(f[0]))
        self.play(Write(props))
        self.wait(2)
        self.play(FadeOut(props))
        
        props2 = VGroup(
            MathTex(r"a^{m}\times a^{n}=a^{m+n}"),
            MathTex(r"(a^{m})^{n}=a^{m\times n}"),
            MathTex(r"(ab)^{m}=a^m \times b^{m}"),
            MathTex(r"a^{-m}=\frac{1}{a^m}"),
            MathTex(r"\left( \frac{a}{b} \right)^{m}=\frac{a^{m}}{b^{m}}"),
            MathTex(r"\frac{a^{m}}{a^{n}}=a^{m-n}"),
            MathTex(r"a^{0}=1 \quad \{a\neq 0\}"),
            MathTex(r"\sqrt[n]{a^{m}}=a^{\frac{m}{n}}"),
        ).arrange_in_grid(rows=4, cols=2, buff=(1.0, 0.5))

        self.play(
            Write(props2),)
        
        
        self.wait(2)

class elog_20(Scene):
    def construct(self):
        f = [
            mt(r"\ln(x)=\ln(4)"),
            mt(r"\ln (x)=1 \cdot \ln(4)"),
            mt(r"\frac{\ln (x)}{\ln(4)}=1"),
            mt(r"\frac{\log_{e}(x)}{\log_{e}(4)}=1"),
            mt(r"\log_{4}x=1"),

            mt(r"x=4^{1}"),
            mt(r"x=4"),
            mt(r"\log_{e}x = \log_{e}4"),
            mt(r"e^{\log_{e}x}=e^{\log_{e}4}"),
            mt(r"x=4"),
        ]

        self.play(Write(f[0]))
        a = f[0].copy()
        self.wait(1)
        self.play(f[0].animate.shift(UP*2))
        self.wait(1)
        self.play(TransformMatchingShapes(a, f[1]))
        self.wait(1)

        for i in range(1, 6):
            self.play(TransformMatchingShapes(f[i], f[i+1]), path_arc=PI/2)
            self.wait(1)

        self.play(f[6].animate.next_to(f[0], DOWN))
        self.wait(1)
        
        self.play(Write(a))

        self.play(TransformMatchingShapes(a, f[7]))
        self.wait(1)

        self.play(TransformMatchingShapes(f[7], f[8]), path_arc=PI/2)
        self.wait(1)

        self.play(TransformMatchingShapes(f[8], f[9]), path_arc=PI/2)
        self.wait(1)

        self.play(FadeOut(f[9]))
        self.play(VGroup(f[0], f[6]).animate.arrange(DOWN))
        self.wait(1)

class elog_30(Scene):
    def construct(self):
        f = [
            mt(r"S=k\ln \Omega \to \Omega=?"),
            mt(r"S=k\ln \Omega"),
            mt(r"\frac{S}{k}=\ln\Omega"),
            mt(r"e^{S/k}=e^{\ln\Omega}"),
            mt(r"e^{S/k}=e^{\log_{e}\Omega}"),
            mt(r"e^{S/k}=\Omega"),
            mt(r"\Omega=e^{S/k}"),
            ]

        self.play(Write(f[0]))
        # a = f[1].copy()
        self.wait(1)
        # self.add(a)
        self.play(Write(f[1]), f[0].animate.shift(UP*2))
        self.wait(1)

        self.play(TransformMatchingShapes(f[1], f[2]), path_arc=PI/2)
        self.wait(1)
    
        for i in range(2, 6):
            self.play(TransformMatchingShapes(f[i], f[i+1]), path_arc=PI/2)
            self.wait(1)

        self.play(VGroup(f[0], f[6]).animate.arrange(DOWN))
        self.wait(1)



class elog_40(Scene):
    def construct(self):
        f = [
            mt(r"q=q_{0}(1-e{^{t/\tau}})\to t=?"),
            mt(r"\begin{cases} \tau  & \text{tau} \\ q & \text{carga} \\ q_{0} & \text{carga inicial} \\ t & \text{tiempo} \end{cases}"),
            mt(r"q=q_{0}(1-e{^{t/\tau}})"),
            mt(r"\frac{q}{q_{0}}=1-e{^{t/\tau}} "),
            mt(r"e^{t/\tau}=1-\frac{q}{q_{0}}"),
            mt(r"\ln(e^{t/\tau})=\ln\left( 1-\frac{q}{q_{0}} \right)"),
            mt(r"\frac{t}{\tau}\ln e=\ln\left( 1-\frac{q}{q_{0}} \right)"),
            mt(r"t(\log_{e}e)=\tau \ln\left( 1-\frac{q}{q_{0}} \right)"),
            mt(r"t=\tau \ln\left( 1-\frac{q}{q_{0}} \right)"),
            ]

        self.play(Write(f[0]))
        self.wait(1)
        self.play(Write(f[1].next_to(f[2], LEFT, buff=1.5)))
        self.wait(1)
        self.play(Write(f[2]), f[0].animate.shift(UP*2))
        self.wait(1)
    
        for i in range(2, 8):
            self.play(TransformMatchingShapes(f[i], f[i+1]), path_arc=PI/2)
            self.wait(1)

        self.play(FadeOut(f[1]), VGroup(f[0], f[8]).animate.arrange(DOWN))
        self.wait(1)



class elog_50(Scene):
    def construct(self):
        f = [
            mt(r"(\alpha+\beta)^{1/\gamma} = P_{0}e^{ \frac{A}{A_{0}} \tau } \to \gamma = ?"),
            mt(r"(\alpha+\beta)^{1/\gamma} = P_{0}e^{ \frac{A}{A_{0}} \tau }"),
            mt(r"\ln[(\alpha+\beta)^{1/\gamma}]=\ln(P_{0}e^{(A/A_{0})\tau})"),
            mt(r"\frac{1}{\gamma}\ln(\alpha+\beta)=\ln(P_{0}e^{(A/A_{0})\tau})"),
            # mt(r"\frac{1}{\gamma}\ln(\alpha+\beta)=\ln(P_{0}e^{(A/A_{0})\tau})"),
            mt(r"\frac{1}{\gamma}\ln(\alpha+\beta)=\ln(P_{0}) +\frac{A}{A_{0}}  \tau\ln(e)"),
            mt(r"\frac{1}{\gamma}\ln(\alpha+\beta )=\ln(P_{0}) +\frac{A}{A_{0}}\tau"),
            mt(r"\ln(\alpha+\beta)=\left( \ln(P_{0}) +\frac{A}{A_{0}}\tau \right)\gamma"),
            mt(r"\frac{\ln(\alpha+\beta)}{ \ln(P_{0}) +\frac{A}{A_{0}}\tau} = \gamma"),
            mt(r"\gamma=\frac{\ln(\alpha+\beta)}{ \ln(P_{0}) +\frac{A}{A_{0}}\tau} "),
            ]

        self.play(Write(f[0]), run_time = 0.8)
        self.wait(1)
        self.play(Write(f[1]), f[0].animate.shift(UP*2), run_time = 0.8)
        self.wait(1)
    
        for i in range(1, 8):
            self.play(TransformMatchingShapes(f[i], f[i+1]), path_arc=PI/2)
            self.wait(1)

        self.play(VGroup(f[0], f[8]).animate.arrange(DOWN))
        self.wait(1)


class elog_60(Scene):
    def construct(self):
        f = [
            mt(r"N=N_{0}e^{-\lambda t} \to \lambda = ?"),
            mt(r"N=N_{0}e^{-\lambda t}"),
            mt(r"\frac{N}{N_{0}}=e^{-\lambda t}"),
            mt(r"e^{-\lambda t}=\frac{N}{N_{0}}"),
            mt(r"\ln(e^{-\lambda t}) = \ln\left( \frac{N}{N_{0}} \right)"),
            mt(r"-\lambda t=\ln\left( \frac{N}{N_{0}} \right)"),
            mt(r"t=\frac{\ln\left( N/N_{0} \right)}{-\lambda}"),
            ]

        self.play(Write(f[0]), run_time = 0.8)
        self.wait(1)
        self.play(Write(f[1]), f[0].animate.shift(UP*2), run_time = 0.8)
        self.wait(1)
    
        for i in range(1, 6):
            self.play(TransformMatchingShapes(f[i], f[i+1]), path_arc=PI/2)
            self.wait(1)

        self.play(VGroup(f[0], f[6]).animate.arrange(DOWN))
        self.wait(1)

class elog_70(Scene):
    def construct(self):
        f = [
            mt(r"T=T^{\alpha}+(T_{0}-T_{\beta})e^{-kt} \to \alpha = ?"),
            mt(r"T=T^{\alpha}+(T_{0}-T_{\beta})e^{-kt}"),
            mt(r"T-(T_{0}-T_{\beta})e^{-kt} = T^{\alpha}"),
            mt(r"\ln [T-(T_{0}-T_{\beta})e^{-kt} ] = \ln(T^{\alpha})"),
            mt(r"\ln [T-(T_{0}-T_{\beta})e^{-kt} ] =\alpha \ln T"),
            mt(r"\alpha = \frac{\ln [T-(T_{0}-T_{\beta})e^{-kt} ]}{\ln T}"),
            ]

        self.play(Write(f[0]), run_time = 0.8)
        self.wait(1)
        self.play(Write(f[1]), f[0].animate.shift(UP*2), run_time = 0.8)
        self.wait(1)
    
        for i in range(1, 5):
            self.play(TransformMatchingShapes(f[i], f[i+1]), path_arc=PI/2)
            self.wait(1)

        self.play(VGroup(f[0], f[5]).animate.arrange(DOWN))
        self.wait(1)

class elog_80(Scene):
    def construct(self):
        f = [
            mt(r"x = \sqrt[W]{ Mt \ln\left( \frac{C}{\lambda +\phi} \right) } \to \phi=?"),
            mt(r"x = \sqrt[W]{ Mt \ln\left( \frac{C}{\lambda +\phi} \right) }"),
            mt(r"x=  \left[ Mt \ln\left( \frac{C}{\lambda +\phi} \right) \right]^{1/W}"),
            mt(r"(x)^{W}=  \left( \left[ Mt \ln\left( \frac{C}{\lambda +\phi} \right) \right]^{1/W} \right)^{W}"),
            mt(r"x^{W}=\left[ Mt\ln\left( \frac{C}{\lambda+\phi} \right) \right]^{W/W}"),

            mt(r"x^{W}=Mt\ln\left( \frac{C}{\lambda+\phi} \right)"),
            mt(r"\frac{x^{W}}{Mt}=\ln\left( \frac{C}{\lambda + \phi} \right)"),
            mt(r"\ln\left( \frac{C}{\lambda + \phi} \right) =\frac{x^{W}}{Mt}"),
            mt(r"\log_{e}\left( \frac{C}{\lambda + \phi} \right) =\frac{x^{W}}{Mt}"),
            mt(r"e^{\log_{e}\left( \frac{C}{\lambda + \phi} \right) }=e^{x^{W}/Mt}"),

            mt(r"\frac{C}{\lambda+\phi}=e^{x^{W}/Mt}"),
            mt(r"\frac{C}{e^{x^{W}/Mt} }=\lambda+\phi"),
            mt(r"\phi=\frac{C}{e^{x^{W}/Mt}}-\lambda"),
            mt(r"\phi = Ce^{-x^{W}/Mt}-\lambda"),
  
            ]

        self.play(Write(f[0]), run_time = 0.8)
        self.wait(1)
        self.play(Write(f[1]), f[0].animate.shift(UP*2), run_time = 0.8)
        self.wait(1)
    
        for i in range(1, 13):
            self.play(TransformMatchingShapes(f[i], f[i+1]), path_arc=PI/2)
            self.wait(1)

        self.play(VGroup(f[0], f[13]).animate.arrange(DOWN))
        self.wait(1)

def mt(t: str):
    return MathTex(t)

def t(t: str):
    return Tex(t)