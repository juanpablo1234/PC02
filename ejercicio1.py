# Inicio
#inic = [0,0]
x1 = 0
y1 = 0
# Proceso
x2 = int(input("Ingrese coordenada X = "))
y2 = int(input("Ingrese coordenada Y = "))

# Salida
# Coordenada
pfx = x2 - x1
pfy = y2 - y1

# Distancia
d = ( (x2 - x1)*(x2-x1) + (y2-y1)*(y2-y1) )**0.5


print("La distancia es =",d,"; de la coordenda ingresada =","[",x2,",",y2,"]")