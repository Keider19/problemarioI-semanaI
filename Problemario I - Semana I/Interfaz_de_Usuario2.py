#EJERCICIO 2 A RESOLVER:
#Todo sistema de análisis comienza con una interfaz de usuario. Tu
#tarea es crear un programa que solicite al usuario su nombre y su cargo (ej. "Analista"), y
#luego imprima un mensaje de bienvenida personalizado que diga: "Acceso concedido:
#Bienvenido, [Nombre], al sistema de [Cargo]". Este ejercicio evalúa tu capacidad para
#capturar entradas (input) y concatenar cadenas de texto.
#Pista: Puedes unir textos de dos formas: usando el símbolo + (concatenación) o usando
#comas dentro del print(). Sin embargo, para un nivel profesional, intenta usar f-strings
#(poniendo una f antes de las comillas) para insertar las variables directamente.

#Aqui le pedimos al usuario su nombre y el cargo que lleva a cabo
Nombre_del_Usuario = input("Me podria indicar cual es su nombre: ")
Cargo_del_Usuario = input("Me podria indicar cual es su cargo: ")

#aqui le mostramos al usuario que puedo acceder al sistema y le damos el saldo de bienvenida.
print("Acceso concedido")
print(f"Bienvenido {Nombre_del_Usuario}, al sistema de {Cargo_del_Usuario}")
