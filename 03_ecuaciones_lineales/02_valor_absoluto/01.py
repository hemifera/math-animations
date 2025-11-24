from manim import *

class vabs_00(Scene):
    def construct(self):
        img = ImageMobject("../../img/udb_logo_high.png")
        t1 = Text(r"Valor absoluto")
        t2 = Text(r"Visualización y teoría", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))