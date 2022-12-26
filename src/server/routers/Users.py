import fastapi
from server.sql_base.models import User
from server.resolvers.Users import new_user,  update_user, get_all_user,  delete_user, get_user

user_router = fastapi.APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/")
def start_page():
    return ""


@user_router.post("/new/")
def new_users(user: User):
    return new_user(user)


@user_router.get("/get/{user_id}")
def gets_users(user_id: int):
    return get_user(user_id)


@user_router.get("/get/")
def get_all_users():
    return get_all_user()


@user_router.put("/update/{user_id}")
def update_users(user_id: int, new_data: User):
    return update_user(user=new_data, user_id=user_id)


@user_router.delete("/delete/{user_id}")
def delete_users(user_id: int):
    return delete_user(user_id)