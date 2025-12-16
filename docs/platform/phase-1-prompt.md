# 🚀 EduFlow - Fase 1: MVP Development Prompt

## 📋 Contexto

Estás desarrollando **EduFlow Fase 1**: un MVP de plataforma de gestión de aprendizaje para el curso **CodeGol** (Python para niños mediante fútbol).

**Objetivo de Fase 1**: Sistema básico funcional para gestionar 10-20 estudiantes y 24 lecciones del curso CodeGol.

**Duración estimada**: 4-6 semanas desarrollo

**Usuario piloto**: 2 niños de 8-14 años + 1 instructor

---

## 🎯 Features de Fase 1

### ✅ DEBE TENER (Must-Have)

#### 1. Autenticación Básica
- [ ] Registro de usuarios (estudiante/instructor)
- [ ] Login con email + contraseña
- [ ] JWT tokens en HTTP-only cookies
- [ ] Logout
- [ ] Middleware de autenticación

#### 2. Gestión de Estudiantes
- [ ] Perfil de estudiante
- [ ] Vista de progreso personal
- [ ] Lista de lecciones disponibles
- [ ] XP total y nivel
- [ ] Badges obtenidos

#### 3. Gestión de Lecciones
- [ ] CRUD de cursos (solo instructor/admin)
- [ ] CRUD de lecciones
- [ ] Visualización de contenido (markdown)
- [ ] Lista de ejercicios por lección
- [ ] Código starter descargable

#### 4. Sistema de Progreso
- [ ] Marcar lección como "iniciada"
- [ ] Marcar lección como "completada"
- [ ] Tracking de tiempo por lección
- [ ] Porcentaje de progreso general
- [ ] Historial de actividad

#### 5. Badges Básicos
- [ ] 6 badges predefinidos:
  - 🥇 Primer Programa
  - 🔄 Loop Master
  - ⚙️ Ingeniero de Funciones
  - 🌐 Conectado al Mundo
  - 💾 Guardián de Datos
  - 🌟 CodeGol Graduate
- [ ] Otorgamiento manual por instructor
- [ ] Vista de badges en perfil

#### 6. Dashboard Instructor
- [ ] Lista de estudiantes del cohort
- [ ] Progreso de cada estudiante (%)
- [ ] Última actividad
- [ ] Otorgar badges manualmente
- [ ] Vista general del cohort

### 🟡 DESEABLE (Should-Have)

- [ ] Evaluación de código básica (Pyodide)
- [ ] Sistema de XP automático
- [ ] Leaderboard simple
- [ ] Notificaciones por email (completó lección, badge)

### ⚪ NO INCLUIR (Fase 2+)

- ❌ Tests unitarios automáticos (Fase 2)
- ❌ Feedback inteligente (Fase 2)
- ❌ Gamificación avanzada (Fase 3)
- ❌ Analytics ML (Fase 4)
- ❌ Multi-curso (Fase 5)

---

## 🏗️ Arquitectura Fase 1 (Simplificada)

```
┌─────────────────────────────────┐
│   Frontend (React + Vite)       │
│   - Student Portal              │
│   - Instructor Dashboard        │
└────────────┬────────────────────┘
             │ REST API
┌────────────▼────────────────────┐
│   Backend (FastAPI)             │
│   - Auth endpoints              │
│   - Student endpoints           │
│   - Course endpoints            │
│   - Progress endpoints          │
└────────────┬────────────────────┘
             │
    ┌────────┼────────┐
    │        │        │
┌───▼───┐ ┌──▼──┐ ┌──▼──┐
│ PostgreSQL │ Redis │ S3  │
│ (Main)  │ (Cache)│(Assets)
└────────┘ └─────┘ └─────┘
```

---

## 🗄️ Schema de Base de Datos (Fase 1)

```sql
-- USUARIOS Y AUTENTICACIÓN
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(200) UNIQUE NOT NULL,
    password_hash VARCHAR(200) NOT NULL,
    role VARCHAR(50) NOT NULL, -- 'student' | 'instructor' | 'admin'
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ESTUDIANTES
CREATE TABLE students (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) UNIQUE,
    full_name VARCHAR(200) NOT NULL,
    date_of_birth DATE,
    cohort_id UUID REFERENCES cohorts(id),
    xp_total INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- COHORTES (Grupos de estudiantes)
CREATE TABLE cohorts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(200) NOT NULL,
    course_id UUID REFERENCES courses(id),
    instructor_id UUID REFERENCES users(id),
    start_date DATE,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- CURSOS
CREATE TABLE courses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(200) NOT NULL,
    description TEXT,
    total_sessions INTEGER,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- LECCIONES
CREATE TABLE lessons (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    course_id UUID REFERENCES courses(id) ON DELETE CASCADE,
    session_number INTEGER NOT NULL,
    title VARCHAR(300) NOT NULL,
    description TEXT,
    content_markdown TEXT, -- Contenido completo
    estimated_duration INTEGER, -- minutos
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(course_id, session_number)
);

-- PROGRESO DE ESTUDIANTES
CREATE TABLE student_progress (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
    status VARCHAR(50) DEFAULT 'not_started', -- 'not_started' | 'in_progress' | 'completed'
    time_spent_minutes INTEGER DEFAULT 0,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    last_accessed_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(student_id, lesson_id)
);

-- BADGES
CREATE TABLE badge_types (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(200) UNIQUE NOT NULL,
    description TEXT,
    icon_emoji VARCHAR(10), -- '🥇', '🔄', etc.
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE student_badges (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    badge_type_id UUID REFERENCES badge_types(id),
    awarded_by UUID REFERENCES users(id), -- Instructor que otorgó
    earned_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(student_id, badge_type_id)
);

-- ÍNDICES
CREATE INDEX idx_progress_student ON student_progress(student_id, status);
CREATE INDEX idx_lessons_course ON lessons(course_id, session_number);
CREATE INDEX idx_students_cohort ON students(cohort_id);
CREATE INDEX idx_badges_student ON student_badges(student_id);
```

---

## 📡 API Endpoints (Fase 1)

### Autenticación
```
POST   /api/v1/auth/register
POST   /api/v1/auth/login
POST   /api/v1/auth/logout
GET    /api/v1/auth/me
```

### Estudiantes
```
GET    /api/v1/students/{id}
GET    /api/v1/students/{id}/progress
GET    /api/v1/students/{id}/badges
PUT    /api/v1/students/{id}
```

### Cursos y Lecciones
```
GET    /api/v1/courses
GET    /api/v1/courses/{id}
GET    /api/v1/courses/{id}/lessons
GET    /api/v1/lessons/{id}
POST   /api/v1/lessons               # Instructor only
PUT    /api/v1/lessons/{id}          # Instructor only
```

### Progreso
```
POST   /api/v1/progress/start        # Marcar lección iniciada
POST   /api/v1/progress/complete     # Marcar lección completada
GET    /api/v1/progress/{student_id} # Vista completa de progreso
```

### Badges
```
GET    /api/v1/badges                # Listar tipos de badges
POST   /api/v1/badges/award          # Otorgar badge (instructor only)
GET    /api/v1/badges/student/{id}   # Badges de un estudiante
```

### Dashboard Instructor
```
GET    /api/v1/instructor/cohort/{id}/students
GET    /api/v1/instructor/cohort/{id}/overview
```

---

## 🎨 Páginas Frontend (Fase 1)

### Student Portal

```
/login
/register
/dashboard                    # Vista general estudiante
/lessons                      # Lista de lecciones
/lessons/{id}                 # Detalle lección + contenido
/profile                      # Perfil + badges + stats
```

### Instructor Dashboard

```
/instructor/dashboard         # Vista general del cohort
/instructor/students          # Lista de estudiantes
/instructor/students/{id}     # Detalle de estudiante
/instructor/lessons           # Gestión de lecciones
/instructor/lessons/new       # Crear lección
/instructor/lessons/{id}/edit # Editar lección
```

---

## 🔨 Código Base Inicial

### Backend Structure

```
/backend
├── /app
│   ├── main.py                 # FastAPI app
│   ├── /api
│   │   ├── /v1
│   │   │   ├── /endpoints
│   │   │   │   ├── auth.py
│   │   │   │   ├── students.py
│   │   │   │   ├── courses.py
│   │   │   │   ├── lessons.py
│   │   │   │   ├── progress.py
│   │   │   │   └── badges.py
│   │   │   └── router.py
│   ├── /core
│   │   ├── config.py           # Settings
│   │   ├── security.py         # JWT, hashing
│   │   └── database.py         # DB connection
│   ├── /models
│   │   ├── user.py
│   │   ├── student.py
│   │   ├── course.py
│   │   ├── lesson.py
│   │   └── badge.py
│   ├── /schemas
│   │   ├── user.py             # Pydantic models
│   │   ├── student.py
│   │   └── ...
│   └── /services
│       ├── auth_service.py
│       ├── student_service.py
│       └── ...
├── /tests
├── pyproject.toml
└── .env.example
```

### Frontend Structure

```
/frontend
├── /src
│   ├── main.jsx
│   ├── App.jsx
│   ├── /components
│   │   ├── /common
│   │   │   ├── Navbar.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   └── Loading.jsx
│   │   ├── /student
│   │   │   ├── LessonCard.jsx
│   │   │   ├── ProgressBar.jsx
│   │   │   ├── BadgeDisplay.jsx
│   │   │   └── Dashboard.jsx
│   │   └── /instructor
│   │       ├── StudentList.jsx
│   │       ├── StudentDetail.jsx
│   │       └── CohortOverview.jsx
│   ├── /pages
│   │   ├── Login.jsx
│   │   ├── Register.jsx
│   │   ├── /student
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Lessons.jsx
│   │   │   ├── LessonDetail.jsx
│   │   │   └── Profile.jsx
│   │   └── /instructor
│   │       ├── Dashboard.jsx
│   │       ├── Students.jsx
│   │       └── LessonManagement.jsx
│   ├── /services
│   │   └── api.js              # Axios instance
│   ├── /store
│   │   ├── authStore.js        # Zustand
│   │   └── studentStore.js
│   └── /utils
│       ├── auth.js
│       └── formatting.js
├── package.json
├── vite.config.js
└── tailwind.config.js
```

---

## 💻 Código de Ejemplo

### Backend: Auth Endpoint

```python
# app/api/v1/endpoints/auth.py
from fastapi import APIRouter, HTTPException, Response, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import create_access_token, verify_password, get_password_hash
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.models.user import User

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create user
    hashed_password = get_password_hash(user_data.password)
    user = User(
        email=user_data.email,
        password_hash=hashed_password,
        role=user_data.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

@router.post("/login")
async def login(credentials: UserLogin, response: Response, db: Session = Depends(get_db)):
    # Verify credentials
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user or not verify_password(credentials.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create token
    access_token = create_access_token(data={"sub": str(user.id), "role": user.role})

    # Set HTTP-only cookie
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=1800  # 30 minutes
    )

    return {"status": "success", "user": {"id": user.id, "email": user.email, "role": user.role}}

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {"status": "success"}
```

### Frontend: Student Dashboard

```jsx
// src/pages/student/Dashboard.jsx
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../../services/api';
import ProgressBar from '../../components/student/ProgressBar';
import BadgeDisplay from '../../components/student/BadgeDisplay';
import LessonCard from '../../components/student/LessonCard';

export default function StudentDashboard() {
    const [student, setStudent] = useState(null);
    const [progress, setProgress] = useState(null);
    const [recentLessons, setRecentLessons] = useState([]);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        fetchDashboardData();
    }, []);

    async function fetchDashboardData() {
        try {
            const [studentRes, progressRes, lessonsRes] = await Promise.all([
                api.get('/students/me'),
                api.get('/students/me/progress'),
                api.get('/lessons?recent=5')
            ]);

            setStudent(studentRes.data);
            setProgress(progressRes.data);
            setRecentLessons(lessonsRes.data);
        } catch (error) {
            console.error('Failed to load dashboard:', error);
        } finally {
            setLoading(false);
        }
    }

    if (loading) return <div className="flex justify-center p-8"><Spinner /></div>;

    return (
        <div className="container mx-auto px-4 py-8">
            {/* Header */}
            <div className="bg-white rounded-lg shadow-md p-6 mb-6">
                <h1 className="text-3xl font-bold text-gray-800">
                    ¡Hola, {student.full_name}! ⚽
                </h1>
                <p className="text-gray-600 mt-2">
                    Nivel {student.level} • {student.xp_total} XP
                </p>
            </div>

            {/* Progress Overview */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
                <div className="bg-white rounded-lg shadow p-6">
                    <h3 className="text-lg font-semibold mb-2">Progreso General</h3>
                    <ProgressBar
                        current={progress.lessons_completed}
                        total={progress.lessons_total}
                    />
                    <p className="text-sm text-gray-600 mt-2">
                        {progress.lessons_completed} de {progress.lessons_total} lecciones
                    </p>
                </div>

                <div className="bg-white rounded-lg shadow p-6">
                    <h3 className="text-lg font-semibold mb-2">Experiencia</h3>
                    <div className="text-3xl font-bold text-blue-600">
                        {student.xp_total} XP
                    </div>
                    <p className="text-sm text-gray-600 mt-2">
                        Nivel {student.level}
                    </p>
                </div>

                <div className="bg-white rounded-lg shadow p-6">
                    <h3 className="text-lg font-semibold mb-2">Badges</h3>
                    <BadgeDisplay badges={progress.badges} limit={3} />
                    <button
                        onClick={() => navigate('/profile')}
                        className="text-sm text-blue-600 hover:underline mt-2"
                    >
                        Ver todos →
                    </button>
                </div>
            </div>

            {/* Recent Lessons */}
            <div className="bg-white rounded-lg shadow-md p-6">
                <h2 className="text-2xl font-bold mb-4">Continúa Aprendiendo</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {recentLessons.map(lesson => (
                        <LessonCard
                            key={lesson.id}
                            lesson={lesson}
                            progress={progress.lessons[lesson.id]}
                        />
                    ))}
                </div>
            </div>
        </div>
    );
}
```

---

## ✅ Checklist de Desarrollo

### Semana 1: Setup + Auth
- [ ] Setup repo (backend + frontend)
- [ ] Configurar PostgreSQL + Redis
- [ ] Implementar modelos de DB
- [ ] Crear migraciones (Alembic)
- [ ] Implementar auth endpoints
- [ ] Implementar login/register frontend
- [ ] JWT funcionando end-to-end

### Semana 2: Student Management
- [ ] CRUD estudiantes (backend)
- [ ] Perfil de estudiante (frontend)
- [ ] Sistema de progreso (backend)
- [ ] Dashboard estudiante (frontend)
- [ ] Vista de lecciones (frontend)

### Semana 3: Course Management
- [ ] CRUD cursos y lecciones (backend)
- [ ] Renderizado de markdown (frontend)
- [ ] Gestión de lecciones instructor (frontend)
- [ ] Sistema de archivos/assets

### Semana 4: Badges + Polish
- [ ] Sistema de badges (backend)
- [ ] Badges en perfil (frontend)
- [ ] Dashboard instructor (frontend)
- [ ] Otorgar badges (instructor)
- [ ] Polish UI/UX
- [ ] Bug fixes

### Semana 5-6: Testing + Deploy
- [ ] Tests unitarios backend (pytest)
- [ ] Tests e2e frontend (Vitest)
- [ ] Deploy backend (Railway/Fly.io)
- [ ] Deploy frontend (Vercel)
- [ ] Setup CI/CD (GitHub Actions)
- [ ] Monitoring (Sentry)
- [ ] Documentación

---

## 🎯 Criterios de Éxito Fase 1

**Functionality**:
- [ ] Instructor puede crear 24 lecciones CodeGol
- [ ] Estudiante puede ver lecciones y marcar progreso
- [ ] Progreso se trackea correctamente
- [ ] Badges se otorgan y muestran
- [ ] Dashboard instructor muestra progreso de estudiantes

**Performance**:
- [ ] Page load < 2s
- [ ] API responses < 200ms (p95)

**UX**:
- [ ] Mobile-responsive
- [ ] Navegación intuitiva
- [ ] Feedback claro de acciones

**Deploy**:
- [ ] En producción y accesible
- [ ] HTTPS configurado
- [ ] Backup de DB automático

---

## 🚀 Comandos de Inicio Rápido

### Backend

```bash
# Setup
cd backend
poetry install
cp .env.example .env  # Configurar variables

# Crear DB
poetry run alembic upgrade head

# Seed data (opcional)
poetry run python scripts/seed_codegol.py

# Run dev server
poetry run uvicorn app.main:app --reload

# Run tests
poetry run pytest
```

### Frontend

```bash
# Setup
cd frontend
pnpm install

# Run dev server
pnpm dev

# Build para producción
pnpm build

# Run tests
pnpm test
```

---

## 📚 Recursos

- **Backend docs**: FastAPI tiene excelente documentación oficial
- **Frontend**: React docs + TailwindCSS docs
- **DB**: PostgreSQL docs para queries complejas
- **Deployment**: Railway/Fly.io tienen tutoriales step-by-step

---

## 🎉 ¿Listo para Construir?

1. Lee completa esta especificación
2. Setup el proyecto base
3. Sigue el checklist semana por semana
4. Haz commits frecuentes
5. Deploy early y frecuentemente
6. Pide feedback de usuarios reales

**¡A programar! 🚀⚽💻**
