import fastapi
from server.sql_base.models import Resourses
from server.resolvers.Resourses import new_resourses, update_resourses, get_all_resourses, delete_resourses, get_resourses

resourses_router = fastapi.APIRouter(prefix="/resourses", tags=["Resourses"])


@resourses_router.get("/")
def start_page():
    return ""


@resourses_router.post("/new/")
def new_resours(resourses: Resourses):
    return new_resourses(resourses)


@resourses_router.get("/get/{resourses_id}")
def gets_resours(resourses_id: int):
    return get_resourses(resourses_id)


@resourses_router.get("/get/")
def get_all_resours():
    return get_all_resourses()


@resourses_router.put("/update/{resourses_id}")
def update_resours(resourses_id: int, new_data: Resourses):
    return update_resourses(resourses=new_data, resourses_id=resourses_id)


@resourses_router.delete("/delete/{resourses_id}")
def delete_resours(resourses_id: int):
    return delete_resourses(resourses_id)