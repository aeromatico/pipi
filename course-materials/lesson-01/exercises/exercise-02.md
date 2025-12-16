# 📝 Ejercicio 2: Comparador de Jugadores

## 🎯 Objetivo
Crear un programa que capture datos de 2 jugadores y los muestre lado a lado para comparar.

## 📋 Requisitos

### Nivel Básico 🥉
Crea un programa que:
1. Pida datos de 2 jugadores
2. Capture al menos 4 campos por jugador:
   - Nombre
   - Edad
   - Equipo
   - Goles en carrera
3. Muestre los datos de ambos jugadores claramente

### Nivel Intermedio 🥈
Además de lo básico:
1. Muestra los jugadores en formato "VS" (lado a lado)
2. Incluye decoración visual
3. Agrega 2 campos más (ej: asistencias, valor de mercado)

### Nivel Avanzado 🥇
Además de todo lo anterior:
1. Crea una tabla comparativa visual
2. Usa caracteres especiales para mejor presentación
3. Agrega una sección de "estadísticas totales"
4. Incluye emojis temáticos

## 💡 Ejemplo de Estructura

```python
# Capturar Jugador 1
print("=== JUGADOR 1 ===")
nombre1 = input("Nombre: ")
edad1 = input("Edad: ")
goles1 = input("Goles: ")

# Capturar Jugador 2
print("")
print("=== JUGADOR 2 ===")
nombre2 = input("Nombre: ")
edad2 = input("Edad: ")
goles2 = input("Goles: ")

# Mostrar comparación
print("")
print("===== COMPARACIÓN =====")
print(nombre1 + " vs " + nombre2)
print("Edad: " + edad1 + " vs " + edad2)
print("Goles: " + goles1 + " vs " + goles2)
```

## 🎨 Ejemplo de Output Avanzado

```
╔═══════════════════════════════════════════════════════╗
║              ⚔️  BATALLA DE LEYENDAS  ⚔️              ║
╚═══════════════════════════════════════════════════════╝

┌─────────────────────────┬─────────────────────────┐
│      👑 JUGADOR 1       │      👑 JUGADOR 2       │
├─────────────────────────┼─────────────────────────┤
│  Lionel Messi           │  Cristiano Ronaldo      │
│  36 años                │  38 años                │
│  Inter Miami            │  Al Nassr               │
│  ⚽ 800+ goles          │  ⚽ 850+ goles          │
│  🅰️ 350+ asistencias   │  🅰️ 250+ asistencias   │
│  💰 $400M valor         │  💰 $500M valor         │
└─────────────────────────┴─────────────────────────┘

╔═══════════════════════════════════════════════════════╗
║                  📊 RESUMEN TOTAL                     ║
╠═══════════════════════════════════════════════════════╣
║  Total de goles combinados: 1650+                     ║
║  Total de asistencias: 600+                           ║
║  Valor de mercado total: $900M                        ║
╚═══════════════════════════════════════════════════════╝
```

## 🔥 Desafíos Extra

### Desafío 1: Formato de Tabla
Intenta alinear la información usando espacios:
```python
print("Nombre:  " + nombre1 + "     vs     " + nombre2)
```

### Desafío 2: Suma Simple
Aunque aún no aprendimos matemáticas en Python, intenta esto:
```python
# Captura goles como texto
goles1 = input("Goles jugador 1: ")
goles2 = input("Goles jugador 2: ")

# Intenta mostrar "total"
print("Total goles: " + goles1 + goles2)

# ¿Qué pasa? ¿Por qué?
# Investiga y anota tus observaciones
```

**Reflexión**: ¿El resultado es el esperado? ¿Por qué sí o por qué no?

### Desafío 3: Jugadores Históricos
Crea comparaciones famosas:
- Messi vs Ronaldo
- Maradona vs Pelé
- Mbappé vs Haaland

## ✅ Checklist de Completado

- [ ] Captura datos de 2 jugadores
- [ ] Muestra ambos jugadores claramente
- [ ] Tiene formato "VS" o comparativo
- [ ] El código no tiene errores
- [ ] (Opcional) Tiene decoración visual
- [ ] (Opcional) Intenta calcular algún "total"
- [ ] (Opcional) Usa tabla o formato avanzado

## 💭 Preguntas para Reflexionar

1. **¿Qué pasó cuando intentaste sumar los goles?**
   _________________________________________________________________

2. **¿Notaste diferencia entre números y texto?**
   _________________________________________________________________

3. **¿Qué te gustaría que el programa hiciera automáticamente?**
   _________________________________________________________________

**Nota**: En la Sesión 3-4 aprenderás a hacer comparaciones automáticas. Por ahora, ¡solo muestra los datos!

## 📤 Entrega

**Guarda tu archivo como**: `comparador.py`

**Ubicación**: `CodeGol/Sesion01/Ejercicios/`

**Bonus**: Imprime tu output más bonito y pégalo en tu cuaderno.
