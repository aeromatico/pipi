# ⚽ CodeGol - Sesión 1: Tu Primera Ficha de Jugador

**Nombre**: ________________________  **Fecha**: __________

---

## 🎯 Hoy Aprenderás

Al final de esta clase podrás:
- ✅ Crear tu primer programa Python
- ✅ Guardar información en variables
- ✅ Mostrar mensajes en pantalla
- ✅ Crear fichas de jugadores personalizadas

**Proyecto del día**: Generador de Fichas de Jugadores ⚽

---

## 💡 Conceptos Clave

### 1️⃣ Variables: Cajas que Guardan Información

```
Piensa en variables como CAJAS con ETIQUETAS:

┌─────────────┐
│  "Messi"    │  ← Esta caja se llama: nombre
└─────────────┘

┌─────────────┐
│     36      │  ← Esta caja se llama: edad
└─────────────┘
```

**En código Python**:
```python
nombre = "Messi"
edad = 36
equipo = "Inter Miami"
```

**Reglas**:
- El texto va entre comillas: `"así"`
- Los números van sin comillas: `36`
- El nombre de la variable va a la izquierda del `=`

---

### 2️⃣ print() - Mostrar Mensajes

Para mostrar algo en pantalla usamos `print()`:

```python
print("¡Hola CodeGol!")
# Resultado: ¡Hola CodeGol!

nombre = "Cristiano"
print(nombre)
# Resultado: Cristiano
```

**Pruébalo tú**:
```python
# Escribe aquí tu primer print:




```

---

### 3️⃣ input() - Pedir Información al Usuario

Para que el usuario escriba información:

```python
nombre = input("¿Cuál es tu jugador favorito? ")
print("Tu favorito es: " + nombre)
```

**¿Qué pasa aquí?**
1. El programa pregunta: "¿Cuál es tu jugador favorito?"
2. Tú escribes: "Messi"
3. Se guarda en la variable `nombre`
4. El programa muestra: "Tu favorito es: Messi"

---

### 4️⃣ Juntar Texto - Concatenación

Para juntar texto con variables usamos `+`:

```python
nombre = "Neymar"
equipo = "Al-Hilal"

print("El jugador " + nombre + " juega en " + equipo)
# Resultado: El jugador Neymar juega en Al-Hilal
```

**¡Importante!** Nota los espacios dentro de las comillas: `" juega en "`

---

## 🏗️ Construyendo Tu Ficha - Paso a Paso

### Paso 1: Tu Primer Programa

Escribe esto exactamente:

```python
print("¡Hola CodeGol!")
```

Guarda el archivo (Ctrl + S) como: `mi_primera_ficha.py`

Ejecuta (F5 o botón Run)

**¿Funcionó?** ✅ ¡Felicidades! Eres programador.

---

### Paso 2: Crear Variables

Ahora escribe:

```python
nombre = "Lionel Messi"
edad = 36
equipo = "Inter Miami"

print(nombre)
print(edad)
print(equipo)
```

**Prueba cambiando los datos por tu jugador favorito:**

Mi jugador favorito:
- Nombre: _______________________
- Edad: _________________________
- Equipo: _______________________

---

### Paso 3: Capturar Información del Usuario

Modifica tu código:

```python
nombre = input("Nombre del jugador: ")
edad = input("Edad: ")
equipo = input("Equipo: ")

print("Nombre: " + nombre)
print("Edad: " + edad)
print("Equipo: " + equipo)
```

**Ejecuta y prueba con diferentes jugadores**

---

### Paso 4: ¡Crear Tu Ficha Completa!

```python
# === GENERADOR DE FICHAS ===
print("=== GENERADOR DE FICHAS DE JUGADORES ===")
print("")

# Pedir información
nombre = input("Nombre del jugador: ")
edad = input("Edad: ")
equipo = input("Equipo: ")
posicion = input("Posición (DEL/MED/DEF/GK): ")
numero = input("Número de camiseta: ")

# Mostrar la ficha
print("")
print("=============================")
print("     FICHA DE JUGADOR")
print("=============================")
print("Nombre: " + nombre)
print("Edad: " + edad)
print("Equipo: " + equipo)
print("Posición: " + posicion)
print("Número: " + numero)
print("=============================")
```

**Copia este código y ejecútalo** ✨

---

## 🎮 Ejercicios de Práctica

### 🥉 Nivel Básico - Todos Deben Completar

**Ejercicio 1**: Agrega 2 campos más a tu ficha:
- Nacionalidad
- Goles en su carrera

**Ejercicio 2**: Cambia las líneas decorativas (`====`) por otra cosa:
- Puedes usar: `***`, `---`, `~~~`, o lo que quieras

---

### 🥈 Nivel Intermedio - ¡Desafío!

**Ejercicio 3**: Haz tu ficha más bonita:
- Agrega líneas en blanco con `print("")`
- Crea un título llamativo
- Usa emojis si quieres: ⚽ 🏆 ⭐ 👟

**Ejemplo**:
```python
print("⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽")
print("   FICHA OFICIAL")
print("⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽")
```

---

### 🥇 Nivel Avanzado - Exploradores

**Ejercicio 4**: Crea fichas de 3 jugadores diferentes:
- Usa variables: `nombre1`, `nombre2`, `nombre3`
- Muestra las 3 fichas

**Ejercicio 5**: Investiga:
- ¿Cómo hacer que `print()` NO salte a la línea siguiente?
- Pista: Busca en Google "python print same line"
- Pruébalo en tu ficha

---

## 🐛 ¿Encontraste un Error? ¡Normal!

Los programadores encuentran errores todo el tiempo. Es parte del proceso.

### Errores Comunes:

**Error 1**: `SyntaxError: invalid syntax`
```python
# ❌ Olvidaste las comillas
nombre = Messi

# ✅ Solución: Agrega comillas
nombre = "Messi"
```

**Error 2**: `NameError: name 'nombre' is not defined`
```python
# ❌ Usaste variable antes de crearla
print(nombre)
nombre = "Messi"

# ✅ Solución: Primero crea, después usa
nombre = "Messi"
print(nombre)
```

**Error 3**: Nada aparece en pantalla
- ¿Guardaste el archivo? (Ctrl + S)
- ¿Ejecutaste el programa? (F5 o Run)

---

## ✅ Checklist de Hoy

Al terminar la clase, marca lo que lograste:

- [ ] Ejecuté mi primer programa
- [ ] Creé variables con texto
- [ ] Creé variables con números
- [ ] Usé `print()` para mostrar mensajes
- [ ] Usé `input()` para pedir información
- [ ] Junté texto con variables usando `+`
- [ ] Mi ficha completa funciona sin errores
- [ ] Agregué al menos 1 campo extra
- [ ] ¡Me divertí programando! 🎉

---

## 🎨 Espacio Creativo

**Diseña tu ficha ideal en papel**:

Dibuja cómo te gustaría que se vea tu ficha perfecta:

```
┌─────────────────────────────┐
│                             │
│   [Dibuja tu diseño aquí]   │
│                             │
│                             │
│                             │
│                             │
│                             │
│                             │
└─────────────────────────────┘
```

**Campos que quiero agregar**:
1. _____________________________
2. _____________________________
3. _____________________________

---

## 🏠 Tarea Opcional (Solo si Quieres)

**No es obligatoria**, pero si te gustó, puedes:

1. **Mejorar tu ficha**: Hazla más bonita y completa
2. **Crear fichas de tu equipo favorito**: 11 jugadores
3. **Mostrarle a tu familia**: Explícales qué aprendiste

**Guarda todos tus programas en**: `Mi-Carpeta-CodeGol/Sesion-01/`

---

## 📝 Reflexión Final

**Responde honestamente**:

### ¿Qué aprendiste hoy?
_______________________________________________________________
_______________________________________________________________

### ¿Qué fue lo más divertido?
_______________________________________________________________
_______________________________________________________________

### ¿Qué fue lo más difícil?
_______________________________________________________________
_______________________________________________________________

### ¿Qué quieres aprender en la próxima clase?
_______________________________________________________________
_______________________________________________________________

### Dale una puntuación a esta clase: ⭐⭐⭐⭐⭐
(Marca las estrellas que te gustó)

---

## 🔥 Preview de la Próxima Sesión

**Sesión 2: Tu Programa Toma Decisiones**

Haremos un juego que PIENSA:
- Predice resultados de partidos
- Toma decisiones automáticas
- ¡Interactúa contigo!

**Concepto nuevo**: `if` / `else` (Condicionales)

```python
# Un adelanto...
edad = 18

if edad >= 18:
    print("¡Puede jugar en primera!")
else:
    print("Todavía en juveniles")
```

**¿Listo para que tu código sea inteligente? ⚡**

---

## 🎓 Glosario

**Términos que aprendiste hoy**:

| Término | Significado |
|---------|-------------|
| **Variable** | Caja que guarda información con un nombre |
| **String** | Texto entre comillas: `"así"` |
| **Integer** | Número entero: `36` |
| **print()** | Mostrar algo en pantalla |
| **input()** | Pedir información al usuario |
| **Concatenar** | Juntar texto con `+` |
| **Sintaxis** | Las reglas de escritura de Python |
| **Ejecutar** | Correr tu programa (F5) |

---

## 🏆 Tu Primera Insignia

**¡Felicidades! Desbloqueaste**:

```
╔════════════════════════════╗
║                            ║
║    🥇 PRIMER PROGRAMA      ║
║                            ║
║    Creaste tu primera      ║
║    aplicación Python       ║
║                            ║
║    Nombre: ____________    ║
║    Fecha: _____________    ║
║                            ║
╚════════════════════════════╝
```

**Guarda este cuaderno. Es el inicio de tu viaje como programador. 🚀⚽**

---

## 📚 Recursos Adicionales

**Si quieres practicar más**:

- **Python Tutor**: pythontutor.com (visualiza tu código)
- **Repl.it**: replit.com (programa desde el navegador)
- **Code.org**: code.org (juegos de programación)

**Recuerda**: No necesitas entender TODO hoy. ¡Es tu primera clase!

---

**¿Preguntas? ¿Dudas? ¡Pregunta a tu instructor! 💬**

**Nos vemos en la Sesión 2. ¡Prepárate para hacer JUEGOS! 🎮⚽**
