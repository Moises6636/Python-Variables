#Define una variable de cada tipo de primitivo

Edad = 27
Estatura = 1.80
Booleano = True
cadena = "La informacion requerida:"

#Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable

resultado_concatenacion = cadena + "Edad: " + str(Edad) + " Estatura: " + str(Estatura) + " Valor: " +str(Booleano)

#Impresion de la concatenacion

print(resultado_concatenacion)


""" Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo """
"""int / Integer: Int puede almacenar todos los valores enteros. 
Este tipo de datopuede ser de cualquier tamaño. No hay límite de tamaño.
float: el flotante incluye todos los valores de punto flotante. 
Tampoco hay restricciones sobre el tamaño de un número de punto flotante."""

#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable

n = 5

suma_pares = n * (n + 1)

print("La suma de los primeros", n, "números pares es:", suma_pares)


