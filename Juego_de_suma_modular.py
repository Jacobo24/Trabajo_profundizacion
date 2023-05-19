def jugar_suma_modular(modulo, numero_inicial, numero_objetivo):
    resultado = numero_inicial
    while resultado != numero_objetivo:
        numero = int(input("Ingresa un número para sumar: "))
        resultado = (resultado + numero) % modulo
        print(f"Resultado parcial: {resultado}")

    print("¡Ganaste!")

modulo_juego = 7
numero_inicial_juego = 2
numero_objetivo_juego = 5

jugar_suma_modular(modulo_juego, numero_inicial_juego, numero_objetivo_juego)