# ⚽ CodeGol - Aprende Python Jugando con Fútbol

**Curso progresivo de Python para niños 8-14 años usando datos del fútbol mundial**

## 🎯 Visión del Proyecto

**CodeGol** es un curso de programación Python diseñado específicamente para niños de países en desarrollo, que combina:
- 🎮 Gamificación adictiva basada en fútbol
- 📚 Pedagogía probada y progresiva
- 🌍 Funciona sin internet confiable (offline-first)
- 🚀 Resultados visibles en cada sesión
- 📊 Plataforma de gestión escalable

## 📁 Estructura del Proyecto

```
/pipi
├── /docs                          # Documentación completa
│   ├── /course                    # Documentación del curso
│   │   ├── README.md              # Visión general del curso
│   │   ├── curriculum.md          # Programa completo 24 sesiones
│   │   ├── pedagogy.md            # Metodología y teoría pedagógica
│   │   └── /lessons               # Guías detalladas por lección
│   │       ├── lesson-01.md
│   │       ├── lesson-02.md
│   │       └── ...
│   └── /platform                  # Documentación de la plataforma
│       ├── README.md              # Visión de la plataforma
│       ├── architecture.md        # Arquitectura técnica
│       ├── roadmap.md             # Fases de desarrollo
│       ├── tech-stack.md          # Stack tecnológico
│       └── phase-1-prompt.md      # Prompt para desarrollo fase 1
│
├── /course-materials              # Materiales listos para usar
│   ├── /lesson-01                 # Primera lección completa
│   │   ├── instructor-guide.md    # Guía del instructor
│   │   ├── student-workbook.md    # Cuaderno del estudiante
│   │   ├── /code-examples         # Código de ejemplo
│   │   ├── /exercises             # Ejercicios prácticos
│   │   └── /assets                # Imágenes, recursos
│   ├── /lesson-02
│   ├── ...
│   └── /datasets                  # Datos offline de fútbol
│       └── football-data.json
│
└── /src                           # Código de la plataforma
    └── /platform                  # (Se desarrollará en fases)
```

## 🚀 Quick Start

### Para Instructores (Primeras Clases)

1. **Lee la documentación del curso**:
   ```bash
   docs/course/README.md           # Empieza aquí
   docs/course/curriculum.md        # Programa completo
   docs/course/pedagogy.md          # Metodología
   ```

2. **Prepara la Lección 1**:
   ```bash
   course-materials/lesson-01/instructor-guide.md
   ```

3. **Configura el entorno de los estudiantes**:
   - Python 3.8+ instalado
   - Editor: Thonny o IDLE
   - Copia `course-materials/datasets/` a cada PC

### Para Desarrolladores (Plataforma)

1. **Lee la arquitectura**:
   ```bash
   docs/platform/README.md
   docs/platform/architecture.md
   docs/platform/roadmap.md
   ```

2. **Sigue el prompt de Fase 1**:
   ```bash
   docs/platform/phase-1-prompt.md
   ```

## 📊 Fases del Proyecto

### ✅ Fase 0: Diseño y Documentación (ACTUAL)
- Documentación completa del curso
- Materiales de primeras 4 lecciones
- Arquitectura de plataforma
- Dataset de fútbol offline

### 🎯 Fase 1: Piloto del Curso (Semanas 1-4)
- Probar con 2 niños reales
- Iterar lecciones 1-8
- Validar metodología
- Recoger feedback

### 🏗️ Fase 2: MVP de Plataforma (Mes 2)
- Sistema de gestión de estudiantes
- Tracking de progreso
- Evaluación automática básica
- Dashboard instructor

### 🚀 Fase 3: Escalado (Mes 3-4)
- Completar 24 lecciones
- Gamificación completa
- Multi-instructor
- Analytics avanzado

### 🌍 Fase 4: Generalización (Mes 5+)
- Plataforma multi-curso
- Marketplace de contenidos
- Adaptación IA
- Expansión internacional

## 🎓 El Curso: CodeGol

**24 sesiones | 12 semanas | 2 sesiones/semana | 60 min/sesión**

### Fases del Aprendizaje:
1. **Primeros Pasos** (6 sesiones) - Variables, condicionales, loops
2. **Constructor de Juegos** (6 sesiones) - Listas, funciones, lógica
3. **Conectando con el Mundo** (6 sesiones) - APIs, JSON, internet
4. **Creadores de Experiencias** (6 sesiones) - Proyectos finales

Ver detalles completos en: `docs/course/curriculum.md`

## 🏗️ La Plataforma: EduFlow

**Sistema modular de gestión de aprendizaje escalable**

### Módulos Core:
- 📚 Gestión de Cursos
- 👥 Gestión de Estudiantes
- 🧪 Evaluación Automática
- 📊 Analytics
- 🎮 Gamificación
- 🔌 Extensiones

Ver arquitectura completa en: `docs/platform/architecture.md`

## 🌟 APIs de Fútbol Utilizadas

### Principales:
- **API-Football** (api-football.com) - Datos en tiempo real
- **TheSportsDB** (thesportsdb.com) - Datos históricos gratuitos
- **Football-Data.org** - Competiciones europeas

### Estrategia Offline-First:
- Dataset pre-cargado con 1000+ jugadores
- Datos de ligas: La Liga, Premier, Bundesliga, Serie A, Libertadores
- Estadísticas históricas de Copas del Mundo
- Funciona 100% offline con fallback a APIs online

## 🤝 Contribuir

Este proyecto está diseñado para crecer. Áreas donde puedes contribuir:

1. **Contenido del Curso**:
   - Nuevas lecciones
   - Ejercicios adicionales
   - Traducciones

2. **Plataforma**:
   - Nuevos módulos
   - Mejoras de UI/UX
   - Tests

3. **Datasets**:
   - Más datos de fútbol
   - Otros deportes
   - Temas no deportivos

## 📞 Contacto

- **Proyecto**: CodeGol - Python para niños
- **Objetivo**: Educación tecnológica accesible en países en desarrollo
- **Status**: Fase 0 - Diseño y Documentación

---

**Próximo paso**: Lee `docs/course/README.md` para empezar con el curso, o `docs/platform/README.md` para la plataforma.
