#El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
#El nombre de usuario debe ser alfanumérico.
#Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
#Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
#Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras y números".
#Nombre de usuario válido, retorna True.
usuario = False
print ("Vamos a crear su usuario")
while usuario == False:
    nombre_usuario = input("\n\tIngrese su nombre de usuario: ")
    if len(nombre_usuario) <6:
        print("\nEl nombre de usuario debe contener al menos 6 caracteres")
        usuario == False
    elif len(nombre_usuario) >12:
        print("\nEl nombre de usuario no puede contener más de 12 caracteres")
        usuario == False
    elif nombre_usuario.isalnum() == False:
        print("\nEl nombre de usuario puede contener solo letras y números")
        usuario == False
    else:
        usuario = True

#La contraseña debe contener un mínimo de 8 caracteres.
#Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
#La contraseña no puede contener espacios en blanco.
#Contraseña válida, retorna True.
#Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura".

password = False
print("\n¡Perfecto! Ahora")
while password == False:
    password_usuario = input("\n\tIngrese su contraseña: ")
    if len(password_usuario) <8:
        print("\n\tLa contraseña debe contener un mínimo de 8 caracteres.")
        password = False
    elif password_usuario.islower() == True or password_usuario.isupper() == True:
        print("\n\tLa contraseña debe contener letras minúsculas y mayúsculas")
        password = False
    elif password_usuario.isspace() == True:
        print("\n\tLa contraseña no debe tener espacios en blanco")
    elif password_usuario.isalpha() == True:
        print("\n\tLa contraseña de contener números")
        password = False
    elif password_usuario.isalnum() == True:
        print("\n\tLa contraseña debe contener al menos 1 caracter NO alphanumérico")
        password = False
    else:
        password = True

print("\n¡Excelente! Usuario y contraseña creados exitosamente")
