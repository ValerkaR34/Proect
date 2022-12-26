import fastapi
from server.sql_base.models import Personal
from server.resolvers.Personal import new_personal,  update_personal,  get_all_personal, delete_personal, get_personal

personal_router = fastapi.APIRouter(prefix="/personal", tags=["Personal"])


@personal_router.get("/")
def start_page():
    return ""


@personal_router.post("/new/")
def new_personaly(personal: Personal):
    return new_personal(personal)


@personal_router.get("/get/{personal_id}")
def gets_personaly(personal_id: int):
    return get_personal(personal_id)


@personal_router.get("/get/")
def get_all_personaly():
    return get_all_personal()


@personal_router.put("/update/{personal_id}")
def update_personaly(personal_id: int, new_data: Personal):
    return update_personal(personal=new_data, personal_id=personal_id)


@personal_router.delete("/delete/{personal_id}")
def delete_personaly(personal_id: int):
    return delete_personal(personal_id)