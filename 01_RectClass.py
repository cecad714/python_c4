class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

length1 = float(input("Enter length for Rectangle 1: "))
breadth1 = float(input("Enter breadth for Rectangle 1: "))
rectangle1 = Rectangle(length1, breadth1)

length2 = float(input("Enter length for Rectangle 2: "))
breadth2 = float(input("Enter breadth for Rectangle 2: "))
rectangle2 = Rectangle(length2, breadth2)

print("Area of Rectangle 1:", rectangle1.area())
print("Area of Rectangle 2:", rectangle2.area())

if rectangle1.area() > rectangle2.area():
    print("Rectangle 1 has a larger area.")
elif rectangle1.area() < rectangle2.area():
    print("Rectangle 2 has a larger area.")
else:
    print("Both rectangles have the same area.")
