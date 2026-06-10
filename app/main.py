from fastapi import FastAPI
from app.database import engine, Base
from app.routers import users, auth, tasks, categories

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="A RESTful API for managing tasks with FastAPI and PostgreSQL",
    version="1.0.0"
)

# Include routers
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(categories.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Task Management API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}