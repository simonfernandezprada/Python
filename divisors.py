print ("\n\t\tWelcome to DIVISORS\n")
x = int(input("Please, write a number to see a list of all its divisors: "))
i = 1000
print("\n")
while i > 0:
    if x % i == 0:
        print(f"\t\t{i}")
    i -= 1
