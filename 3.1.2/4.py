#Realiza un código que permita calcular la factorial de un número ingresado por pantalla, para ello debe
#tener en consideración que un número factorial se calcula de la siguiente manera:
#Ejemplo Factorial de 5
#5! = 5*4*3*2*1 = 120

fact = 1
n = int(input("\n\tIngresa un número y te diremos su factorial: "))
for i in range(1, n+1):
    fact *= i
print(f"\n\tThe factorial of {n} is {fact}")
