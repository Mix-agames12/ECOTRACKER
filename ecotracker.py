# ecotracker.py

"""
EcoTracker - Versión inicial de la aplicación para monitorear hábitos sostenibles
Objetivo: Registrar acciones diarias sostenibles (como reciclaje, uso de bicicleta, ahorro de energía)
y calcular un puntaje ecológico semanal para el usuario.
"""

import json
import datetime

# Lista de acciones sostenibles predefinidas y su puntaje asociado
actions_catalog = {
    "reciclaje": 10,
    "bicicleta": 15,
    "transporte_publico": 10,
    "ahorro_agua": 8,
    "ahorro_energia": 12,
    "reutilizacion": 10
}

# Base de datos simulada
user_log = []

# Registrar una acción

def registrar_accion(usuario, accion):
    fecha = datetime.date.today().isoformat()
    if accion in actions_catalog:
        entrada = {
            "usuario": usuario,
            "accion": accion,
            "puntaje": actions_catalog[accion],
            "fecha": fecha
        }
        user_log.append(entrada)
        print(f"Acción registrada: {accion} (+{actions_catalog[accion]} puntos)")
    else:
        print("Acción no reconocida. Intente nuevamente.")

# Calcular puntaje total semanal

def calcular_puntaje_semanal(usuario):
    hoy = datetime.date.today()
    semana_actual = hoy.isocalendar()[1]
    total = sum(
        entrada["puntaje"]
        for entrada in user_log
        if entrada["usuario"] == usuario and datetime.date.fromisoformat(entrada["fecha"]).isocalendar()[1] == semana_actual
    )
    return total

# Mostrar historial

def mostrar_historial(usuario):
    historial = [e for e in user_log if e["usuario"] == usuario]
    for entrada in historial:
        print(f"{entrada['fecha']}: {entrada['accion']} (+{entrada['puntaje']})")

# Menú de interacción básico

def menu():
    usuario = input("Ingrese su nombre de usuario: ")
    while True:
        print("\n--- EcoTracker ---")
        print("1. Registrar acción")
        print("2. Ver puntaje semanal")
        print("3. Ver historial")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Acciones disponibles:", ", ".join(actions_catalog.keys()))
            accion = input("Ingrese la acción realizada: ").strip().lower()
            registrar_accion(usuario, accion)
        elif opcion == "2":
            puntaje = calcular_puntaje_semanal(usuario)
            print(f"Puntaje ecológico semanal: {puntaje} puntos")
        elif opcion == "3":
            mostrar_historial(usuario)
        elif opcion == "4":
            print("Gracias por usar EcoTracker. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
