from fastapi.routing import APIRouter

from api.system.views import router as system_router
from api.search.views import router as search_router
from api.user.views import router as user_router


api_router = APIRouter()
api_router.include_router(system_router, prefix="/system", tags=["system"])
api_router.include_router(search_router, prefix="/search", tags=["search"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
