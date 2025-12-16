# 🏗️ EduFlow - Arquitectura Técnica Detallada

## 📋 Tabla de Contenidos

1. [Visión General](#visión-general)
2. [Arquitectura de Alto Nivel](#arquitectura-de-alto-nivel)
3. [Componentes Principales](#componentes-principales)
4. [Modelo de Datos](#modelo-de-datos)
5. [Flujos de Datos](#flujos-de-datos)
6. [Seguridad](#seguridad)
7. [Escalabilidad](#escalabilidad)
8. [Offline-First Strategy](#offline-first-strategy)

---

## 🎯 Visión General

### Principios Arquitectónicos

1. **Modularidad**: Cada módulo es independiente y reemplazable
2. **Escalabilidad**: Crece horizontal y verticalmente
3. **Mantenibilidad**: Código limpio, documentado, testeable
4. **Resilencia**: Falla gracefully, auto-recuperación
5. **Performance**: < 2s load, < 100ms interactions

### Patrón Arquitectónico

**Microservicios ligeros** con comunicación REST/gRPC

```
Ventajas:
✅ Desarrollo independiente por módulo
✅ Escala solo lo necesario
✅ Deploy independiente
✅ Stack heterogéneo si es necesario

Desventajas (mitigadas):
⚠️ Complejidad (minimizada con API Gateway)
⚠️ Testing (mitigado con contracts)
⚠️ Latencia (mitigada con cache)
```

---

## 🏛️ Arquitectura de Alto Nivel

### Diagrama de Capas

```
┌─────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Student    │  │  Instructor  │  │    Admin     │  │
│  │    Portal    │  │   Dashboard  │  │    Panel     │  │
│  │   (React)    │  │   (React)    │  │   (React)    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└────────────────────────┬────────────────────────────────┘
                         │ HTTPS / WebSocket
┌────────────────────────▼────────────────────────────────┐
│                     API GATEWAY                         │
│  ┌────────────────────────────────────────────────────┐ │
│  │  FastAPI + Nginx                                   │ │
│  │  - Routing                                         │ │
│  │  - Rate Limiting                                   │ │
│  │  - Authentication (JWT)                            │ │
│  │  - Request/Response logging                        │ │
│  └────────────────────────────────────────────────────┘ │
└────────────────────────┬────────────────────────────────┘
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
┌──────▼──────┐  ┌───────▼────────┐  ┌────▼─────────┐
│   COURSE    │  │    STUDENT     │  │  EVALUATION  │
│   SERVICE   │  │    SERVICE     │  │   SERVICE    │
└──────┬──────┘  └───────┬────────┘  └────┬─────────┘
       │                 │                 │
       │    ┌────────────┼────────────┐    │
       │    │            │            │    │
┌──────▼────▼──┐  ┌──────▼─────┐  ┌──▼────▼──────┐
│ GAMIFICATION │  │ ANALYTICS  │  │ NOTIFICATION │
│   SERVICE    │  │  SERVICE   │  │   SERVICE    │
└──────┬───────┘  └─────┬──────┘  └──┬───────────┘
       │                │             │
       └────────────────┼─────────────┘
                        │
       ┌────────────────┼─────────────────┐
       │                │                 │
┌──────▼──────┐  ┌──────▼──────┐  ┌──────▼──────┐
│ PostgreSQL  │  │    Redis    │  │   S3/Blob   │
│  (Primary)  │  │   (Cache)   │  │  (Assets)   │
└─────────────┘  └─────────────┘  └─────────────┘
```

---

## 🧩 Componentes Principales

### 1. API Gateway

**Responsabilidades**:
- Enrutamiento a servicios
- Autenticación y autorización
- Rate limiting
- Request/Response transformation
- Logging centralizado

**Tech Stack**:
```python
# FastAPI + Nginx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis

app = FastAPI(title="EduFlow API Gateway")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://eduflow.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate Limiting (Redis)
@app.on_event("startup")
async def startup():
    redis_conn = await redis.from_url("redis://localhost")
    await FastAPILimiter.init(redis_conn)

# Auth Middleware
from fastapi_jwt_auth import AuthJWT

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    # Verify JWT token
    # Inject user_id into request
    response = await call_next(request)
    return response
```

**Endpoints Core**:
```
/api/v1/
├── /auth
│   ├── POST /login
│   ├── POST /register
│   ├── POST /refresh
│   └── POST /logout
├── /students
│   ├── GET  /{id}
│   ├── PUT  /{id}
│   └── GET  /{id}/progress
├── /courses
│   ├── GET  /
│   ├── GET  /{id}
│   └── GET  /{id}/lessons
├── /lessons
│   ├── GET  /{id}
│   └── GET  /{id}/exercises
├── /submissions
│   ├── POST /
│   ├── GET  /{id}
│   └── GET  /{id}/feedback
├── /badges
│   └── GET  /student/{id}
└── /analytics
    ├── GET  /progress/{student_id}
    └── GET  /class/{cohort_id}
```

---

### 2. Course Service

**Responsabilidades**:
- CRUD de cursos
- Gestión de lecciones
- Organización de contenido
- Templates y versionado

**Modelo de Datos**:
```sql
-- Cursos
CREATE TABLE courses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(200) NOT NULL,
    description TEXT,
    difficulty VARCHAR(50), -- beginner/intermediate/advanced
    total_sessions INTEGER,
    language VARCHAR(10) DEFAULT 'es',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    created_by UUID REFERENCES users(id)
);

-- Lecciones
CREATE TABLE lessons (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    course_id UUID REFERENCES courses(id) ON DELETE CASCADE,
    session_number INTEGER NOT NULL,
    title VARCHAR(300) NOT NULL,
    description TEXT,
    objectives JSONB, -- ["obj1", "obj2", ...]
    content_markdown TEXT,
    estimated_duration INTEGER, -- minutos
    difficulty_level INTEGER, -- 1-5
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(course_id, session_number)
);

-- Ejercicios
CREATE TABLE exercises (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
    title VARCHAR(300) NOT NULL,
    description TEXT,
    starter_code TEXT,
    solution_code TEXT,
    test_cases JSONB, -- Array de tests
    difficulty_level INTEGER, -- 1-3 (básico/intermedio/avanzado)
    xp_reward INTEGER DEFAULT 10,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Assets (imágenes, archivos)
CREATE TABLE lesson_assets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
    asset_type VARCHAR(50), -- image/video/file
    asset_url VARCHAR(500),
    file_size_kb INTEGER,
    uploaded_at TIMESTAMPTZ DEFAULT NOW()
);
```

**API Endpoints**:
```python
from fastapi import APIRouter, Depends
from typing import List

router = APIRouter(prefix="/courses")

@router.get("/", response_model=List[CourseSchema])
async def list_courses(
    skip: int = 0,
    limit: int = 20,
    difficulty: Optional[str] = None
):
    # Retorna lista de cursos
    pass

@router.get("/{course_id}", response_model=CourseDetailSchema)
async def get_course(course_id: UUID):
    # Detalle completo del curso + lecciones
    pass

@router.post("/", response_model=CourseSchema)
async def create_course(
    course: CourseCreateSchema,
    current_user: User = Depends(get_current_user)
):
    # Solo instructores/admins
    pass
```

---

### 3. Student Service

**Responsabilidades**:
- Gestión de estudiantes
- Tracking de progreso
- Portfolio
- Preferencias y configuración

**Modelo de Datos**:
```sql
-- Estudiantes
CREATE TABLE students (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    full_name VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    date_of_birth DATE,
    cohort_id UUID REFERENCES cohorts(id),
    xp_total INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    streak_days INTEGER DEFAULT 0,
    last_active_at TIMESTAMPTZ,
    preferences JSONB, -- {"theme": "dark", "notifications": true}
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Cohortes (grupos de estudiantes)
CREATE TABLE cohorts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(200) NOT NULL,
    course_id UUID REFERENCES courses(id),
    instructor_id UUID REFERENCES users(id),
    start_date DATE,
    end_date DATE,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Progreso
CREATE TABLE student_progress (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
    status VARCHAR(50), -- not_started/in_progress/completed
    completion_percentage INTEGER DEFAULT 0,
    time_spent_minutes INTEGER DEFAULT 0,
    attempts INTEGER DEFAULT 0,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    last_accessed_at TIMESTAMPTZ,
    UNIQUE(student_id, lesson_id)
);

-- Portfolio (proyectos destacados)
CREATE TABLE portfolio_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    exercise_id UUID REFERENCES exercises(id),
    title VARCHAR(300),
    description TEXT,
    code TEXT,
    output_screenshot_url VARCHAR(500),
    is_featured BOOLEAN DEFAULT false,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

**API Endpoints**:
```python
router = APIRouter(prefix="/students")

@router.get("/{student_id}/progress")
async def get_student_progress(student_id: UUID):
    # Progreso completo del estudiante
    return {
        "overall_progress": 65,  # %
        "lessons_completed": 15,
        "lessons_total": 24,
        "xp_total": 1250,
        "level": 5,
        "streak_days": 12,
        "badges": [...],
        "recent_activity": [...]
    }

@router.get("/{student_id}/portfolio")
async def get_portfolio(student_id: UUID):
    # Portfolio de proyectos
    pass
```

---

### 4. Evaluation Service

**Responsabilidades**:
- Ejecución de código estudiante
- Correr tests unitarios
- Generar feedback
- Anti-plagio básico

**Arquitectura de Evaluación**:

```
┌────────────────────────────────────────┐
│   Frontend (Student submits code)     │
└────────────────┬───────────────────────┘
                 │ POST /submissions
┌────────────────▼───────────────────────┐
│        API Gateway                     │
└────────────────┬───────────────────────┘
                 │
┌────────────────▼───────────────────────┐
│      Evaluation Service                │
│  1. Valida código                      │
│  2. Enqueue en Redis/Celery            │
│  3. Retorna submission_id              │
└────────────────┬───────────────────────┘
                 │
┌────────────────▼───────────────────────┐
│         Worker Queue (Celery)          │
│  Múltiples workers procesando          │
│  ┌──────────┐  ┌──────────┐           │
│  │ Worker 1 │  │ Worker 2 │  ...      │
│  └────┬─────┘  └────┬─────┘           │
│       │             │                  │
│  ┌────▼─────────────▼──────────┐      │
│  │    Pyodide Sandbox          │      │
│  │  - Run code in isolation    │      │
│  │  - 3s timeout               │      │
│  │  - Memory limit: 50MB       │      │
│  │  - CPU limit                │      │
│  └─────────────┬───────────────┘      │
└────────────────┼────────────────────────┘
                 │
┌────────────────▼───────────────────────┐
│   Results stored in DB                 │
│   Notification sent to student         │
└────────────────────────────────────────┘
```

**Modelo de Datos**:
```sql
-- Submissions
CREATE TABLE submissions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID REFERENCES students(id),
    exercise_id UUID REFERENCES exercises(id),
    code TEXT NOT NULL,
    language VARCHAR(20) DEFAULT 'python',
    status VARCHAR(50), -- pending/running/completed/failed/timeout
    score INTEGER, -- 0-100
    passed_tests INTEGER DEFAULT 0,
    total_tests INTEGER,
    execution_time_ms INTEGER,
    feedback JSONB, -- {"general": "...", "tests": [...]}
    error_message TEXT,
    submitted_at TIMESTAMPTZ DEFAULT NOW(),
    evaluated_at TIMESTAMPTZ,
    attempt_number INTEGER DEFAULT 1
);

-- Test Results
CREATE TABLE test_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    submission_id UUID REFERENCES submissions(id) ON DELETE CASCADE,
    test_name VARCHAR(200),
    passed BOOLEAN,
    expected_output TEXT,
    actual_output TEXT,
    error_message TEXT,
    execution_time_ms INTEGER
);
```

**Código de Evaluación** (simplificado):
```python
from celery import Celery
import pyodide
import json

app = Celery('evaluator', broker='redis://localhost')

@app.task
def evaluate_submission(submission_id: str):
    # 1. Obtener submission de DB
    submission = get_submission(submission_id)
    exercise = get_exercise(submission.exercise_id)

    # 2. Preparar código + tests
    student_code = submission.code
    test_cases = exercise.test_cases

    # 3. Ejecutar en sandbox
    results = []
    for test in test_cases:
        result = run_test_in_sandbox(
            code=student_code,
            test=test,
            timeout=3
        )
        results.append(result)

    # 4. Calcular score
    passed = sum(1 for r in results if r['passed'])
    score = int((passed / len(results)) * 100)

    # 5. Generar feedback
    feedback = generate_feedback(results, score)

    # 6. Guardar resultados
    update_submission(
        submission_id,
        status='completed',
        score=score,
        feedback=feedback,
        passed_tests=passed,
        total_tests=len(results)
    )

    # 7. Notificar estudiante
    notify_student(submission.student_id, {
        'type': 'submission_evaluated',
        'score': score
    })

    return {'submission_id': submission_id, 'score': score}

def run_test_in_sandbox(code: str, test: dict, timeout: int):
    """Ejecuta código en Pyodide sandbox"""
    try:
        # Setup sandbox
        env = create_pyodide_env()

        # Run student code
        env.run_python(code)

        # Run test
        test_code = f"""
{test['setup']}
result = {test['call']}
expected = {test['expected']}
assert result == expected, f"Expected {{expected}}, got {{result}}"
"""
        env.run_python_async(test_code)

        return {
            'test_name': test['name'],
            'passed': True,
            'output': env.stdout
        }
    except TimeoutError:
        return {'passed': False, 'error': 'Timeout (> 3s)'}
    except AssertionError as e:
        return {'passed': False, 'error': str(e)}
    except Exception as e:
        return {'passed': False, 'error': f'Error: {str(e)}'}
```

---

### 5. Gamification Service

**Responsabilidades**:
- Sistema XP y niveles
- Badges y achievements
- Leaderboards
- Streaks

**Modelo de Datos**:
```sql
-- Badges disponibles
CREATE TABLE badge_types (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(200) UNIQUE NOT NULL,
    description TEXT,
    icon_url VARCHAR(500),
    criteria JSONB, -- {"type": "lessons_completed", "count": 5}
    xp_reward INTEGER DEFAULT 50,
    rarity VARCHAR(50) -- common/rare/epic/legendary
);

-- Badges obtenidos
CREATE TABLE student_badges (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID REFERENCES students(id),
    badge_type_id UUID REFERENCES badge_types(id),
    earned_at TIMESTAMPTZ DEFAULT NOW(),
    metadata JSONB, -- Info específica del logro
    UNIQUE(student_id, badge_type_id)
);

-- XP Transactions
CREATE TABLE xp_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID REFERENCES students(id),
    amount INTEGER NOT NULL,
    reason VARCHAR(200), -- "completed_exercise", "earned_badge", etc.
    reference_id UUID, -- ID del ejercicio, badge, etc.
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Leaderboards (cache en Redis)
-- Key: leaderboard:{cohort_id}:{period}
-- Value: ZSET de student_id con score (xp)
```

**Sistema de XP**:
```python
class XPSystem:
    XP_PER_LEVEL = 100  # Base

    @staticmethod
    def calculate_level(total_xp: int) -> int:
        """Calcula nivel basado en XP total"""
        # Progresión exponencial ligera
        level = 1
        xp_needed = 0
        while total_xp >= xp_needed:
            level += 1
            xp_needed += XPSystem.XP_PER_LEVEL * (1.1 ** (level - 1))
        return level - 1

    @staticmethod
    def xp_for_next_level(current_xp: int) -> dict:
        """XP necesario para siguiente nivel"""
        current_level = XPSystem.calculate_level(current_xp)
        xp_for_current = XPSystem.total_xp_for_level(current_level)
        xp_for_next = XPSystem.total_xp_for_level(current_level + 1)

        return {
            'current_level': current_level,
            'current_xp': current_xp,
            'xp_in_level': current_xp - xp_for_current,
            'xp_needed': xp_for_next - current_xp,
            'next_level': current_level + 1
        }

async def award_xp(student_id: UUID, amount: int, reason: str):
    """Otorga XP y chequea level up"""
    # 1. Crear transacción
    await create_xp_transaction(student_id, amount, reason)

    # 2. Actualizar total
    student = await get_student(student_id)
    new_xp = student.xp_total + amount
    old_level = XPSystem.calculate_level(student.xp_total)
    new_level = XPSystem.calculate_level(new_xp)

    await update_student(student_id, xp_total=new_xp, level=new_level)

    # 3. Si level up, celebrar
    if new_level > old_level:
        await send_level_up_notification(student_id, new_level)

    # 4. Chequear badges nuevos
    await check_and_award_badges(student_id)
```

**Leaderboard (Redis)**:
```python
import redis.asyncio as redis

class Leaderboard:
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client

    async def update_score(self, cohort_id: UUID, student_id: UUID, xp: int):
        """Actualiza score en leaderboard"""
        key = f"leaderboard:{cohort_id}:alltime"
        await self.redis.zadd(key, {str(student_id): xp})

    async def get_top(self, cohort_id: UUID, limit: int = 10):
        """Obtiene top N estudiantes"""
        key = f"leaderboard:{cohort_id}:alltime"
        top = await self.redis.zrevrange(
            key, 0, limit - 1,
            withscores=True
        )

        # Enriquecer con datos de estudiante
        results = []
        for student_id, xp in top:
            student = await get_student(UUID(student_id))
            results.append({
                'rank': len(results) + 1,
                'student_name': student.full_name,
                'xp': int(xp),
                'level': student.level
            })

        return results

    async def get_student_rank(self, cohort_id: UUID, student_id: UUID):
        """Posición del estudiante en ranking"""
        key = f"leaderboard:{cohort_id}:alltime"
        rank = await self.redis.zrevrank(key, str(student_id))
        return rank + 1 if rank is not None else None
```

---

### 6. Analytics Service

**Responsabilidades**:
- Dashboards instructor
- Identificación de dificultades
- Reportes automáticos
- Alertas proactivas

**Métricas Clave**:
```python
class AnalyticsMetrics:
    @staticmethod
    async def cohort_overview(cohort_id: UUID):
        """Overview general del cohort"""
        students = await get_cohort_students(cohort_id)

        return {
            'total_students': len(students),
            'active_this_week': await count_active_students(cohort_id, days=7),
            'average_progress': await avg_progress(cohort_id),
            'average_xp': await avg_xp(cohort_id),
            'completion_rate': await completion_rate(cohort_id),
            'at_risk_students': await identify_at_risk(cohort_id)
        }

    @staticmethod
    async def lesson_difficulty_analysis(lesson_id: UUID):
        """Identifica si una lección es muy difícil"""
        submissions = await get_lesson_submissions(lesson_id)

        metrics = {
            'total_attempts': len(submissions),
            'first_attempt_success': sum(1 for s in submissions if s.attempt_number == 1 and s.score >= 80) / len(submissions),
            'average_attempts': np.mean([s.attempt_number for s in submissions]),
            'average_score': np.mean([s.score for s in submissions]),
            'average_time_minutes': np.mean([s.time_spent for s in submissions]),
            'common_errors': await analyze_common_errors(lesson_id)
        }

        # Determinar dificultad
        if metrics['first_attempt_success'] < 0.3:
            metrics['difficulty_assessment'] = 'too_hard'
        elif metrics['first_attempt_success'] > 0.8:
            metrics['difficulty_assessment'] = 'too_easy'
        else:
            metrics['difficulty_assessment'] = 'appropriate'

        return metrics

    @staticmethod
    async def identify_at_risk(cohort_id: UUID):
        """Estudiantes en riesgo de abandonar"""
        students = await get_cohort_students(cohort_id)
        at_risk = []

        for student in students:
            risk_score = 0

            # No activo en 7+ días
            if (datetime.now() - student.last_active_at).days > 7:
                risk_score += 3

            # Progreso < 50% del promedio
            avg_progress = await avg_progress(cohort_id)
            if student.completion_percentage < avg_progress * 0.5:
                risk_score += 2

            # Múltiples submissions fallidas
            recent_fails = await count_recent_fails(student.id, days=7)
            if recent_fails > 5:
                risk_score += 2

            # Streak roto
            if student.streak_days == 0:
                risk_score += 1

            if risk_score >= 4:
                at_risk.append({
                    'student': student,
                    'risk_score': risk_score,
                    'reasons': [...]  # Detalladas
                })

        return at_risk
```

---

## 🔐 Seguridad

### Autenticación

**JWT (JSON Web Tokens)**:
```python
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "..." # Env variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(user_id: str):
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode = {"sub": user_id, "exp": expire, "type": "refresh"}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

### Autorización (RBAC - Role-Based Access Control)

```python
from enum import Enum

class Role(str, Enum):
    STUDENT = "student"
    INSTRUCTOR = "instructor"
    ADMIN = "admin"

class Permission(str, Enum):
    READ_COURSE = "read:course"
    WRITE_COURSE = "write:course"
    READ_STUDENT = "read:student"
    WRITE_STUDENT = "write:student"
    EVALUATE = "evaluate:submission"
    # ...

ROLE_PERMISSIONS = {
    Role.STUDENT: [
        Permission.READ_COURSE,
        Permission.READ_STUDENT,  # Solo su propio perfil
    ],
    Role.INSTRUCTOR: [
        Permission.READ_COURSE,
        Permission.WRITE_COURSE,
        Permission.READ_STUDENT,  # Todos sus estudiantes
        Permission.EVALUATE,
    ],
    Role.ADMIN: [
        # Todos los permisos
    ]
}

def require_permission(permission: Permission):
    def decorator(func):
        async def wrapper(*args, current_user: User, **kwargs):
            user_permissions = ROLE_PERMISSIONS.get(current_user.role, [])
            if permission not in user_permissions:
                raise HTTPException(status_code=403, detail="Insufficient permissions")
            return await func(*args, current_user=current_user, **kwargs)
        return wrapper
    return decorator

# Uso:
@router.post("/courses")
@require_permission(Permission.WRITE_COURSE)
async def create_course(course: CourseCreate, current_user: User = Depends(get_current_user)):
    # Solo instructores y admins pueden crear cursos
    pass
```

### Sandbox de Código

**Límites de Seguridad**:
```python
import resource
import signal

def execute_code_safely(code: str, timeout: int = 3):
    """Ejecuta código con límites de recursos"""

    # Timeout
    def timeout_handler(signum, frame):
        raise TimeoutError("Execution exceeded time limit")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)

    try:
        # Límite de memoria (50MB)
        resource.setrlimit(
            resource.RLIMIT_AS,
            (50 * 1024 * 1024, 50 * 1024 * 1024)
        )

        # Límite de CPU
        resource.setrlimit(
            resource.RLIMIT_CPU,
            (timeout, timeout)
        )

        # Blacklist de imports peligrosos
        forbidden = ['os', 'sys', 'subprocess', 'eval', 'exec', '__import__']

        # Ejecutar en namespace limitado
        safe_globals = {
            '__builtins__': {
                'print': print,
                'input': input,
                'len': len,
                'range': range,
                'str': str,
                'int': int,
                'float': float,
                'list': list,
                'dict': dict,
                # ... solo built-ins seguros
            }
        }

        exec(code, safe_globals, {})

    finally:
        signal.alarm(0)  # Cancelar alarma
```

---

## 📈 Escalabilidad

### Caching Strategy (Redis)

```python
import redis.asyncio as redis
import json
from functools import wraps

redis_client = redis.from_url("redis://localhost")

def cache(ttl: int = 300):  # 5 min default
    """Decorator para cachear resultados"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Generar cache key
            cache_key = f"{func.__name__}:{json.dumps(args)}:{json.dumps(kwargs)}"

            # Intentar obtener del cache
            cached = await redis_client.get(cache_key)
            if cached:
                return json.loads(cached)

            # Ejecutar función
            result = await func(*args, **kwargs)

            # Guardar en cache
            await redis_client.setex(
                cache_key,
                ttl,
                json.dumps(result)
            )

            return result
        return wrapper
    return decorator

# Uso:
@cache(ttl=600)  # 10 minutos
async def get_course_details(course_id: UUID):
    # Esta query se cachea
    return await db.query(Course).filter(Course.id == course_id).first()
```

### Database Optimization

**Índices Estratégicos**:
```sql
-- Queries comunes de progreso
CREATE INDEX idx_progress_student ON student_progress(student_id, completed_at);
CREATE INDEX idx_progress_lesson ON student_progress(lesson_id, status);

-- Leaderboards
CREATE INDEX idx_students_xp ON students(cohort_id, xp_total DESC);

-- Submissions por estudiante
CREATE INDEX idx_submissions_student ON submissions(student_id, submitted_at DESC);

-- Búsquedas de lecciones
CREATE INDEX idx_lessons_course ON lessons(course_id, session_number);

-- Badges
CREATE INDEX idx_badges_student ON student_badges(student_id, earned_at DESC);
```

**Particionamiento** (para escala futura):
```sql
-- Particionar submissions por fecha
CREATE TABLE submissions_2024_01 PARTITION OF submissions
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE submissions_2024_02 PARTITION OF submissions
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
-- ...
```

### Horizontal Scaling

```
┌───────────────────────────────────────────────┐
│          Load Balancer (Nginx)                │
└────────────────┬──────────────────────────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
┌───▼────┐  ┌───▼────┐  ┌───▼────┐
│ API    │  │ API    │  │ API    │
│ Node 1 │  │ Node 2 │  │ Node N │
└───┬────┘  └───┬────┘  └───┬────┘
    │           │           │
    └───────────┼───────────┘
                │
    ┌───────────▼───────────┐
    │  PostgreSQL Primary   │
    │  (Write)              │
    └───────────┬───────────┘
                │
    ┌───────────┴───────────┐
    │                       │
┌───▼────────┐      ┌───────▼──────┐
│ Replica 1  │      │  Replica 2   │
│ (Read)     │      │  (Read)      │
└────────────┘      └──────────────┘
```

---

## 📱 Offline-First Strategy

### Service Worker (PWA)

```javascript
// service-worker.js
const CACHE_NAME = 'eduflow-v1';
const OFFLINE_CACHE = [
    '/',
    '/courses',
    '/static/css/main.css',
    '/static/js/main.js',
    '/offline.html'
];

// Instalar SW y cachear recursos
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(OFFLINE_CACHE);
        })
    );
});

// Interceptar requests
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            // Retornar del cache si existe
            if (response) {
                return response;
            }

            // Intentar fetch de red
            return fetch(event.request).catch(() => {
                // Si falla, mostrar página offline
                return caches.match('/offline.html');
            });
        })
    );
});
```

### Sincronización Local

```javascript
// IndexedDB para almacenamiento local
import { openDB } from 'idb';

const db = await openDB('eduflow-local', 1, {
    upgrade(db) {
        // Store para submissions pendientes
        db.createObjectStore('pending-submissions', {
            keyPath: 'id',
            autoIncrement: true
        });

        // Store para progreso local
        db.createObjectStore('local-progress', {
            keyPath: 'lesson_id'
        });
    }
});

// Guardar submission offline
async function submitOffline(code, exercise_id) {
    const submission = {
        exercise_id,
        code,
        timestamp: Date.now(),
        synced: false
    };

    await db.add('pending-submissions', submission);
}

// Sincronizar cuando vuelve conexión
window.addEventListener('online', async () => {
    const pending = await db.getAll('pending-submissions');

    for (const submission of pending) {
        try {
            await fetch('/api/submissions', {
                method: 'POST',
                body: JSON.stringify(submission)
            });

            // Marcar como sincronizado
            await db.delete('pending-submissions', submission.id);
        } catch (e) {
            console.error('Sync failed', e);
        }
    }
});
```

---

## 📚 Próximos Pasos

1. **Implementar Fase 1**: Ver `phase-1-prompt.md`
2. **Definir API completa**: Ver `api-spec.md`
3. **Setup infrastructure**: Ver `deployment.md`
4. **Escribir tests**: Ver `testing-strategy.md`

---

**Esta arquitectura está diseñada para crecer. Empieza simple (Fase 1), escala según necesidad. 🚀**
