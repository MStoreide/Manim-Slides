from manim import *
import numpy as np
import math as m

class SVGTest(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        test = Text("Test")

        self.play(Write(test))
        self.wait()