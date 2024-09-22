altura = int(input("Por favor, ingresa la altura del árbol"))
tronco = int(input("Por favor; ingresa el tamaño del árbol"))

for j in range(altura):
    
    print(" " * (altura - j - 1) + "*" * (2 * j + 1))

for j in range(tronco):
    
    print(" " * (altura - 1) + "*")
    
