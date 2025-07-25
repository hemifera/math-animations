from manim import *
import numpy as np

class cpb_00(Scene):
    def construct(self):
        img = ImageMobject("img/udb_logo_high.png")
        t1 = Text(r"Polinomios de mayor orden")
        t2 = Text(r"Cubo perfecto de binomios", font_size=32) 

        v = Group(img, t1, t2)
        self.add(img.scale(0.25), v.arrange(DOWN))

