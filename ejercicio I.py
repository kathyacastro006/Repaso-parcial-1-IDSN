pedidonum1 = int(input())
pedidonum2 = int(input())

platos = ("Hamburguesa","Pizza","Tacos","Pupusas","HotDog")
complementos = ("Papas fritas","Alitas de pollo","Ensalada","Sopa","Lasaña")

orden1 = platos[pedidonum1-1]
orden2 = complementos[pedidonum2-1]

print(f"El pedido de Alvin es: {platos[pedidonum1-1]} con {complementos[pedidonum2-1]}")