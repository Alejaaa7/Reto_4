# 2. Using the classes Point() and Line() define a new super-class Shape().

# Se incluyen las dos clases Point y line que se usaron en los anteriores
# retos: 

# Se empieza creando Point, porque Line la necesita:


from math import degrees, atan2, acos

class Point:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
    
    def compute_distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
    
# Ahora, se crea la clase Line:

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.compute_length()
#        self.slope = self.compute_slope()

    def compute_length(self):
        return self.start_point.compute_distance(self.end_point)
    
#    def compute_slope(self):
#        dx = self.end_point.x - self.start_point.x
#        dy = self.end_point.y - self.start_point.y

#        return degrees(atan2(dy, dx))
    
# Se crea la nueva superclase Shape:

class Shape:
    def __init__(self):
        self.is_regular = None
        self.vertices = []
        self.edges =  []
        self.inner_angles = []

    def check_if_is_regular(self):
        if not self.edges or not self.inner_angles:
            return False
        edge_lengths = [edge.length for edge in self.edges]
        if all(l == edge_lengths[0] for l in edge_lengths) and \
        all(angle == self.inner_angles[0] for angle in self.inner_angles):
            return True
        return False

    def compute_area(self):
        raise NotImplementedError("Subclasses must implement compute_area()")
    
    def compute_perimeter(self):
        raise NotImplementedError("Subclasses must implement compute_perimeter()")
    
    def compute_inner_angles(self):
        raise NotImplementedError("Subclasses must implement compute_inner_angles()")
    
# Se empieza creando la subclase Triangle:

class Triangle(Shape):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__()
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.vertices = [point1, point2, point3]
        self.edges = [
            Line(point1, point2),
            Line(point2, point3),
            Line(point3, point1),
        ]
        # estos se van a calcular en funciones aparte:
        self.inner_angles = self.compute_inner_angles()
        self.is_regular = self.check_if_is_regular()

    def compute_area(self):
    # Se va a calcular el area usando la formula de Heron, porque en 
    # este caso es más sencillo así:
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length

        semiperimeter = (a + b + c) / 2
        area = (semiperimeter * (semiperimeter - a) * (semiperimeter - b) \
                * (semiperimeter - c)) ** 0.5
        return area
    
    def compute_perimeter(self):
        return self.edges[0].length + self.edges[1].length + self.edges[2].length

    def compute_inner_angles(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length

        angle_A = degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c )))
        angle_B = degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c )))
        angle_C = degrees(acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b )))
    
        return [angle_A, angle_B, angle_C]
    
# Ahora empezamos a crear las subclases de Triangle:

class Isosceles(Triangle):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__(point1, point2, point3)
        if not self.is_isosceles():
            raise ValueError("The points do not form an isosceles triangle.")
        
    def is_isosceles(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        
        return a == b or b == c or c == a 
    
class Equilateral(Triangle):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__(point1, point2, point3)
        if not self.is_equilateral():
            raise ValueError("The points do not form an equilateral triangle.")
    
    def is_equilateral(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length

        return a == b and b == c and c == a

class Scalene(Triangle):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__(point1, point2, point3)
        if not self.is_scalene():
            raise ValueError("The points do not form an scalene triangle.")
        
    def is_scalene(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length

        return a != b and b != c and c != a
    
# Ahora sí se crea la subclase Rectangle:

class Rectangle(Shape):
    # Esta vez, para variar, se creará con líneas, como en el Reto 3:
    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point):
        super().__init__()
        self.vertices = [point1, point2, point3, point4]
        self.edges = [
            Line(point1, point2),
            Line(point2, point4),
            Line(point4, point3),
            Line(point3, point1)
        ]
        self.inner_angles = self.compute_inner_angles()
        self.is_regular = self.check_if_is_regular()

    def compute_area(self):
        return self.edges[0].length * self.edges[1].length
    
    def compute_perimeter(self):
        return self.edges[0].length + self.edges[1].length \
                + self.edges[2].length + self.edges[3].length
    
    def compute_inner_angles(self):
        return [90, 90, 90, 90] # porque ya sabemos que es un rectángulo
    
# Ahora creamos Square:

class Square(Rectangle):
    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point):
        super().__init__(point1, point2, point3, point4)
        if not self.is_a_square():
            raise ValueError("The points do not form a Square.")
    def is_a_square(self):
        return all(edge.length == self.edges[0].length for edge in self.edges)

        
# Ahora para probarlo:

print("Probando clases base:")
p1 = Point(0, 0)
p2 = Point(3, 4)
print("Distancia entre puntos:", p1.compute_distance(p2))

l1 = Line(p1, p2)
print("Longitud de la línea:", l1.length) 

print("Probando Triangle:")
A = Point(0, 0)
B = Point(4, 0)
C = Point(0, 3)
tri = Triangle(A, B, C)
print("Perímetro:", tri.compute_perimeter())
print("Área:", tri.compute_area())
print("Ángulos:", tri.inner_angles)

print("Probando Isosceles:")
iso = Isosceles(Point(0, 0), Point(2, 3), Point(4, 0))
print("Área Isósceles:", iso.compute_area()) 
print("Perímetro Isósceles:", iso.compute_perimeter())
print("Ángulos Isósceles:", iso.inner_angles)

print("Probando Equilateral:")
eq = Equilateral(Point(0, 0), Point(1, 3 ** 0.5), Point(2, 0))
print("Área Equilátero:", eq.compute_area())
print("Perímetro Equilátero:", eq.compute_perimeter())
print("Ángulos Equilátero:", eq.inner_angles) 
print("¿Es regular?", eq.is_regular)  

print("Probando Scalene:")
sca = Scalene(Point(0, 0), Point(3, 0), Point(2, 2))
print("Área Escaleno:", sca.compute_area())
print("Perímetro Escaleno:", sca.compute_perimeter())
print("Ángulos Escaleno:", sca.inner_angles)  

print("Probando Rectangle:")
R1 = Point(0, 0)
R2 = Point(0, 2)
R3 = Point(4, 0)
R4 = Point(4, 2)
rect = Rectangle(R1, R2, R4, R3)
print("Área:", rect.compute_area())  
print("Perímetro:", rect.compute_perimeter()) 
print("Ángulos:", rect.inner_angles)   

print("Probando Square:")
sq = Square(Point(0, 0), Point(0, 2), Point(2, 0), Point(2, 2)) 
print("Área cuadrado:", sq.compute_area())           
print("Perímetro cuadrado:", sq.compute_perimeter())
print("¿Es regular?", sq.is_regular)
