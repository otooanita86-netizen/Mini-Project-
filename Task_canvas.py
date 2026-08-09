class Something:


    def get_String(self):
        self.string = input("Enter a string: ")


    def print_string(self):
        print(self.string.upper())


my_string = Something()

my_string.get_String()
my_string.print_string()


class Rectangle:

    def Length(self):
        self.length = float(input("Enter the length: "))

    def width(self):
        self.width = float(input("Enter the width: "))

    def Area(self):
        area = self.length * self.width
        print("The area is:", area)
rectangle = Rectangle()


rectangle.Length()
rectangle.width()
rectangle.Area()



#Inheritance

     