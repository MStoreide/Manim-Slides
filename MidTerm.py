from manim import *
from manim_slides import Slide, ThreeDSlide

#Should also have a packup Powerpoint just in case

class Midterm(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

#Slide 1: Cover

        colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png").move_to([3,0.5,0])
        colorlab.scale(2)
        colorlabtext = Text("Colourlab").move_to([-1,0,0])
        colorlabtext.scale(2)
        cg = Text("IDIG4002 - Computer Graphics").move_to([0,-1,0])
        cg.scale(0.5)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + RIGHT)
        colorlabcorner.scale(0.5)
        NTNU = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNU.png").move_to([0, 2, 0])
        NTNU.scale(0.3)
        NTNUcorner = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNU.png").move_to([-5, -3, 0])
        NTNUcorner.scale(0.2)

        self.play(FadeIn(colorlab, shift=RIGHT*2), FadeIn(NTNU, shift=RIGHT*2), Write(colorlabtext, shift=LEFT*2), Write(cg, run_time=0.7))
        self.next_slide()

### Content ###

# Intro 
# Lab Engineer Position (Drones etc)
# Course Progress
# Outreach Participation
# Secondments and Travel
# Timeplan



## Courses ##


## Travel, Outreach and Participation ##

# All NO-CHANGE visits and presentations
# MANER Mobility at Yale
# MANER Training School
# CHANGE Training School

# Conferences

# DT4BH in Orleans
# Archiving 2023


## Research ##

# 3D Scanning - Point Clouds
# Simplification Algorithms - Visualize Examples
# Acquisition of Color and Texture
# Fusing Color and Texture


## Publications ##



## Timeplan ##


## Questions? ##


# What fancy functions to visualize?
# - Point cloud simplifications
# - Spectral Image Processing ( Think wavelengths etc)
# - Hausdorff Measurements
# - Statistical Models

hausdorff_eq = MathTex(r"d_h(X,Y) = max(sup inf d(x,y), sup inf d(x,y))")

chamfer_eq = MathTex(r"d_CD (X,Y) = \sum_{x \in X}min(MISSING) \| x-y \| 2² + \sum_{y \in Y} min(MISSING) \| x-y \| 2²")

rendering_eq = MathTex(r"L_o(x, \omega_o, \Lambda, t) = L_e(x, \omega_o, \Lambda, t) + \int_{\Omega} f_r(x, \omega_i, \omega_o, \Lambda, t)(\omega_i . \textbf{n}) d \omega_i")
# Does not account for: Transmission, Subsurface Scattering, Polarization, Phosphorescence, Interference, Flourescence.

quadric_error_eq = Matrix([q_11,q_12,q_13,q_14],
                          [q_12,q_22,q_23,q_24],
                          [q_13,q_23,q_33,q_34],
                          [0,0,0,1]^-1)

color_rectangle = Rectangle(
                            width=FRAME_WIDTH-1,
                            height=1,
                            fill_opacity=1,
                            sheen_direction=RIGHT,
                            stroke_width=0,)