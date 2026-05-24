from contextlib import asynccontextmanager
 
from fastapi import FastAPI


async def init_db():
    pass

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
 
 
app = FastAPI(
    title="IntelligenceDiagnosticsService",
    version="0.1.0",
    description="Log diagnostics service with reactive and proactive pipelines.",
    lifespan=lifespan,
    debug=True
)
