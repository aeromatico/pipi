"""
CodeGol - Sesión 1: Generador de Fichas - VERSIÓN AVANZADA
PARA EXPLORADORES

Esta versión incluye:
- Múltiples jugadores
- Decoración mejorada
- Más campos de datos
- Mejor formato

¡Desafío para estudiantes rápidos!
"""

# ============================================
# GENERADOR AVANZADO DE FICHAS
# ============================================

print("╔════════════════════════════════════════╗")
print("║  ⚽ GENERADOR PROFESIONAL DE FICHAS ⚽  ║")
print("╔════════════════════════════════════════╗")
print("")

# Preguntar cuántos jugadores quiere crear
cantidad = input("¿Cuántos jugadores quieres registrar? ")
print("")
print("Perfecto! Vamos a crear " + cantidad + " fichas.")
print("")

# ============================================
# JUGADOR 1
# ============================================

print("--- JUGADOR 1 ---")
nombre1 = input("Nombre completo: ")
edad1 = input("Edad: ")
equipo1 = input("Equipo: ")
posicion1 = input("Posición: ")
numero1 = input("Número: ")
nacionalidad1 = input("Nacionalidad: ")
goles1 = input("Goles en carrera: ")
valor1 = input("Valor de mercado (millones): ")

print("")

# ============================================
# JUGADOR 2 (Solo si el usuario quiere más de 1)
# ============================================

print("--- JUGADOR 2 ---")
nombre2 = input("Nombre completo: ")
edad2 = input("Edad: ")
equipo2 = input("Equipo: ")
posicion2 = input("Posición: ")
numero2 = input("Número: ")
nacionalidad2 = input("Nacionalidad: ")
goles2 = input("Goles en carrera: ")
valor2 = input("Valor de mercado (millones): ")

print("")
print("")
print("")

# ============================================
# MOSTRAR FICHAS GENERADAS
# ============================================

print("╔════════════════════════════════════════╗")
print("║        FICHAS GENERADAS CON ÉXITO      ║")
print("╚════════════════════════════════════════╝")
print("")

# FICHA JUGADOR 1
print("┌────────────────────────────────────────┐")
print("│          ⭐ FICHA JUGADOR #1 ⭐        │")
print("├────────────────────────────────────────┤")
print("│ Nombre:       " + nombre1)
print("│ Edad:         " + edad1 + " años")
print("│ Nacionalidad: " + nacionalidad1)
print("│ ────────────────────────────────────   │")
print("│ Equipo:       " + equipo1)
print("│ Posición:     " + posicion1)
print("│ Número:       #" + numero1)
print("│ ────────────────────────────────────   │")
print("│ Goles:        " + goles1)
print("│ Valor:        $" + valor1 + " millones")
print("└────────────────────────────────────────┘")
print("")

# FICHA JUGADOR 2
print("┌────────────────────────────────────────┐")
print("│          ⭐ FICHA JUGADOR #2 ⭐        │")
print("├────────────────────────────────────────┤")
print("│ Nombre:       " + nombre2)
print("│ Edad:         " + edad2 + " años")
print("│ Nacionalidad: " + nacionalidad2)
print("│ ────────────────────────────────────   │")
print("│ Equipo:       " + equipo2)
print("│ Posición:     " + posicion2)
print("│ Número:       #" + numero2)
print("│ ────────────────────────────────────   │")
print("│ Goles:        " + goles2)
print("│ Valor:        $" + valor2 + " millones")
print("└────────────────────────────────────────┘")
print("")

# ============================================
# COMPARACIÓN RÁPIDA
# ============================================

print("╔════════════════════════════════════════╗")
print("║           COMPARACIÓN RÁPIDA           ║")
print("╚════════════════════════════════════════╝")
print("")
print("🏃 " + nombre1 + " (" + edad1 + " años) vs " + nombre2 + " (" + edad2 + " años)")
print("⚽ Goles: " + goles1 + " vs " + goles2)
print("💰 Valor: $" + valor1 + "M vs $" + valor2 + "M")
print("")

# ============================================
# MENSAJE FINAL
# ============================================

print("═══════════════════════════════════════════")
print("  ✅ ¡" + cantidad + " fichas creadas exitosamente!")
print("  🎮 Generado con CodeGol 2024")
print("  💻 Programado por: [Tu nombre aquí]")
print("═══════════════════════════════════════════")
print("")
print("🚀 DESAFÍO EXTRA:")
print("¿Puedes agregar un JUGADOR #3?")
print("Copia el código de Jugador 1 y modifícalo!")
print("")

# ============================================
# NOTAS PARA EL ESTUDIANTE AVANZADO:
# ============================================
"""
🎓 CONCEPTOS EXTRA QUE APRENDISTE AQUÍ:

1. ORGANIZACIÓN: Separar código en secciones claras
2. COMENTARIOS: Explicar qué hace cada parte
3. DECORACIÓN: Caracteres especiales para mejor visual
   (╔, ║, ═, ┌, │, ├, └, etc.)
4. CONSISTENCIA: Mismo formato para múltiples fichas
5. ESCALABILIDAD: Fácil agregar más jugadores

🔥 PRÓXIMOS PASOS:
- En Sesión 2 aprenderás condicionales (if/else)
- Podrás comparar automáticamente qué jugador es mejor
- Tu programa tomará decisiones solo!

🐛 ¿NOTAS ALGO REPETITIVO?
Escribimos casi el mismo código 2 veces para los 2 jugadores.
En Sesión 9 (Funciones) aprenderás a NO repetir código.
¡Por ahora es perfecto así!

💡 EXPERIMENTA:
- Cambia los caracteres decorativos
- Agrega más campos (altura, peso, pie hábil)
- Agrega emojis: ⚽🏆⭐👟🥇
- Crea tu propio estilo de ficha
"""
