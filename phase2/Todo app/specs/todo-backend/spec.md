/sp.constitution

Project: Todo Full-Stack Web Application

Core principles:
- Spec-driven development (no manual coding)
- Clear separation: frontend, backend, auth, database
- User isolation and data security by default
- Reproducible agent workflow (same prompts → same result)
- Simplicity first, scale later

Key standards:
- All features must come from written specs
- Every change must update the spec first
- REST API must follow defined endpoints exactly
- JWT auth must be verified on every backend request
- All data access filtered by authenticated user

Constraints:
- Tech stack fixed:
  - Frontend: Next.js App Router
  - Backend: FastAPI (Python)
  - ORM: SQLModel
  - DB: Neon Serverless PostgreSQL
  - Auth: Better Auth + JWT
- No manual coding outside agent workflow
- Environment variables for secrets only
- API returns JSON only

Security rules:
- All endpoints require valid JWT
- No user can access another user’s data
- Token expiry enforced
- Shared JWT secret via env variable

Success criteria:
- Multi-user Todo app works end-to-end
- Users only see their own tasks
- All endpoints secured
- Spec → Plan → Tasks → Code flow followed
- Reviewers can reproduce project using specs only