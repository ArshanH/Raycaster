import data
import math

def scale_vector(vector, scalar):
    x = vector.x * scalar 
    y = vector.y * scalar
    z = vector.z * scalar
    return data.Vector(x,y,z)
def dot_vector(vector1,vector2):
    x = vector1.x * vector2.x
    y = vector1.y * vector2.y
    z = vector1.z * vector2.z
    return (x + y + z)
def length_vector(vector):
    x = vector.x ** 2
    y = vector.y ** 2
    z = vector.z ** 2
    return math.sqrt(x + y + z)
def normalize_vector(vector):
    b = length_vector(vector)
    x = vector.x / b
    y = vector.y / b
    z = vector.z / b
    return data.Vector(x,y,z)
def difference_point(point1,point2):
    x = point2.x - point1.x
    y = point2.y - point1.y
    z = point2.z - point1.z
    return data.Vector(x,y,z)
def difference_vector(vector1,vector2):
    x = vector2.x - vector1.x
    y = vector2.y - vector1.y
    z = vector2.z - vector1.z
    return data.Vector(x,y,z)
def translate_point(point,vector):
    x = point.x + vector.x
    y = point.y + vector.y
    z = point.z + vector.z
    return data.Point(x,y,z)
def vector_from_to(from_point,to_point):
    x = to_point.x - from_point.x
    y = to_point.y - from_point.y
    z = to_point.z - from_point.z
    return data.Vector(x,y,z)

