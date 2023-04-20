import uvicorn
from fastapi import FastAPI

from database.db import database, engine, metadata
from routes.articles import router as ArticleRouter
from routes.auth import router as AuthRouter
from routes.users import router as UserRouter

metadata.create_all(engine)

app = FastAPI(
    title="My Async API",
    description="This is a very fancy project, with auto docs for the API and everything. And we are using FastAPI with async.",
    docs_url="/",
)

app.include_router(ArticleRouter)
app.include_router(UserRouter)
app.include_router(AuthRouter)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True, log_level="info")
