from manim import *
from manim_slides import Slide, ThreeDSlide


def create_textbox(color, string): #Can add height and width to these inputs as well.
    result = VGroup() 
    box = Rectangle(  
        height=2, width=3, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center())
    result.add(box, text) # add both objects to the VGroup
    return result

#Should also have a packup Powerpoint just in case. 

class Header(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

#Slide 1: Cover

        colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png").move_to([3,0.5,0])
        colorlab.scale(2)
        colorlabtext = Text("PhD Midterm - Markus Sebastian Bakken Storeide").move_to([-1,0,0])
        colorlabtext.scale(2)
        cg = Text("Colorlab").move_to([0,-1,0])
        cg.scale(0.5)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + RIGHT)
        colorlabcorner.scale(0.5)
        NTNUText = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNUText.png").move_to([0, 2, 0])
        NTNU.scale(0.3)
        NTNUcorner = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNU.png").move_to([-5, -3, 0])
        NTNUcorner.scale(0.2)

        self.play(FadeIn(colorlab, shift=RIGHT*2), FadeIn(NTNU, shift=RIGHT*2), Write(colorlabtext, shift=LEFT*2), Write(cg, run_time=0.7))
        self.next_slide()

### Content ###

# Intro w. Timeplan
# Lab Engineer Position (Drones etc), Drone Operations Manager and Writing the Manual
# Course Progress
# Outreach Participation
# Secondments and Travel
# Timeplan

# Notes
# Jira should be fully developed and updated to visualize the project tracking. As well as xMind, Zotero



## Intro w. Timeplan ##
class Intro(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

courses = create_textbox(color=RED, string="Courses")
self.add(courses)


# Start with quick timeplan to visualize the plan, also a good intro to the Lab-Engineer position.
# Also end with updated timeplan.

# Jira-esque visualization in Manim?




## Lab Engineer Position (50% Employed) ##
class Lab(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

LFT = ImageMobjectNTNU = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Luftfarttilsynet.png")

LFT_Text = Text("Sent application to Luft")



## Courses ##
class Courses(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

NTNU = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNU.png")
UIO = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/UiO.png")
WUT = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/WUT.png")

ECT = Text("7.5", "ECT") # Can just duplicate and change this f.eks

# DT8121 - Color Imaging
CI = Text("DT8121 - Colour Imaging")
# STK9900 - Statistics
STK = Text("STK9900 - Statistical Methods and Applications")
# IDIG4002 - Computer Graphics
IDIG = Text("IDIG4002 - Computer Graphics Fundamentals and Applications")
# CHANGE Training School - 3D Scanning
# HFEL8000 - Communicating Science
HFEL = Text("HFEL8000 - Communicating Science")
# IDT8000 - Research Ethics
IDT = Text("IDT8000 - Research Ethics")
 
ECT = Text("7.5", "ECT") # Can just duplicate and change this f.eks





## Travel, Outreach and Participation ## (Visualize these with a map?)
class Outreach(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

# All NO-CHANGE visits and presentations
NOCHANGE = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NO-CHANGE.png")
# CHANGE Training School
CHANGE = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CHANGE.png")
# MANER Mobility at Yale
MANER = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/MANER.png")
YALE = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/YALE.png")
# MANER Training School at Chiba 
CHIBA = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CHIBA.png")

# Other Visits

# Balke Center
# Kolbu Dør
# Uvdal Stavkirke?
# Maihaugen?
# TexRec
# Department of Conservation at UiO?



## Conferences ##
class Conferences(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

# DT4BH in Orleans (Workshop)
ATHENA = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ATHENA.png")
DT4BH = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/DT4BH.jpg")


# Archiving 2023
ARCHIVING = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ARCHIVING.png")




## Research ##
class Research(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

# 3D Scanning - Point Clouds
# Simplification Algorithms - Visualize Examples
# Acquisition of Color and Texture
# Fusing Color and Texture


## Publications ##
class Publications(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E


# Review Paper

# Statistics Paper

# Planned Papers

## Timeplan Summary ##
class Summary(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E



## Questions? ##
class Questions(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E





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