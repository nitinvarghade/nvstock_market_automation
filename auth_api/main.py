from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="NVStock Authentication API",
    version="1.0.0",
)

# No permissive browser CORS configuration.
# Authentication will use same-origin requests via Nginx.


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "nvstock-auth-api",
    }


@app.get("/")
def root():
    return {
        "message": "NVStock Authentication API",
    }
