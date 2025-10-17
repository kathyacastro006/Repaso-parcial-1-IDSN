correo = input()
print(correo.count("@") ==1
and correo.index("@")>= 3 and 
"." in correo 
and " " not in correo 
and correo[0] != "." 
and correo[-1] != ".")



#El correo contiene exactamente un @: correo.count("@") ==1

#Antes y después del @ debe haber al menos 3 caracteres: correo.index("@")>= 3
#index te devuelve en que posición está el caracter que pongas, es este caso el @, o sea lo busca y te dice que hay 3 o más caracteres antes de él

#El correo debe contener al menos un punto: "." in correo

#correo no puede contener espacios: " " not in

#El correo no puede iniciar ni terminar con un punto: correo[-1] != "."
