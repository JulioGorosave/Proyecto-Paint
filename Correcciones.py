import pygame
import math
# Inicializar Pygame
pygame.init()
# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
WIDTH = 800
HEIGHT = 600
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
BAKCKGROUND_COLOR = (255, 23, 100)
SURFACE.fill(BAKCKGROUND_COLOR)
# Colores disponibles
colors = {
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "amarillo": (255, 255, 0)
}
# Color predeterminado para el fondo
current_background_color = BAKCKGROUND_COLOR
# Color predeterminado para las líneas
current_color = colors["rojo"]
# Grosor predeterminado para las líneas
current_line_thickness = 1
# Lista de dibujos realizados
drawings = []
class Triangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        pass
class TrianguloIsosceles(Triangulo):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height
    def draw(self):
        point1 = (self.x, self.y)
        point2 = (self.x + self.base, self.y)
        point3 = (self.x + self.base / 2, self.y - self.height)
        pygame.draw.polygon(SURFACE, current_color, [point1, point2, point3], current_line_thickness)
        pygame.display.flip()
        # Agregar el dibujo a la lista
        drawings.append(("triangle_isosceles", self.x, self.y, self.base, self.height))
class TrianguloEquilatero(Triangulo):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side
    def draw(self):
        height = self.side * math.sqrt(3) / 2
        point1 = (self.x, self.y)
        point2 = (self.x + self.side, self.y)
        point3 = (self.x + self.side / 2, self.y - height)
        pygame.draw.polygon(SURFACE, current_color, [point1, point2, point3], current_line_thickness)
        pygame.display.flip()
        # Agregar el dibujo a la lista
        drawings.append(("triangle_equilateral", self.x, self.y, self.side))
class TrianguloEscaleno(Triangulo):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1)
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def draw(self):
        point1 = (self.x, self.y)
        point2 = (self.x2, self.y2)
        point3 = (self.x3, self.y3)
        pygame.draw.polygon(SURFACE, current_color, [point1, point2, point3], current_line_thickness)
        pygame.display.flip()
        # Agregar el dibujo a la lista
        drawings.append(("triangle_scalene", self.x, self.y, self.x2, self.y2, self.x3, self.y3))
def draw_square(x, y):
    pygame.draw.rect(SURFACE, current_color, pygame.Rect(x, y, 100, 100), current_line_thickness)
    pygame.display.flip()
    # Agregar el dibujo a la lista
    drawings.append(("square", x, y))
def draw_rectangle(x, y):
    pygame.draw.rect(SURFACE, current_color, pygame.Rect(x, y, 100, 200), current_line_thickness)
    pygame.display.flip()
    # Agregar el dibujo a la lista
    drawings.append(("rectangle", x, y))
def draw_circle(x, y, radius):
    if radius <= 0:
        print("El radio debe ser mayor que 0.")
        return
    pygame.draw.circle(SURFACE, current_color, (x, y), radius, current_line_thickness)
    pygame.display.flip()
    # Agregar el dibujo a la lista
    drawings.append(("circle", x, y, radius))
def draw_line(x1, y1, x2, y2):
    pygame.draw.line(SURFACE, current_color, (x1, y1), (x2, y2), current_line_thickness)
    pygame.display.flip()
    # Agregar el dibujo a la lista
    drawings.append(("line", x1, y1, x2, y2))
def cambiar_fondo(color):
    global current_background_color
    current_background_color = color
    SURFACE.fill(current_background_color)
    pygame.display.flip()
def borrar_ultimo_dibujo():
    if drawings:
        last_drawing = drawings.pop()
        SURFACE.fill(current_background_color)
        for drawing in drawings:
            if drawing[0] == "square":
                draw_square(drawing[1], drawing[2])
            elif drawing[0] == "rectangle":
                draw_rectangle(drawing[1], drawing[2])
            elif drawing[0] == "circle":
                draw_circle(drawing[1], drawing[2], drawing[3])
            elif drawing[0] == "line":
                draw_line(drawing[1], drawing[2], drawing[3], drawing[4])
            elif drawing[0] == "triangle_isosceles":
                triangle = TrianguloIsosceles(drawing[1], drawing[2], drawing[3], drawing[4])
                triangle.draw()
            elif drawing[0] == "triangle_equilateral":
                triangle = TrianguloEquilatero(drawing[1], drawing[2], drawing[3])
                triangle.draw()
            elif drawing[0] == "triangle_scalene":
                triangle = TrianguloEscaleno(drawing[1], drawing[2], drawing[3], drawing[4], drawing[5], drawing[6])
                triangle.draw()
        pygame.display.flip()
        print("Último dibujo borrado.")
    else:
        print("No hay dibujos para borrar.")
# Función para mostrar el menú
def show_menu():
    print("Selecciona una opción:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")
    print("4. Línea")
    print("5. Dibujar triángulo")
    print("6. Cambiar color de las líneas")
    print("7. Cambiar fondo de pantalla")
    print("8. Borrar último dibujo")
    print("9. Grosor de líneas")
# Función para mostrar el menú de tipos de triángulos
def show_triangle_menu():
    print("Selecciona un tipo de triángulo:")
    print("1. Triángulo isósceles")
    print("2. Triángulo equilátero")
    print("3. Triángulo escaleno")
# Esperar a que el usuario cierre la ventana
while True:
    show_menu()  # Mostrar el menú
    cmd = input("Selecciona una opción (1-9), o escribe 'exit' para salir: ")
    if cmd == "exit":
        pygame.quit()
        break
    elif cmd == "1":
        x = int(input("Ingresa la coordenada x del cuadrado: "))
        y = int(input("Ingresa la coordenada y del cuadrado: "))
        draw_square(x, y)
    elif cmd == "2":
        x = int(input("Ingresa la coordenada x del rectángulo: "))
        y = int(input("Ingresa la coordenada y del rectángulo: "))
        draw_rectangle(x, y)
    elif cmd == "3":
        x = int(input("Ingresa la coordenada x del círculo: "))
        y = int(input("Ingresa la coordenada y del círculo: "))
        while True:
            radius = int(input("Ingresa el radio del círculo: "))
            if radius > 0:
                break
            else:
                print("El radio debe ser mayor que 0.")
        draw_circle(x, y, radius)
    elif cmd == "4":
        x1 = int(input("Ingresa la coordenada x del punto A: "))
        y1 = int(input("Ingresa la coordenada y del punto A: "))
        x2 = int(input("Ingresa la coordenada x del punto B: "))
        y2 = int(input("Ingresa la coordenada y del punto B: "))
        draw_line(x1, y1, x2, y2)
    elif cmd == "5":
        show_triangle_menu()
        triangle_option = input("Selecciona una opción para dibujar un triángulo (1-3): ")
        if triangle_option == "1":
            x = int(input("Ingresa la coordenada x del triángulo isósceles: "))
            y = int(input("Ingresa la coordenada y del triángulo isósceles: "))
            base = int(input("Ingresa la base del triángulo isósceles: "))
            HEIGHT = int(input("Ingresa la altura del triángulo isósceles: "))
            triangle = TrianguloIsosceles(x, y, base, HEIGHT)
            triangle.draw()
        elif triangle_option == "2":
            x = int(input("Ingresa la coordenada x del triángulo equilátero: "))
            y = int(input("Ingresa la coordenada y del triángulo equilátero: "))
            side = int(input("Ingresa el tamaño del lado del triángulo equilátero: "))
            triangle = TrianguloEquilatero(x, y, side)
            triangle.draw()
        elif triangle_option == "3":
            x1 = int(input("Ingresa la coordenada x del punto A: "))
            y1 = int(input("Ingresa la coordenada y del punto A: "))
            x2 = int(input("Ingresa la coordenada x del punto B: "))
            y2 = int(input("Ingresa la coordenada y del punto B: "))
            x3 = int(input("Ingresa la coordenada x del punto C: "))
            y3 = int(input("Ingresa la coordenada y del punto C: "))
            triangle = TrianguloEscaleno(x1, y1, x2, y2, x3, y3)
            triangle.draw()
        else:
            print("Opción inválida. Volviendo al menú principal.")
    elif cmd == "6":
        print("Selecciona un color para las líneas:")
        print("1. Rojo")
        print("2. Verde")
        print("3. Azul")
        print("4. Amarillo")
        color_option = input("Selecciona una opción para cambiar el color (1-4): ")
        if color_option == "1":
            current_color = colors["rojo"]
        elif color_option == "2":
            current_color = colors["verde"]
        elif color_option == "3":
            current_color = colors["azul"]
        elif color_option == "4":
            current_color = colors["amarillo"]
        else:
            print("Opción inválida. Se utilizará el color predeterminado.")
    elif cmd == "7":
        print("Selecciona un color para el fondo:")
        print("1. Rojo")
        print("2. Verde")
        print("3. Azul")
        print("4. Amarillo")
        color_option = input("Selecciona una opción para cambiar el color de fondo (1-4): ")
        if color_option == "1":
            cambiar_fondo((255, 0, 0))
        elif color_option == "2":
            cambiar_fondo((0, 255, 0))
        elif color_option == "3":
            cambiar_fondo((0, 0, 255))
        elif color_option == "4":
            cambiar_fondo((255, 255, 0))
        else:
            print("Opción inválida. Se utilizará el color de fondo predeterminado.")
    elif cmd == "8":
        borrar_ultimo_dibujo()
    elif cmd == "9":
        thickness = int(input("Ingresa el grosor de las líneas: "))
        current_line_thickness = thickness
    else:
        print("Opción inválida. Inténtalo nuevamente.")

