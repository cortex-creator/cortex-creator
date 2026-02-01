from fastapi import FastAPI

from .database import Base, engine
from .routes import applications, jobs, resume

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FREE Job Application Bot")

app.include_router(resume.router)
app.include_router(jobs.router)
app.include_router(applications.router)
