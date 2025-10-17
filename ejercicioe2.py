dato1 = float(input())
dato2 = float(input())
dato3 = float(input())
dato4 = float(input())
dato5 = float(input())
dato6 = float(input())

notas = [dato1,dato2,dato3,dato4,dato5,dato6]


print(f"Maximo:{max(notas):.2f}")
print(f"Minimo: {min(notas):.2f}")
print(f"Diferencia: {max(notas)-min(notas):.2f}")
print(f"Suma: {sum(notas):.2f}")
print(f"promedio: {sum(notas)/6:.2f}")