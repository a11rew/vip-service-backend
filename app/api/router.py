from fastapi.routing import APIRouter

from api.system.views import router as system_router
from api.user.views import router as user_router
from api.search.views import router as search_router
from api.user.views import router as user_router
from api.history.views import router as history_router



api_router = APIRouter()


api_router.include_router(system_router, prefix="/system", tags=["system"])
api_router.include_router(example_router, prefix="/example", tags=["example"])
api_router.include_router(search_router, prefix="/search", tags=["search"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(history_router, prefix="/history", tags=["history"])
