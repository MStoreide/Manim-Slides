from manim import *
from manim_slides import Slide, ThreeDSlide

#Should also have a packup Powerpoint just in case

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