X = int(input())
a = input()
b = input()

parte1 = a[:X]
parte2 = b[-X:]

contrasena = parte1+parte2
print(contrasena)
