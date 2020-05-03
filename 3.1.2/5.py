#Solicite un valor numérico por pantalla, el valor debe ser impar, por lo que cada vez que se ingrese un
#número par, el sistema deberá mostrar un mensaje de error y volver a solicitar la variable, para este
#ejercicio use un ciclo de condición y el operador aritmético ‘%’, al ingresar el número impar el sistema
#deberá mostrar por una salida de pantalla el valor multiplicado por 4
n = 1
while n % 2 != 0:
    n = int(input("\n\tIngrese un número par y este será multiplicado por 4: "))
    if n % 2 != 0:
        print(f"\n\tEl número ingresado {n} es impar.")
    else:
        n4 = n*4
        print(f"\n\tEl {n} multiplicado por 4 es igual a {n4}")
        
