from fastapi import FastAPI

from app.api import auth
from app.api import applications

app = FastAPI(title="Job Application Tracker API")

# Routers
app.include_router(auth.router)
app.include_router(applications.router)
