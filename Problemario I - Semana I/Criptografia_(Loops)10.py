#EJERCICIO 10 A RESOLVER:
#En criptografía, los "números perfectos" son aquellos cuya suma de
#divisores (excluyendo el número mismo) es igual al número original. Escribe una función
#que reciba un número entero positivo y determine si cumple con esta propiedad. Este reto
#exige un uso eficiente de bucles for y acumuladores lógicos para procesar todos los
#posibles divisores.
#Pista: Necesitas una variable "acumuladora" que empiece en 0. Usa un for i in range(1,
#numero):. Si numero % i == 0, significa que i es un divisor, así que lo sumas a tu
#acumulador. Al final del bucle, comprueba si la suma == numero.




def numeros_perfectos(numero_ingresado_por_el_usuario):
    #un numero perfecto debe ser un entero y no puede ser negativo
    if numero_ingresado_por_el_usuario <= 0:
        return False
    
    #aqui creamos el acumulador para guardar la suma de los divisores
    acumulador = 0
    
    #el rango excluye el numero mismo, asi como nos indica el ejercicio
    for i in range(1, numero_ingresado_por_el_usuario):
        #el operador % nos dice si  i divide a numero_ingresado_por_el_usuario
        if numero_ingresado_por_el_usuario % i == 0:
            acumulador += i  #si es divisor, lo sumamos al acumulador
            
    #aqui comparamos si la suma acumulada es igual al numero original
    return acumulador == numero_ingresado_por_el_usuario

#aqui hacemos la prueba si esta bien la funcion
numero = int(input("Ingrese un número para verificar si es perfecto: "))

if numeros_perfectos(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
    

