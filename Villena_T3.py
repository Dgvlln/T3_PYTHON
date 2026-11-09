import math
import random

def punto_aleatorio(a, b):
    return random.uniform(-a, a), random.uniform(-b, b)

def en_elipse(x, y, a, b):
    return x * x / (a * a) + y * y / (b * b) <= 1

def en_hiperbola(x, y, c, d):
    return x * x / (c * c) - y * y / (d * d) >= 1

def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("  Debe ser un entero positivo.")
        except ValueError:
            print("  Debe ser un entero positivo.")


print("=== Area de interseccion elipse-hiperbola (Monte Carlo) ===")
a = leer_entero_positivo("a (semieje x de la elipse): ")
b = leer_entero_positivo("b (semieje y de la elipse): ")
c = leer_entero_positivo("c (hiperbola): ")
d = leer_entero_positivo("d (hiperbola): ")
n = leer_entero_positivo("Cantidad de numeros aleatorios: ")

p_elipse = 0
p_interseccion = 0
for _ in range(n):
    x, y = punto_aleatorio(a, b)
    if en_elipse(x, y, a, b):
        p_elipse += 1
        if en_hiperbola(x, y, c, d):
            p_interseccion += 1

area_elipse = math.pi * a * b

print("\n--- Resultados ---")
print(f"Puntos generados                  : {n}")
print(f"Puntos dentro de la elipse        : {p_elipse}")
print(f"Puntos en la interseccion         : {p_interseccion}")
print(f"Area de la elipse (formula)       : {area_elipse:.4f}")

if p_elipse == 0:
    print("Ningun punto cayo en la elipse; use mas puntos.")
else:
    area_interseccion = area_elipse * p_interseccion / p_elipse
    print(f"Area aproximada de la interseccion: {area_interseccion:.4f}")