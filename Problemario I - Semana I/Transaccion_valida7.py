#EJERCICIO 7 A RESOLVER:
#Un procesador de pagos requiere validar la integridad de las
#transacciones antes de su registro. Implementa un flujo que solicite al usuario un método
#de pago y su respectiva clave de validación: si es "Pago Móvil", debe poseer exactamente
#8 dígitos; si es "Tarjeta", debe poseer 16. El programa debe utilizar estructuras de control
#para rechazar entradas con longitudes incorrectas o caracteres no numéricos.
#Pista: Necesitas dos validaciones: len(variable) para contar los caracteres y .isdigit() para
#asegurar que no metieron letras. Usa un if anidado o operadores lógicos and para verificar
#que ambas condiciones se cumplan al mismo tiempo.

#aqui le pedimos al usuario el metodo de pago y su clave de validacion 
#le colocamos .strip() para eliminar espacios accidentales al principio o al final escritos por el usuario 
#le colocamos .title() para convertir el texto a formato de titulo para que no importe si el usuario escribe pago movil o tarjeta en minúsculas, el programa aun lo pueda reconocer.
Metodo_de_pago = input("Ingrese su metodo de pago (Pago movil o Tarjeta): ").strip().title()
Clave_de_validacion = input("Ingrese su clave de validacion: ").strip()

#aqui creamos un condicional
if Metodo_de_pago == "Pago Movil":
    #aqui usamos un operador logico and, que para que se cumpla la condicion los 2 tienen que ser verdadero.
    if len(Clave_de_validacion) == 8 and Clave_de_validacion.isdigit():
        print("Transaccion de Pago Movil exitosa.")
    else:
        print("La clave debe de tener exactamente 8 digitos.")
elif Metodo_de_pago == "Tarjeta":
    if len(Clave_de_validacion) == 16 and Clave_de_validacion.isdigit():
        print("Transaccion de Tarjeta exitosa.")
    else:
        print("La clave debe tener exactamente 16 digitos.")
        

