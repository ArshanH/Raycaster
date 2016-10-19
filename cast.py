import collisions
import vector_math
import math
import data
def distance(point_1,point_2):
    return vector_math.length_vector(vector_math.vector_from_to(point_1,point_2))

def cast_ray(ray,sphere_list,ambient,light,point):
    a = collisions.find_intersection_points(sphere_list,ray)
    if a == []:
        return data.Color(1.0,1.0,1.0)
    sphere_look = a[0]
    for x in a:
        if distance(ray.pt,x[1]) < distance(ray.pt,sphere_look[1]):
            sphere_look = x
    
    red = sphere_look[0].color.r * sphere_look[0].finish.ambient * ambient.r
    green = sphere_look[0].color.g * sphere_look[0].finish.ambient * ambient.g
    blue = sphere_look[0].color.b * sphere_look[0].finish.ambient * ambient.b

    n = collisions.sphere_normal_at_point(sphere_look[0],sphere_look[1])
    pe=vector_math.translate_point(sphere_look[1],vector_math.scale_vector(n,.01))
    visible_ray = data.Ray(pe,vector_math.vector_from_to(pe,light.point))
    ldir = vector_math.normalize_vector(visible_ray.dir)
    visible = vector_math.dot_vector(ldir,n)
    n = collisions.sphere_normal_at_point(sphere_look[0],sphere_look[1])
    ldir_dot_n = vector_math.dot_vector(ldir,n)
    reflection_vector = vector_math.difference_vector(vector_math.scale_vector(n,ldir_dot_n *2),ldir)
    vdir = vector_math.normalize_vector(vector_math.vector_from_to(point,pe))
    specular_intensity = vector_math.dot_vector(reflection_vector,vdir)
    if visible > 0:
        if collisions.find_intersection_points(sphere_list,visible_ray) == []:
            red += (visible * light.color.r * sphere_look[0].color.r * sphere_look[0].finish.diffuse)
            green += (visible * light.color.g * sphere_look[0].color.g * sphere_look[0].finish.diffuse)
            blue += (visible * light.color.b * sphere_look[0].color.b * sphere_look[0].finish.diffuse)
    if specular_intensity > 0:
        spec_intensity_calc = specular_intensity ** (1 / sphere_look[0].finish.roughness)
        red += light.color.r * sphere_look[0].finish.specular * spec_intensity_calc
        green += light.color.g * sphere_look[0].finish.specular * spec_intensity_calc
        blue += light.color.b * sphere_look[0].finish.specular * spec_intensity_calc
    return data.Color(red,green,blue)



def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambient,light):
    try:
        fh = open("image.ppm","w")
    except: 
        print "Cannot open image.ppm"        
    fh.write("P3")
    fh.write(str(width)+ ' ' + str(height) + '\n')
    fh.write("255\n")
    delta_x = (max_x - min_x)/(float(width))
    delta_y = (max_y - min_y)/(float(height))
    for y in range(height):
        for x in range(width):
            x_val = min_x + x * delta_x
            y_val = max_y - y * delta_y
            dir = vector_math.vector_from_to(eye_point,data.Point(x_val,y_val,0))
            r = data.Ray(eye_point,dir)
            color = cast_ray(r,sphere_list,ambient,light,eye_point)
            a = min(int(color.r * 255),255)
            b = min(int(color.g * 255),255)
            c = min(int(color.b * 255),255)
            fh.write(str(a)+" "+str(b)+" "+str(c)+"\n")


