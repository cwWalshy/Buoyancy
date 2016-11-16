import math

def cubic_volume(length_of_side):
    return length_of_side**3
# length_of_side = 2
# cubic_volume = float(length_of_side) ** 3
# print 'The vomlume of the cube is', cubic_volume



def getdensity(mass, volumeo):
    return (mass/volumeo)

def volume_submerged(fluid_density, object_density, object_volume):
    return (object_density*object_volume)/fluid_density

def fraction_submerged(volume_submerged, object_volume):
    return (volume_submerged/object_volume)

def pyrimidal_volume(base_length,pyramid_height):
    print base_length
    print pyramid_height
    print (1/3)
    print (1.0/3.0)
    return (1.0/3.0)*base_length*pyramid_height

def spherical_volume(radius):
    return (((4/3.0) * math.pi) * radius**3)

def conical_volume(radius):
    return (((1.0 / 3.0) * math.pi) * radius ** 2)

def cylindrical_volume(radius, height):
    return (math.pi * radius ** 2) * height

def prism_volume(surface_area, length):
    return surface_area * length

def cuboid_volume(length, breadth, height):
    return length * height * breadth

