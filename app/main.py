from fastapi import FastAPI

from app.routers import items

app = FastAPI(
    title="FastAPI+MCP Coding Test",
    description="This is a FastAPI application for the MCP Coding Test.",
    version="1.0.0",
)


@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}


app.include_router(items.router)
