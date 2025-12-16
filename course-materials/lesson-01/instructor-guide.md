# 📘 Lección 1: Bienvenida al Código - Guía del Instructor

## 📋 Información General

| Campo | Detalle |
|-------|---------|
| **Sesión** | 1 de 24 |
| **Fase** | 1 - Los Primeros Goles |
| **Duración** | 60 minutos |
| **Nivel** | Principiante absoluto |
| **Prerequisitos** | Ninguno (primera clase) |

## 🎯 Objetivos de Aprendizaje

Al final de esta sesión, los estudiantes podrán:

1. ✅ **Ejecutar** su primer programa Python
2. ✅ **Crear** y usar variables básicas
3. ✅ **Imprimir** mensajes en pantalla con `print()`
4. ✅ **Capturar** entrada del usuario con `input()`
5. ✅ **Combinar** texto con variables (concatenación)
6. ✅ **Generar** una ficha de jugador personalizada

**Concepto Central**: *Las variables son cajas que guardan información*

## 🧠 Conexión con Conocimiento Previo

**Activador** (usar en minutos 0-5):
```
"¿Alguna vez coleccionaron figuritas de fútbol?
¿Qué información tiene una figurita?

- Nombre del jugador
- Equipo
- Edad
- Posición
- Número

Hoy vamos a crear un GENERADOR DIGITAL de fichas.
¡Pero en vez de comprarlas, las programaremos!"
```

## ⏱️ Estructura Minuto a Minuto

### **[0-10 min] 🔥 Warm-up e Introducción**

**[0-3 min] Bienvenida y Contexto**:
```
"¡Bienvenidos a CodeGol! En 12 semanas serán programadores.

Pregunta: ¿Quién tiene celular? [manos arriba]
TODOS los apps fueron creados por programadores como ustedes.

Hoy harán su primer programa: Generador de Fichas de Jugadores.
En 60 minutos lo tendrán funcionando. ¿Listos?"
```

**[3-5 min] Setup Check**:
- Todos tienen Python abierto (IDLE o Thonny)
- Pueden crear nuevo archivo
- Saben dónde guardar (carpeta "CodeGol/Sesion01/")

**[5-10 min] Primera Magia**:
```python
# Instructor escribe en pantalla compartida:
print("¡Hola CodeGol!")

# Ejecuta (F5 o Run)
# Sale: ¡Hola CodeGol!

"¿Vieron? Le dijimos a la computadora que IMPRIMA algo.
Ahora todos: escriban esto y ejecútenlo."
```

**Punto Clave**: Celebrar el primer programa de cada uno. "¡Felicidades, son programadores!"

---

### **[10-25 min] 📚 Concepto Nuevo: Variables**

**[10-13 min] Concepto 1: Variables como Cajas**:

```python
# En pantalla:
"Las variables son CAJAS que guardan información"

# Ejemplo visual en pizarra:
┌─────────────┐
│  "Messi"    │  ← nombre = "Messi"
└─────────────┘

# En código:
nombre = "Messi"
print(nombre)
```

**Analogía**:
```
"Variable = Caja con etiqueta

🏷️ nombre → 📦 contiene "Messi"
🏷️ edad   → 📦 contiene 36
🏷️ equipo → 📦 contiene "Inter Miami"

La computadora recuerda lo que guardaste en cada caja."
```

**[13-17 min] Concepto 2: Tipos de Datos Básicos**:

```python
# Strings (texto) - siempre entre comillas
nombre = "Cristiano Ronaldo"
equipo = "Al Nassr"

# Integers (números enteros)
edad = 38
goles = 850

# Ver diferencia:
print(nombre)    # Cristiano Ronaldo
print(edad)      # 38
```

**Punto Clave**: "Texto SIEMPRE con comillas. Números sin comillas."

**[17-21 min] Concepto 3: input() - Capturar Información**:

```python
# Demo en vivo:
nombre = input("¿Cuál es tu jugador favorito? ")
print("Tu jugador favorito es:")
print(nombre)

# Ejecutar y mostrar interacción
```

**[21-25 min] Concepto 4: Juntando Todo**:

```python
# Primera ficha básica:
nombre = input("Nombre del jugador: ")
edad = input("Edad: ")
equipo = input("Equipo: ")

print("=== FICHA DE JUGADOR ===")
print("Nombre: " + nombre)
print("Edad: " + edad)
print("Equipo: " + equipo)
```

**Ejecutar en vivo, llenar con Messi o jugador local popular**

---

### **[25-50 min] 💻 Práctica Activa (3 Niveles)**

#### **[25-35 min] Ejercicio Guiado - Todos Juntos**:

**Instructor dicta paso a paso**:
```python
# Paso 1: Pedir datos
print("=== GENERADOR DE FICHAS ===")
nombre = input("Nombre: ")
edad = input("Edad: ")
equipo = input("Equipo: ")
posicion = input("Posición (DEL/MED/DEF/GK): ")

# Paso 2: Mostrar ficha
print("")  # Línea en blanco
print("=== TU FICHA ===")
print("Nombre: " + nombre)
print("Edad: " + edad)
print("Equipo: " + equipo)
print("Posición: " + posicion)
```

**Mientras dictan**:
- Circular entre estudiantes
- Ayudar con errores de sintaxis
- Celebrar cuando funciona: "¡Perfecto!"

---

#### **[35-45 min] Práctica Semi-Independiente**:

**Proyectar instrucciones**:
```
🥉 NIVEL BÁSICO (Todos deben completar):
Agrega 2 campos más a tu ficha:
- Número de camiseta
- Nacionalidad

🥈 NIVEL INTERMEDIO (Desafío):
Haz que tu ficha se vea más bonita:
- Agrega líneas decorativas (=====)
- Usa print("") para espacios
- Crea un "título" llamativo

🥇 NIVEL AVANZADO (Exploradores):
Investiga: ¿Puedes hacer que print()
muestre todo en UNA sola línea?
Pista: Google "python print same line"
```

**Rol del instructor**:
- No dar respuestas directas
- Preguntas socráticas: "¿Qué has intentado?"
- Guiar debugging: "Lee el error, ¿qué dice?"

---

#### **[45-50 min] Experimentación Libre**:

```
"Últimos 5 minutos de código:
¡Personalicen su ficha! Háganla única.
Ideas:
- Agregar más datos
- Decoración creativa
- Emoji si quieren (⚽🏆⭐)
- Lo que imaginen

En 5 min mostramos las mejores."
```

---

### **[50-60 min] 🏆 Show & Tell + Cierre**

**[50-55 min] Presentaciones**:
```
"¿Quién quiere mostrar su ficha?"

[Elegir 2-3 estudiantes]

Para cada uno:
1. Proyectar su pantalla o que la muestren
2. Ejecutan su programa
3. Clase aplaude

Instructor celebra:
- "¡Miren esa decoración!"
- "¿Vieron cuántos datos captura?"
- "Funciona perfecto, excelente"
```

**[55-58 min] Recap de Conceptos**:
```
"¿Qué aprendimos hoy? [Preguntar a diferentes estudiantes]

✅ Variables: Cajas que guardan información
✅ print(): Mostrar mensajes
✅ input(): Pedir datos al usuario
✅ Strings: Texto entre comillas
✅ Juntarlo todo: ¡Primera app!"
```

**[58-60 min] Preview Emocionante**:
```
"Próxima clase:
Haremos un JUEGO INTERACTIVO.
Tu programa tomará DECISIONES solo.
¿Están listos para que su código piense?

Tarea OPCIONAL (solo si quieren):
Mejoren su ficha, agreguen más jugadores.

¡Nos vemos próxima sesión! 🚀⚽"
```

---

## 🐛 Problemas Comunes y Soluciones

### Error 1: Syntax Error - Comillas Faltantes
```python
# ❌ Mal:
nombre = Messi

# ✅ Bien:
nombre = "Messi"
```
**Solución**: "El texto SIEMPRE va entre comillas"

---

### Error 2: NameError - Variable No Definida
```python
# ❌ Mal:
print(nombre)  # Si nombre no existe

# ✅ Bien:
nombre = "Messi"
print(nombre)
```
**Solución**: "Primero creas la caja (variable), después la usas"

---

### Error 3: Concatenación sin +
```python
# ❌ Mal:
print("Nombre:" nombre)

# ✅ Bien:
print("Nombre: " + nombre)
```
**Solución**: "Para juntar texto con variable usa +"

---

### Error 4: No Guardar antes de Ejecutar
**Solución**: "Siempre guarda (Ctrl+S) antes de ejecutar (F5)"

---

### Error 5: Python No Instalado / No Abre
**Plan B**:
- Usar online: repl.it o trinket.io
- Pair programming (compartir PC)
- Mostrar en proyector mientras arreglan

---

## 🌟 Diferenciación

### Para Estudiantes que Terminan Rápido:

**Desafío Extra 1: Multi-Jugador**:
```python
# Crear fichas de 3 jugadores diferentes
# Guardar en variables nombre1, nombre2, nombre3
# Mostrar los 3
```

**Desafío Extra 2: Calculadora Simple**:
```python
# Pedir número de goles en 3 partidos
goles1 = input("Goles partido 1: ")
goles2 = input("Goles partido 2: ")
goles3 = input("Goles partido 3: ")

# Mostrar total
# Nota: Esto da resultado raro (concatena strings)
# Es intro para próxima clase (tipos de datos)
```

### Para Estudiantes con Dificultades:

**Versión Simplificada**:
```python
# Solo 3 campos en vez de 5
nombre = input("Nombre: ")
equipo = input("Equipo: ")

print("Jugador: " + nombre)
print("Equipo: " + equipo)
```

**Pair Programming**:
- Emparejar con compañero avanzado
- Rol de Navigator (piensan juntos)

---

## 📦 Materiales Necesarios

### Antes de la Clase:

**Preparación Técnica**:
- [ ] Python instalado en todas las PCs (3.8+)
- [ ] IDLE o Thonny funcionando
- [ ] Proyector para demo del instructor
- [ ] Carpeta "CodeGol/Sesion01/" creada en cada PC

**Materiales Físicos**:
- [ ] Pizarra/pizarrón para diagramas
- [ ] Marcadores de colores
- [ ] (Opcional) Figuritas de fútbol reales para mostrar

**Materiales Digitales**:
- [ ] `starter-code.py` - Código inicial comentado
- [ ] `solution.py` - Solución completa
- [ ] `advanced-solution.py` - Versión extendida

**Documentos para Estudiantes**:
- [ ] `student-workbook.md` - Impreso o digital
- [ ] (Opcional) Hoja de referencia de sintaxis

---

## 📊 Evaluación de la Sesión

### Checklist de Éxito (80%+ debe lograr):

Al final de la clase, estudiantes pueden:
- [ ] Crear variables y asignar valores
- [ ] Usar `print()` para mostrar mensajes
- [ ] Usar `input()` para capturar datos
- [ ] Concatenar strings con +
- [ ] Ejecutar su programa sin errores

### Evaluación Formativa:

**Thumbs Check** (min 20):
```
"Levanten pulgar según entiendan variables:
👍 = Lo entiendo
👉 = Más o menos
👎 = Necesito ayuda"
```

**Exit Ticket** (min 60):
```markdown
En una hoja responde:

1. ¿Qué hace print()?
2. ¿Qué hace input()?
3. ¿Qué fue lo más interesante hoy?

Nombre: __________
```

### Autoevaluación del Instructor:

Después de la clase, responder:
- ¿Qué % logró completar el ejercicio básico?
- ¿Qué concepto fue más difícil de entender?
- ¿Qué ajustaría para próxima vez?
- ¿Algún estudiante necesita atención extra?

---

## 🔗 Conexión con Próxima Sesión

**Sesión 2 Preview**:
```python
# Teaser rápido (30 segundos):
edad = 18

if edad >= 18:
    print("¡Puede jugar en primera división!")
else:
    print("Todavía en juveniles")

"Próxima clase: Su código TOMA DECISIONES.
¡Predictor de partidos! ⚽🎮"
```

---

## 💡 Tips de Enseñanza

### DO (Hacer):
✅ Celebrar cada pequeño éxito
✅ Hacer analogías con fútbol constantemente
✅ Circular por el salón, ayudar individualmente
✅ Mostrar tu pantalla mientras codeas
✅ Cometer errores intencionalmente (enseñar debugging)
✅ Usar lenguaje simple, evitar jerga técnica innecesaria

### DON'T (No Hacer):
❌ Asumir conocimiento previo
❌ Ir demasiado rápido
❌ Resolver todo por ellos (guiar, no hacer)
❌ Usar ejemplos abstractos sin contexto
❌ Frustrate when they struggle (es parte del proceso)
❌ Olvidar el "wow moment" final

---

## 📸 Momento Foto

**Al final de la clase**:
```
Tomar captura de pantalla o foto de:
- 2-3 fichas de ejemplo creadas por estudiantes
- Algún error interesante que encontraron
- La clase celebrando

Guardar en: course-materials/lesson-01/assets/class-photos/
Sirve para documentar progreso y mejorar curso.
```

---

## 🎯 Recuerda

Esta es la **sesión más importante del curso**.

Si los engancha hoy, seguirán 23 sesiones más.
Si no, puede perderlos.

**Claves del éxito**:
1. 🎉 Celebrar cada logro (mucho)
2. ⚡ Resultados rápidos (primera app en 30 min)
3. ⚽ Conexión constante con fútbol (su pasión)
4. 🤝 Ambiente seguro (el error es aprendizaje)
5. 🚀 Terminar con "wow" (quieren más)

**¡Tú puedes! ¡Son 60 minutos que cambiarán vidas! 💻⚽**

---

## 📚 Recursos Adicionales

- **Código de ejemplo**: `code-examples/`
- **Ejercicios extra**: `exercises/`
- **Cuaderno del estudiante**: `student-workbook.md`
- **Documentación oficial Python**: docs.python.org (para instructor)

---

**Próximo paso**: Leer `student-workbook.md` para ver la perspectiva del estudiante.
