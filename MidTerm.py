from manim import *
from manim_slides import Slide, ThreeDSlide
import numpy as np
import math as m


### Content ###

# Header
# Intro w. Timeplan
# Lab Engineer Position (Drones etc), Drone Operations Manager and Writing the Manual
# Course Progress
# Outreach Participation
# Data Collection
# Secondments and Travel
# Research
# Publications
# Future Work & Timeplan
# Summary

# Notes
# Jira should be fully developed and updated to visualize the project tracking. As well as xMind, Zotero
# Should also have a packup Powerpoint just in case. 


## Some Rules ##
# - Only use (Write) for equations.
# - Use (FadeIn) and (Transform) for normal text.
# - How to do citations? Small text on the bottom?

def textbox(color, scolor, string): #Can be used to create several boxes which together makes a Gantt chart?
    result = VGroup()
    text = Text(string)
    text_high = text.height
    text_width = text.width
    box = Rectangle(
                    height = text_high + 0.5,
                    width = text_width + 0.5,
                    color = color,
                    stroke_color = scolor,
                    )
    box.set_fill(color, opacity = 0.3)
    result.add(text, box)
    return result

def PDF_normal(x, mu, sigma):
        return m.exp(-((x-mu)**2)/(2*sigma**2))/(sigma*m.sqrt(2*m.pi))

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


class SVGTest(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        SVG = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Office365.svg")

        self.play(Write(SVG), run_time=2)
        self.wait(2)

class FUNCTest(Scene):
        def construct(self):
                self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

                box1 = textbox(PURE_RED, PURE_RED, "STK9900")
                box2 = textbox(PURE_BLUE, PURE_BLUE, "DT8121").next_to(box1, DOWN)

                boxes = VGroup(box1, box2)

                banner = ManimBanner()

                self.play(Create(banner))
                self.wait(2)


class Header(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        #Slide 1: Cover

        COLORLAB = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png").move_to([3,0.5,0])
        COLORLAB.scale(2)
        midterm_title = Text("PhD Midterm - Markus Sebastian Bakken Storeide")
        cl = Text("Colorlab").move_to([0,-1,0])
        cl.scale(0.5)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)
        NTNUText = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNUText.png").move_to([0, 2, 0])
        NTNUText.scale(0.3)
        NTNUcorner = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNUText.png").move_to([-5, -3, 0])
        NTNUcorner.scale(0.2)

        self.play(FadeIn(COLORLAB, shift=RIGHT*2), FadeIn(NTNUText, shift=RIGHT*2), Write(midterm_title, shift=LEFT*2), Write(cl, run_time=0.7))
        self.next_slide()


class Intro(ThreeDScene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title1 = Text("Introduction", font_size = 40).to_corner(UP + LEFT)
        slide_number1 = Text("1", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        PhD_Title = Text("Multiresolution and Multimodal Acquisiton and Fusion of Heterogeneous Data")

        SONY_t = Text("Main Supervisor: Sony George", font_size=20)
        SONY = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/SONY.jpg", scale_to_resolution=2000).next_to(SONY_t, LEFT)
        ADITYA_t = Text("Co-Supervisor #1: Aditya Sole", font_size=20).next_to(SONY_t, DOWN)
        ADITYA = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ADITYA.jpg", scale_to_resolution=2000).next_to(ADITYA_t, LEFT)
        JON_t = Text("Co-Supervisor #2: Jon Yngve Hardeberg", font_size=20).next_to(ADITYA_t, DOWN)
        JON = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/JON.jpg", scale_to_resolution=2000).next_to(JON_t, LEFT)

        self.play(FadeIn(SONY_t), FadeIn(ADITYA_t), FadeIn(JON_t), run_time=2)
        self.play(FadeIn(SONY), FadeIn(ADITYA), FadeIn(JON))
        self.wait()

        # Research Intro

        # Moving imgages from 2D to 3D, have 2D image as example, and how to project this onto a 3D object. 
        # Deform the image to see that direct projection is inaccurate.

        # 2D_e = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Blender.png").move_to([3,3,3])
        # 3D_e = Cube(side_length=1, fill_color=PURPLE, fill_opacity=1)
        #  axes_e = ThreeDAxes()
        # array_e = #An image as an array as example 

        #  x_label_e = axes.get_x_axis_label(Tex("x"))
        #  y_label_e = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8)
        #  z_label_e = axes.get_z_axis_label(Tex("z")).shift(IN * 1.8)

        # Move to 3D Scene
        #  self.move_camera(phi=40 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)

        # Zoom into surface and visualize a BRDF with the rendering equation. Include multispectral ect.

        # Timepland Draft
        #  text = textbox(GREEN, ORANGE, "Test text")
        # self.play(Write(text))
        #  self.wait(2)

        # Start with quick timeplan to visualize the plan, also a good intro to the Lab-Engineer position.
        # Also end with updated timeplan.

        # Jira-esque visualization in Manim?

        ## Project Management ##

        # Using Jira, Confluence, xMind, Teams, and Outlook

        # Change slides here. Make

        JIRA = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/JIRA.svg")
        JIRA_t = Text("Jira")
        CONF = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Confluence.svg")
        CONF_t = Text("Confluence")
        GIT = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Github.svg")
        GIT_t = Text("Github")
        #DATA MANAGEMENT??? MongoDB? Colourlab Server?

        MNG = Text("Project Management Tools:").move_to(UP + LEFT)

        START = Text("Start date: ???")

        # Data Management

        # Colorlab Server, MongoDB?, Local Storage
        # Make sure it is stored in at least 3 locations. 

class Lab(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title2 = Text("Lab Engineer", font_size = 40).to_corner(UP + LEFT)
        slide_number2 = Text("2", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        LFT = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Luftfarttilsynet.png")
        GIT = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Github.svg")
        BOOK = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Bookitlab.png")

        LFT_Text = Text("- Sent application to Civil Aviation Authority of Norway (CAA)",
                        "- Registered NTNU - Gjøvik as Droneoperator in Flydrone.no",
                        "- Wrote Operations Manual",
                        "- Serve as Operations Manager")

        GIT_CL = Text("Colourlab Github Organization")

        BOOK_Text = Text("BookitLab Setup and Asset Organization")


class Courses(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title3 = Text("Coursework", font_size = 40).to_corner(UP + LEFT)
        slide_number3 = Text("3", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        CI = Text("DT8121 - Colour Imaging", font_size=20).move_to([-3.5,3,0])
        IDIG = Text("IDIG4002 - Computer Graphics Fundamentals and Applications", font_size=20).next_to(CI, DOWN, aligned_edge=LEFT)
        HFEL = Text("HFEL8000 - Communicating Science", font_size=20).next_to(IDIG, DOWN, aligned_edge=LEFT)
        IDT = Text("IDT8000 - Research Ethics", font_size=20).next_to(HFEL, DOWN, aligned_edge=LEFT)
        STK = Text("STK9900 - Statistical Methods and Applications", font_size=20).next_to(IDT, DOWN, aligned_edge=LEFT)
        CHG = Text("CHANGE Training School - Poland", font_size=20).next_to(STK, DOWN, aligned_edge=LEFT)
 
        ECT1 = Text("7.5", "ECT") #Create table?

        PASS = Text("Passed", color = GREEN_C)

        CO = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsvg.svg")
        NTNU = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNUsvgT.svg").next_to(CI, LEFT)
        NTNU.scale(0.3)  #Remove text
        WUT = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Julia.svg").next_to(CHG, LEFT)
        UIO = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/UIO.svg").next_to(STK, LEFT) #Remove text

        self.add(slide_title, slide_number)
        self.play(FadeIn(CI), FadeIn(IDIG), FadeIn(HFEL), FadeIn(IDT), FadeIn(NTNU), run_time=2)
        self.wait(1)
        self.play(FadeIn(STK), FadeIn(UIO), run_time=2)
        self.wait(1)
        self.play(FadeIn(CHG), FadeIn(WUT), run_time=2)
        self.wait(2)


class Outreach(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Outreach and Dissemination", font_size = 40).to_corner(UP + LEFT)
        slide_number = Text("4", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        # All NO-CHANGE visits and presentations
        NOCHANGE = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NO-CHANGE.png") #Change to SVG
        NOR = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NOR.png").move_to(3,0,0) #Change to SVG
        TRON = Text("Trondheim ????", font_size=20, should_center=False).move_to([-3,3,0]) # ADD SVG logos for all locations
        BERG = Text("Bergen - 07.03.2022", font_size=20, should_center=False).next_to(TRON, DOWN)
        ÅLES = Text("Ålesund - 09.03.2022", font_size=20, should_center=False).next_to(BERG, DOWN)
        TROM = Text("Tromsø - 09.05.2022", font_size=20).next_to(ÅLES, DOWN)
        SVAL = Text("Svalbard - 22.09.2022", font_size=20).next_to(TROM, DOWN) #Sjekk disse datoene, er litt usikker her.
        STAV = Text("Stavanger - 03.10.2022", font_size=20).next_to(SVAL, DOWN)
        MUNCH = Text("Oslo MUNCH Museum - 29.11.2022", font_size=20).next_to(STAV, DOWN)

        RIKS_NIKU = Text("Presentations for Riksantikvaren and NIKU")

        # NO-CHANGE Visit Logos
        NIDR = SVGMobject(Nidaros).next_to(TRON, LEFT)
        UMBG = SVGMobject(MuseetBergen).next_to(BERG, LEFT)
        DIÅL = SVGMobject(DigSenter).next_to(ÅLES, LEFT)
        MUTR = SVGMobject(MusetTromsø).next_to(TROMS, LEFT)
        MUSV = SVGMobject(SvalMus).next_to(SVAL, LEFT)
        MUST = SVGMobject(MUstStav).next_to(STAV, LEFT)
        MUMU = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/MUNCH.svg").next_to(MUNCH, LEFT)

        RIKS = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Riksantikvaren.svg")
        NIKU = SVGMobject(Niku)

        # CHANGE Training School
        CHANGE = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CHANGE.png")

        # MANER Mobility at Yale
        MANER = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/MANER.png")
        YALE = SVGMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/YALE.svg")

        YALE_Text = Text("University of Yale")
        YALE_info = Text("Discussed some research approaches")
        YALE_info2 = Text("Inverse Procedural Rendering") 

        # MANER Training School at Chiba 
        CHIBA = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CHIBA.png")


        self.play(FadeIn(TRON))
        self.wait()
        self.play(Transform(TRON,BERG))
        self.wait()
        self.play(Transform(BERG,ÅLES))
        self.wait()
        self.play(Transform(ÅLES,TROM))
        self.wait()
        self.play(Transform(TROM, SVAL))
        self.wait()
        self.play(Transform(SVAL, STAV))
        self.wait()
        self.play(Transform(STAV, MUNCH))
        self.wait()
        self.play(Write(YALE), run_time=2)
        self.wait()


class DataCollection(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Data Collection", font_size = 40).to_corner(UP + LEFT)
        slide_number = Text("4", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        # Eidskog Kirke
        EIDS_t = Text("Eidskog Kirke")
        EIDS = SVGMobject(NorskeKirke)
        EIDS_data = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Eidskogdata.jpeg")

        # Balke Center
        BALKE_t = Text("Balke Senteret")
        BALKE = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/BalkeSenteret.svg")
        BALKE_data = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Balkedata.jpeg")

        # Kolbu Dør
        KOLB_t = Text("Kolbu Barn Door")
        KOLB = SVGMobject(Kommunevåpen)
        KOLB_data = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Kolbudata.jpeg")
        # Mention NRK

        # Uvdal Stavkirke?
        # Other Visits

        MAIHAUGEN_t = Text("Maihaugen | Lillehammer Museum")
        MAIH = SVGMobject(Maihaugen)
        # TexRec
        # Department of Conservation at UiO?


class Conferences(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Conferences", font_size = 40).to_corner(UP + LEFT)
        slide_number = Text("???", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

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
        self.play(Write(cat_bar_lbls))
        self.wait(5)
        # Can also make tables here, similar to the excel ones.


class ResearchRev(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Research Work - 3D Review", font_size = 40).to_corner(UP + LEFT)
        slide_number = Text("???", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        # Review Paper
        project_category_chart = BarChart(
                                         values = [2,6,7],
                                         bar_names = ["Open Source", "Non-Profit", "Proprietary"],
                                        y_range = [-3, 10, 1],
                                        y_length = 6,
                                        x_length = 10,
                                        x_axis_config = {"font_size": 36},
                                        )
        c_bar_lbls = project_category_chart.get_bar_labels(font_size = 48)

         # Add 3D viewers, and 
         # workflows?


class ResearchStat(ThreeDSlide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Research Work - Mesh Statistics", font_size = 25).to_corner(UP + LEFT)
        slide_number = Text("9", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        #self.add(slide_title, slide_number, colorlabcorner)

        # Statistics Paper
        PyPacs = Text("Pandas, Dask, Open3D, PyMeshLab, CloudComPy")
        PYTH = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Python.svg")
        PANDA = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Pandas.svg")
        OP3D = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Open3D.svg")
        #MESH = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Meshlab.png")
        #CLCP = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Cloudcompare.png")
        STATM = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/STATM.svg")

        vertices = [1, 2, 3, 4,]# Can maybe do the fadeout this way
        edges =  [(1, 2), (2, 3), (3, 4)]# Can maybe do the fadeout this way
        g = Graph(vertices, edges, 
                 layout={1: [-3, 0, 0], 2: [-1, 0, 0], 3: [1, 0, 0], 4: [3, 0, 0]})

        vertices2 = [1, 2, 3]# Can maybe do the fadeout this way
        edges2 =  [(1, 2), (2, 3)]# Can maybe do the fadeout this way
        g2= Graph(vertices2, edges2, 
                 layout={1: [-3, 0, 0], 2: [1, 0, 0], 3: [3, 0, 0]})
        #surface = Graph([1, 2, 3, 4, 5, 6, 7, 8, 9], [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)],
        #          layout={1: [-4, 0, 0], 2: [-3, 0, 0], 3: [-2, 0, 0], 4: [-1, 0, 0], 5: [0, 0, 0], 6: [1, 0, 0], 7: [2, 0, 0], 8: [3, 0, 0], 9: [4, 0, 0]}
        #          )
        #self.play(Create(g), run_time=3)
        #self.play(g[2].animate.move_to([-1, 2, 0]))
        #self.wait()
        #self.play(Transform(g, g2))
        #self.wait
        #self.play(surface.animate.change_layout("circular")) # Can be used to show how vertices have differetn importance
                                                             # for different surfaces
        #self.wait(2)
        #self.play(FadeOut(g))

        DECI_t = Text("Decimation iteratively removes vertices in a mesh based on an evaluation of optimal local geometry.") 
        VECL_t = Text("Vertex Clustering takes vertices in close proximity to each other and clusters and merges them into a single vertex. Surrounding polygons are then re-triangulated.")
        QEM_t = Text("Quadric Error Metrics utilizes a plane equation of a given triangle to estimate the ideal location of vertices")
        CFM_t = Text("Coplanar facets merging looks at planar divergence between polygons and merges them if they are above a certain threshold.")
        EDCO_t = Text("Edge Collapse finds pairs of vertices that are close together, and collapses the edge between them. This creates a new vertex at the halfway point between the two original vertices.")

        # Practice working with a sin wave as the surface, and to plot points on that surface. 

        obj_stats1 = Table([["Object Name", "SM Baseline", "SMD 1"],
                           ["Vertices", "16812", "n"],
                           ["Edges", "50430", "n"],
                           ["MaxEdge Length", "n", "n"],
                           ["MinEdge Length", "n", "n"],
                           ["MeanEdge Length", "n", "n"],
                           ["MedianEdge Length", "n", "n"],
                           ["Faces", "33620", "n"],
                           ["MaxFace Size", "n", "n"],
                           ["MinFace Size", "n", "n"],
                           ["MeanFace Size", "n", "n"],
                           ["MedianFace Size", "n", "n"],
                           ["B.B Diagonal", "15.018574", "n"],
                           ["Max Poly \n Surface", "0.006", "n"],
                           ["Min Poly \n Surface", "0.004", "n"],
                           ["MaxDifference", "n", "n"],
                           ["MinDifference", "n", "n"],
                           ["Rest of them", "0.004", "n"]
                            ])

        obj_stats2 = Table([["Hausdorff Distance Max", "SM Baseline", "SMD 1", "n"],
                           ["Hausdorff Distance Min", "16812", "n", "n"],
                           ["Hausdorff Distance RMS", "50430", "n", "n"],
                           ["Hausdorff Distance Mean", "n", "n", "n"],
                           ["Hausdorff Distance Median", "n", "n", "n"],
                           ["Chamfer Distance", "n", "n", "n"],
                           ["Sørensen-Dice Coefficient", "n", "n", "n"],
                           ["Pearson Correlation X", "33620", "n", "n"],
                           ["Pearson Correlation Y", "n", "n", "n"],
                           ["Pearson Correlation Z", "n", "n", "n"],
                           ["Spearman Correlation X", "n", "n", "n"],
                           ["Spearman Correlation Y", "n", "n", "n"],
                           ["Spearman Correlation Z", "15.018574", "n", "n"],
                           ["Earth Movers Distance", "0.006", "n", "n"],
                           ["Minowski Sum", "0.004", "n", "n"],
                           ["MaxDifference", "n", "n", "n"],
                           ["MinDifference", "n", "n", "n"],
                           ["Rest of them", "0.004", "n", "n"]
                            ])
        
        obj_stats1.scale(0.3)
        obj_stats2.scale(0.3)

        #edge_frame = obj_stats1.add(obj_stats1.get_cell((3,1), color = YELLOW))
        #face_frame = obj_stats1.add(obj_stats1.get_cell((8,1), color = YELLOW))

        hausdorff_Text = Text("Hausdorff Distance measures ...")
        #hausdorff_eq = MathTex(r"d_H(X,Y_i) = max \biggl\{sup_{x \in X} d(x,Y_i), sup_{y \in Y_i} d(X,y) \biggr\}")

        chamfer_Text = Text("Chamfer Distance measures...")
        #chamfer_eq = MathTex(r"d_C(X,Y_i) = \sum_{x \in X} min_{y \in Y_i} \| x-y \|_2^2 + \sum_{y \in Y_i} min_{x \in X} \| x-y \|_2^2")
       # chamfer_eq.scale(0.7)

        earth_mover_Text = Text("Earth Mover Distance measures energy...")
        #earth_mover_eq = MathTex(r"d_EM = \sum_{i = 1}^{m} \sum_{i = 1}^{n} M_{ij}d{ij}")

        minowski_sum_Text = Text("Minowski sum gives...")
        #minowski_sum_eq = MathTex(r"2+56")

        percor_Text = Text("Pearson correlation coefficient...")
        #percor = MathTex(r"r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y}{\sqrt{\sum (x_i-\bar{x})^2 \sum (y_i - \bar{y})^2}}")

        sprcor_Text = Text("Spearman correlation coefficient...")
        #sprcor = MathTex(r"\rho = 1 - \frac{6 \sum d_i^2}{n(n²-1)}")

        sørensen_dice_Text = Text("Sørensen-Dice Coefficient measures the similarity of two sets...")
        #sørensen_dice_eq = MathText(r"SDC = \frac{2|X \cap Y|}{|X|+|Y|}")

        # Hausdorff Example
        # Chamfer Example

        # Write someting about how it is to work with these huge arrays. Using Dask?

        self.play(Write(obj_stats1))
        self.wait()
        self.play(FadeOut(obj_stats1))
        self.wait()
        self.play(Write(obj_stats2))
        self.wait()


class ResearchSpect(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Research Work - Spectral Rendering", font_size = 40).to_corner(UP + LEFT)
        slide_number = Text("???", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        # 3D Scanning - Point Clouds
        # Acquisition of Color and Texture
        # Fusing Color and Texture

        spectrum_rectangle = Rectangle(
                                        fill_color = color_gradient((RED, ORANGE, YELLOW, GREEN_C, GREEN, BLUE_C, BLUE, PURPLE, PURPLE), 10), 
                                        fill_opacity = 1,
                                        width = 10,
                                        height=1
                                        )
        spect_ax = NumberLine(x_range=[380,720,20], length=10, include_numbers=True, font_size=12).next_to(spectrum_rectangle, DOWN)

        curve_ax = Axes(
                x_range=[-5,5,1],
                y_range=[0,0.5,0.1],
                axis_config={"include_numbers":False}
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

        XYZ_Text = Text("XYZ Coordinates")
        XYZ_coor = Table([["X", "Y", "Z"],
                          ["35", "79", "148"],
                          ["36", "78", "149"],
                          ["n", "n", "n"],
                          ["150", "340", "701"]])

        RGB_Text = Text("RGB Values - Per Point")
        RGB_vals = Table([["R", "G", "B"],
                          ["35", "79", "148"],
                          ["36", "78", "149"],
                          ["n", "n", "n"],
                          ["147", "27", "201"]])
        
        # Add values if using UV Projection - Resolution etc.

        SPEC_vals = Table([["\lambda", "Reflectance"],
                          ["300", "34",],
                          ["301", "34"],
                          ["n", "n"],
                          ["1000", "89"]])




        # Add multispectral curves, and hyperspectral continous curve

        # Add example showing difference between UV Projection rendering and Vertex Color Rendering | Side by side

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


class Publications(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Publications", font_size = 40).to_corner(UP + LEFT)
        slide_number = Text("???", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        # Journals and Conferences

        #HRSC = Image
        HRSC_title = Text("Journal of Heritage Science")
        HRSC_paper = Text("Standardization of Digitized Heritage: A Review of General-Purpose Implementations of 3D in Cultural Heritage")
        
        # Archiving 2023
        # ARCHIVING = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ARCHIVING.png")
        arch_talk = Text("Statistical Evaluation of 3D Manifolds Shape Retention During Simplification Stages")
        JIST = Text("JIST VERSION")

        #JCCH = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/JournCompCH.png")
        JCCH_title = Text("Journal of Computing and Cultural Heritage")
        JCCH_pap = Text("STATM - A Statistical Toolbox for Analysis of Triangulated Manifolds")

        # Whispers 2023
        # WHISP = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Whispers.png")
        WHISP_title = Text("WHISPERS - Workshop on Hyperspectral Image and Signal Processing")
        WHISP_paper = Text("Pixel-based Point Cloud Clustering for Spectral Data Enrichment")

        # Planned Papers

        PAP_3 = Text("Modular Digitization / Resolution Loss in Data Fusion")
        PAP_4 = Text("Material Characteristics")
        PAP_5 = Text("Resolution Errors in Fusing Data Modalities for Large CH Objects?")
        PAP_6 = Text("Quality Metric")

        # Coop
        CoPAP_1 = Text("Error Diffusion Texture 3D Printing")
        CoPAP_2 = Text("Parametric Shape in CT Medical Scan")
        CoPAP_3 = Text("Spectral Rendering w Milan?")

        AUTH1 = Text("First Author", color = GREEN_D)
        AUTH2 = Text("Second Author", color = ORANGE)

        JOURN = Text("Journal")
        CONFE = Text("Conference")

        STATUS = Text("Status")
        STATUS_1 = Text("Complete", color = GREEN_D)
        STATUS_2 = Text("Planned", color = RED_C)
        STATUS_3 = Text("In Works", color = ORANGE)
        PUB_1 = Text("Published", color = GREEN_D)
        PUB_2 = Text("Submitted", color = ORANGE)

        LVL_1 = Text("Level 1")
        LVL_2 = Text("Level 2")

        Empty = Text("-")
        #                       Title, Status, Published/Submitted, Level
        PubTab = MobjectTable([[PAP_6, STATUS_1, PUB_1],
                               [PAP_6.copy(), STATUS_1.copy(), PUB_2],
                               [PAP_6.copy(), STATUS_2, Empty]])
        PubTab.scale(0.5)

        #ConfTab = MobjectTable([[],
        #                      ])

        self.play(Write(PubTab), run_time = 1)
        self.wait(2)

        # Proposed publication Journals and Conferences

        JRNCH = Text("Journal of Cultural Heritage")
        COGR = Text("Computers & Graphics")
        COCH = Text("Journal of Computing and Cultural Heritage")

        TDOR = Text("Symposium of 3D Object Retrieval (3DOR)")
        TDIA = Text("3D Imaging and Applications (3DIA)")
        CIC = Text("Color and Imaging Conference (CIC)")

class Other(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Other Work", font_size = 40).to_corner(UP + LEFT)
        slide_number = Text("???", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        # IDIG4002 TA   # Can run parts of the videos as a small window in this slide. Import the code here and scale it. 
        IDIG4002_title = Text("IDIG4002 - Teaching Assistant")

        # IMT4310 Lecture and Student Work
        IMT4310_title = Text("IMT4310 - Guest Lecture and Student Work")
        IMT4310_image1 = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/IMT1.jpg/")
        IMT4310_image2 = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/IMT2.jpg").next_to(IMT4310_image1, RIGHT)


class FutureWork(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Future Work", font_size = 40).to_corner(UP + LEFT)
        slide_number = Text("???", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)


class Summary(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Summary", font_size = 25).to_corner(UP + LEFT)
        slide_number = Text("???", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        ## Timeplan Summary ##


class Questions(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Questions and Comments", font_size = 40).to_corner(UP + LEFT)
        slide_number = Text("???", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        banner = ManimBanner().move_to(DOWN)
        banner.scale(0.3)
        madeuse = Text("Made using ", font_size = 10).next_to(banner, LEFT)

        self.add(slide_title, slide_number)
        self.play(Create(banner), Write(madeuse))
        self.play(banner.expand)
        self.wait(2)

        ## Questions? ##






# What fancy functions to visualize?
# - Point cloud simplifications
# - Spectral Image Processing (Think wavelengths etc)
#       - RGB Function Curves vs Hyperspectral Function Curves, with simoultaneous visualization
#       - Also note going into the IR and UV
#       - Should I characterize our scanners? Probably a good idea. 
#       - Resolution of Hyperspectral Image vs normal image, projecting it onto a UV map from our scanners
# - Hausdorff Measurements | with visual example
# - Statistical Models | with visual example
# - Minowski Sum | with visual example

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