w = input("\n\tEnter a word and we'll tell you if its palindrome or not: ")
print (f"\n\tYour word backwards looks like this: {w[::-1]}")
if (w[::-1] == w):
    print (f"\n\tCongrats, the word {w.upper()} is palindrome")
else:
    print (f"\n\tBummer, {w.upper()} is not palindrome. Keep trying!")
