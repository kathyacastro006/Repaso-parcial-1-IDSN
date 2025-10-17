correo = input("escriba su correo electrónico: ")

print(correo.count("@") ==1 and correo.find("@")> 3 and "." in correo and " " not in correo and correo[0] != "." and correo[-1] != ".")



#El correo contiene exactamente un @: correo.count("@") ==1

#Antes y después del @ debe haber al menos 3 caracteres: correo.find("@")> 3
#"find" sirve para encontrar la posición de un caracter dentro del input. eso de ahí significa "significa “¿la posición del @ es mayor que 3 caracteres?”"

#El correo debe contener al menos un punto: "." in correo

#correo no puede contener espacios: " " not in

#El correo no puede iniciar ni terminar con un punto: correo[-1] != "."