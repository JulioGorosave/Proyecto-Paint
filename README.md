# Proyecto 'Paint' a base de comandos en consola.

## Informacion general.

El archivo que se debe correr es 'correcciones.py'.

Este codigo permite hacer lineas, cuadrados, rectangulos, circulos, tres tipos de triangulos distintos, cambiar el color del fondo asi como el color del dibujo, tambien da la opcion de deshacer el ultimo comando ejecutado.

En cuanto se corre el codigo se muestran los comandos disponibles y la seleccion se efectua en base a la enumeracion que muestra el menu.

Los colores soportados por este codigo son: rojo, verde, azul y amarillo.

## Explicacion del codigo. 

Se genera la interfaz grafica con dimensiones de 800 x 600 pixeles y se le da un color al fondo.

Se muestran los colores soportados.

Se crean variables para el color del fondo, el color del dibujo y el grosor del dibujo, asi como una lista para guardar los dibujos realizados.

A continuacion se crea la clase triangulo que sera la clase padre para los tres distintos tipos de triangulos soportados, siendo estos el triangulo isosceles, equilatero y escaleno.

Las clases piden como parametros los puntos de los vertices de dichos triangulos y en estas mismas clases se hacen los calculos para la creacion de la figura seleccionada con las configuraciones de color y grosor previamente seleccionadas desde el menu principal.

Despues se tienen funciones para hacer cuadrados y rectangulos, estos tienen como entrada de parametros el punto de origen para la figura.

La funcion circulo requiere que se le de el punto de origen y el radio de la circunferencia, este debe ser un valor positivo de lo contrario no se generara nada.

Tambien esta la funcion para crear una linea solicitando las coordenadas de inicio y fin.

El cambio del color de fondo se efectua con una funcion que manda a llamar la variable que contiene el color del fondo y la cambia por otro color que el usuario elija.

La funcion para borrar el ultimo dibujo revisa cual es el ultimo objeto agragado en la lista que guarda los dibujos realizados y lo quita de la lista.

Se tienen dos funciones que muestran tanto el menu principal como la seleccion del tipo de triangulo que se desea dibujar.
