def encontrar_numero_reloj(modulo, posicion):
    return posicion % modulo

modulo_reloj = 12
posicion_deseada = 37

numero_en_posicion = encontrar_numero_reloj(modulo_reloj, posicion_deseada)
print(f"El número en la posición {posicion_deseada} del reloj (módulo {modulo_reloj}) es: {numero_en_posicion}")