__RETO 4__

En este repositorio se incluye el desarrollo del reto 4. Siendo:
- 4.1. Crear una superclase llamada shape (), que es la base de las clases rectangle () y square (), definiendo los métodos compute_area y compute_perimeter in shape () y luego usando el polimorfismo para redefinir los métodos correctamente en rectángulo y en cuadrado.
- 4.2. Crear una nueva forma de la superclase Shape usando:
- 4.3. Hacerle algunos cambios y añadirle cosas a Restaurant Scenario (del Reto 3)
```mermaid
 classDiagram
    class Shape {
        + vertices: list(Point)
        + edges: list(Line)
        + inner_angles: list(float)
        + is_regular: bool
        + compute_area(self)
        + compute_perimeter(self)
        + compute_inner_angles(self)
    }

    class Point {
        + x: int
        + y: int
        + compute_distance(self, Point)
    }

    class Line {
        + start_point: Point
        + end_point: Point
        + length: float
    }

    class Triangle {
    }

    class Isosceles{
    }

    class Equilateral{
    }

    class Scalene{
    }

    class TriRectangle{
    }

    class Rectangle{
    }

    class Square{
    }

    Shape *-- Line 
    Shape *-- Point
    Triangle --|> Shape
    Isosceles --|> Triangle
    Equilateral --|> Triangle
    Scalene --|> Triangle
    TriRectangle --|> Triangle
    Rectangle --|> Shape
    Square --|> Rectangle
