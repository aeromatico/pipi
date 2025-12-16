# 🏗️ EduFlow - Plataforma de Gestión de Aprendizaje

## 🎯 Visión

**EduFlow** es una plataforma modular de gestión de aprendizaje (LMS) diseñada para:

1. **Corto plazo** (Meses 1-3): Gestionar el curso CodeGol
2. **Mediano plazo** (Meses 4-6): Escalar a múltiples cursos de tecnología
3. **Largo plazo** (Mes 7+): Convertirse en plataforma de e-learning general

## 🌟 Diferenciadores Clave

### 1. **Pedagógico desde el Diseño**
No es un LMS genérico adaptado. Cada feature está diseñado con pedagogía en mente:
- Evaluación formativa continua
- Feedback inmediato
- Diferenciación por niveles
- Gamificación intrínseca

### 2. **Modular y Escalable**
Arquitectura de microservicios que permite:
- Agregar módulos independientemente
- Escalar componentes según demanda
- Reutilizar entre diferentes tipos de cursos

### 3. **Offline-First**
Funciona en contextos de conectividad limitada:
- Sincronización inteligente
- Caché local
- Modo completamente offline

### 4. **Datos para Mejorar**
Analytics no solo para reportes, sino para:
- Identificar dificultades comunes
- Adaptar contenido
- Personalizar experiencia

### 5. **Open Architecture**
API pública para:
- Marketplace de contenidos
- Integraciones terceros
- Extensibilidad infinita

## 📊 Fases de Desarrollo

### **Fase 0: Piloto Manual** (Actual)
- ✅ Documentación completa
- ✅ Materiales de curso
- 🎯 Probar con 2 niños
- 📝 Google Sheets para tracking

**Objetivo**: Validar metodología sin plataforma

---

### **Fase 1: MVP Core** (Mes 1-2)
**Objetivo**: Gestión básica de CodeGol

**Módulos**:
- 👥 Gestión de estudiantes
- 📚 Gestión de lecciones
- 📊 Tracking de progreso básico
- 🎮 Sistema de badges simple

**Stack**:
- Backend: FastAPI (Python)
- Frontend: React + TailwindCSS
- DB: PostgreSQL
- Auth: JWT simple

**Métricas de éxito**:
- Instructor puede ver progreso de 10 estudiantes
- Estudiantes ven su portfolio
- Sistema de badges funciona

Ver: `phase-1-prompt.md` para desarrollo

---

### **Fase 2: Evaluación Inteligente** (Mes 2-3)
**Objetivo**: Auto-corrección de código

**Features Nuevas**:
- ✅ Sandbox de código (Pyodide)
- ✅ Tests unitarios automáticos
- ✅ Feedback instantáneo
- ✅ Hints progresivos

**Tecnologías**:
- Pyodide (Python en navegador)
- Judge0 API (alternativa)
- Sistema de hints basado en errores comunes

**Métricas de éxito**:
- 70%+ de ejercicios auto-evaluados
- Estudiantes reciben feedback < 1 segundo
- Reducción 50% en tiempo de corrección manual

---

### **Fase 3: Gamificación Avanzada** (Mes 3-4)
**Objetivo**: Engagement máximo

**Features Nuevas**:
- 🎮 Sistema XP completo
- 🏆 Leaderboards múltiples
- 🔥 Streaks y rachas
- 🤝 Desafíos entre estudiantes
- 🎯 Metas personalizadas

**Integración**:
- Notificaciones push
- Emails de achievements
- Dashboard gamificado

**Métricas de éxito**:
- 80%+ tasa de completado de lecciones
- Engagement diario > 15 min
- Satisfacción > 4.5/5

---

### **Fase 4: Analytics & AI** (Mes 4-5)
**Objetivo**: Insights accionables

**Features Nuevas**:
- 📈 Dashboard instructor avanzado
- 🎯 Identificación automática de dificultades
- 🤖 Sugerencias de intervención
- 📊 Reportes personalizados

**ML Features**:
- Predicción de estudiantes en riesgo
- Recomendación de contenido
- Agrupación automática por nivel

**Métricas de éxito**:
- Instructor identifica problemas en < 5 min
- Tasa de éxito aumenta 20%
- Satisfacción instructor > 4.7/5

---

### **Fase 5: Multi-Curso** (Mes 5-6)
**Objetivo**: Escalar a múltiples cursos

**Features Nuevas**:
- 📚 Creador de cursos (no-code)
- 🎨 Templates reutilizables
- 🔄 Import/export contenido
- 🏪 Marketplace interno

**Arquitectura**:
- Separación completa curso/plataforma
- Schema flexible para diferentes materias
- Sistema de tags y metadata

**Métricas de éxito**:
- 3+ cursos activos en plataforma
- Instructor crea curso nuevo en < 4 horas
- Reutilización de módulos > 60%

---

### **Fase 6: Generalización** (Mes 7+)
**Objetivo**: E-learning universal

**Features Nuevas**:
- 🌍 Multi-idioma
- 🎓 Multi-nivel (primaria, secundaria, universidad)
- 📝 Multi-formato (video, texto, interactivo)
- 👨‍🏫 Multi-instructor
- 🏢 Multi-tenant (organizaciones)

**Marketplace**:
- Creadores de contenido independientes
- Sistema de revenue share
- Certificaciones oficiales

**Métricas de éxito**:
- 10+ organizaciones usando plataforma
- 5+ cursos no tecnológicos
- 1000+ estudiantes activos

---

## 🏗️ Arquitectura High-Level

```
┌─────────────────────────────────────────────────────┐
│                   FRONTEND (React)                  │
├───────────────┬─────────────────┬───────────────────┤
│   Student     │   Instructor    │     Admin         │
│   Portal      │   Dashboard     │     Panel         │
└───────┬───────┴────────┬────────┴──────┬────────────┘
        │                │               │
        └────────────────┼───────────────┘
                         │
                ┌────────▼────────┐
                │   API Gateway   │
                │   (FastAPI)     │
                └────────┬────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
┌───────▼───────┐ ┌─────▼──────┐ ┌──────▼───────┐
│   Course      │ │  Student   │ │ Evaluation   │
│   Service     │ │  Service   │ │  Service     │
└───────┬───────┘ └─────┬──────┘ └──────┬───────┘
        │               │               │
        └───────────────┼───────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
┌───────▼────┐  ┌──────▼──────┐  ┌─────▼─────┐
│ PostgreSQL │  │    Redis    │  │   S3/     │
│  (Main DB) │  │   (Cache)   │  │  Storage  │
└────────────┘  └─────────────┘  └───────────┘
```

Ver: `architecture.md` para detalles técnicos

---

## 🎯 Módulos Core

### 1. **Course Management** 📚
Gestión completa de cursos:
- Creación de lecciones
- Organización de contenido
- Versionado de materiales
- Templates reutilizables

**Tech**: PostgreSQL + S3 para assets

---

### 2. **Student Management** 👥
Gestión de estudiantes:
- Registro y perfiles
- Tracking de progreso
- Portfolio de proyectos
- Historial completo

**Tech**: PostgreSQL + Redis para sesiones

---

### 3. **Evaluation Engine** 🧪
Auto-evaluación de código:
- Sandbox seguro
- Tests unitarios
- Feedback instantáneo
- Anti-plagio básico

**Tech**: Pyodide / Judge0 + Queue system

---

### 4. **Analytics** 📊
Inteligencia de datos:
- Dashboard tiempo real
- Reportes automáticos
- Identificación de patrones
- Alertas proactivas

**Tech**: PostgreSQL + Pandas + Charts.js

---

### 5. **Gamification** 🎮
Sistema de engagement:
- XP y niveles
- Badges y achievements
- Leaderboards
- Desafíos

**Tech**: Redis para rankings + PostgreSQL para persistencia

---

### 6. **Notifications** 📧
Sistema de comunicación:
- Emails transaccionales
- Push notifications
- In-app notifications
- Resúmenes diarios/semanales

**Tech**: SendGrid + Firebase Cloud Messaging

---

## 🔌 API Pública

### Endpoints Principales:

```
POST   /api/v1/students          # Crear estudiante
GET    /api/v1/students/{id}     # Obtener info

GET    /api/v1/courses           # Listar cursos
GET    /api/v1/courses/{id}      # Detalle curso

POST   /api/v1/submissions       # Enviar ejercicio
GET    /api/v1/submissions/{id}  # Resultado evaluación

GET    /api/v1/progress/{id}     # Progreso estudiante
GET    /api/v1/badges/{id}       # Badges obtenidos

# ... ver docs/platform/api-spec.md
```

**Autenticación**: JWT Bearer tokens

---

## 💾 Modelo de Datos Core

```sql
-- Estudiantes
students (
  id, name, email, cohort_id,
  xp_total, level, created_at
)

-- Cursos
courses (
  id, name, description, difficulty,
  total_sessions, created_at
)

-- Lecciones
lessons (
  id, course_id, session_number,
  title, content, objectives
)

-- Progreso
progress (
  id, student_id, lesson_id,
  status, completed_at, attempts
)

-- Badges
badges (
  id, student_id, badge_type,
  earned_at, metadata
)

-- Submissions (Entregas)
submissions (
  id, student_id, exercise_id,
  code, status, score, feedback
)
```

Ver: `architecture.md` para schema completo

---

## 🚀 Tech Stack

**Ver**: `tech-stack.md` para decisiones detalladas

### Backend
- **Framework**: FastAPI (Python)
- **DB**: PostgreSQL 15+
- **Cache**: Redis
- **Queue**: Celery (para evaluaciones async)

### Frontend
- **Framework**: React 18+
- **Styling**: TailwindCSS
- **State**: Zustand (simple) o Redux (si crece)
- **Charts**: Chart.js / Recharts

### DevOps
- **Hosting**: DigitalOcean / Railway / Fly.io
- **CI/CD**: GitHub Actions
- **Monitoring**: Sentry + Simple Analytics
- **Logs**: Papertrail

### Evaluación de Código
- **Sandbox**: Pyodide (Python en browser)
- **Alternativa**: Judge0 API
- **Seguridad**: Timeout + resource limits

---

## 📐 Principios de Diseño

### 1. **Mobile-First pero Desktop-Optimized**
Estudiantes pueden revisar en móvil, pero programan en desktop.

### 2. **Progressive Enhancement**
Funciona sin JS, mejora con JS. Offline-capable.

### 3. **Accessibility (a11y)**
WCAG 2.1 AA mínimo. Keyboard navigation completa.

### 4. **Performance**
- Tiempo de carga < 2s
- Interactions < 100ms
- Evaluaciones < 3s

### 5. **Security**
- Input sanitization
- SQL injection prevention
- XSS protection
- Rate limiting

---

## 📊 Métricas de Plataforma

### KPIs Fase por Fase:

**Fase 1**:
- [ ] 10 estudiantes gestionados
- [ ] 100% uptime
- [ ] < 2s page load

**Fase 2**:
- [ ] 100 evaluaciones auto-corregidas
- [ ] 90% accuracy en feedback
- [ ] < 3s evaluation time

**Fase 3**:
- [ ] 80% engagement rate
- [ ] 50+ badges distribuidos
- [ ] 4.5+ satisfacción

**Fase 4**:
- [ ] 5+ insights accionables/semana
- [ ] 20% mejora en tasas de éxito

**Fase 5**:
- [ ] 3+ cursos activos
- [ ] Curso nuevo en < 4 horas

**Fase 6**:
- [ ] 10+ organizaciones
- [ ] 1000+ estudiantes activos
- [ ] $10K+ MRR

---

## 🤝 Contribución

Este es un proyecto open-source (licencia pendiente de definir).

**Áreas de contribución**:
- 🐛 Bug fixes
- ✨ Nuevas features
- 📚 Documentación
- 🎨 Diseño UI/UX
- 🧪 Tests
- 🌍 Traducciones

Ver: `CONTRIBUTING.md` (próximamente)

---

## 📚 Siguientes Pasos

1. **Para Desarrolladores**: Lee `architecture.md` y `tech-stack.md`
2. **Para Empezar Fase 1**: Ve a `phase-1-prompt.md`
3. **Para API**: Revisa `api-spec.md`
4. **Para Roadmap Detallado**: Lee `roadmap.md`

---

## 📞 Contacto

**Proyecto**: CodeGol → EduFlow
**Status**: Fase 0 - Diseño
**Próximo Hito**: Piloto manual con 2 estudiantes

---

**¿Listo para construir el futuro de la educación? 🚀📚**
