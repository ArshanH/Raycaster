import sys
import data
import commandline
import cast

try: 
    file_name = open(sys.argv[1],"r")
except:
    print "Cannot Open File"
    sys.exit()

arg_list = commandline.cmd_line(sys.argv)
def read_file(file_name):
    count = 0
    list_of_spheres = []
    for line in file_name:
        count += 1
        a = line.split()
        if len(a) != 11:
            print "malformed sphere on line ", count, " ...skipping"
        else:
                try:
                    sphere_center = data.Point(float(a[0]),float(a[1]),float(a[2]))
                    sphere_radius = float(a[3])
                    sphere_color = data.Color(float(a[4]),float(a[5]),float(a[6]))
                    sphere_finish = data.Finish(float(a[7]),float(a[8]),float(a[9]),float(a[10]))
                    sphere_complete = data.Sphere(sphere_center,sphere_radius,sphere_color,sphere_finish)
                    list_of_spheres.append(sphere_complete)
                except:
                    print "malformed sphere on line ", count, "...skipping"
    return list_of_spheres
list_of_spheres = read_file(file_name)
cast.cast_all_rays(arg_list[1],arg_list[2],arg_list[3],arg_list[4],int(arg_list[5]),int(arg_list[6]),arg_list[0],list_of_spheres,arg_list[8],arg_list[7])

