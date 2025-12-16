# 📝 Ejercicio 1: Mi Equipo Favorito

## 🎯 Objetivo
Crear fichas para 3 jugadores de tu equipo favorito.

## 📋 Requisitos

### Nivel Básico 🥉
Crea un programa que:
1. Pida información de 3 jugadores (uno por uno)
2. Para cada jugador capture:
   - Nombre
   - Posición
   - Número de camiseta
3. Muestre las 3 fichas al final

### Nivel Intermedio 🥈
Además de lo básico:
1. Agrega decoración bonita (líneas, espacios)
2. Agrupa por posición: "DELANTEROS", "MEDIOCAMPISTAS", etc.
3. Incluye 2 campos adicionales por jugador

### Nivel Avanzado 🥇
Además de todo lo anterior:
1. Crea fichas para 11 jugadores (equipo completo)
2. Organiza por formación (ej: 4-4-2)
3. Agrega un título con el nombre de tu equipo
4. Usa emojis y decoración creativa

## 💡 Pistas

**Para guardar múltiples jugadores**:
```python
nombre1 = input("Jugador 1 - Nombre: ")
nombre2 = input("Jugador 2 - Nombre: ")
nombre3 = input("Jugador 3 - Nombre: ")
# ... y así sucesivamente
```

**Para organizar por posición**:
```python
print("===== DELANTEROS =====")
print("1. " + delantero1)
print("2. " + delantero2)

print("")
print("===== MEDIOCAMPISTAS =====")
# ... etc.
```

## ✅ Checklist de Completado

- [ ] Mi programa pide información de al menos 3 jugadores
- [ ] Muestra las 3 fichas claramente
- [ ] No tiene errores al ejecutar
- [ ] (Opcional) Tiene buena decoración
- [ ] (Opcional) Está organizado por posición
- [ ] (Opcional) Incluye el equipo completo (11 jugadores)

## 🎨 Ejemplo de Output Esperado

```
=================================
    MI EQUIPO: REAL MADRID
=================================

----- DELANTEROS -----
🥇 #9 - Karim Benzema
🥇 #7 - Vinicius Jr

----- MEDIOCAMPISTAS -----
⭐ #10 - Luka Modric
⭐ #8 - Toni Kroos
⭐ #15 - Federico Valverde
⭐ #12 - Eduardo Camavinga

----- DEFENSAS -----
🛡️ #4 - David Alaba
🛡️ #3 - Eder Militao
🛡️ #2 - Dani Carvajal
🛡️ #23 - Ferland Mendy

----- PORTERO -----
🧤 #1 - Thibaut Courtois

=================================
```

## 🚀 Desafío Extra

**¿Puedes hacer que el programa pregunte primero el nombre del equipo?**

```python
nombre_equipo = input("¿Cuál es tu equipo favorito? ")

print("=================================")
print("    MI EQUIPO: " + nombre_equipo)
print("=================================")
```

## 📤 Entrega

**Guarda tu archivo como**: `mi_equipo.py`

**Ubicación**: `CodeGol/Sesion01/Ejercicios/`

**Opcional**: Toma captura de pantalla del resultado y compártela con el instructor.
