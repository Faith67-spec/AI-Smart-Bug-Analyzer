from fastapi import FastAPI
from app.routes.bug_routes import router

app = FastAPI(
    title="AI Smart Bug Analyzer",
    description="Bug Submission API",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "AI Smart Bug Analyzer API is running"
    }