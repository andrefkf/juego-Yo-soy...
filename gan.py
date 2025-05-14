import random
import json
import os

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Cargar reglas desde el JSON
with open("reglas.json", "r", encoding="utf-8") as f:
    reglas_crudas = json.load(f)

# Normalizar reglas
reglas = {}
for clave, lista in reglas_crudas.items():
    clave = clave.strip().lower()
    reglas[clave] = [x.strip().lower() for x in lista]

def le_gana(jugador, bot):
    jugador = jugador.strip().lower()
    bot = bot.strip().lower()
    return bot in reglas.get(jugador, [])

objetos = list(reglas.keys())

def como_jugar():
    limpiar_pantalla()
    print("=== ¿CÓMO JUGAR? ===\n")
    print("El bot empieza diciendo: 'yo soy X'")
    print("Vos respondés: 'yo soy Y' (solo escribí el nombre del objeto)")
    print("Si Y le gana a X, el bot intentará responder con algo que le gane a lo tuyo.")
    print("Si no le ganás, perdés.")
    print("El bot no puede usar las mismas combinaciones más de una vez por partida.\n")
    input("Presioná ENTER para volver al menú...")

# Mostrar las reglas
def mostrar_reglas():
    limpiar_pantalla()
    print("=== REGLAS: ¿Quién le gana a quién? ===\n")
    for clave, lista in reglas.items():
        gana_a = ', '.join(lista)
        print(f"→ {clave} le gana a: {gana_a}")
    print()
    input("Presioná ENTER para volver al menú...")

# Jugar al juego
def jugar():
    limpiar_pantalla()
    puntaje = 0
    objeto_bot = random.choice(objetos)
    historial_bot = set()  # guarda (objeto, contra_qué_objeto)

    while True:
        print(f"\nMáquina: yo soy {objeto_bot.upper()}")
        entrada = input("Tu turno yo soy: ").strip().lower()

        if entrada in ["?", "ayuda"]:
            print("→ Opciones válidas:", ", ".join(objetos))
            continue

        if entrada not in objetos:
            print("Objeto no válido. Escribí '?' para ver la lista.")
            continue

        if le_gana(entrada, objeto_bot):
            puntaje += 1
            print(f"¡Correcto! {entrada} le gana a {objeto_bot}")

            posibles = [
                obj for obj in objetos
                if le_gana(obj, entrada) and (obj, entrada) not in historial_bot
            ]

            if posibles:
                objeto_bot = random.choice(posibles)
                historial_bot.add((objeto_bot, entrada))
            else:
                print(f"No tengo nada nuevo que le gane a {entrada}. ¡Ganaste esta ronda!")
                print(f"Puntaje final: {puntaje}")
                break
        else:
            print(f"{entrada} NO le gana a {objeto_bot}")
            print("Suerte la próxima.")
            print(f"Puntaje final: {puntaje}")
            break

    input("\nPresioná ENTER para volver al menú...")

# Menú principal
def menu():
    while True:
        limpiar_pantalla()
        print("===== Bienvenido al juego 'yo soy...' =====\n")
        print("1. Jugar")
        print("2. Cómo jugar")
        print("3. Reglas")
        print("4. Salir\n")

        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            jugar()
        elif opcion == "2":
            como_jugar()
        elif opcion == "3":
            mostrar_reglas()
        elif opcion == "4":
            limpiar_pantalla()
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("Opción inválida. Presioná ENTER para intentar de nuevo.")
            input()

# Ejecutar menú
menu()
