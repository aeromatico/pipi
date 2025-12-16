"""
CodeGol - Sesión 1: Generador de Fichas de Jugadores
SOLUCIÓN COMPLETA

Este es el código de ejemplo completo para la Sesión 1.
Muestra todas las funcionalidades básicas enseñadas.
"""

# ============================================
# GENERADOR DE FICHAS DE JUGADORES
# ============================================

# Mostrar título del programa
print("========================================")
print("   GENERADOR DE FICHAS DE JUGADORES")
print("========================================")
print("")

# Capturar información del usuario
print("Ingresa los datos del jugador:")
print("")

nombre = input("Nombre completo: ")
edad = input("Edad: ")
equipo = input("Equipo actual: ")
posicion = input("Posición (DEL/MED/DEF/GK): ")
numero = input("Número de camiseta: ")
nacionalidad = input("Nacionalidad: ")

# Línea en blanco para separar
print("")
print("")

# Mostrar la ficha generada
print("========================================")
print("         ⚽ FICHA OFICIAL ⚽")
print("========================================")
print("")
print("Nombre:       " + nombre)
print("Edad:         " + edad + " años")
print("Nacionalidad: " + nacionalidad)
print("Equipo:       " + equipo)
print("Posición:     " + posicion)
print("Número:       #" + numero)
print("")
print("========================================")
print("   Ficha generada por CodeGol 2024")
print("========================================")

# Mensaje final
print("")
print("¡Ficha creada exitosamente! 🎉")
print("¿Quieres crear otra? ¡Ejecuta el programa de nuevo!")
