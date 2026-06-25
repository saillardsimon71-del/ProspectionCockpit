from __future__ import annotations

"""FastAPI application entrypoint for ProspectionCockpit."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from prospection_cockpit import __version__


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan (DB connection, etc. later)."""
    # TODO: init DB engine, run migrations, etc.
    yield
    # shutdown


app = FastAPI(
    title="ProspectionCockpit API",
    description="API du cockpit de prospection pour artisans - Loop Engineering",
    version=__version__,
    lifespan=lifespan,
)


@app.get("/health", tags=["System"])
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": __version__,
        "message": "ProspectionCockpit API is running (Loop Engineering mode)",
    }


@app.get("/", tags=["System"])
async def root() -> dict[str, str]:
    return {
        "message": "Bienvenue sur ProspectionCockpit API",
        "docs": "/docs",
        "health": "/health",
    }
