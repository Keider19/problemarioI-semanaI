#EJERCICIO 5 A RESOLVER:
#Para optimizar una base de datos distribuida, los registros
#deben enviarse a diferentes servidores según su ID único. Desarrolla un componente que
#evalúe un número entero N ingresado por consola; si el ID es par, el sistema debe imprimir
#"Servidor A", y si es impar, "Servidor B". Este ejercicio evalúa tu comprensión de
#operadores aritméticos de residuo y bifurcación lógica simple.
#Pista: El operador residuo (%) es tu mejor amigo aquí. Si un número dividido entre 2 deja
#un residuo de 0 (n % 2 == 0), es par. Cualquier otro resultado indica que es impar, el
#operador % (módulo) devuelve el "sobrante" de una división. En una entrevista, menciona
#que esta es la forma más eficiente de balancear cargas de trabajo (sharding) entre
#servidores.

#Aqui solicitamos al usuario su ID_UNICO y lo convertimos a entero.
ID_Unico = input("Ingresa tu ID unico: ")
ID_Unico = int(ID_Unico)

#aqui agregamos un condicional.
if ID_Unico % 2 == 0:
    #si el residuo es == 0, el numero es par
    print("Servidor A")
else:
    #si el residuo no es == 0, el numero es impar
    print("Servidor B")





