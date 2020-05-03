#Calcular la potencia de un número usando ciclos (no podrá usar el operador aritmético **), para ello el
#sistema solicitará por pantalla el valor de la base y el valor del exponente (ejemplo, base=4, exponente=
#2 entonces el resultado será 16), una vez realizado el calculo se mostrará el resultado por una salida por
#pantalla mostrando la información de la siguiente manera ↓
#“El resultado de la potencia de base 4 y exponente 2 es 16.”

i = 1
elevado = 1

numero = int(input("Ingrese la base de la potencia: "))
exponente = int(input("Ingrese el exponente de la potencia: "))
while i <= exponente:
    elevado = elevado * numero
    i = i+1

print(f"\n\n\tEl resultado de una potencia con base {numero} y exponente {exponente} es igual a {elevado}")
