from manim import *
from manim_slides import Slide, ThreeDSlide


def create_textbox(color, string, height, width): #Can add height and width to these inputs as well.
    result = VGroup() 
    box = Rectangle(  
        height=height, width=width, fill_color=color, 
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

        COLORLAB = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png").move_to([3,0.5,0])
        COLORLAB.scale(2)
        midterm_title = Text("PhD Midterm - Markus Sebastian Bakken Storeide").move_to([-1,0,0])
        midterm_title.scale(2)
        cl = Text("Colorlab").move_to([0,-1,0])
        cl.scale(0.5)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + RIGHT)
        colorlabcorner.scale(0.5)
        NTNUText = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNUText.png").move_to([0, 2, 0])
        NTNUText.scale(0.3)
        NTNUcorner = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNUText.png").move_to([-5, -3, 0])
        NTNUcorner.scale(0.2)

        self.play(FadeIn(COLORLAB, shift=RIGHT*2), FadeIn(NTNUText, shift=RIGHT*2), Write(midterm_title, shift=LEFT*2), Write(cl, run_time=0.7))
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

        PhD_Title = Text("Multiresolution and Multimodal Acquisiton and Fusion of Heterogeneous Data")

        SONY = ImageMobject(filename_or_array) #Their headshots
        ADITYA = ImageMobject(filename_or_array)
        JON = ImageMobject(filename_or_array)

        supervisors = Text("Main Supvervisor: Sony George",
                   "Co-Supervisor #1: Aditya Sole",
                   "Co-Supervisor #2: Jon Yngve Hardeberg")

# Timepland Draft
        courses = create_textbox(color=RED, string="Courses") #Just add an image instead of doing it manually? Will trade for animation though. 
        self.add(courses)


# Start with quick timeplan to visualize the plan, also a good intro to the Lab-Engineer position.
# Also end with updated timeplan.

# Jira-esque visualization in Manim?




## Lab Engineer Position (50% Employed) ##
class Lab(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

        LFT = ImageMobjectNTNU = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Luftfarttilsynet.png")

        LFT_Text = Text("Sent application to Civil Aviation Authority of Norway (CAA)",
                "Wrote Operations Manual",
                "Serve as Operations Manager")



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
        NOR = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NOR.png")
        TRON = Text("Trondheim ????")
        BERG = Text("Bergen - 07.03.2022")
        ÅL = Text("Ålesund - 09.03.2022")
        TROM = Text("Tromsø - 09.05.2022")
        SVAL = Text("Svalbard - 22.09.2022")
        STAV = Text("Stavanger - 03.10.2022")
        MUNCH = Text("Oslo - 29.11.2022")

        RIKS_NIKU = Text("Presentations for Riksantikvaren and NIKU")

        self.add(Write(TRON))
        self.wait
        self.add(Transform(TRON,BERG))

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
        dt4bh_talk = Text("50 Years of Digitizing Cultural Heritage: What has been achieved?")

# Archiving 2023
        ARCHIVING = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ARCHIVING.png")

        arch_talk = Text("Statistical Evaluation of 3D Manifolds Shape Retention During Simplification Stages")







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
        project_category_chart = BarChart(
                                         values = [2,6,7],
                                         bar_names = ["Open Source", "Non-Profit", "Proprietary"],
                                        y_range = [-3, 10, 1],
                                        y_length = 6,
                                        x_length = 10,
                                        x_axis_config = {"font_size": 36},
                                        )
        c_bar_lbls = project_chart.get_bar_labels(font_size = 48)

        self.add(project_chart, c_bar_lbls)

# Add 3D viewers, and workflows?

# Statistics Paper

# Planned Papers







## Timeplan Summary ##
class Summary(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

# Be clear about the specific cooperations I have for the different topics. Gloss: UiO and Noelle. Hyperspectral: Balke and NIKU, etc.

## Questions? ##
class Questions(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E





# What fancy functions to visualize?
# - Point cloud simplifications
# - Spectral Image Processing (Think wavelengths etc)
#       - RGB Function Curves vs Hyperspectral Function Curves, with simoultaneous visualization
#       - Should I characterize our scanners? Probably a good idea. 
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