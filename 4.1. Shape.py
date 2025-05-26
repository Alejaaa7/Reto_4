# 1. Create a superclass called Shape(), which is the base of the classes 
# Reactangle() and Square(), define the methods compute_area and 
# compute_perimeter in Shape() and then using polymorphism redefine the 
# methods properly in Rectangle and in Square.
#----------------------------------------------------------------------#

# Se crea la superclase Shape

class Shape:
    def __init__(self):
        pass

    def compute_area(self):
        raise NotImplementedError("Subclasees must implement compute_area()")
    
    def compute_perimeter(self):
        raise NotImplementedError("Subclasses must implement compute_perimeter()")
    
# Se crea la subclase Rectangle que hereda de Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    # Setter

    def set_width(self, width):
        if width >= 0:
            self.__width = width
            return True
        
    def set_height(self, height):
        if height >= 0:
            self.__height = height
            return True
        
    # Getter

    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height

# Implementación de los métodos compute_area y compute_perimeter:
    
    def compute_area(self):
        return self.__width * self.__height
    
    def compute_perimeter(self):
        return 2 * (self.__width + self.__height)
    
class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.__side = side

    # Setter

    def set_side(self, side):
        if side >= 0:
            self.__side = side 
            return True
        
    # Getter

    def get_side(self):
        return self.__side
    
# Implementación de los métodos compute_area y compute_perimeter:

    def compute_area(self):
        return self.__side ** 2
    
    def compute_perimeter(self):
        return self.__side * 4
    

#Ejemplo de uso 

rectangulo1 = Rectangle(2, 3)
cuadrado1 = Square(2)

print(f"El area del rectangulo es: {rectangulo1.compute_area()}")
print(f"El area del cuadrado es: {cuadrado1.compute_area()}")

print(f"El perímero del rectangulo es : {rectangulo1.compute_perimeter()}")
print(f"El perímero del cuadrado es : {cuadrado1.compute_perimeter()}")
