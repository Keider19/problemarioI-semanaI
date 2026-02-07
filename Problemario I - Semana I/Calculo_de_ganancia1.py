#EJERCICIO 1 A RESOLVER:
#Como analista junior, debes calcular la ganancia neta de un
#producto. Solicita el "Precio de Venta" y el "Costo de Fabricación". Resta el costo del
#precio y muestra el resultado. Asegúrate de usar números con decimales (float) para que
#el cálculo sea exacto para la contabilidad.
#Pista: Los datos que vienen de un input() siempre son texto. Para hacer cálculos, debes
#envolver el input en la función float(). Ejemplo: precio = float(input("...")). La ganancia se
#obtiene con una resta simple.

#Lo que hicimos primero fue pedir al usuario El precio de venta y el costo de fabricacion 
Precio_de_venta = float(input("Me podria indicar cual es el Precio de Venta: "))
Costo_de_Fabricacion = float(input("Me podria indicar cual es el Costo de Fabricacion: "))

#Luego realizamos una resta para verificar la ganancia que estamos obteniendo
Ganancia = Precio_de_venta - Costo_de_Fabricacion

#Aqui le mostramos al usuario El precio de venta, el costo de fabricacion y la ganancia obtenido.
print(f"El precio de venta es de: {Precio_de_venta}")
print(f"El costo de fabricacion es de: {Costo_de_Fabricacion}")
#print(f"El calculo de la ganacia es:")
#print(f"El precio de venta: {Precio_de_venta} - el costo de fabricacion: {Costo_de_Fabricacion}")
print(f"La ganancia seria de: {Ganancia}")




