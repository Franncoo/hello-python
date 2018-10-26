# import math
# def area_circle (radius):
#     return math.pi * radius ** 2

# # data = input("Enter Raduis of  " + "a circle: ")
# # radius =float(data)

# # print("Are of a cicle {:.4f}"
# #     .format(area_circle(radius)))

# if __name__ == "__main__":
#     print("this is from geometry.py")



#def triangle_perimeter (a, b, c):
    #return a 
def triangle_perimeter (radius):
    return radius ** 2

data = input("Enter the side lengths of a triangle: ")
values = data.split(",")
#a =int(data)

 #a =float(data)
 #b =float(data)
 #c =float(data)

print("Enter the side lengths of a triangle: {}"
        .format(triangle_perimeter(radius)))
