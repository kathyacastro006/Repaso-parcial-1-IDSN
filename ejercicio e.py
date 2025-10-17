dato1 = float(input())
dato2 = float(input())
dato3 = float(input())
dato4 = float(input())
dato5 = float(input())
dato6 = float(input())

notas = [dato1,dato2,dato3,dato4,dato5,dato6]
maximo = max(notas)
minimo = min(notas)
diferencia = maximo-minimo
suma = sum(notas)
promedio = suma/len(notas)

print(f"Maximo:{maximo:.2f}")
print(f"Minimo: {minimo:.2f}")
print(f"Diferencia: {diferencia:.2f}")
print(f"Suma: {suma:.2f}")
print(f"promedio: {promedio:.2f}")