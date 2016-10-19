from data import *
import vector_math
import math

def sphere_intersection_point(ray, sphere) : 
   a = ray.dir.x **2 + ray.dir.y **2 + ray.dir.z **2
   b = 2 * ( (ray.pt.x - sphere.center.x) * (ray.dir.x) + (ray.pt.y - sphere.center.y) * (ray.dir.y) + (ray.pt.z - sphere.center.z) * (ray.dir.z) )
   c =   ( (ray.pt.x - sphere.center.x) **2 + (ray.pt.y - sphere.center.y) **2 + (ray.pt.z - sphere.center.z) **2 ) - sphere.radius **2
   
   if (b**2 >= 4*a*c) :
      t = (- b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
      t2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
      if (t >= 0 and t2 >= 0) :
	 tf = min(t, t2)
	 intX = ray.pt.x + ray.dir.x * tf
	 intY = ray.pt.y + ray.dir.y * tf
	 intZ = ray.pt.z + ray.dir.z * tf
	 return Point(intX, intY, intZ)
      elif (t < 0 and t2 < 0) :
         return None
      elif (t >= 0 and t2 < 0 or t2 >= 0 and t < 0) :
	 tf = max(t, t2)
	 intX = ray.pt.x + ray.dir.x * tf
	 intY = ray.pt.y + ray.dir.y * tf
	 intZ = ray.pt.z + ray.dir.z * tf
	 return Point(intX, intY, intZ)
   else :
      return None
   

def find_intersection_points(sphere_list,ray):
    pair_list = []
    for sphere in sphere_list :
        pt = sphere_intersection_point(ray, sphere) 
        if pt :
            pair_list.append((sphere, pt))
    return pair_list
    
def sphere_normal_at_point(sphere,point):
	a = vector_math.vector_from_to(sphere.center,point)
	return vector_math.normalize_vector(a)
