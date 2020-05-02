num = int(input("Enter a number: "))
print("Divisors are:")
divisors = [x for x in range(1, int(num/2)+1) if num%x == 0]
divisors.append(num)
print(divisors)
