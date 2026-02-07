#EJERCICIO 9 A RESOLVER:
#Como parte de un motor de procesamiento de lenguaje natural
#(NLP), se te pide identificar caracteres clave. Crea un script que reciba un solo carácter de
#texto y determine si pertenece al conjunto de vocales. El programa debe ser robusto
#frente a variaciones de caja, tratando 'A' y 'a' como equivalentes, y devolviendo un valor
#booleano o un mensaje de confirmación de detección.
#Pista: En lugar de escribir un if gigante con 10 condiciones (a, e, i, o, u en mayúsculas y
#minúsculas), usa el operador in. Ejemplo: if letra.lower() in "aeiou":. Esto hace que tu
#código sea mucho más legible y profesional.

#aqui le pedimos al usuario el caracter para analizar
Un_solo_caracter = input("Ingresa un solo caracter para analizar: ")

#el operador len() sirve para contar cuántos elementos hay dentro de algo.
if len(Un_solo_caracter) == 1:
    #.lower() lo que hace es tomar cualquier cadena de texto y convierte todas las letras mayusculas en minusculas.
    #el operador in busca si una letra o una palabra completa aparece en la frase.
    Vocal = Un_solo_caracter.lower() in "aeiou"
    if Vocal:
        print(f"Deteccion Positiva:{Un_solo_caracter} es una vocal.")
    else:
        print(f"Deteccion negativa: {Un_solo_caracter} no es una vocal.")
else:
    print("Ingrese solamente 1 caracter.")
    
    



