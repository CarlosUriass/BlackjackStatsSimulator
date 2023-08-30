import random
import matplotlib.pyplot as plt

PALOS = ['corazones', 'diamantes', 'treboles', 'picas']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def crear_carta():
    carta = []
    for palo in PALOS:
        for valor in VALORES:
            carta.append((palo, valor))
    return carta

def obtener_mano(cartas, tamaño_mano):
    mano = random.sample(cartas, tamaño_mano)
    return mano

def valor_carta(carta):
    valor = carta[1]
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'as':
        return 11
    else:
        return int(valor)

def calcular_suma_mano(mano):
    suma = sum(valor_carta(carta) for carta in mano)
    # Ajustar el valor del As si es necesario (para evitar pasarse de 21)
    for carta in mano:
        if carta[1] == 'as' and suma > 21:
            suma -= 10
    return suma

def obtener_mano_crupier(cartas):
    mano = []
    while calcular_suma_mano(mano) < 17:  # Regla del crupier: Tomar hasta llegar a 17 o más
        mano.append(random.choice(cartas))
    return mano

def plot_probabilities(prob_blackjack_perfecto, prob_ganar_con_dos_cartas):
    labels = ['Blackjack Perfecto', 'Ganar con 2 Cartas']
    probabilities = [prob_blackjack_perfecto, prob_ganar_con_dos_cartas]

    plt.bar(labels, probabilities, color=['blue', 'green'])
    plt.ylabel('Probabilidad')
    plt.title('Probabilidades en el Juego de Blackjack')
    plt.ylim(0, 1)  # Rango del eje y de 0 a 1 para las probabilidades

    # Agregar porcentajes en las barras
    for i, prob in enumerate(probabilities):
        plt.text(i, prob + 0.02, f'{prob:.2%}', ha='center', color='black')

    plt.show()

def main(tamaño_mano, intentos):
    cartas = crear_carta()

    manos = []
    manos_crupier = []
    blackjack_perfecto = 0
    ganar_con_dos_cartas = 0

    for _ in range(intentos):
        mano_jugador = obtener_mano(cartas, tamaño_mano)
        mano_crupier = obtener_mano_crupier(cartas)
        manos.append(mano_jugador)
        manos_crupier.append(mano_crupier)

        suma_jugador = calcular_suma_mano(mano_jugador)
        suma_crupier = calcular_suma_mano(mano_crupier)

        # Verificar si el jugador tiene blackjack perfecto (suma de 21 con dos cartas)
        if suma_jugador == 21 and len(mano_jugador) == 2:
            blackjack_perfecto += 1

        # Verificar si el jugador gana con solamente dos cartas (crupier se pasa de 21)
        if suma_crupier > 21 and suma_jugador <= 21:
            ganar_con_dos_cartas += 1

    prob_blackjack_perfecto = blackjack_perfecto / intentos
    prob_ganar_con_dos_cartas = ganar_con_dos_cartas / intentos

    print(f"Probabilidad de sacar blackjack perfecto: {prob_blackjack_perfecto:.4f}")
    print(f"Probabilidad de ganar con dos cartas: {prob_ganar_con_dos_cartas:.4f}")

    plot_probabilities(prob_blackjack_perfecto, prob_ganar_con_dos_cartas)

    
# Llamar a la función main con el tamaño de mano deseado y el número de intentos.
main(tamaño_mano=2, intentos=1000000)
