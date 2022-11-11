from fastapi.routing import APIRouter
from api.signup.views import router as signup_router
from api.example.views import router as example_router
from api.system.views import router as system_router

api_router = APIRouter()

api_router.include_router(example_router, prefix="/example", tags=["example"])
api_router.include_router(system_router, prefix="/system", tags=["system"])
api_router.include_router(signup_router, prefix="/signup", tags=["signup"])

