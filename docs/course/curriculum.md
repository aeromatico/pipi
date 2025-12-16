# 📅 CodeGol - Curriculum Completo (24 Sesiones)

## 🎯 Objetivos Generales del Curso

Al finalizar las 24 sesiones, los estudiantes podrán:
- ✅ Escribir programas Python de 100+ líneas independientemente
- ✅ Consumir APIs REST y procesar JSON
- ✅ Crear juegos y aplicaciones interactivas
- ✅ Debuggear errores sistemáticamente
- ✅ Leer y modificar código de otros
- ✅ Diseñar y completar proyectos propios

---

## 📊 FASE 1: Los Primeros Goles (Semanas 1-3)

### **Sesión 1: Bienvenida al Código**
**Concepto**: Variables, strings, print(), input()

**Proyecto**: Generador de Fichas de Jugadores
```python
# Output esperado:
=== FICHA DE JUGADOR ===
Nombre: Lionel Messi
Edad: 36
Equipo: Inter Miami
Posición: Delantero
```

**Habilidades**:
- Asignar variables
- Usar print() con formato
- Capturar input del usuario
- Concatenar strings

**Wow Moment**: "¡Creaste tu primera ficha en 10 minutos!"

---

### **Sesión 2: El Juego Comienza**
**Concepto**: Condicionales básicos (if/else)

**Proyecto**: Predictor Simple de Partidos
```python
# Usuario ingresa 2 equipos
# Programa "predice" ganador aleatoriamente
# Muestra resultado con condiciones
```

**Habilidades**:
- if/else básico
- Comparaciones (==, >, <)
- bool y lógica simple
- Primera interacción real

**Wow Moment**: "¡Tu código toma decisiones solo!"

---

### **Sesión 3: Decisiones Complejas**
**Concepto**: if/elif/else, operadores lógicos (and/or)

**Proyecto**: Clasificador de Posiciones FIFA
```python
# Ingresa puntos de un equipo
# Clasifica: Campeón, Clasificado, Eliminado, etc.
# Usa múltiples condiciones
```

**Habilidades**:
- Múltiples condiciones con elif
- Operadores and/or
- Rangos numéricos
- Lógica más compleja

**Wow Moment**: "Tu programa es como un árbitro inteligente"

---

### **Sesión 4: Mini-Proyecto Integrador 1**
**Concepto**: Repaso + integración

**Proyecto**: Juego "Adivina el Jugador"
```python
# Programa piensa en un jugador
# Da pistas (edad, liga, posición)
# Usuario adivina con 3 intentos
# Usa todo lo aprendido
```

**Habilidades**:
- Integrar variables + condicionales
- Lógica de juego
- Feedback al usuario
- Primer proyecto "completo"

**Wow Moment**: "¡Tienes un juego real funcionando!"

---

### **Sesión 5: Repetir para Ganar**
**Concepto**: Loops - for con range()

**Proyecto**: Generador de Calendarios de Liga
```python
# Genera fixture completo
# 10 equipos, todos contra todos
# Imprime calendario legible
```

**Habilidades**:
- for con range()
- Iteraciones básicas
- Formateo de output
- Contadores

**Wow Moment**: "¡Generaste 90 partidos con 5 líneas!"

---

### **Sesión 6: Tablas y Estadísticas**
**Concepto**: while loops, acumuladores

**Proyecto**: Simulador de Tabla de Posiciones
```python
# Simula partidos uno por uno
# Acumula puntos por equipo
# Muestra tabla actualizada
# Loop hasta terminar torneo
```

**Habilidades**:
- while loops
- Variables acumuladoras
- Control de flujo
- Lógica de simulación

**Wow Moment**: "¡Simulaste un torneo completo!"

**🏆 HITO FASE 1**: Pueden crear juegos simples funcionando

---

## 📊 FASE 2: Construyendo Estadios (Semanas 4-6)

### **Sesión 7: Armando el Equipo**
**Concepto**: Listas, append(), len()

**Proyecto**: Constructor de Alineaciones
```python
# Lista vacía para alineación
# Agrega 11 jugadores
# Muestra formación (4-4-2, etc.)
# Valida posiciones
```

**Habilidades**:
- Crear y modificar listas
- append() y métodos básicos
- Indexación [0], [-1]
- len() y validaciones

**Wow Moment**: "¡Puedes guardar equipo completo en una variable!"

---

### **Sesión 8: Equipos Aleatorios**
**Concepto**: random.choice(), random.shuffle()

**Proyecto**: Generador de Equipos Balanceados
```python
# Pool de 20 jugadores
# Genera 2 equipos aleatorios
# Balancea por posiciones
# Muestra alineaciones
```

**Habilidades**:
- Módulo random
- Mezclar y elegir elementos
- Lógica de balanceo simple
- Manipulación de listas

**Wow Moment**: "¡Nunca hay mismo partido dos veces!"

---

### **Sesión 9: Tu Primera Función**
**Concepto**: Funciones básicas, def, return

**Proyecto**: Calculadora de Estadísticas
```python
def calcular_promedio_goles(goles_lista):
    # ...
    return promedio

def es_goleador(goles):
    # ...
    return True/False
```

**Habilidades**:
- Definir funciones
- Parámetros
- return valores
- Reutilizar código

**Wow Moment**: "¡Escribe una vez, usa mil veces!"

---

### **Sesión 10: Biblioteca de Fútbol**
**Concepto**: Múltiples funciones, organización

**Proyecto**: Módulo Reutilizable
```python
# Crea archivo funciones_futbol.py con:
- calcular_puntos()
- determinar_ganador()
- simular_partido()
- generar_estadisticas()
```

**Habilidades**:
- Múltiples funciones relacionadas
- Parámetros múltiples
- Organización de código
- Documentación con comentarios

**Wow Moment**: "¡Tienes tu propia librería FIFA!"

---

### **Sesión 11: Datos Complejos**
**Concepto**: Diccionarios básicos

**Proyecto**: Base de Datos de Jugadores
```python
messi = {
    "nombre": "Lionel Messi",
    "edad": 36,
    "goles": 800,
    "equipo": "Inter Miami",
    "posicion": "DEL"
}
# Acceder, modificar, agregar datos
```

**Habilidades**:
- Crear diccionarios
- Acceder con claves
- Modificar valores
- Estructura key: value

**Wow Moment**: "¡Un jugador es más que un nombre!"

---

### **Sesión 12: Colección de Estrellas**
**Concepto**: Listas de diccionarios

**Proyecto**: Mi Base de Datos FIFA Personalizada
```python
# Lista con 10+ jugadores (diccionarios)
# Funciones para:
- buscar_por_nombre()
- filtrar_por_posicion()
- top_goleadores()
- agregar_jugador()
```

**Habilidades**:
- Estructuras complejas
- Iteración sobre diccionarios
- Búsqueda y filtrado
- CRUD básico (Create, Read, Update)

**Wow Moment**: "¡Tienes tu propia base de datos!"

**🏆 HITO FASE 2**: Pueden crear aplicaciones con datos estructurados

---

## 📊 FASE 3: La Liga Digital (Semanas 7-9)

### **Sesión 13: Primera Conexión**
**Concepto**: APIs, requests.get(), status codes

**Proyecto**: Consultor de Equipos Reales
```python
import requests

# Primera llamada a TheSportsDB
# Obtener datos de un equipo real
# Mostrar información básica
```

**Habilidades**:
- Importar módulos
- requests.get()
- Verificar status (200, 404, etc.)
- Primera interacción con API

**Wow Moment**: "¡Estás conectado con datos del mundo real!"

---

### **Sesión 14: El Lenguaje JSON**
**Concepto**: JSON básico, .json(), navegación

**Proyecto**: Explorador de Ligas
```python
# Conecta a API de fútbol
# Obtiene lista de ligas
# Parsea JSON
# Muestra ligas disponibles
```

**Habilidades**:
- .json() para parsear
- Navegar estructura JSON
- Acceder a datos anidados
- Entender formato de datos

**Wow Moment**: "¡Entiendes el idioma de las APIs!"

---

### **Sesión 15: Búsqueda Avanzada**
**Concepto**: Parámetros de API, query strings

**Proyecto**: Buscador de Jugadores Global
```python
# Función buscar_jugador(nombre)
# Usa parámetros de búsqueda
# Filtra resultados
# Muestra información detallada
```

**Habilidades**:
- Parámetros en requests (params={})
- Filtrado de resultados JSON
- Manejo de múltiples resultados
- Formateo de datos complejos

**Wow Moment**: "¡Puedes buscar cualquier jugador del mundo!"

---

### **Sesión 16: Datos a tu Medida**
**Concepto**: Transformación de datos, list comprehensions

**Proyecto**: Generador de Reportes Personalizados
```python
# Obtiene datos de API
# Filtra solo lo necesario
# Transforma a formato propio
# Genera reporte legible
```

**Habilidades**:
- Extraer datos específicos de JSON
- List comprehensions básicas
- Formateo avanzado de strings
- Transformación de datos

**Wow Moment**: "¡Controlas exactamente qué datos quieres!"

---

### **Sesión 17: Resistencia a Fallos**
**Concepto**: try/except, manejo de errores

**Proyecto**: App Robusta con Fallbacks
```python
# Intenta conectar a API
# Si falla, usa datos locales
# Maneja errores gracefully
# Siempre funciona
```

**Habilidades**:
- try/except básico
- Detectar tipos de errores
- Mensajes de error amigables
- Fallback strategies

**Wow Moment**: "¡Tu app nunca se rompe!"

---

### **Sesión 18: Modo Offline**
**Concepto**: Lectura de archivos JSON locales

**Proyecto**: App Híbrida (Online + Offline)
```python
# Intenta API primero
# Si falla, lee JSON local
# Guarda datos para próxima vez
# Sistema de caché simple
```

**Habilidades**:
- Leer archivos con open()
- json.load() para archivos
- Lógica de fallback completa
- Primera persistencia de datos

**Wow Moment**: "¡Funciona con o sin internet!"

**🏆 HITO FASE 3**: Pueden crear apps conectadas a internet real

---

## 📊 FASE 4: Copa Mundial del Código (Semanas 10-12)

### **Sesión 19: Memoria Permanente**
**Concepto**: Escribir archivos, persistencia

**Proyecto**: Sistema de Guardado de Partidos
```python
# Simula partidos
# Guarda resultados en archivo
# Lee historial al iniciar
# Estadísticas acumuladas
```

**Habilidades**:
- open() con modo 'w', 'r', 'a'
- json.dump() para guardar
- Persistencia entre ejecuciones
- Sistema de "base de datos" simple

**Wow Moment**: "¡Tu programa recuerda todo!"

---

### **Sesión 20: Tu Marca Personal**
**Concepto**: Organización avanzada, módulos propios

**Proyecto**: Librería Personal Documentada
```python
# Crea tu_nombre_futbol.py
# 10+ funciones pulidas
# Comentarios claros
# Ejemplos de uso
# README de tu librería
```

**Habilidades**:
- Organización profesional
- Documentación
- Imports entre archivos
- Buenas prácticas

**Wow Moment**: "¡Código que otros pueden usar!"

---

### **Sesión 21: Planificando el Gran Proyecto**
**Concepto**: Diseño de proyecto, pseudocódigo

**Proyecto**: Especificación de Proyecto Final
```markdown
# Cada estudiante elige:
- Trivia de fútbol avanzada
- Simulador de torneo completo
- Fantasy football tracker
- Comparador de jugadores
- [Su idea creativa]

# Crean plan paso a paso
```

**Habilidades**:
- Planificación de software
- Pseudocódigo
- Descomponer problemas
- Pensamiento algorítmico

**Wow Moment**: "¡Diseñas como programador profesional!"

---

### **Sesión 22: Construyendo el Sueño**
**Concepto**: Desarrollo iterativo

**Proyecto**: Implementación Proyecto Final (Parte 1)
```python
# Primera versión funcionando
# Características core
# Testing básico
# Iteración basada en pruebas
```

**Habilidades**:
- Desarrollo incremental
- Testing manual
- Debugging complejo
- Resolución de problemas

**Wow Moment**: "¡Tu idea cobra vida!"

---

### **Sesión 23: Puliendo la Joya**
**Concepto**: Refinamiento, UX

**Proyecto**: Implementación Proyecto Final (Parte 2)
```python
# Mejoras de interfaz
# Manejo de errores completo
# Features extras
# Documentación de uso
```

**Habilidades**:
- User experience
- Validación de inputs
- Mensajes claros
- Polish profesional

**Wow Moment**: "¡Parece app comercial!"

---

### **Sesión 24: Demo Day - ¡Todos son Estrellas!**
**Concepto**: Presentación, retroalimentación

**Proyecto**: Presentaciones y Certificación
```markdown
# Cada estudiante:
1. Presenta su proyecto (5 min)
2. Demo en vivo
3. Explica código interesante
4. Recibe feedback positivo
5. Recibe certificado

# Celebración final
# Próximos pasos
```

**Habilidades**:
- Presentación técnica
- Explicar código
- Recibir feedback
- Reflexión sobre aprendizaje

**Wow Moment**: "¡SOY UN PROGRAMADOR DE VERDAD!"

**🏆 HITO FASE 4**: Portfolio completo, certificación, confianza total

---

## 📈 Progresión de Complejidad

### Líneas de Código por Fase:
- Fase 1 (S1-6): 10-30 líneas por proyecto
- Fase 2 (S7-12): 30-70 líneas por proyecto
- Fase 3 (S13-18): 50-100 líneas por proyecto
- Fase 4 (S19-24): 100-200+ líneas proyecto final

### Conceptos Acumulativos:
```
Sesión 6:  Variables, condicionales, loops
Sesión 12: + Listas, diccionarios, funciones
Sesión 18: + APIs, JSON, archivos
Sesión 24: + Proyectos complejos, organización profesional
```

## 🎯 Sistema de Logros (Badges)

Los estudiantes desbloquean badges al completar hitos:

**Fase 1**:
- 🥇 "Primer Programa" (S1)
- 🧠 "Pensador Lógico" (S3)
- 🔄 "Loop Master" (S6)

**Fase 2**:
- 📚 "Coleccionista" (S7)
- ⚙️ "Ingeniero de Funciones" (S10)
- 🗄️ "Arquitecto de Datos" (S12)

**Fase 3**:
- 🌐 "Conectado al Mundo" (S13)
- 🔍 "JSON Explorer" (S16)
- 💪 "Código Indestructible" (S18)

**Fase 4**:
- 💾 "Guardián de Datos" (S19)
- 🏗️ "Constructor de Proyectos" (S23)
- 🌟 "CodeGol Graduate" (S24)

## 📊 Evaluación por Fase

### Criterios de Éxito:

**Fase 1**: ¿Pueden escribir un juego simple solos?
- ✅ Uso correcto de variables
- ✅ Lógica condicional funcional
- ✅ Al menos un loop trabajando

**Fase 2**: ¿Pueden organizar datos complejos?
- ✅ Listas y diccionarios correctos
- ✅ Funciones reutilizables
- ✅ Código organizado

**Fase 3**: ¿Pueden conectar con APIs?
- ✅ Request exitoso a API
- ✅ Parseo de JSON correcto
- ✅ Manejo básico de errores

**Fase 4**: ¿Pueden completar proyecto propio?
- ✅ Proyecto funcional completo
- ✅ Código organizado y documentado
- ✅ Capacidad de explicar su trabajo

## 🔄 Flexibilidad del Curriculum

### Adaptaciones Recomendadas:

**Si el grupo avanza rápido**:
- Añadir "Desafío Avanzado" cada sesión
- Introducir conceptos extra (OOP básica, etc.)
- Proyectos más ambiciosos

**Si necesitan más tiempo**:
- Sesiones dobles para conceptos difíciles
- Más práctica guiada
- Reducir alcance de proyectos finales

**Para grupos mixtos** (niveles diferentes):
- Sistema de "achievements" opcionales
- Peer teaching (avanzados ayudan a otros)
- Proyectos con niveles escalables

## 🎓 Certificación Final

Al completar las 24 sesiones, estudiantes reciben:

**Certificado Digital "CodeGol Graduate"** que incluye:
- Nombre completo del estudiante
- 24 sesiones completadas
- Lista de proyectos en portfolio
- Skills aprendidas
- Próximos pasos recomendados

**Portfolio incluye**:
- 24 proyectos completados
- Proyecto final destacado
- Badges obtenidos
- Líneas de código escritas (~2000+)

---

## 🚀 ¿Qué Sigue Después?

### Módulos de Extensión (Post-graduación):

**Nivel 2: Web Developer Junior**
- Flask para web apps
- HTML/CSS básico
- Desplegar en internet

**Nivel 2: Data Scientist Junior**
- Pandas para datos
- Matplotlib para gráficos
- Análisis de estadísticas reales

**Nivel 2: Game Developer Junior**
- Pygame para juegos visuales
- Sprites y animaciones
- Juegos más complejos

**Nivel 2: Bot Creator**
- Telegram/Discord bots
- Automatización simple
- Proyectos creativos

---

**Este curriculum es un organismo vivo. Mejora con cada cohorte. Documenta tus ajustes. 🚀⚽**
