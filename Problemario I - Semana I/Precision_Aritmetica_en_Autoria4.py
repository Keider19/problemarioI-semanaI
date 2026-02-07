#EJERCICIO 4 A RESOLVER:
#En el sector financiero, la precisión es crítica. Tu tarea es
#escribir una expresión aritmética en Python que utilice exactamente una multiplicación,
#una división, un exponente, una suma y una resta para procesar tres variables de entrada,
#de modo que el valor de retorno sea estrictamente igual a $100.25$. Debes demostrar el
#dominio de la precedencia de operadores y el manejo de tipos de datos float para evitar
#errores de redondeo en auditorías.
#Pista: Recuerda que en Python la potencia se escribe con **. Piensa en el orden de las
#operaciones (PEMDAS): Paréntesis, Exponentes, Multiplicación/División,
#Adición/Sustracción. El uso de decimales (.0) asegura que el resultado sea un float, para
#llegar a .25, piensa en divisiones entre 4 o multiplicaciones por 0.25. Juega con los
#paréntesis para forzar a Python a que sume o reste después de haber hecho la potencia.

# estas serian las variables de entrada 
numero1 = 10.0
numero2 = 2.0
numero3 = 0.25

# Expresión aritmética que cumple con todos los requisitos que pide el ejercicio
resultado = (numero1 ** numero2) + (numero2 * numero3) / numero2 - 0.0

# resultado final
print(f"Resultado final: {resultado}")
print(f"¿Es exactamente 100.25?: {resultado == 100.25}")





