# 🛠️ EduFlow - Tech Stack

## 📋 Decisiones Tecnológicas

Este documento explica **por qué** elegimos cada tecnología.

---

## 🔙 Backend

### FastAPI (Python)

**Elegido porque**:
✅ **Velocidad**: Performance comparable a Node.js/Go
✅ **Type Safety**: Pydantic para validación automática
✅ **Documentación Auto**: Swagger/OpenAPI out-of-the-box
✅ **Async nativo**: Para operaciones concurrentes
✅ **Ecosistema Python**: Acceso a pandas, sklearn, etc.
✅ **Curva de aprendizaje**: Familiar para el equipo

**Alternativas consideradas**:
- ❌ Django: Demasiado "batteries included", menos flexible
- ❌ Flask: Menos features modernas, más boilerplate
- ❌ Node.js/Express: Requiere cambio de ecosistema

**Ejemplo**:
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="EduFlow API")

class StudentCreate(BaseModel):
    name: str
    email: str
    cohort_id: UUID

@app.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreate):
    # Validación automática
    # Documentación automática
    # Type hints everywhere
    return await db.students.create(student)
```

---

## 💾 Bases de Datos

### PostgreSQL 15+

**Elegido porque**:
✅ **Robustez**: ACID completo, transacciones confiables
✅ **JSONB**: Flexibilidad sin sacrificar estructura
✅ **Performance**: Índices avanzados, query optimization
✅ **Extensiones**: PostGIS, pg_trgm, etc.
✅ **Open source**: Sin vendor lock-in
✅ **Escalabilidad**: Replicación, particionamiento

**Schema híbrido**:
```sql
-- Estructura para datos core
CREATE TABLE students (
    id UUID PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    -- ...
);

-- JSONB para datos flexibles
ALTER TABLE students ADD COLUMN preferences JSONB;

-- Índice en JSONB
CREATE INDEX idx_prefs ON students USING GIN (preferences);

-- Query mixto
SELECT * FROM students
WHERE preferences->>'theme' = 'dark'
AND cohort_id = 'xxx';
```

**Alternativas consideradas**:
- ❌ MySQL: Menos features avanzados
- ❌ MongoDB: Sin transacciones multi-doc (hasta v4), menos maduro
- ❌ SQLite: No escala para multi-user

---

### Redis

**Elegido porque**:
✅ **Velocidad**: < 1ms response time
✅ **Structures**: ZSET perfecto para leaderboards
✅ **Cache**: TTL automático
✅ **Pub/Sub**: Para notificaciones real-time
✅ **Session store**: JWT refresh tokens

**Casos de uso**:
```python
import redis.asyncio as redis

r = await redis.from_url("redis://localhost")

# 1. Cache de queries
await r.setex("course:123", 300, json.dumps(course_data))

# 2. Leaderboard (ZSET)
await r.zadd("leaderboard:cohort_1", {"student_1": 1500, "student_2": 1200})
top_10 = await r.zrevrange("leaderboard:cohort_1", 0, 9, withscores=True)

# 3. Rate limiting
pipe = r.pipeline()
key = f"rate_limit:{user_id}:{minute}"
pipe.incr(key)
pipe.expire(key, 60)
count = (await pipe.execute())[0]
if count > 100:
    raise RateLimitExceeded()

# 4. Sessions
await r.setex(f"session:{session_id}", 3600, user_data)
```

**Alternativas consideradas**:
- ❌ Memcached: Menos features (no persistence, no structures)
- ❌ In-memory dict: No persiste, no distributed

---

## 🎨 Frontend

### React 18+

**Elegido porque**:
✅ **Ecosistema maduro**: Infinitas librerías
✅ **Componentes reutilizables**: DRY principle
✅ **Virtual DOM**: Performance optimizado
✅ **Hooks**: State management simple
✅ **Comunidad**: Stack Overflow, tutoriales abundantes
✅ **Hiring**: Fácil encontrar devs React

**Alternativas consideradas**:
- ❌ Vue: Menos momentum, comunidad más pequeña
- ❌ Svelte: Muy joven, menos librerías
- ❌ Angular: Demasiado opinionated, curva empinada

---

### TailwindCSS

**Elegido porque**:
✅ **Utility-first**: Desarrollo rápido
✅ **Consistencia**: Design system implícito
✅ **Performance**: Tree-shaking, CSS mínimo
✅ **Responsive**: Mobile-first out-of-the-box
✅ **Customizable**: Fácil theming

```jsx
// Componente con Tailwind
export function StudentCard({ student }) {
    return (
        <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-xl transition">
            <h3 className="text-xl font-bold text-gray-800">
                {student.name}
            </h3>
            <p className="text-gray-600 mt-2">
                XP: {student.xp_total}
            </p>
            <div className="mt-4 flex gap-2">
                {student.badges.map(badge => (
                    <Badge key={badge.id} {...badge} />
                ))}
            </div>
        </div>
    );
}
```

**Alternativas consideradas**:
- ❌ Bootstrap: Menos customizable, más "samey"
- ❌ Material-UI: Pesado, opinionated design
- ❌ CSS Modules: Más boilerplate

---

### Zustand (State Management)

**Elegido porque**:
✅ **Simple**: Menos boilerplate que Redux
✅ **Lightweight**: 1KB vs 40KB (Redux + toolkit)
✅ **Hooks-based**: Integración natural con React
✅ **TypeScript**: First-class support
✅ **DevTools**: Compatible con Redux DevTools

```javascript
import create from 'zustand';

// Store simple
const useStudentStore = create((set) => ({
    students: [],
    loading: false,

    fetchStudents: async (cohortId) => {
        set({ loading: true });
        const response = await fetch(`/api/students?cohort=${cohortId}`);
        const students = await response.json();
        set({ students, loading: false });
    },

    addXP: (studentId, amount) => set((state) => ({
        students: state.students.map(s =>
            s.id === studentId
                ? { ...s, xp: s.xp + amount }
                : s
        )
    }))
}));

// Uso en componente
function StudentList({ cohortId }) {
    const { students, loading, fetchStudents } = useStudentStore();

    useEffect(() => {
        fetchStudents(cohortId);
    }, [cohortId]);

    if (loading) return <Spinner />;

    return (
        <div>
            {students.map(s => <StudentCard key={s.id} student={s} />)}
        </div>
    );
}
```

**Alternativas consideradas**:
- ❌ Redux: Demasiado boilerplate para proyecto inicial
- ❌ Context API: Performance issues con muchos consumers
- ❌ MobX: Menos predictible, más magia

---

## 🧪 Code Evaluation

### Pyodide

**Elegido porque**:
✅ **En navegador**: No servidor de ejecución necesario
✅ **Seguro**: Sandboxed por default (WASM)
✅ **Python completo**: CPython en WebAssembly
✅ **Offline capable**: Funciona sin backend
✅ **Latencia baja**: Ejecuta local

```javascript
import { loadPyodide } from 'pyodide';

let pyodide = await loadPyodide();

async function evaluateCode(studentCode, testCases) {
    try {
        // Ejecutar código del estudiante
        await pyodide.runPythonAsync(studentCode);

        // Correr tests
        const results = [];
        for (const test of testCases) {
            const result = await pyodide.runPythonAsync(`
${test.setup}
result = ${test.call}
result == ${test.expected}
            `);
            results.push({ passed: result, test: test.name });
        }

        return results;
    } catch (error) {
        return { error: error.message };
    }
}
```

**Alternativas consideradas**:
- ❌ Judge0: Requiere servidor, costos por API call
- ❌ Backend execution: Seguridad más compleja, escalabilidad
- ❌ Skulpt: Python parcial, limitaciones

**Limitaciones de Pyodide**:
- ⚠️ No todos los paquetes disponibles (numpy ✅, requests ❌)
- ⚠️ Primera carga ~6MB (cacheable)
- ⚠️ Performance ~2-3x más lento que CPython

**Solución híbrida** (Fase 3+):
```
Ejercicios simples → Pyodide (client-side)
Ejercicios avanzados → Backend sandbox (server-side)
```

---

## 📦 Package Management

### Poetry (Python)

**Elegido porque**:
✅ **Dependency resolution**: Mejor que pip
✅ **Lock file**: Builds reproducibles
✅ **Virtual envs**: Manejo automático
✅ **Publish**: Fácil publicar a PyPI si queremos

```toml
# pyproject.toml
[tool.poetry]
name = "eduflow"
version = "0.1.0"

[tool.poetry.dependencies]
python = "^3.10"
fastapi = "^0.104.0"
uvicorn = {extras = ["standard"], version = "^0.24.0"}
sqlalchemy = "^2.0.0"
pydantic = "^2.0.0"
redis = "^5.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
black = "^23.0.0"
mypy = "^1.5.0"
```

---

### pnpm (JavaScript)

**Elegido porque**:
✅ **Rápido**: 2x más rápido que npm
✅ **Eficiente**: Deduplicación de paquetes
✅ **Strict**: Evita phantom dependencies
✅ **Monorepo**: Workspaces built-in

```json
{
  "name": "eduflow-frontend",
  "version": "0.1.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "test": "vitest"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "zustand": "^4.4.0",
    "axios": "^1.5.0",
    "@tanstack/react-query": "^5.0.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "typescript": "^5.2.0",
    "tailwindcss": "^3.3.0"
  }
}
```

---

## 🚀 Build & Bundling

### Vite

**Elegido porque**:
✅ **Velocidad**: HMR instantáneo
✅ **ESM nativo**: Aprovecha módulos del navegador
✅ **Optimización**: Tree-shaking, code-splitting automático
✅ **DX**: Error overlay, fast refresh
✅ **TypeScript**: Built-in support

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
    plugins: [react()],
    build: {
        rollupOptions: {
            output: {
                manualChunks: {
                    'react-vendor': ['react', 'react-dom'],
                    'ui-vendor': ['@headlessui/react', 'chart.js']
                }
            }
        }
    },
    server: {
        proxy: {
            '/api': 'http://localhost:8000'
        }
    }
});
```

**Alternativas consideradas**:
- ❌ Webpack: Más lento, más configuración
- ❌ Parcel: Menos control, menos maduro

---

## ☁️ Hosting & Infrastructure

### Railway / Fly.io (MVP)

**Elegido para empezar porque**:
✅ **Simple**: Deploy con git push
✅ **Económico**: Free tier generoso
✅ **PostgreSQL incluido**: Managed DB
✅ **Redis incluido**: Managed cache
✅ **Auto-scaling**: Crece con demanda

```toml
# railway.toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
healthcheckPath = "/health"
restartPolicyType = "on-failure"

[[services]]
name = "api"
plan = "starter"

[[services]]
name = "postgres"
plan = "starter"

[[services]]
name = "redis"
plan = "starter"
```

**Migración futura** (cuando crecemos):
- DigitalOcean Kubernetes
- AWS ECS/EKS
- Google Cloud Run

---

### Vercel (Frontend)

**Elegido porque**:
✅ **Optimizado para React**: Zero-config
✅ **Edge Network**: CDN global
✅ **Preview deploys**: Branch = URL
✅ **Analytics**: Web Vitals built-in
✅ **Free tier**: Generoso para MVP

```json
// vercel.json
{
  "buildCommand": "pnpm build",
  "outputDirectory": "dist",
  "devCommand": "pnpm dev",
  "installCommand": "pnpm install",
  "framework": "vite",
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "https://api.eduflow.app/api/$1"
    }
  ]
}
```

---

## 🔐 Autenticación

### JWT + HTTP-only Cookies

**Elegido porque**:
✅ **Stateless**: No sesiones en servidor
✅ **Escalable**: No shared session store
✅ **Seguro**: HTTP-only cookies previenen XSS
✅ **Refresh tokens**: Expiración segura

```python
from fastapi import HTTPException, Response, Cookie
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "..." # Env variable
ACCESS_TOKEN_EXPIRE = 15  # minutos
REFRESH_TOKEN_EXPIRE = 30  # días

def create_tokens(user_id: str):
    access = jwt.encode({
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE),
        "type": "access"
    }, SECRET_KEY)

    refresh = jwt.encode({
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE),
        "type": "refresh"
    }, SECRET_KEY)

    return access, refresh

@app.post("/login")
async def login(credentials: LoginCredentials, response: Response):
    user = await authenticate(credentials)

    access_token, refresh_token = create_tokens(str(user.id))

    # Set HTTP-only cookies
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,  # HTTPS only
        samesite="lax",
        max_age=ACCESS_TOKEN_EXPIRE * 60
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=REFRESH_TOKEN_EXPIRE * 86400
    )

    return {"status": "success", "user": user.dict()}
```

**Alternativas consideradas**:
- ❌ Sessions en DB: No escala bien
- ❌ OAuth only: Overkill para MVP, dependencia externa
- ❌ LocalStorage JWT: Vulnerable a XSS

---

## 📊 Analytics & Monitoring

### Sentry (Errores)

**Elegido porque**:
✅ **Detalles completos**: Stack traces, breadcrumbs
✅ **Alerts**: Email/Slack cuando hay errores
✅ **Performance**: Slow query detection
✅ **Free tier**: 5K eventos/mes

```python
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

sentry_sdk.init(
    dsn="...",
    integrations=[FastApiIntegration()],
    traces_sample_rate=0.1,  # 10% de transactions
    environment="production"
)
```

---

### Plausible Analytics (Web)

**Elegido porque**:
✅ **Privacy-first**: GDPR compliant
✅ **Simple**: Dashboard claro
✅ **Lightweight**: < 1KB script
✅ **No cookies**: No consent banner necesario

```html
<script defer data-domain="eduflow.app" src="https://plausible.io/js/script.js"></script>
```

**Alternativas consideradas**:
- ❌ Google Analytics: Privacy concerns, pesado
- ❌ Mixpanel: Overkill para MVP
- ❌ Self-hosted: Más trabajo, no vale la pena inicial

---

## 🧪 Testing

### pytest (Backend)

```python
# tests/test_students.py
import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app)

def test_create_student(client):
    response = client.post("/students", json={
        "name": "Juan Pérez",
        "email": "juan@example.com",
        "cohort_id": "..."
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Juan Pérez"

def test_student_progress(client):
    # ...
```

---

### Vitest (Frontend)

```javascript
// tests/StudentCard.test.jsx
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import StudentCard from './StudentCard';

describe('StudentCard', () => {
    it('renders student name', () => {
        const student = { name: 'Juan', xp: 100 };
        render(<StudentCard student={student} />);
        expect(screen.getByText('Juan')).toBeInTheDocument();
    });

    it('displays XP correctly', () => {
        const student = { name: 'Juan', xp: 100 };
        render(<StudentCard student={student} />);
        expect(screen.getByText('XP: 100')).toBeInTheDocument();
    });
});
```

---

## 📦 Deployment Pipeline

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: poetry install
      - run: poetry run pytest

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: superfly/flyctl-actions/setup-flyctl@master
      - run: flyctl deploy --remote-only
        env:
          FLY_API_TOKEN: ${{ secrets.FLY_API_TOKEN }}
```

---

## 🎯 Resumen: Stack Completo

```
┌─────────────────────────────────────┐
│         FRONTEND (Vercel)           │
│  React + Vite + TailwindCSS         │
│  Zustand + React Query              │
│  Pyodide (code evaluation)          │
└─────────────────┬───────────────────┘
                  │ HTTPS
┌─────────────────▼───────────────────┐
│      BACKEND (Railway/Fly.io)       │
│  FastAPI + Uvicorn                  │
│  Pydantic + SQLAlchemy              │
└─────────────────┬───────────────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
┌───▼───┐   ┌─────▼────┐   ┌───▼────┐
│ PostgreSQL│   Redis   │   S3/Blob │
└──────────┘   └────────┘   └────────┘

📊 Monitoring: Sentry + Plausible
🔐 Auth: JWT + HTTP-only cookies
🧪 Testing: pytest + Vitest
🚀 CI/CD: GitHub Actions
```

---

## 💰 Costos Estimados (MVP - 100 estudiantes)

| Servicio | Costo/mes | Notas |
|----------|-----------|-------|
| Railway (Backend + DB + Redis) | $5-20 | Free tier primero |
| Vercel (Frontend) | $0 | Free tier suficiente |
| SendGrid (Emails) | $0 | 100/día gratis |
| Sentry (Errors) | $0 | 5K eventos gratis |
| Plausible (Analytics) | $9 | O self-host ($0) |
| **TOTAL** | **$14-29/mes** | Extremadamente económico |

**Escala a 1,000 estudiantes**: ~$50-100/mes
**Escala a 10,000 estudiantes**: ~$300-500/mes

---

**Stack elegido para balance perfecto entre: velocidad de desarrollo, costos, escalabilidad y mantenibilidad. 🚀**
