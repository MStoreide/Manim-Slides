from manim import *
from manim_slides import Slide, ThreeDSlide
import numpy as np
import math as m

class Header(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([1/255, 70/255, 147/255])

        Slide_Title = Text("Statistical Evaluation of 3D Manifolds Shape Retention During Simplification Stages", font_size = 25)
        Date = Text("20.06.2023")
        Name = Text("Markus Sebastian Bakken Storeide")
        Colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").move_to([-6.5, -3.5, 0])
        Colorlab.scale(0.5)
        Archiving = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Archiving.png/").move_to([4, -3.5, 0])
        Archiving.scale(0.2)
        ISNT = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ISNT.png/").move_to([1.5, -3.5, 0])
        ISNT.scale(0.05)
        NTNU = ImageMobject(NTNU)

        # Transition: Transform Images to small, Title to Slide Title

class Overview(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])
        
        Slide_Title = Text("Overview", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("1", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)
        Colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").move_to([-6.5, -3.5, 0])
        Colorlab.scale(0.5)
        Archiving = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Archiving.png/").move_to([4, -3.5, 0])
        Archiving.scale(0.2)
        ISNT = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ISNT.png/").move_to([1.5, -3.5, 0])
        ISNT.scale(0.05)

        # Transition: Remove Images

class Introduction(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])
        
        Slide_Title = Text("Introduction", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("2", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)

class SimplAlgo(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])
        
        Slide_Title = Text("Simplification Algorithms", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("2", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)

        SIMP = Text("Simplification removes vertices while\nattempting to retain the most geometry.", font_size = 20).move_to([-4,2.5,0])
        SimpsRefS = Text("[1] Cignoni, P., Montani, C., & Scopigno, R. (1998). A comparison\nof mesh simplification algorithms. Computers & Graphics,\n22(1), 37-54.", font_size=8).move_to(-4,-3,0)

        DECI_t = Text("Decimation iteratively removes vertices in a mesh\nbased on an evaluation of optimal local geometry.", font_size = 20).move_to([0,-2,0])
        DECI_t2 = Text("Decimation", font_size = 20, weight = BOLD).move_to([-4, 1.5, 0])
        VECL_t = Text("Vertex Clustering takes vertices in close proximity\nto each other and clusters and merges them into a single vertex.", font_size = 20).move_to([0,-2,0])
        VECL_t2 = Text("Vertex Clustering", font_size = 20, weight = BOLD).next_to(DECI_t2, DOWN)
        QEM_t = Text("Quadric Error Metrics utilizes a plane equation of a\ngiven triangle to estimate the ideal location of vertices.", font_size = 20).move_to([0,-2,0])
        QEM_t2 = Text("Quadric Error Metrics", font_size = 20, weight = BOLD).next_to(VECL_t2, DOWN)
        CFM_t = Text("Coplanar facets merging looks at planar divergence\nbetween polygons and merges them if they are above a certain threshold.", font_size = 20).move_to([0,-2,0])
        CFM_t2 = Text("Coplanar Facets Merging", font_size = 20, weight = BOLD).next_to(QEM_t2, DOWN)
        EDCO_t = Text("Edge Collapse finds pairs of vertices that are\nclose together, and collapses the edge between them.", font_size = 20).move_to([0,-2,0])
        EDCO_t2 = Text("Edge Collapse", font_size = 20, weight = BOLD).next_to(CFM_t2, DOWN)

        surface = Graph([1, 2, 3, 4, 5, 6, 7, 8, 9], [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)],
                  layout={1: [-4, 0, 0], 2: [-3, 0, 0], 3: [-2, 0, 0], 4: [-1, 0, 0], 5: [0, 0, 0], 6: [1, 0, 0], 7: [2, 0, 0], 8: [3, 0, 0], 9: [4, 0, 0]}
                  )
        Def_lay = layout={1: [-4, 0, 0], 2: [-3, 0, 0], 3: [-2, 0, 0], 4: [-1, 0, 0], 5: [0, 0, 0], 6: [1, 0, 0], 7: [2, 0, 0], 8: [3, 0, 0], 9: [4, 0, 0]}
        Min_Surface = Graph([1,2], [(1,2)], layout = {1: [-4,0,0], 2: [4,0,0]}).shift(DOWN*2.5)
        Rem_Surface = Graph([1, 2, 3, 4, 5, 6, 7, 8, 9], [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)],
                            layout={1: [-4, 0, 0], 2: [-3, 0, 0], 3: [-2, 0, 0], 4: [-1, 0, 0], 5: [0, 0, 0], 6: [1, 0, 0], 7: [2, 0, 0], 8: [3, 0, 0], 9: [4, 0, 0]},
                            vertex_config={2: {"fill_color": RED},
                                            3: {"fill_color": RED},
                                            4: {"fill_color": RED},
                                            5: {"fill_color": RED},
                                            6: {"fill_color": RED},
                                            7: {"fill_color": RED},
                                            8: {"fill_color": RED}},
                            edge_config={(2,3): {"stroke_color": RED},
                                        (3,4): {"stroke_color": RED},
                                        (4,5): {"stroke_color": RED},
                                        (5,6): {"stroke_color": RED},
                                        (6,7): {"stroke_color": RED},
                                        (7,8): {"stroke_color": RED}}
                            ).shift(DOWN*3)
        Dec_Surface = Graph([1, 2, 3, 4, 5, 6, 7, 8, 9], [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)],
                            layout={1: [-4, 0, 0], 2: [-3, 0, 0], 3: [-2, 0, 0], 4: [-1, 0, 0], 5: [0, 0, 0], 6: [1, 0, 0], 7: [2, 0, 0], 8: [3, 0, 0], 9: [4, 0, 0]},
                            vertex_config={2: {"fill_color": RED},
                                            4: {"fill_color": RED},
                                            6: {"fill_color": RED},
                                            8: {"fill_color": RED}}
                  )
        Dec_Surface_Simp = Graph([1,2,3,4,5], [(1,2),(2,3),(3,4),(4,5)],
                                 layout={1:[-4,0,0], 2:[-2,0,0], 3:[0,0,0], 4:[2,0,0], 5:[4,0,0]}).shift(DOWN)
        Dec_Group = VGroup(Dec_Surface, Dec_Surface_Simp).move_to([4,3,0]).scale(0.6)

        Redu = Text("* Reduction of ")



        self.add(Slide_Title, Slide_Number)
        self.play(Create(surface), run_time=3)
        self.wait(2)
        self.play(surface.animate.change_layout("circular"))
        self.wait(2)
        self.play(surface.animate.change_layout("spiral"))
        self.wait(2)
        self.play(surface.animate.change_layout("planar"))
        self.wait(2)
        self.play(surface.animate.change_layout("spectral"))
        self.wait(2)
        self.play(surface.animate.change_layout("spring"))
        self.wait(2)
        self.play(surface.animate.change_layout("random"))
        self.wait(2)
        self.play(surface.animate.change_layout(Def_lay))
        self.wait()
        self.play(surface.animate.shift(DOWN*3))
        self.wait()
        self.play(Transform(surface, Rem_Surface))
        self.wait()
        self.play(FadeIn(Min_Surface), shift = UP)
        self.play(FadeIn(SIMP))
        self.play(FadeIn(DECI_t))
        self.play(Transform(DECI_t, DECI_t2))
        self.play(FadeIn(VECL_t))
        self.play(Transform(VECL_t, VECL_t2))
        self.play(FadeIn(QEM_t))
        self.play(Transform(QEM_t, QEM_t2))
        self.play(FadeIn(CFM_t))
        self.play(Transform(CFM_t, CFM_t2))
        self.play(FadeIn(EDCO_t))
        self.play(Transform(EDCO_t, EDCO_t2))
        self.wait()
        self.play(DECI_t2.animate.move_to([0,3.5,0]), Create(Dec_Group))
        self.wait()
class Statm(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])
        
        Slide_Title = Text("Introduction", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("3", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)

        PYTH = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Python.svg") #FIX
        PANDA = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Pandas.svg").next_to(PYTH, RIGHT) #FIX
        OP3D = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Open3D.svg").next_to(PYTH, DOWN)
        MESH = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Meshlab.svg").next_to(OP3D, RIGHT)  #FIX SVG
        CLCP = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CloudCompare.svg").next_to(MESH, RIGHT)
        DASK = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Dask.svg").next_to(PANDA, RIGHT) #FIX
        STATM = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/STATMWhite.svg")
        ModGrp = VGroup(PYTH, PANDA, OP3D, MESH, CLCP, DASK)

        OP3DRefS = Text("[?] Zhou, Q. Y., Park, J., & Koltun, V. (2018). Open3D: A modern library for 3D data processing. arXiv preprint arXiv:1801.09847.", font_size=10).move_to([-2,-2.5,0])
        MESHRefS = Text("[?] Cignoni, P., Callieri, M., Corsini, M., Dellepiane, M., Ganovelli, F., & Ranzuglia, G. (2008, July). Meshlab: an open-source mesh processing tool. In Eurographics Italian chapter conference (Vol. 2008, pp. 129-136).", font_size=10).next_to(OP3DRefS, DOWN)
        CLCPRefS = Text("[?] CloudCompare Open Source Project, “Cloudcompare - 3D point cloud and mesh processing software,” 2020.", font_size=10).next_to(MESHRefS, DOWN)

        self.play(Write(ModGrp))
        self.wait()
        self.add(OP3DRefS, MESHRefS, CLCPRefS)
        self.wait()
class ThreeDShapes(ThreeDSlide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])
        
        Slide_Title = Text("Introduction", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("3", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)

        #SVGs of some of the shapes? Definetly of angle shape to show angle measurements. 

        PrimS = Sphere().move_to([-3,0,0]) 
        PrimS.set_color(RED)
        PrimC = Cube().next_to(PrimS, RIGHT)
        PrimC.set_color(BLUE)
        PrimCy = Cylinder().next_to(PrimC, RIGHT)
        PrimCy.set_color(GREEN)
        PrimD = Dodecahedron().next_to(PrimS, DOWN)
        PrimD.set_color(TEAL)
        PrimT = Torus().next_to(PrimD, RIGHT)
        PrimT.scale(0.5)
        PrimT.set_color(PURPLE)
        PrimCo = Cone().next_to(PrimT, RIGHT)
        PrimCo.set_color(ORANGE) 

        Prim = VGroup(PrimS, PrimC, PrimCy, PrimD, PrimT, PrimCo) #Add that they slowly rotate while talking. WIth a loop

        Ext = Text("*Extended it to include slightly more complex shapes.")

        #Add images of all shapes so far (Render as pngs without background)
        self.play(FadeIn(Prim))
        self.wait()


class OBJINFO(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        Slide_Title = Text("Statistical Data - Objects", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("8", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)
        Colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").move_to([-6.5, -3.5, 0])
        Colorlab.scale(0.5)

        OBJ_Stats1 = Table([["Object Name", "SM Baseline", "SMD 1"],
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
                           ["Convex Hull Surface", "0.006", "n"],
                           ["Point Surface Density", "0.004", "n"],
                           ["Point Volume Density", "n", "n"],
                            ]).move_to([1,0,0])

        OBJ_Stats2 = Table([["Hausdorff Distance Max", "SM Baseline", "SMD 1", "n"],
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
                           ["..........", "0.004", "n", "n"],
                           [".....", "n", "n", "n"],
                            ]).next_to(obj_stats1)
        



        OBJ_Stats1.scale(0.3)
        OBJ_Stats2.scale(0.3)

        self.add(Slide_Number, Slide_Title, Colorlab)
        self.wait()
        self.next_slide()
        self.play(Write(OBJ_Stats1))
        self.wait()
        self.next_slide()
        self.play(OBJ_Stats1.animate.shift(LEFT*2), Write(OBJ_Stats2))
        self.wait()
        self.next_slide()

        
class OBJDIST(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        Slide_Title = Text("Statistical Data - Objects", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("8", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)
        Colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").move_to([-6.5, -3.5, 0])
        Colorlab.scale(0.5)

        OP3D = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Open3D.svg").to_corner(UP + RIGHT)
        MESH = SVGMobject(f"/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Meshlab.svg").next_to(OP3D, LEFT)

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

        Haus_Frame = obj_stats2.add(obj_stats2.get_cell((1,1), color = YELLOW))
        Chamf_Frame = obj_stats2.add(obj_stats2.get_cell((6,1), color = YELLOW))

        Samp_Surface = Graph([1,2],[(1,2)], layout={1:[-2,0,0], 2:[2,0,0]})
        Ver_Arr1 = Arrow(np.array([-2,0,0]), np.array([-3,2,0]), color=ORANGE)
        Ver_Arr2 = Arrow(np.array([2,0,0]), np.array([3,2,0]), color=ORANGE)
        Face_Arr = Arrow(np.array([0,0,0]), np.array([0,3,0]), color=GREEN)

        Haus_Text = Text("Hausdorff Distance measures ...")
        Haus_Eq = MathTex(r"d_H(X,Y_i) = max \biggl\{sup_{x \in X} d(x,Y_i), sup_{y \in Y_i} d(X,y) \biggr\}").next_to(Haus_Text, DOWN)
        Haus_Eq.scale(0.7)

        Chamf_Text = Text("Chamfer Distance measures...")
        Chamf_Eq = MathTex(r"d_C(X,Y_i) = \sum_{x \in X} min_{y \in Y_i} \| x-y \|_2^2 + \sum_{y \in Y_i} min_{x \in X} \| x-y \|_2^2").next_to(Chamf_Text, DOWN)
        Chamf_Eq.scale(0.7)


        
        self.play(Create(Samp_Surface))
        self.wait()
        self.play(GrowArrow(Ver_Arr1), GrowArrow(Ver_Arr2))
        self.play(GrowArrow(Face_Arr))
        self.wait()
        self.play(Write(Haus_Eq))

class Graphs(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        Slide_Title = Text("Graphs", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("8", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)
        Colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").move_to([-6.5, -3.5, 0])
        Colorlab.scale(0.5)

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
        DeciMeanGrp = VGroup(DeciMean_Axes, DeciTit, DeciMean_Lables, DNUGraph, DUGraph, DSGraph, DRGraph)

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
        DeciMaxGrp = VGroup(DeciMaxAxes, DeciTitMax, DNUMaGraph, DUMaGraph, DSMaGraph, DRMaGraph).move_to([-5.5,-2,0])
        DeciMaxGrp.scale(0.2)
        
        VeClMaxAxes = Axes(x_range = [-1, 16, 1],
                              y_range = [0, 0.08, 0.02]
        )
        VeClTitMax = Text("Vertex Clustering - Max Error", font_size=25).next_to(VeClMaxAxes, DOWN)
        VCNUMaGraph = VeClMaxAxes.plot_line_graph(x_values = X, y_values = VCNUyMax, line_color = RED)
        VCUMaGraph = VeClMaxAxes.plot_line_graph(x_values = X, y_values = VCUyMax, line_color = GREEN)
        VCSMaGraph = VeClMaxAxes.plot_line_graph(x_values = X, y_values = VCSyMax, line_color = BLUE)
        #VCAMaGraph = VeClMaxAxes.plot_line_graph(x_values = X, y_values = VCAyMax, line_color = PURPLE)
        VCRMaGraph = VeClMaxAxes.plot_line_graph(x_values = X, y_values = VCRyMax, line_color = GOLD)
        VeClMaxGrp = VGroup (VeClMaxAxes, VeClTitMax, VCNUMaGraph, VCUMaGraph, VCSMaGraph, VCRMaGraph).move_to([-2.5,-2,0])
        VeClMaxGrp.scale(0.2)

        QEMMaxAxes = Axes(x_range = [-1, 16, 1],
                              y_range = [0, 0.08, 0.02]
        )
        QEMTitMax = Text("Quadric Error Metrics - Max Error", font_size=25).next_to(QEMMaxAxes, DOWN)
        QEMNUMaGraph = QEMMaxAxes.plot_line_graph(x_values = X, y_values = QEMNUyMax, line_color = RED)
        QEMUMaGraph = QEMMaxAxes.plot_line_graph(x_values = X, y_values = QEMUyMax, line_color = GREEN)
        QEMSMaGraph = QEMMaxAxes.plot_line_graph(x_values = X, y_values = QEMSyMax, line_color = BLUE)
        #QEMAMaGraph = QEMMaxAxes.plot_line_graph(x_values = X, y_values = QEMAyMax, line_color = PURPLE)
        QEMRMaGraph = QEMMaxAxes.plot_line_graph(x_values = X, y_values = QEMRyMax, line_color = GOLD)
        QEMMaxGrp = VGroup(QEMMaxAxes, QEMTitMax, QEMNUMaGraph, QEMUMaGraph, QEMSMaGraph, QEMRMaGraph).move_to([0.5,-2,0])
        QEMMaxGrp.scale(0.2)

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
        ECTitMax = Text("Decimation - Max Error", font_size=25).next_to(ECMaxAxes, DOWN)
        ECNUMaGraph = ECMaxAxes.plot_line_graph(x_values = X, y_values = ECNUyMax, line_color = RED)
        ECUMaGraph = ECMaxAxes.plot_line_graph(x_values = X, y_values = ECUyMax, line_color = GREEN)
        ECSMaGraph = ECMaxAxes.plot_line_graph(x_values = X, y_values = ECSyMax, line_color = BLUE)
        #ECAMaGraph = ECMaxAxes.plot_line_graph(x_values = X, y_values = ECAyMax, line_color = PURPLE)
        ECRMaGraph = ECMaxAxes.plot_line_graph(x_values = X, y_values = ECRyMax, line_color = GOLD)
        ECMaxGrp = VGroup(ECMaxAxes, ECTitMax, ECNUMaGraph, ECUMaGraph, ECSMaGraph, ECRMaGraph).move_to([6.5,-2,0])
        ECMaxGrp.scale(0.2)

        MeanTit = Text("Mean Error", font_size=20).next_to(QEMMeanGrp, UP)
        MaxTit = Text("Max Error", font_size=20).next_to(QEMMaxGrp, UP)


        self.add(Slide_Title, Slide_Number, Colorlab)
        self.play(Write(DeciMean_Axes), Write(DeciMean_Lables), Write(DeciTit))
        self.wait()
        self.play(Write(DNUGraph), run_time = 2)
        self.wait()
        self.play(Write(DUGraph), run_time = 2)
        self.wait()
        self.play(Write(DSGraph), run_time = 2)
        self.wait()
        self.play(Write(DRGraph), run_time = 2)
        self.wait()
        self.play(DeciMeanGrp.animate.scale(0.3))
        self.play(DeciMeanGrp.animate.move_to([-4,1,0]))
        self.play(Write(VerCluMeanGrp))
        self.play(VerCluMeanGrp.animate.scale(0.3))
        self.play(VerCluMeanGrp.animate.move_to([-2,1,0]))
        self.play(Write(QEMMeanGrp))
        self.play(QEMMeanGrp.animate.scale(0.3))
        self.play(QEMMeanGrp.animate.move_to([0,1,0]))
        self.play(Write(EdColMeanGrp))
        self.play(EdColMeanGrp.animate.scale(0.3))
        self.play(EdColMeanGrp.animate.move_to([5,1,0]))
        self.wait()
        self.play(Write(ECMaxGrp), Write(DeciMaxGrp), Write(VeClMaxGrp), Write(QEMMaxGrp), Write(MaxTit), Write(MeanTit))
        self.wait()


class Analysis(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        Slide_Title = Text("Analysis and Interpretation", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("8", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)
        Colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").move_to([-6.5, -3.5, 0])
        Colorlab.scale(0.5)

        STATM = SVGMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/STATMWhite.svg")

        ObDat = Text("* Provide insightful information about the object.")
        ErDet = Text("* Automatically detect errors during acquisiton or processing.").next_to(ObDat, DOWN)
        SimCh = Text("* Select optimal simplification approach based on object geometry.").next_to(ErDet, DOWN)
        UsSim = Text("* Useable on original and simplified objects.").next_to(SimCh, DOWN)

class FutureWork(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        Slide_Title = Text("Graphs", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("8", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)
        Colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").move_to([-6.5, -3.5, 0])
        Colorlab.scale(0.5)
        
        STATM = SVGMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/STATMWhite.svg")
        Impl = Text("* Implement other desired features.")
        ApSh = Text("* Apply the toolbox and investigation to CH objects.")
        GUI = Text("* Develop a GUI for non-CS users(?)")
        OpSo = Text("* Open Source when developed.")


class Citation(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        Slide_Title = Text("Citations and Contact", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("8", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)
        Colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").move_to([-6.5, -3.5, 0])
        Colorlab.scale(0.5)
        Archiving = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/Archiving.png/").move_to([4, -3.5, 0])
        Archiving.scale(0.2)
        ISNT = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/ISNT.png/").move_to([1.5, -3.5, 0])
        ISNT.scale(0.05)

        Name = Text("Markus Sebastian Bakken Storeide", font_size = 20).move_to([0,-1.5,0])
        EMail = Text("markus.s.b.storeide@ntnu.no", font_size = 20).next_to(Name, DOWN)
        NTNU = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/NTNUText.png").move_to([-3,-3.5,0])
        NTNU.scale(0.2)

        MetroRef = Text("[1] Cignoni, P., Rocchini, C., & Scopigno, R. (1998, June). Metro:\nmeasuring error on simplified surfaces. In Computer graphics\nforum (Vol. 17, No. 2, pp. 167-174). Oxford, UK and Boston,\nUSA: Blackwell Publishers.", font_size=10).move_to([-3,2.5,0])
        SimpsRef = Text("[2] Cignoni, P., Montani, C., & Scopigno, R. (1998). A comparison\nof mesh simplification algorithms. Computers & Graphics,\n22(1), 37-54.", font_size=10).next_to(MetroRef, DOWN)

        self.add(Slide_Title, Slide_Number, Colorlab, NTNU, Archiving, ISNT)
        self.play(FadeIn(Name, EMail))
        self.wait()
        self.play(FadeIn(MetroRef, SimpsRef))
        self.wait()