print("""
           ____________________________
          |  ________________________  |
          | |                        | |
          | |                        | |
          | |       * * * * *        | |
          | |       Welcome to       | |
          | |                        | |
          | |         CHULIO         | |
          | |        Customs'        | |
          | |         Agency         | |
          | |                        | |
          | |       * * * * *        | |
          | |                        | |
          | |________________________| |
          |____________________________| """)

X = float(input("\n\n\nPor favor, introduzca los mt3 de carga que desea transportar: "))
Y = float(input("\nIntroduzca el valor declarado en dólares: USD$"))
costo = 0

if (X >= 5):
    costo += 100 * X
else:
    costo += 150 * X

subtotal = Y + costo
total = 0
print(f"\nEl costo de transporte más el valor declarado en dolares suman USD${subtotal}")
imp = 0
if (Y >= 5000):
    imp = 0.19
    total += subtotal * imp
    print(f"\nEl valor declarado en dolares es igual o superior a los USD$5.000 \nSe aplicará un 19% de impuesto sobre el valor declarado más el costo de transporte")
else:
    imp = 0.1
    total += subtotal * imp
    print(f"\nEl valor declarado en dolares es inferior a los USD$5.000 \nSe aplicará un 10% de impuesto sobre el valor declarado más el costo de transporte")
print(f"""
        La carga a transportar es de {X}mt3
        El valor declarado es de USD${Y}.-
        El costo de transporte de USD${costo}.-
        El impuesto a aplicar es ({imp}).-
        Valor total a pagar USD${total}.- """)
