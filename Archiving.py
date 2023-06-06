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


class ThreeDShapes(ThreeDSlide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])
        
        Slide_Title = Text("Introduction", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("3", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)

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
                           ["Max Poly \n Surface", "0.006", "n"],
                           ["Min Poly \n Surface", "0.004", "n"],
                           ["MaxDifference", "n", "n"],
                           ["MinDifference", "n", "n"],
                           ["Rest of them", "0.004", "n"]
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
                           ["Minowski Sum", "0.004", "n", "n"],
                           ["MaxDifference", "n", "n", "n"],
                           ["MinDifference", "n", "n", "n"],
                           ["Rest of them", "0.004", "n", "n"]
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

        Haus_Text = Text("Hausdorff Distance measures ...")
        Haus_Eq = MathTex(r"d_H(X,Y_i) = max \biggl\{sup_{x \in X} d(x,Y_i), sup_{y \in Y_i} d(X,y) \biggr\}")

        Chamf_Text = Text("Chamfer Distance measures...")
        Chamf_Eq = MathTex(r"d_C(X,Y_i) = \sum_{x \in X} min_{y \in Y_i} \| x-y \|_2^2 + \sum_{y \in Y_i} min_{x \in X} \| x-y \|_2^2")
        Chamf.Eq.scale(0.7)

class Graphs(Slide):  
    def construct(self):
        self.camera.background_color = rgb_to_color([38/255, 45/255, 53/255])

        Slide_Title = Text("Graphs", font_size = 25, weight=BOLD).to_corner(UP + LEFT)
        Slide_Number = Text("8", font_size = 15, weight=BOLD).to_corner(DOWN + RIGHT)
        Colorlab = ImageMobject("/home/markus/Priv_Manim_Slides/Manim-Slides/Logos/CLsmall.png/").move_to([-6.5, -3.5, 0])
        Colorlab.scale(0.5)

        X = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        DNUy = [0.000022,
                0.000068,
                0.00013,
                0.000203,
                0.000287,
                0.000384,
                0.000489,
                0.000599,   
                0.000725,
                0.000864,
                0.001016,
                0.001183,
                0.001374,
                0.001588,
                0.001807,
                0.002001]
        
        DUy = [0.000067,
                0.000155,
                0.000277,
                0.000435,
                0.000646,
                0.000907,
                0.001222,
                0.001635,
                0.002174,
                0.002912,
                0.003831,
                0.005132,
                0.007041,
                0.009728,
                0.014257,
                0.022024]

        DSy = [0.000164,
                0.00045,
                0.000967,
                0.001558,
                0.002264,
                0.003053,
                0.003979,
                0.004888,
                0.005783,
                0.006765,
                0.0079,
                0.009215,
                0.010796,
                0.012556,
                0.01473,
                0.017454]

        DAy = []
        DRy = [0.000033,
                0.000094,
                0.000175,
                0.000272,
                0.000388,
                0.000519,
                0.000667,
                0.000838,
                0.001028,
                0.001239,
                0.001478,
                0.001749,
                0.002074,
                0.002476,
                0.002992,
                0.003734]

        VCNUy = []
        VCUy = []
        VCSy = []
        VCAy = []
        VCRUy = []

        QEMNUy = []
        QEMUy = []
        QEMSy = []
        QEMAy = []
        QEMRy = []

        CFMNUy = []
        CFMUy = []
        CFMSy = []
        CFMAy = []
        CFMRy = []

        ECNUy = []
        ECUy = []
        ECSy = []
        ECAy = []
        ECRy = []
        

        DeciMean_Axes = Axes(x_range = [-1, 16, 1],
                             y_range = [0, 0.025, 0.005]
        )
        DeciMean_Lables = DeciMean_Axes.get_axis_labels(x_label = "Simplification Stage", y_label = "Hausdorff Distance")
        DNUGraph = DeciMean_Axes.plot_line_graph(x_values = X, y_values = DNUy, line_color = RED)
        DUGraph = DeciMean_Axes.plot_line_graph(x_values = X, y_values = DUy, line_color = GREEN)
        DSGraph = DeciMean_Axes.plot_line_graph(x_values = X, y_values = DSy, line_color = BLUE)
        #DAGraph = DeciMean_Axes.plot_line_graph(x_values = X, y_values = DAy, line_color = YELLOW)
        DRGraph = DeciMean_Axes.plot_line_graph(x_values = X, y_values = DRy, line_color = GOLD)

        VerCluMean_Axes = Axes(x_range = [-1, 16, 1],
                               y_range = [0, 0.025, 0.005]
        )
        VCNUGraph = VerCluMean_Axes.plot_line_graph(x_values = X, y_values = VCNUy, line_color = RED)
        VCUGraph = VerCluMean_Axes.plot_line_graph(x_values = X, y_values = VCUy, line_color = GREEN)
        VCSGraph = VerCluMean_Axes.plot_line_graph(x_values = X, y_values = VCSy, line_color = BLUE)
        #VCAGraph = VerCluMean_Axes.plot_line_graph(x_values = X, y_values = VCAy, line_color = YELLOW)
        VCRGraph = VerCluMean_Axes.plot_line_graph(x_values = X, y_values = VCRy, line_color = GOLD)

        
        QEMMean_Axes = Axes(x_range = [-1, 16, 1],
                               y_range = [0, 0.025, 0.005]
        )
        QEMNUGraph = QEMMean_Axes.plot_line_graph(x_values = X, y_values = QEMNUy, line_color = RED)
        QEMUGraph = QEMMean_Axes.plot_line_graph(x_values = X, y_values = QEMUy, line_color = GREEN)
        QEMSGraph = QEMMean_Axes.plot_line_graph(x_values = X, y_values = QEMSy, line_color = BLUE)
        #QEMCAGraph = QEMMean_Axes.plot_line_graph(x_values = X, y_values = QEMAy, line_color = YELLOW)
        QEMRGraph = QEMMean_Axes.plot_line_graph(x_values = X, y_values = QEMRy, line_color = GOLD)

        CFMMean_Axes = Axes(x_range = [-1, 16, 1],
                               y_range = [0, 0.025, 0.005]
        )
        CFMNUGraph = CFMMean_Axes.plot_line_graph(x_values = X, y_values = CFMNUy, line_color = RED)
        CFMUGraph = CFMMean_Axes.plot_line_graph(x_values = X, y_values = CFMMUy, line_color = GREEN)
        CFMSGraph = CFMMean_Axes.plot_line_graph(x_values = X, y_values = CMFSy, line_color = BLUE)
        #CFMCAGraph = CFMMean_Axes.plot_line_graph(x_values = X, y_values = CFMAy, line_color = YELLOW)
        CFMRGraph = CFMMean_Axes.plot_line_graph(x_values = X, y_values = CFMRy, line_color = GOLD)
        
        EdColMean_Axes = Axes(x_range = [-1, 16, 1],
                              y_range = [0, 0.025, 0.005]
        )
        ECNUGraph = EdColMean_Axes.plot_line_graph(x_values = X, y_values = ECNUy, line_color = RED)
        ECUGraph = EdColMean_Axes.plot_line_graph(x_values = X, y_values = ECMUy, line_color = GREEN)
        ECSGraph = EdColMean_Axes.plot_line_graph(x_values = X, y_values = ECSy, line_color = BLUE)
        #ECCAGraph = EdColMean_Axes.plot_line_graph(x_values = X, y_values = ECAy, line_color = YELLOW)
        ECRGraph = EdColMean_Axes.plot_line_graph(x_values = X, y_values = ECRy, line_color = GOLD)

        self.add(Slide_Title, Slide_Number, Colorlab)
        self.play(Write(DeciMean_Axes), Write(DeciMean_Lables))
        self.wait()
        self.play(Write(DNUGraph), run_time = 2)
        self.wait()
        self.play(Write(DUGraph), run_time = 2)
        self.wait()
        self.play(Write(DSGraph), run_time = 2)
        self.wait()
        self.play(Write(DRGraph), run_time = 2)
        self.wait()