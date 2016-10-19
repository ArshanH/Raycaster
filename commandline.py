import sys
import data
import cast

def cmd_line(command_arguments):
    eye = data.Point(0,0,-14)
    min_x = -10.0
    max_x = 10.0
    min_y = -7.5
    max_y = 7.5
    width = 1024.0
    height = 768.0
    light = data.Light(data.Point(-100.0,100.0,-100.0),data.Color(1.5,1.5,1.5))
    ambient = data.Color(1.0,1.0,1.0)
    for idx, arg in enumerate(command_arguments[2:]):
        if arg == "-eye":
            try: 
                eye = data.Point(float(command_arguments[idx + 3]),float(command_arguments[idx + 4]),float(command_arguments[idx + 5]))
            except:
                print "argument error in eye"
                sys.exit()
        elif arg == "-view":
            try:
                min_x = float(command_arguments[idx + 3])
                max_x = float(command_arguments[idx + 4])
                min_y = float(command_arguments[idx + 5])
                max_y = float(command_arguments[idx + 6])
                width = float(command_arguments[idx + 7])
                height = float(command_arguments[idx + 8])
            except:
                print "argument error in view"
                sys.exit()
        elif arg == "-light":
            try:
                light_point = data.Point(float(command_arguments[idx + 3]),float(command_arguments[idx + 4]),float(command_arguments[idx + 5]))
                light_color = data.Color(float(command_arguments[idx + 6]),float(command_arguments[idx + 7]),float(command_arguments[idx + 8]))
                light = data.Light(light_point,light_color)
            except:
                print "argument error in light"
                sys.exit()
        elif arg == "-ambient":
            try:
                ambient = data.Color(float(command_arguments[idx + 3]),float(command_arguments[idx + 4]),float(command_arguments[idx + 5]))
            except:
                print "argument error in ambient"
        else:
            try:
                test_float = float(arg)
            except:
                print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"
    arg_list = [eye, min_x, max_x, min_y, max_y, width, height, light, ambient]
    return arg_list





