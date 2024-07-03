# Write a Python program that calculates the area of a circle based on the radius entered by the user.
def area_of_circle(radius):
    return 3.14 * radius ** 2
radius = int(input("Enter the radius of the circle: "))
print("The area of the circle is: ", area_of_circle(radius))