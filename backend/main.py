from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from auth import router as auth_router

app= FastAPI(title="Kubernetes Tryout",version ="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
PORT: int=8000
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "App is up and running"}

@app.get("/health")
async def health():
     return {"status": "healthy", "service": "backend"}
 
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Task Manager API is starting up!")
    logger.info("Login functionality started")
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)