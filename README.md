# Tarea-1
“ALGORITMOS DE BUSQUEDA Y MODULARIZACION”

Este proyecto permite comparar el rendimiento de dos algoritmos de búsqueda en una lista de usuarios:

-Búsqueda Lineal: 
Busca el valor uno por uno en una lista de elementos

-Búsqueda Binaria:
Divide la lista ordenada en mitades y compara el valor con el elemento central.

El objetivo es medir la velocidad en la que podemos encontrar un usuario en una lista de 1000000 elementos.

Características 
•	Genera 1000000 usuarios aleatorios con nombre, edad e ID
•	Implementa los dos tipos de búsqueda antes mencionado para encontrar un usuario
•	Se hace uso de timeit para medir el rendimiento de cada algoritmo
•	Utiliza librerías como random, timeit y bisect

Funcionamiento del código

	El programa genera 1000000 usuarios aleatorios asignándoles un ID, nombre y edad.
	Selecciona un ID aleatorio para buscar
	Ejecuta los dos métodos de búsqueda 
	Mide el tiempo de ejecución de ambos métodos y compara los resultados 

