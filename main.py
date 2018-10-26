import geometry
def area_circle (radius):
    return math.pi * radius ** 2

data = input("Enter Raduis of  " + "a circle: ")
radius =float(data)
print("Are of a cicle {:.2f}"
    .format(geometry.area_circle(radius)))