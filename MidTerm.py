from manim import *
from manim_slides import Slide, ThreeDSlide
import open3d as o3d
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

class Point_Cloud(PMobject):
    def __init__(self, path, sample_num=int(1e4), load_scale=1, stroke_width=1, **kwargs):
        PMobject.__init__(self, stroke_width=stroke_width, **kwargs)
        mesh = o3d.io.read_triangle_mesh(path).scale(load_scale, center=ORIGIN)
        mesh.compute_vertex_normals()
        pcd = mesh.sample_points_poisson_disk(number_of_points=sample_num, init_factor=5)

        self.vertices = np.asarray(pcd.points)
        self.normals = np.asarray(pcd.normals)
        self.add_points(self.vertices, color=self.color)

    def lightup(self, light_vector=UP):
        # compute the dot product of normal vectors and light vector, and normalize to [0, 1]
        # use them as the lightup weight
        lightup_value = np.expand_dims(
            (np.sum(self.normals * light_vector, axis=1) + 1)/2,
            axis=1
        )
        # concatenate as [point_num, 4] lihtup weight array
        lightup_expand = np.concatenate(
            (
                lightup_value, 
                lightup_value, 
                lightup_value, 
                np.ones((len(self.vertices), 1))
            ),
            axis=1
        )
        # use the lightup weight array to lightup/shadow the rgbs attribute
        # noted that the opacity channel aren't changed
        self.rgbas = lightup_expand * self.rgbas

class Mesh(VGroup):
    def __init__(self, path, stroke_width=0, fill_opacity=1, **kwargs):
        VGroup.__init__(self, stroke_width=stroke_width, fill_opacity=fill_opacity, **kwargs)
        mesh = o3d.io.read_triangle_mesh(path)
        mesh.compute_triangle_normals()

        self.vertices = np.asarray(mesh.vertices)
        self.triangles = np.asarray(mesh.triangles)
        self.normals = np.asarray(mesh.triangle_normals)

        faces = VGroup()
        for tri in self.triangles:
            face = ThreeDVMobject()
            face.set_points_as_corners([
                    self.vertices[tri[0]],
                    self.vertices[tri[1]],
                    self.vertices[tri[2]],
                ],
            )
            faces.add(face)
        
        faces.set_fill(color=self.fill_color, opacity=self.fill_opacity)
        faces.set_stroke(
            color=self.stroke_color,
            width=self.stroke_width,
            opacity=self.stroke_opacity,
        )
        self.add(*faces)

    def lightup(self, light_vector=UP):
        # compute the dot product of normal vectors and light vector, and normalize to [0, 1]
        # use them as the lightup weight
        lightup_value = (np.sum(self.normals * light_vector, axis=1) + 1)/2
        # use the lightup weight array to lightup/shadow the face color
        # noted that the opacity channel aren't changed
        for idx in range(len(self.submobjects)):
            face = self.submobjects[idx]
            weight = lightup_value[idx]
            original_rgba = color_to_rgba(face.color)
            
            lightup_rgba = weight * original_rgba
            lightup_rgba[-1] = 1.0
            face.set_fill(color=rgba_to_color(lightup_rgba))

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

        SVG = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/SVALW.svg")
        SVG.scale(2)

        self.play(Write(SVG), run_time=2)
        self.wait(2)

class FUNCTest(Scene):
    def construct(self):
            self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

            cloud_1 = PointCloudDot(color=RED)
            cloud_2 = PointCloudDot(stroke_width=4, radius=1)
            cloud_3 = PointCloudDot(density=15)

            group = Group(cloud_1, cloud_2, cloud_3).arrange()
            self.add(group)
            self.wait(2)

class TDTest(ThreeDScene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])
        self.set_camera_orientation(phi=60 * DEGREES)

        pcd = Point_Cloud("/home/markus/Priv_Manim_Slides/Manim-Slides/3D/bunny/reconstruction/bun_zipper.ply")
        pcd.scale(5)
        pcd.lightup()
        pcd.rotate(90*DEGREES, RIGHT)
        

        self.add(pcd)
        self.begin_ambient_camera_rotation(rate=4)
        self.wait()


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


class Intro(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        st1 = Text("Introduction", font_size = 40, font="FreeSans").move_to([-5, 3.5, 0])
        sn1 = Text("1", font_size = 10, weight=BOLD).move_to([6, -3.5,0])
        CLs = ImageMobject("/home/markus/CL_Manim/Manim_IDIG4002/Logos/CLsmall.png/").move_to([6.5, -3.5,0])
        CLs.scale(0.5)

        PhD_Title = Text("Multiresolution and Multimodal Acquisiton\nand Fusion of Heterogeneous Data", font_size=30, font="FreeSans").move_to([0,2,0])

        SONY_t = Text("Main Supervisor:\nSony George", font_size=15, font="FreeSans")
        SONY = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/SONY.jpg", scale_to_resolution=3000).next_to(SONY_t, LEFT)
        ADITYA_t = Text("Co-Supervisor #1:\nAditya Sole", font_size=15, font="FreeSans").next_to(SONY_t, DOWN)
        ADITYA = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ADITYA.jpg", scale_to_resolution=3000).next_to(ADITYA_t, LEFT)
        JON_t = Text("Co-Supervisor #2:\nJon Yngve Hardeberg", font_size=15, font="FreeSans").next_to(ADITYA_t, DOWN)
        JON = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/JON.jpg", scale_to_resolution=3000).next_to(JON_t, LEFT)

        SupvGrp = Group(SONY_t, ADITYA_t, JON_t, SONY, ADITYA, JON).arrange_in_grid(rows=2, cols=3, buff=0.3).move_to([-3,-3,0])

        RQ1 = Text("Research Question 1: INSERT", font_size=20, font="FreeSans", t2w={"Research Question 1:":BOLD})
        RQ2 = Text("Research Question 2: INSERT", font_size=20, font="FreeSans", t2w={"Research Question 2:":BOLD})
        RQ3 = Text("Research Question 3: INSERT", font_size=20, font="FreeSans", t2w={"Research Question 3:":BOLD})

        RQGrp = Group(RQ1, RQ2, RQ3).move_to([-4,1,0])
        RQGrp.arrange(DOWN, center=False, aligned_edge=LEFT)

    # Modalities


        # Add other modalities (NeRF, gloss measurements) and variations of the, (Meshes and point clouds.)

        Data_Title = Text("Data Modalities", font_size=20, font="FreeSans").move_to([-5,2,0])

        colimg = Rectangle(width=6, height=4, grid_xstep=0.2, grid_ystep=0.2).move_to([-4,0,0])
        colimg.scale(0.5)
        RCube = Rectangle(width=2, height=1, color=RED)
        GCube = Rectangle(width=2, height=1, color=GREEN)
        BCube = Rectangle(width=2, height=1, color=BLUE)
        
        spcimg = Rectangle(width=6, height=4, grid_xstep=0.5, grid_ystep=0.5).move_to([0,0,0])
        spcimg.scale(0.5)
        spectrum_rectangle = Rectangle(
                                        fill_color = color_gradient((RED, ORANGE, YELLOW, GREEN_C, GREEN, BLUE_C, BLUE, PURPLE, PURPLE), 10), 
                                        fill_opacity = 1,
                                        width = 6,
                                        height=0.3
                                        ).next_to(spcimg, DOWN)
        spectrum_rectangle.scale(0.5)

        pcd = Point_Cloud("/home/markus/Priv_Manim_Slides/Manim-Slides/3D/bunny/reconstruction/bun_zipper.ply").move_to([4,0,0])
        pcd.scale(5)
        pcd.lightup()
        pcd.rotate(90*DEGREES, RIGHT)

    # Resolution Difference
        
        self.add(st1,sn1,CLs)
        self.play(Write(PhD_Title))
        self.next_slide()
        self.play(FadeIn(SupvGrp), run_time=0.3)
        self.next_slide()
        self.play(FadeIn(RQGrp[0]), run_time=0.3)
        self.next_slide()
        self.play(FadeIn(RQGrp[1]), run_time=0.3)
        self.next_slide()
        self.play(FadeIn(RQGrp[2]), run_time=0.3)
        self.next_slide()
        self.play(FadeOut(SupvGrp), FadeOut(RQGrp), Transform(PhD_Title, Data_Title))
        self.next_slide()
        self.play(Create(colimg))
        self.next_slide()
        self.play(Create(spcimg), FadeIn(spectrum_rectangle))
        self.next_slide()
        self.play(FadeIn(pcd))
        self.next_slide()
        self.start_loop()
        self.play(Rotate(pcd, angle=2*PI, about_point=[4,0,0], rate_func=linear, run_time=25))
        self.end_loop()
        self.play(FadeOut(colimg), FadeOut(spcimg), FadeOut(spectrum_rectangle))
        self.next_slide()
        self.play(pcd.animate.move_to([0,0,0]))
        self.play(pcd.animate.scale(5))
        self.next_slide()
        self.start_loop()
        self.play(Rotate(pcd, angle=2*PI, about_point=[0,0,0], rate_func=linear, run_time=25))
        self.end_loop()
        self.wait(3)

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
    
    # Resolution Difference

        spcimg = Rectangle(width=6, height=4, grid_xstep=0.5, grid_ystep=0.5)

class Lab(ThreeDSlide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        st2 = Text("Lab Engineer", font_size = 40).to_corner(UP + LEFT)
        sn2 = Text("2", font_size = 10).to_corner(DOWN + RIGHT)
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


class DataCollection(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        st4 = Text("Data Collection", font_size = 40).to_corner(UP + LEFT)
        sn4 = Text("4", font_size = 10).to_corner(DOWN + RIGHT)
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
        FOKUS = ImageMobject(FOKUS)
        # TexRec
        # Department of Conservation at UiO?


class Courses(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        st3 = Text("Courses", font_size = 40, font="FreeSans").move_to([-5, 3.5, 0])
        sn3 = Text("3", font_size = 10, weight=BOLD).move_to([6, -3.5,0])
        CLs = ImageMobject("/home/markus/CL_Manim/Manim_IDIG4002/Logos/CLsmall.png/").move_to([6.5, -3.5,0])
        CLs.scale(0.5)
        NTNUs = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNUText.png").move_to([-5,-4,0])
        NTNUs.scale(0.2)

        CI = Text("DT8121 - Colour Imaging", font_size=20, font="FreeSans")
        CHG = Text("CHANGE Training School - Poland", font_size=20, font="FreeSans")
        HFEL = Text("HFEL8000 - Communicating Science", font_size=20, font="FreeSans")
        STK = Text("STK9900 - Statistical Methods and Applications", font_size=20, font="FreeSans")
        IDT = Text("IDT8000 - Research Ethics", font_size=20, font="FreeSans")
        IDIG = Text("IDIG4002 - Computer Graphics Fundamentals and Applications", font_size=20, font="FreeSans")
        CourseGrp = Group(CI, CHG, HFEL, STK, IDT, IDIG).arrange(DOWN, center=False, aligned_edge=LEFT).move_to([-2.5,1,0])

        CO = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsvg.svg")
        NTNU = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNUsvg.svg")
        WUT = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/WUT.svg")
        UIO = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/UIORed.svg")
        CourseLogoGrp = VGroup(CO, NTNU, WUT, UIO).arrange(DOWN).move_to([4.5,0,0])
        CourseLogoGrp.scale(0.7)

        coursetable = Table(
                            [["Autumn 2021", "Spring 2022", "Autumn 2022", "Spring 2023"],
                            ["DT8121 (7,5)", "HFEL8000 (3)", "IDIG4002 (7,5)", "-"],
                            ["CHANGE WuT (3)", "STK9900 (10)", "IDT8000 (2,5)", "-"],
                            ["","","Total ECTs:","33,5"]]
        ).move_to([-3,-2.5,0])
        coursetable.scale(0.3)

        self.add(st3, sn3, CLs, NTNUs)
        self.play(FadeIn(CourseGrp[0]),
                  FadeIn(CourseGrp[1]),
                  FadeIn(CourseGrp[2]),
                  FadeIn(CourseGrp[3]),
                  FadeIn(CourseGrp[4]),
                  FadeIn(CourseGrp[5]))
        self.play(Write(CourseLogoGrp))
        self.wait()
        self.play(Create(coursetable))
        self.wait(2)

        
class Outreach(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        st4 = Text("Outreach & Dissemination", font_size = 40, font="FreeSans").move_to([-4, 3, 0])
        sn4 = Text("4", font_size = 10, weight=BOLD).move_to([6, -3.5,0])
        CLs = ImageMobject("/home/markus/CL_Manim/Manim_IDIG4002/Logos/CLsmall.png/").move_to([6.5, -3.5,0])
        CLs.scale(0.5)

    # All NO-CHANGE visits and presentations
        #NOCHANGE = ImageMobject(r"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NO-CHANGE.svg") #Change to SVG
        NORW = SVGMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NORW.svg")
        NORW.scale(3)
        NORW.move_to([4,0,0])
        SVALW = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/SVALW.svg")
        SVALW.move_to([3,2,0])
        NOCH = Text("NO-CHANGE Events", font_size=25).move_to([-4,2,0])
        TRON = Text("Trondheim ????", font_size=20) # ADD Points for all locations
        BERG = Text("Bergen - 07.03.2022", font_size=20)
        ÅLES = Text("Ålesund - 09.03.2022", font_size=20)
        TROM = Text("Tromsø - 09.05.2022", font_size=20)
        SVAL = Text("Svalbard - 22.09.2022", font_size=20) #Sjekk disse datoene, er litt usikker her.
        STAV = Text("Stavanger - 03.10.2022", font_size=20)
        MUNCH = Text("Oslo MUNCH Museum - 29.11.2022", font_size=20)

        NoChangeGrp = VGroup(TRON, BERG, ÅLES, TROM, SVAL, STAV, MUNCH)
        NoChangeGrp.arrange(DOWN, aligned_edge=LEFT)
        NoChangeGrp.next_to(NOCH, DOWN)

    # MANER Mobility at Yale
        MANER = SVGMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/MANER.svg")
        YALE = SVGMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/YALEsvg.svg").move_to([2,-2,0])

        YALE_Text = Text("University of Yale")
        YALE_info = Text("Discussed some research approaches")
        YALE_info2 = Text("Inverse Procedural Rendering") 

    # MANER Training School at Chiba 
        CHIBA = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CHIBA.svg")

    # UiO Gloss Presentation
        UIO = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/UIORed.svg")
        UiOText = Text("Acquisition and Reproduction of Gloss Data")

    # Webinars and Workshops
        DT4BHText = Text("International Workshop on Digital Tools for Built Heritage Diagnosis and Monitoring")
        DT4BH = ImageMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/DT4BH.png")

        DaSCHCon = Text("DaSCHCon on IIIF, 3D and Interoperability")


        self.add(st4,sn4,CLs)
        #self.play(Write(NOCHANGE))
    
        self.play(FadeIn(NOCH), Write(NORW), Write(SVALW))
        self.wait()
        self.play(FadeIn(TRON))
        self.play(TransformFromCopy(TRON,BERG),
                  TransformFromCopy(TRON,ÅLES),
                  TransformFromCopy(TRON,TROM),
                  TransformFromCopy(TRON,SVAL),
                  TransformFromCopy(TRON,STAV),
                  TransformFromCopy(TRON,MUNCH))
        self.play(Write(YALE), run_time=2)
        self.wait()

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

        st8 = Text("Statistics", font_size = 40, font="FreeSans").move_to([-5, 3.5, 0])
        sn8 = Text("8", font_size = 10, weight=BOLD).move_to([6, -3.5,0])
        CLs = ImageMobject("/home/markus/CL_Manim/Manim_IDIG4002/Logos/CLsmall.png/").move_to([6.5, -3.5,0])
        CLs.scale(0.5)

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


class ResearchStatGraphs(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        st9 = Text("Statistics - Graphs", font_size = 40, font="FreeSans").move_to([-4.5, 3.5, 0])
        sn9 = Text("9", font_size = 10, weight=BOLD).move_to([6, -3.5,0])
        CLs = ImageMobject("/home/markus/CL_Manim/Manim_IDIG4002/Logos/CLsmall.png/").move_to([6.5, -3.5,0])
        CLs.scale(0.5)


        X = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

        # Mean Values
        DNUyMean = [0.000022, 0.000068, 0.00013, 0.000203, 0.000287, 0.000384, 0.000489, 0.000599, 0.000725, 0.000864, 0.001016, 0.001183, 0.001374, 0.001588, 0.001807, 0.002001]
        DUyMean = [0.000067, 0.000155, 0.000277, 0.000435, 0.000646, 0.000907, 0.001222, 0.001635, 0.002174, 0.002912, 0.003831, 0.005132, 0.007041, 0.009728, 0.014257, 0.022024]
        DSyMean = [0.000164, 0.00045, 0.000967, 0.001558, 0.002264, 0.003053, 0.003979, 0.004888, 0.005783, 0.006765, 0.0079, 0.009215, 0.010796, 0.012556, 0.01473, 0.017454]
        #DAyMean = []
        DRyMean = [0.000033, 0.000094, 0.000175, 0.000272, 0.000388, 0.000519, 0.000667, 0.000838, 0.001028, 0.001239, 0.001478, 0.001749, 0.002074, 0.002476, 0.002992, 0.003734]

        VCNUyMean = [0.00016, 0.000383, 0.000617, 0.000957, 0.001176, 0.00142, 0.001562, 0.001808, 0.00196, 0.002085, 0.002294, 0.002549, 0.002996, 0.003466, 0.004391, 0.007168]
        VCUyMean = [0.000202,0.000524, 0.000897, 0.00198, 0.001353, 0.001837, 0.003112, 0.005039, 0.005459, 0.006791, 0.00913, 0.009944, 0.011251, 0.013204, 0.013866, 0.016397]
        VCSyMean = [0.001433, 0.002938, 0.004038, 0.005485, 0.006635, 0.007769, 0.009293, 0.009853, 0.011052, 0.011958, 0.012706, 0.014196, 0.015011, 0.016028, 0.017455, 0.018818]
        #VCAyMean = []
        VCRyMean = [0.000167, 0.000391, 0.000648, 0.000891, 0.001131, 0.001377, 0.001613, 0.001803, 0.001997, 0.002192, 0.002428, 0.002666, 0.002964, 0.003334, 0.003887, 0.004815]

        QEMNUyMean = [0.000022, 0.00007, 0.00013, 0.000202, 0.000281, 0.000373, 0.000471, 0.000582, 0.000703, 0.000839, 0.000996, 0.001171, 0.001365, 0.002352, 0.001792, 0.001987]
        QEMUYyMean = [0.000048, 0.00011, 0.000181, 0.000263, 0.000349, 0.00044, 0.000546, 0.000657, 0.000772, 0.000903, 0.001038, 0.001195, 0.001352, 0.001521, 0.00168, 0.001824]
        QEMSyMean = [0.000166,0.000472, 0.000927, 0.001433, 0.002049, 0.002701, 0.00344, 0.004232, 0.005026, 0.006112, 0.007344, 0.008861, 0.01071, 0.012805, 0.01525, 0.01758]
        #QEMAyMean = []
        QEMRyMean = [0.00003, 0.000086, 0.00016, 0.000248, 0.000353, 0.00047, 0.000603, 0.000757, 0.000927, 0.00112, 0.001341, 0.001602, 0.001907, 0.002287, 0.002764, 0.003468]

        #CFMNUy = []
        #CFMUy = []
        #CFMSy = []
        #CFMAy = []
        #CFMRy = []

        ECNUyMean = [0.000023, 0.000069, 0.000128, 0.000197, 0.000277, 0.000363, 0.000457, 0.000562, 0.000679, 0.000806, 0.000953, 0.00112, 0.001318, 0.001533, 0.001884, 0.001981]
        ECUyMean = [0.000049, 0.000109, 0.000178, 0.000255, 0.000337, 0.000429, 0.000526, 0.000632, 0.000745, 0.000872, 0.001008, 0.001167, 0.001337, 0.001515, 0.001676, 0.001852]
        ECSyMean = [0.000168, 0.000457, 0.00088, 0.001408, 0.001967, 0.00264, 0.003344, 0.004045, 0.004828, 0.005738, 0.006695, 0.008032, 0.009836, 0.011893, 0.014251, 0.017184]
        #ECAyMean = []
        ECRyMean = [0.000034, 0.000097, 0.000177, 0.000272, 0.000382, 0.000507, 0.000648, 0.000807, 0.000985, 0.001184, 0.001413, 0.001683, 0.002001, 0.00239, 0.00288, 0.003533]

        # Max Values
        DNUyMax = [0.002443, 0.002939, 0.003472, 0.004111, 0.006561, 0.006687, 0.006691, 0.006593, 0.006828, 0.007132, 0.008242, 0.008879, 0.010853, 0.013142, 0.018737, 0.021276]
        DUyMax = [0.020037 ,0.021446, 0.028478, 0.04562, 0.044692, 0.054992, 0.056223, 0.068494, 0.071382, 0.082927, 0.093564, 0.115574, 0.133134, 0.148451, 0.18159, 0.21942]
        DSyMax = [0.006373, 0.012148, 0.019601, 0.024956, 0.026669, 0.033207, 0.032065, 0.038947, 0.037141, 0.046569, 0.048825, 0.058754, 0.06574, 0.063708, 0.073637, 0.100746]
        #DAyMax = []
        DRyMax = [0.007559, 0.009433, 0.009231, 0.011837, 0.010982, 0.012218, 0.010972, 0.013062, 0.013272, 0.014033, 0.015074, 0.018142, 0.02255, 0.022632, 0.024738, 0.029884]
 
        VCNUyMax = [0.00754, 0.00797, 0.009585, 0.012043, 0.015829, 0.018397, 0.019428, 0.023101, 0.026926, 0.029363, 0.032046, 0.033331, 0.039943, 0.04035, 0.044295, 0.05756]
        VCUyMax = [0.006676, 0.00869, 0.011377, 0.01868, 0.019466, 0.02265, 0.028335, 0.031835, 0.035076, 0.037194, 0.042755, 0.043386, 0.049549, 0.056589, 0.059017, 0.063978]
        VCSyMax = [0.041846, 0.049014, 0.047062, 0.048941, 0.050193, 0.051504, 0.053751, 0.055361, 0.054976, 0.056035, 0.057871, 0.062175, 0.059793, 0.062405, 0.066077, 0.067913]
        #VCAyMax = []
        VCRyMax = [0.006981, 0.008674, 0.01069, 0.01141, 0.012589, 0.013831, 0.01595, 0.014809, 0.017402, 0.017442, 0.020999, 0.020664, 0.022785, 0.023581, 0.030788, 0.037792]

        QEMNUyMax = [0.002947, 0.003017, 0.003675, 0.004309, 0.005839, 0.005742, 0.007447, 0.008544, 0.008128, 0.008958, 0.008869, 0.01032, 0.012032, 0.012002, 0.012428, 0.013901]
        QEMUyMax = [0.003225, 0.003925, 0.004415, 0.00649, 0.006654, 0.005573, 0.00718, 0.006979, 0.008333, 0.008349, 0.009277, 0.00941, 0.010608, 0.020899, 0.019218, 0.023241]
        QEMSyMax = [0.009136, 0.012288, 0.015836, 0.024314, 0.025648, 0.034461, 0.03555, 0.043636, 0.043034, 0.044969, 0.055297, 0.057992, 0.06548, 0.066876, 0.071107, 0.074442]
        #QEMAyMax = []
        QEMRyMax = [0.007491, 0.008129, 0.008693, 0.008921, 0.009713, 0.010162, 0.011594, 0.014807, 0.012272, 0.013675, 0.017273, 0.016977, 0.020012, 0.019367, 0.025164, 0.027423]

        #CFMNUyMax = []
        #CFMyMax = []
        #CFMyMax = []
        #VCAyMax = []
        #CFMyMax = []

        ECNUyMax = [0.006568, 0.006485, 0.006508, 0.006656, 0.010559, 0.010504, 0.010441, 0.018388, 0.01953, 0.023292, 0.022719, 0.014242, 0.014251, 0.023741, 0.024254, 0.022875]
        ECUyMax = [0.004941, 0.004084, 0.003111, 0.004521, 0.006403, 0.006722, 0.005238, 0.007588, 0.012894, 0.020817, 0.030439, 0.030569, 0.032247, 0.038162, 0.034766, 0.06502]
        ECSyMax = [0.005358, 0.008439, 0.013182, 0.017365, 0.022764, 0.025011, 0.030076, 0.029797, 0.032495, 0.041226, 0.04489, 0.050919, 0.066813, 0.070168, 0.070143, 0.074579]
        #ECAyMax = []
        ECRyMax = [0.007504, 0.009433, 0.009149, 0.01171, 0.011164, 0.011873, 0.01181, 0.014555, 0.01842, 0.016571, 0.017971, 0.019921, 0.023775, 0.023197, 0.027797, 0.028723]

        
        # Mean Graphs
        DeciMean_Axes = Axes(x_range = [-1, 16, 1],
                             y_range = [0, 0.025, 0.005]
        )
        DeciTit = Text("Decimation - Mean Error", font_size=25).next_to(DeciMean_Axes, DOWN)
        DeciMean_Lables = DeciMean_Axes.get_axis_labels(x_label = "Simplification Stage", y_label = "Hausdorff Distance")
        DNUGraph = DeciMean_Axes.plot_line_graph(x_values = X, y_values = DNUyMean, line_color = RED)
        DUGraph = DeciMean_Axes.plot_line_graph(x_values = X, y_values = DUyMean, line_color = GREEN)
        DSGraph = DeciMean_Axes.plot_line_graph(x_values = X, y_values = DSyMean, line_color = BLUE)
        #DAGraph = DeciMean_Axes.plot_line_graph(x_values = X, y_values = DAyMean, line_color = PURPLE)
        DRGraph = DeciMean_Axes.plot_line_graph(x_values = X, y_values = DRyMean, line_color = GOLD)
        DeciMeanGrp = VGroup(DeciMean_Axes, DeciTit, DNUGraph, DUGraph, DSGraph, DRGraph)

        VerCluMean_Axes = Axes(x_range = [-1, 16, 1],
                               y_range = [0, 0.025, 0.005]
        )
        VerCluTit = Text("Vertex Clustering - Mean Error", font_size=25).next_to(VerCluMean_Axes, DOWN)
        VCNUGraph = VerCluMean_Axes.plot_line_graph(x_values = X, y_values = VCNUyMean, line_color = RED)
        VCUGraph = VerCluMean_Axes.plot_line_graph(x_values = X, y_values = VCUyMean, line_color = GREEN)
        VCSGraph = VerCluMean_Axes.plot_line_graph(x_values = X, y_values = VCSyMean, line_color = BLUE)
        #VCAGraph = VerCluMean_Axes.plot_line_graph(x_values = X, y_values = VCAyMean, line_color = PURPLE)
        VCRGraph = VerCluMean_Axes.plot_line_graph(x_values = X, y_values = VCRyMean, line_color = GOLD)
        VerCluMeanGrp = VGroup(VerCluMean_Axes, VerCluTit, VCNUGraph, VCUGraph, VCSGraph, VCRGraph)

        
        QEMMean_Axes = Axes(x_range = [-1, 16, 1],
                               y_range = [0, 0.025, 0.005]
        )
        QEMTit = Text("Quadric Error Metrics - Mean Error", font_size=25).next_to(QEMMean_Axes, DOWN)
        QEMNUGraph = QEMMean_Axes.plot_line_graph(x_values = X, y_values = QEMNUyMean, line_color = RED)
        QEMUGraph = QEMMean_Axes.plot_line_graph(x_values = X, y_values = QEMUYyMean, line_color = GREEN)
        QEMSGraph = QEMMean_Axes.plot_line_graph(x_values = X, y_values = QEMSyMean, line_color = BLUE)
        #QEMCAGraph = QEMMean_Axes.plot_line_graph(x_values = X, y_values = QEMAyMean, line_color = PURPLE)
        QEMRGraph = QEMMean_Axes.plot_line_graph(x_values = X, y_values = QEMRyMean, line_color = GOLD)
        QEMMeanGrp = VGroup(QEMMean_Axes, QEMTit, QEMNUGraph, QEMUGraph, QEMSGraph, QEMRGraph)

        #CFMMean_Axes = Axes(x_range = [-1, 16, 1],
        #                       y_range = [0, 0.025, 0.005]
        #)
        #CFMTit = Text("Coplanar Facets Merging - Mean Error", font_size=25).next_to(CFMMean_Axes, DOWN)
        #CFMNUGraph = CFMMean_Axes.plot_line_graph(x_values = X, y_values = CFMNUy, line_color = RED)
        #CFMUGraph = CFMMean_Axes.plot_line_graph(x_values = X, y_values = CFMMUy, line_color = GREEN)
        #CFMSGraph = CFMMean_Axes.plot_line_graph(x_values = X, y_values = CMFSy, line_color = BLUE)
        #CFMCAGraph = CFMMean_Axes.plot_line_graph(x_values = X, y_values = CFMAy, line_color = PURPLE)
        #CFMRGraph = CFMMean_Axes.plot_line_graph(x_values = X, y_values = CFMRy, line_color = GOLD)
        
        EdColMean_Axes = Axes(x_range = [-1, 16, 1],
                              y_range = [0, 0.025, 0.005]
        )
        EdColTit = Text("Edge Collapse - Mean Error", font_size=25).next_to(EdColMean_Axes, DOWN)
        ECNUGraph = EdColMean_Axes.plot_line_graph(x_values = X, y_values = ECNUyMean, line_color = RED)
        ECUGraph = EdColMean_Axes.plot_line_graph(x_values = X, y_values = ECUyMean, line_color = GREEN)
        ECSGraph = EdColMean_Axes.plot_line_graph(x_values = X, y_values = ECSyMean, line_color = BLUE)
        #ECCAGraph = EdColMean_Axes.plot_line_graph(x_values = X, y_values = ECAyMean, line_color = PURPLE)
        ECRGraph = EdColMean_Axes.plot_line_graph(x_values = X, y_values = ECRyMean, line_color = GOLD)
        EdColMeanGrp = VGroup(EdColMean_Axes, EdColTit, ECNUGraph, ECUGraph, ECSGraph, ECRGraph)

        StatMeanGrp = Group(DeciMeanGrp, VerCluMeanGrp, QEMMeanGrp, EdColMeanGrp)
        StatMeanGrp.scale(0.3)
        StatMeanGrp.arrange_in_grid(rows=2, cols=3, buff=1)

        # Max Graphs
        DeciMaxAxes = Axes(x_range = [-1, 16, 1],
                              y_range = [0, 0.25, 0.05]
        )
        DeciTitMax = Text("Decimation - Max Error", font_size=25).next_to(DeciMaxAxes, DOWN)
        DNUMaGraph = DeciMaxAxes.plot_line_graph(x_values = X, y_values = DNUyMax, line_color = RED)
        DUMaGraph = DeciMaxAxes.plot_line_graph(x_values = X, y_values = DUyMax, line_color = GREEN)
        DSMaGraph = DeciMaxAxes.plot_line_graph(x_values = X, y_values = DSyMax, line_color = BLUE)
        #DAMaGraph = DeciMaxAxes.plot_line_graph(x_values = X, y_values = DAyMax, line_color = PURPLE)
        DRMaGraph = DeciMaxAxes.plot_line_graph(x_values = X, y_values = DRyMax, line_color = GOLD)
        DeciMaxGrp = VGroup(DeciMaxAxes, DeciTitMax, DNUMaGraph, DUMaGraph, DSMaGraph, DRMaGraph)
        
        VeClMaxAxes = Axes(x_range = [-1, 16, 1],
                              y_range = [0, 0.08, 0.02]
        )
        VeClTitMax = Text("Vertex Clustering - Max Error", font_size=25).next_to(VeClMaxAxes, DOWN)
        VCNUMaGraph = VeClMaxAxes.plot_line_graph(x_values = X, y_values = VCNUyMax, line_color = RED)
        VCUMaGraph = VeClMaxAxes.plot_line_graph(x_values = X, y_values = VCUyMax, line_color = GREEN)
        VCSMaGraph = VeClMaxAxes.plot_line_graph(x_values = X, y_values = VCSyMax, line_color = BLUE)
        #VCAMaGraph = VeClMaxAxes.plot_line_graph(x_values = X, y_values = VCAyMax, line_color = PURPLE)
        VCRMaGraph = VeClMaxAxes.plot_line_graph(x_values = X, y_values = VCRyMax, line_color = GOLD)
        VeClMaxGrp = VGroup (VeClMaxAxes, VeClTitMax, VCNUMaGraph, VCUMaGraph, VCSMaGraph, VCRMaGraph)

        QEMMaxAxes = Axes(x_range = [-1, 16, 1],
                              y_range = [0, 0.08, 0.02]
        )
        QEMTitMax = Text("Quadric Error Metrics - Max Error", font_size=25).next_to(QEMMaxAxes, DOWN)
        QEMNUMaGraph = QEMMaxAxes.plot_line_graph(x_values = X, y_values = QEMNUyMax, line_color = RED)
        QEMUMaGraph = QEMMaxAxes.plot_line_graph(x_values = X, y_values = QEMUyMax, line_color = GREEN)
        QEMSMaGraph = QEMMaxAxes.plot_line_graph(x_values = X, y_values = QEMSyMax, line_color = BLUE)
        #QEMAMaGraph = QEMMaxAxes.plot_line_graph(x_values = X, y_values = QEMAyMax, line_color = PURPLE)
        QEMRMaGraph = QEMMaxAxes.plot_line_graph(x_values = X, y_values = QEMRyMax, line_color = GOLD)
        QEMMaxGrp = VGroup(QEMMaxAxes, QEMTitMax, QEMNUMaGraph, QEMUMaGraph, QEMSMaGraph, QEMRMaGraph)

        #CFMMaxAxes = Axes()
        #CFMTitMax = Text("Decimation - Max Error", font_size=25).next_to(CFMMaxAxes, DOWN)
        #CFMNUMaGraph = CFMMaxAxes.plot_line_graph(x_values = X, y_values = CFMNUyMax, line_color = RED)
        #CFMUMaGraph = CFMMaxAxes.plot_line_graph(x_values = X, y_values = CFMUyMax, line_color = GREEN)
        #CFMSMaGraph = CFMMaxAxes.plot_line_graph(x_values = X, y_values = CFMSyMax, line_color = BLUE)
        #CFMAMaGraph = CFMMaxAxes.plot_line_graph(x_values = X, y_values = CFMAyMax, line_color = PURPLE)
        #CFMRMaGraph = CFMMaxAxes.plot_line_graph(x_values = X, y_values = CFMRyMax, line_color = GOLD)
        #CFMMaxGrp = VGroup(CFMMaxAxes, CFMTitMax, CFMNUMaGraph, CFMUMaGraph, CFMSMaGraph, CFMAMaGraph, CFMRMaGraph)
        #CFMMaxGrp.scale(0.3)

        ECMaxAxes = Axes(x_range = [-1, 16, 1],
                              y_range = [0, 0.08, 0.02]
        )
        ECTitMax = Text("Edge Collapse - Max Error", font_size=25).next_to(ECMaxAxes, DOWN)
        ECNUMaGraph = ECMaxAxes.plot_line_graph(x_values = X, y_values = ECNUyMax, line_color = RED)
        ECUMaGraph = ECMaxAxes.plot_line_graph(x_values = X, y_values = ECUyMax, line_color = GREEN)
        ECSMaGraph = ECMaxAxes.plot_line_graph(x_values = X, y_values = ECSyMax, line_color = BLUE)
        #ECAMaGraph = ECMaxAxes.plot_line_graph(x_values = X, y_values = ECAyMax, line_color = PURPLE)
        ECRMaGraph = ECMaxAxes.plot_line_graph(x_values = X, y_values = ECRyMax, line_color = GOLD)
        ECMaxGrp = VGroup(ECMaxAxes, ECTitMax, ECNUMaGraph, ECUMaGraph, ECSMaGraph, ECRMaGraph)

        StatMaxGrp = VGroup(DeciMaxGrp, VeClMaxGrp, QEMMaxGrp, ECMaxGrp)
        StatMaxGrp.scale(0.3)
        StatMaxGrp.arrange_in_grid(rows=2, cols=3, buff=1)


        self.add(st9, sn9, CLs)
        self.play(Write(DeciMean_Axes), Write(DeciTit))
        self.wait()
        self.play(Write(DNUGraph), run_time = 2)
        self.wait()
        self.play(Write(DUGraph), run_time = 2)
        self.wait()
        self.play(Write(DSGraph), run_time = 2)
        self.wait()
        self.play(Write(DRGraph), run_time = 2)
        self.wait()
        self.play(Write(VerCluMeanGrp), Write(QEMMeanGrp), Write(EdColMeanGrp))
        self.play(FadeOut(StatMeanGrp))
        self.play(Write(StatMaxGrp))
        self.wait()


class ResearchSpectVect(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Research Work - Mesh Statistics", font_size = 25).to_corner(UP + LEFT)
        slide_number = Text("9", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)


        voxelgrid = Rectangle(width=1, height=4, grid_ystep=1, grid_xstep=1)
        kolbuspectimage = ImageMobject("")
        

        self.wait()
        self.play(Create(voxelgrid))

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


        area = curve_ax.get_area(
            blue_curve,
            x_range=(PI / 2, 3 * PI / 2),
            color=color_gradient((RED, ORANGE, YELLOW, GREEN_C, GREEN, BLUE_C, BLUE, PURPLE, PURPLE), 10),
            opacity=1,
        )

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
        self.play(Create(area))
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
        JCCH_title = Text("Journal of Imaging Science and Technology")
        JCCH_pap = Text("STATM - A Statistical Toolbox for Analysis of Triangulated Manifolds")

        # Whispers 2023
        # WHISP = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Whispers.png")
        WHISP_title = Text("WHISPERS - Workshop on Hyperspectral Image and Signal Processing")
        WHISP_paper = Text("Pixel-based Point Cloud Clustering for Spectral Data Enrichment")

        # JOI #1
        JOI1_title = Text("Journal of Imaging: Special Issue on Material Appearance")
        JOI_paper1 = Text("Surface Texture Reproduction using Error Diffusion in 3D Printing")
        # JOI #2
        JOI_paper2 = Text("Material Colour Characterization of Light-based 3D Acquisition Tools")

        # Planned Papers

        PAP_3 = Text("Modular Digitization / Resolution Loss in Data Fusion")
        PAP_4 = Text("Material Characteristics")
        PAP_5 = Text("Resolution Errors in Fusing Data Modalities for Large CH Objects?")
        PAP_6 = Text("Quality Metric")

        # Coop
        CoPAP_1 = Text("Error Diffusion Texture 3D Printing")

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

        WoodProject = Text("Project for Digital tiols for Wood")

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


class Questions(Slide):
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        slide_title = Text("Questions and Comments", font_size = 40).to_corner(UP + LEFT)
        slide_number = Text("???", font_size = 10).to_corner(DOWN + RIGHT)
        colorlabcorner = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").to_corner(DOWN + LEFT)
        colorlabcorner.scale(0.5)

        madeuse = Text("Made using ", font_size = 10)

        self.add(slide_title, slide_number)
        self.play(Write(madeuse))
        self.next_slide()
        self.play(Unwrite(madeuse))
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
