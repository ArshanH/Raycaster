from data import *
from cast import *
from collisions import *
import unittest





eye_point = Point(0.0,0.0,-14.0)
ambient = Color(1.0,1.0,1.0)
light = Light(Point(-100.0,100.0,-100.0),Color(1.5,1.5,1.5))
sphere_list = [Sphere(Point(1.0,1.0,0.0),2.0,Color(0,0,1.0),Finish(.2,.4,.5,.05)),Sphere(Point(0.5,1.5,-3.0),0.5,Color(1.0,0,0),Finish(.4,.4,.5,.05)),Sphere(Point(0.5,1.5,-7.0),0.5,Color(1.0,0,0),Finish(.4,.4,.5,.05))]
cast_all_rays(-10,10,-7.5, 7.5, 1040, 768, eye_point, sphere_list,ambient,light)
