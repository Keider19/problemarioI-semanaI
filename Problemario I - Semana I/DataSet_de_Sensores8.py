#EJERCICIO 8 A RESOLVER:
#Estás trabajando con un dataset de sensores climáticos que envían
#datos en grados Celsius, pero el motor analítico global requiere la escala Fahrenheit.
#Implementa un algoritmo que reciba una lista de valores flotantes y devuelva una nueva
#lista con la conversión aplicada mediante la fórmula: F = (C * 9/5) + 32. El reto consiste en
#procesar la colección completa sin alterar los datos originales (inmutabilidad).
#Pista: Tienes dos caminos. El básico: crear una lista vacía fahrenheit = [], usar un ciclo for
#para recorrer la de Celsius y hacer .append() del resultado. El avanzado (Analista Senior):
#usar una List Comprehension para hacerlo en una sola línea.


Datos_en_grados_Celsius = [20.5, 25.0, 30.2, 15.8, 0.0]
Escala_Fahrenheit = []

for C in Datos_en_grados_Celsius:
    F = (C * 9/5) + 32
    Escala_Fahrenheit.append(F)

print(f"Los datos en grados Celsius son: {Datos_en_grados_Celsius}")
print(f"La escala Fahrenheit es: {Escala_Fahrenheit}")


