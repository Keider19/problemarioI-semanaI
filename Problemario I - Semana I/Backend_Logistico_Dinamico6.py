#EJERCICIO 6 A RESOLVER:
#Diseña el backend de una aplicación de transporte que
#calcule costos en tiempo real. El usuario selecciona un tipo de vehículo (Pickup: $6.00,
#Gandola: $$7.00, Mudanza: $10.00$) y define una distancia en kilómetros. El sistema debe
#aplicar un recargo de $1.50 por cada kilómetro recorrido y generar un reporte final que
#deslose el precio base, el costo por distancia y el monto total facturado.
#Pista: Si usas Python 3.10 o superior, intenta implementar una estructura match-case en
#lugar de muchos if-elif. Es más legible para menús de selección. Asegúrate de convertir la
#entrada de la distancia a float para permitir kilómetros parciales (ej. 5.5 km).
#Si usas match-case, la sintaxis es:
#Python
#match vehiculo:
#case "Pickup":
#base = 6.0
#case _: # Esto atrapa cualquier opción no válida
#print("Error")
#No olvides sumar la base + (distancia * 1.5).


# Definimos la tasa por kilómetro como una constante (en mayúsculas) para 
# que sea fácil de actualizar si cambian los precios del combustible.
Tasa_por_km = 1.50

print("--- SISTEMA DE COTIZACIÓN DE TRANSPORTE EN TIEMPO REAL ---")

# .strip() elimina espacios accidentales al inicio/final.
# .capitalize() asegura que la primera letra sea mayúscula (ej: "pickup" -> "Pickup").
tipo_vehiculo = input("Seleccione tipo de vehículo (Pickup, Gandola, Mudanza): ").strip().capitalize()

# Usamos un bloque try-except para evitar que el programa falle si el usuario no ingresa un número.
try:
    # Convertimos la entrada a float para permitir decimales (ej: 5.5 km).
    distancia_km = float(input("Ingrese la distancia a recorrer (km): "))

    # Lógica de asignación de precio base usando match-case (Disponible en Python 3.10+)
    # Esta estructura es más eficiente y legible que múltiples if-elif.
    match tipo_vehiculo:
        case "Pickup":
            precio_base = 6.0
        case "Gandola":
            precio_base = 7.0
        case "Mudanza":
            precio_base = 10.0
        case _:
            # El guion bajo es el caso 'default'. Si no coincide con los anteriores, es un error.
            precio_base = None

    # Verificamos que el vehículo sea válido y la distancia no sea negativa.
    if precio_base is not None and distancia_km >= 0:
        # Operaciones aritméticas principales
        costo_distancia = distancia_km * Tasa_por_km
        total_facturado = precio_base + costo_distancia

        # Usamos f-strings para formatear la salida. 
        # :>8.2f significa: alinear a la derecha, reservar 8 espacios y usar 2 decimales.
        print("\n" + "="*40)
        print("         REPORTE FINAL DE FACTURACIÓN")
        print("="*40)
        print(f"Vehículo seleccionado:  {tipo_vehiculo}")
        print(f"Distancia recorrida:    {distancia_km:.2f} km")
        print("-" * 40)
        print(f"Precio Base:            ${precio_base:>8.2f}")
        print(f"Costo por Distancia:    ${costo_distancia:>8.2f}")
        print("-" * 40)
        print(f"TOTAL A FACTURAR:       ${total_facturado:>8.2f}")
        print("="*40)
    else:
        # Mensaje de error controlado para el usuario.
        print("\nVehículo no reconocido o distancia inválida.")

except ValueError:
    # Este bloque se activa si float() falla (ej: si el usuario escribe "diez" en vez de 10).
    print("\nPor favor, ingrese un número válido para la distancia.")