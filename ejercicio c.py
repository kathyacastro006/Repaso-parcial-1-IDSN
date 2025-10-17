X = int(input())
a = input()
b = input()

div1 = len(a)// X
div2 = len(b)// X
parte1 = a[0:div1]
parte2 = b[-div2:]
print(parte1+parte2)