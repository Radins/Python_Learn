import math as test

radius = input("Enter the circle radius: ")

perimeter = 2*test.pi*float(radius)
area = test.pi*float(radius)*float(radius)

a="{:.2f}".format(perimeter)

print ('The perimeter is ' + str(round(perimeter,2)) + ', and the area is ' + str(round(area,2)))








