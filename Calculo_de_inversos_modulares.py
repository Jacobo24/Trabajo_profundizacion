def calcular_inverso_modular(a, n):
    for b in range(1, n):
        if (a * b) % n == 1:
            return b
    return None

numero = 7
modulo = 10

inverso = calcular_inverso_modular(numero, modulo)
if inverso is not None:
    print(f"El inverso modular de {numero} módulo {modulo} es: {inverso}")
else:
    print(f"No se encontró un inverso modular de {numero} módulo {modulo}")