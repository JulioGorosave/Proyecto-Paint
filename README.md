# Proyecto-Paint
 En este branch se adjutara el proyecto paint con comandos
El código proporcionado es un programa básico de dibujo utilizando la biblioteca Pygame en Python. Aquí hay un resumen de lo que hace el código:

Importa los módulos pygame y math.
Inicializa Pygame llamando a pygame.init().
Crea una superficie de visualización de 800x600 píxeles utilizando pygame.display.set_mode((width, height)).
Define el color de fondo y llena la superficie con ese color.
Define un diccionario de colores disponibles.
Establece un color predeterminado para el fondo y otro para las líneas, y un grosor predeterminado para las líneas.
Crea las clases Triangulo, TrianguloIsosceles, TrianguloEquilatero y TrianguloEscaleno que representan diferentes tipos de triángulos.
Las clases de triángulo tienen un método draw() que dibuja el triángulo en la superficie.
Define funciones para dibujar un cuadrado, un rectángulo, un círculo y una línea en la superficie.
Hay funciones auxiliares para cambiar el color de fondo, borrar el último dibujo realizado y mostrar menús.
El programa utiliza un bucle infinito que muestra el menú, recibe la entrada del usuario y ejecuta la acción correspondiente.
Las opciones del menú permiten al usuario dibujar diferentes figuras, cambiar colores, cambiar el grosor de las líneas y borrar dibujos anteriores.
El programa utiliza la entrada del usuario para interactuar con el usuario y realizar las acciones correspondientes utilizando las funciones y clases definidas anteriormente.
El bucle infinito continúa hasta que el usuario elija la opción "exit", momento en el que se llama a pygame.quit() para cerrar la ventana y finalizar el programa.
En resumen, el código crea un programa de dibujo interactivo utilizando la biblioteca Pygame en Python, donde el usuario puede dibujar y manipular diferentes formas en una superficie de visualización.
