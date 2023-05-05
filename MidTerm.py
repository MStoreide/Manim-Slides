from manim import *
from manim_slides import Slide, ThreeDSlide
import numpy as np
import math


def create_textbox(color, string, height, width): 
    result = VGroup() 
    box = Rectangle(  
        height=height, width=width, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center())
    result.add(box, text) # add both objects to the VGroup
    return result

def textbox(color, scolor, string):
    result = VGroup()
    text = Text(string)
    text_high = text.height
    text_width = text.width
    box = Rectangle(
                    height = text.height + 0.5,
                    width = text_width + 0.5,
                    color = color,
                    stroke_color = scolor,
                    )
    result.add(text, box)
    return result

#Should also have a packup Powerpoint just in case. 

class Header(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

#Slide 1: Cover

        COLORLAB = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png").move_to([3,0.5,0])
        COLORLAB.scale(2)
        midterm_title = Text("PhD Midterm - Markus Sebastian Bakken Storeide")
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
        supervisors_img = VGroup(SONY, ADITYA, JON)

        supervisors_txt = Text("Main Supvervisor: Sony George",
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
                        "Registeret NTNU - Gjøvik as Droneoperator in Flydrone.no"
                        "Wrote Operations Manual",
                        "Serve as Operations Manager")



## Courses ##
class Courses(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

# DT8121 - Color Imaging
        CI = Text("DT8121 - Colour Imaging", font_size=20).move_to([-3.5,3,0])
# IDIG4002 - Computer Graphics
        IDIG = Text("IDIG4002 - Computer Graphics Fundamentals and Applications", font_size=20).next_to(CI, DOWN, aligned_edge=LEFT)
# CHANGE Training School - 3D Scanning
# HFEL8000 - Communicating Science
        HFEL = Text("HFEL8000 - Communicating Science", font_size=20).next_to(IDIG, DOWN, aligned_edge=LEFT)
# IDT8000 - Research Ethics
        IDT = Text("IDT8000 - Research Ethics", font_size=20).next_to(HFEL, DOWN, aligned_edge=LEFT)
 # STK9900 - Statistics
        STK = Text("STK9900 - Statistical Methods and Applications", font_size=20).next_to(IDT, DOWN, aligned_edge=LEFT)
# CHANGE Training School
        CHG = Text("CHANGE Training School - Poland", font_size=20).next_to(STK, DOWN, aligned_edge=LEFT)
 
       # ECT = Text("7.5", "ECT") # Can just duplicate and change this f.eks

        CO = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsvg.svg")
        NTNU = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNUsvgT.svg").next_to(CI, LEFT)
        NTNU.scale(0.3)  #Remove text
        WUT = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/WUTsvg.svg").next_to(CHG, LEFT)
        UIO = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/UIO.svg").next_to(STK, LEFT) #Remove text

        self.play(Write(CI), Write(IDIG), Write(HFEL), Write(IDT), Write(NTNU), run_time=2)
        self.wait(1)
        self.play(Write(STK), Write(UIO), run_time=2)
        self.wait(1)
        self.play(Write(CHG), Write(WUT), run_time=2)
        self.wait(2)


## Travel, Outreach and Participation ## (Visualize these with a map?)
class Outreach(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E

# All NO-CHANGE visits and presentations
        NOCHANGE = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NO-CHANGE.png") #Change to SVG
        NOR = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NOR.png") #Change to SVG
        TRON = Text("Trondheim ????", font_size=20, should_center=False).move_to([-3,3,0]) # ADD SVG logos for all locations
        BERG = Text("Bergen - 07.03.2022", font_size=20, should_center=False).next_to(TRON, DOWN)
        ÅLES = Text("Ålesund - 09.03.2022", font_size=20, should_center=False).next_to(BERG, DOWN)
        TROM = Text("Tromsø - 09.05.2022", font_size=20).next_to(ÅLES, DOWN)
        SVAL = Text("Svalbard - 22.09.2022", font_size=20).next_to(TROM, DOWN) #Sjekk disse datoene, er litt usikker her.
        STAV = Text("Stavanger - 03.10.2022", font_size=20).next_to(SVAL, DOWN)
        MUNCH = Text("Oslo - 29.11.2022").next_to(STAV, DOWN)

        RIKS_NIKU = Text("Presentations for Riksantikvaren and NIKU")

        self.play(Write(TRON))
        self.wait()
        self.play(Transform(TRON,BERG))
        self.wait()
        self.play(Transform(BERG,ÅLES))
        self.wait()

# CHANGE Training School
        CHANGE = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CHANGE.png")

# MANER Mobility at Yale
        MANER = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/MANER.png")
        YALE = SVGMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/YALE.svg")

# MANER Training School at Chiba 
        CHIBA = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CHIBA.png")

# Other Visits

# Balke Center
        #BALKE = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/BalkeSenteret.svg")
        #self.play(Write(YALE), run_time=2)
        #self.wait()

# Kolbu Dør
# Uvdal Stavkirke?
# Maihaugen?
# TexRec
# Department of Conservation at UiO?
# Eidskog Kirke





## Conferences ##
class Conferences(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

# DT4BH in Orleans (Workshop)
        ATHENA = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ATHENA.png") #Change to SVGs
        DT4BH = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/DT4BH.jpg")
        dt4bh_talk = Text("50 Years of Digitizing Cultural Heritage: What has been achieved?")

# Archiving 2023
        ARCHIVING = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ARCHIVING.png")
        arch_talk = Text("Statistical Evaluation of 3D Manifolds Shape Retention During Simplification Stages")

        project_chart = BarChart(
                                 values = [22,26,26],
                                 bar_names = ["Data Acquisition", "Data Storage", "Open Access"],
                                 y_range = [0,30,5],
                                 y_length = 7,
                                 x_length = 10,
                                 x_axis_config = {"font_size" : 48},
                                )       
        proj_bar_lbls = project_chart.get_bar_labels(font_size = 48, color=WHITE)

        viewer_chart = BarChart(
                                 values = [],
                                 bar_names = [],
                                 y_range = [],
                                 y_length = 7,
                                 x_length = 10,
                                 x_axis_config = {"font_size" : 48},
                                )                 
        view_bar_lbls = viewer_chart.get_bar_labels(font_size = 48, color=WHITE)

        project_category_chart = BarChart(
                                        values = [2,6,7],
                                        bar_names = ["Open Source", "Non-Profit", "Proprietary"],
                                        y_range = [-3, 10, 1],
                                        y_length = 6,
                                        x_length = 10,
                                        x_axis_config = {"font_size": 36},
                                        )
        cat_bar_lbls = project_category_chart.get_bar_labels(font_size = 48, color=WHITE)

        self.play(Write(project_category_chart))
        self.play(Write( cat_bar_lbls))
        self.wait(5)
# Can also make tables here, similar to the excel ones.

# Example of how to show point cloud. Input can be an xyz array
class ImageScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.begin_ambient_camera_rotation()
        Disp_array= VMobject()
        for x in range(-3, 3):
            for y in range(-3, 3):
                for z in range(-3, 3):
                    dot = Dot(point=(x, y, z))
                    Disp_array.add(dot)
        self.add(Disp_array)
        self.wait(2)





## Research ##

def PDF_normal(x, mu, sigma):
        return math.exp(-((x-mu)**2)/(2*sigma**2))/(sigma*math.sqrt(2*math.pi))

class Research(ThreeDSlide):
    def construct(self):
        self.camera.background_color = GRAY_E

# 3D Scanning - Point Clouds
# Simplification Algorithms - Visualize Examples
# Acquisition of Color and Texture
# Fusing Color and Texture

        spectrum_rectangle = Rectangle(
                                        fill_color = color_gradient((RED, ORANGE, YELLOW, GREEN_C, GREEN, BLUE_C, BLUE, PURPLE, PURPLE), 10), 
                                        fill_opacity = 1,
                                        width = 10,
                                        height=1
                                        )
        spect_ax = NumberLine(x_range=[380,720,20], length=10, include_numbers=True, font_size=24).next_to(spectrum_rectangle, DOWN)

        curve_ax = Axes(
                x_range=[-5,5,1],
                y_range=[0,0.5,0.1],
                axis_config={"include_numbers":True}
        )
        mu_b = ValueTracker(0)
        sigma_b = ValueTracker(1)

        blue_curve = always_redraw(
                lambda:curve_ax.plot(
                        lambda x:PDF_normal(x, mu_b.get_value(), sigma_b.get_value()), color=PURE_BLUE
                )
        )

        mu_g = ValueTracker(0)
        sigma_g = ValueTracker(1)

        green_curve = always_redraw(
                lambda:curve_ax.plot(
                        lambda x:PDF_normal(x, mu_g.get_value(), sigma_g.get_value()), color=PURE_GREEN
                )
        )

        mu_r = ValueTracker(0)
        sigma_r = ValueTracker(1)

        red_curve = always_redraw(
                lambda:curve_ax.plot(
                        lambda x:PDF_normal(x, mu_r.get_value(), sigma_r.get_value()), color=PURE_RED
                )
        )

        self.play(Write(spectrum_rectangle), Create(spect_ax))
        self.wait(2)
        self.play(Unwrite(spectrum_rectangle), Uncreate(spect_ax))
        self.play(Create(curve_ax))
        self.wait()
        self.play(Create(blue_curve), run_time=2)
        self.play(Create(green_curve), run_time=2)
        self.play(Create(red_curve), run_time=2)
        self.play((mu_b.animate.set_value(-2)),(sigma_b.animate.set_value(0.5)), run_time=1, rate_func=rate_functions.smooth)
        self.wait(2)
        self.play(
                 mu_r.animate.set_value(2), run_time=1.5,
                rate_func=rate_functions.smooth
                )
        self.wait()


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
#       - Also note going into the IR and UV
#       - Should I characterize our scanners? Probably a good idea. 
#       - Resolution of Hyperspectral Image vs normal image, projecting it onto a UV map from our scanners
# - Hausdorff Measurements
# - Statistical Models

hausdorff_eq = MathTex(r"d_h(X,Y) = max(sup inf d(x,y), sup inf d(x,y))")

chamfer_eq = MathTex(r"d_CD (X,Y) = \sum_{x \in X}min(MISSING) \| x-y \| 2² + \sum_{y \in Y} min(MISSING) \| x-y \| 2²")

rendering_eq = MathTex(r"L_o(x, \omega_o, \Lambda, t) = L_e(x, \omega_o, \Lambda, t) + \int_{\Omega} f_r(x, \omega_i, \omega_o, \Lambda, t)(\omega_i . \textbf{n}) d \omega_i")
# Does not account for: Transmission, Subsurface Scattering, Polarization, Phosphorescence, Interference, Flourescence.

#quadric_error_eq = Matrix([q_11,q_12,q_13,q_14],
#                          [q_12,q_22,q_23,q_24],
#                          [q_13,q_23,q_33,q_34],
#                          [0,0,0,1]^-1)

#color_rectangle = Rectangle(
#                            width=FRAME_WIDTH-1,
#                            height=1,
#                            fill_opacity=1,
#                            sheen_direction=RIGHT,
#                            stroke_width=0,)