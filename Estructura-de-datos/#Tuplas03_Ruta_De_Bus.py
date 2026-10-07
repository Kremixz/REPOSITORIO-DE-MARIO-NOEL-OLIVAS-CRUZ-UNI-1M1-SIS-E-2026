#Tuplas03_Ruta_De_Bus
ruta = ("Esteli", "Managua", 148, 170.00)

origen, destino, km, pasaje = ruta

costo_km = pasaje / km

origen, destino = destino, origen

print("Ruta:",ruta[0:2])
print(f"Distancia: {km} km")
print(f"Pasaje: C$ {pasaje:.2f}")
print(f"Costo por kilómetro: C$ {costo_km:.2f}")
print(f"Ruta de regreso: {origen} - {destino}")