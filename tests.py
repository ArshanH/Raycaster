import unittest
import data
import vector_math
import math
import collisions
import cast
import ray_caster
class TestData(unittest.TestCase):
   def test_cast_ray_1(self):
        pt = data.Point(0,0,0)
        dir = data.Vector(0,0,1)
        ray = data.Ray(pt,dir)
        center_1 = data.Point(12,0,0)
        center_2 = data.Point(0,5,0)
        center_3 = data.Point(5,0,0)
        center_4 = data.Point(50,0,0)
        radius = 2
        color = data.Color(1,0,.1)
        finish = data.Finish(1,.2,1,1)
        light = data.Light(data.Color(1.5,1.5,1.5),data.Point(0,0,0))
        eye_point = data.Point(1,1,1)
        sphere_list = [data.Sphere(center_1,radius,color,finish),data.Sphere(center_2,radius,color,finish),data.Sphere(center_3,radius,color,finish),data.Sphere(center_4,radius,color,finish)]
        test_cast_ray_1 = cast.cast_ray(ray,sphere_list,finish,light,eye_point)
        self.assertTrue(test_cast_ray_1 == data.Color(1,1,1))
    def test_cast_ray_2(self):
        pt = data.Point(0,0,0)
        dir = data.Vector(0,1,0)
        ray = data.Ray(pt,dir)
        center_1 = data.Point(0,0,5)
        center_2 = data.Point(0,5,0)
        center_3 = data.Point(5,0,0)
        radius = 2
        color = data.Color(0,1,0)
        color_1 = data.Color(0,0,0)
        finish = data.Finish(1,1,1,1)
        light = data.Light(data.Point(1,1,1),data.Color(1,1,1))
        eye_point = data.Point(1,1,1)
        ambient = data.Color(1,1,1)
        sphere_list = [data.Sphere(center_1,radius,color_1,finish),data.Sphere(center_2,radius,color,finish),data.Sphere(center_3,radius,color_1,finish)]
        test_cast_ray_2 = cast.cast_ray(ray,sphere_list,ambient,light,eye_point)
        self.assertTrue(test_cast_ray_2 == data.Color(0.328870320968,2.14399924358,0.328870320968))
## assignment 5 processing files

        
if __name__ == '__main__':
    unittest.main()

