nombre = str((input()))
apellido = str((input()))
nick = (nombre[:5]+apellido[0]).lower()
pin = (len(nombre) * 1000 + len(apellido)) % 10000
identificacion = f"C3-{nick}-{pin}"
print(f"Nick:{nick}")
print(f"Pin: {pin}")
print(f"ID: {identificacion}")