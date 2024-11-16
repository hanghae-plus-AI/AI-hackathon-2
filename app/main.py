from fastapi import FastAPI
import uvicorn
from routers.task_router import task_router
from routers.favorites_router import favorites_router


def create_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(task_router)
    _app.include_router(favorites_router)
    return _app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
