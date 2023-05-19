def residuos_cuadrados_modulo(x):
    residuos = []
    for y in range(x):
        if (y ** 2) % x == y:
            residuos.append(y)
    return residuos

numero = 5
residuos_cuadrados = residuos_cuadrados_modulo(numero)
print(f"Los residuos cuadrados módulo {numero} son: {residuos_cuadrados}")