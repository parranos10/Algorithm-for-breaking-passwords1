# Algorithm-for-breaking-passwords1
work in class 

Este programa en Python implementa un método básico de **fuerza bruta** para encontrar una contraseña. La técnica consiste en probar todas las combinaciones posibles de letras hasta encontrar la correcta.


abecedario: cadena de caracteres que contiene las letras usadas para generar combinaciones.
contraseña: clave que el programa intenta adivinar (`"agpd"`).
intentos: contador de intentos realizados.
crackeado: variable booleana que indica si la contraseña fue encontrada.
tiempo: almacena el tiempo inicial de ejecución.

El programa prueba combinaciones de letras de forma progresiva:

Se recorre el abecedario probando cada letra individual.

Se utilizan dos bucles anidados para generar pares de letras.

Se agregan tres niveles de bucles para formar combinaciones más largas.

Se generan combinaciones de cuatro letras, que es la longitud de la contraseña objetivo.

En cada intento:

Se crea una combinación ("intento")
Se incrementa el contador
Se compara con la contraseña

Cuando el programa encuentra la contraseña:

Cambia el valor de "crackeado" a "True"
Detiene los bucles usando "break"
Evita seguir ejecutando intentos innecesarios

Al finalizar, el programa muestra:

La cantidad de intentos realizados
El tiempo total de ejecución


