import fastapi
from sql_base.models import User
from resolvers.Users import check_login, new_user, update_user, get_all_user, delete_user

Users_router = fastapi.APIRouter(prefix="/Users", tags=["Users"])

@Users_router.post("/create/")
def new_client(User: User):
    return new_user(User)

@Users_router.get("/get/{Users_id}")
def proverka_User(Users_id: int):
    return get_Users(Users_id)