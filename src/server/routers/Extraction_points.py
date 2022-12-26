import fastapi
from server.sql_base.models import Extraction_points
from server.resolvers.Extraction_points import new_extraction_points,  update_extraction_points, get_all_extraction_points,delete_extraction_points, get_extraction_points

extraction_points_router = fastapi.APIRouter(prefix="/extraction_points", tags=["Extraction_points"])


@extraction_points_router.get("/")
def start_page():
    return ""


@extraction_points_router.post("/new/")
def new_extraction_pointss(extraction_points: Extraction_points):
    return new_extraction_points(extraction_points)


@extraction_points_router.get("/get/{extraction_points_id}")
def gets_extraction_pointss(extraction_points_id: int):
    return get_extraction_points(extraction_points_id)


@extraction_points_router.get("/get/")
def get_all_extraction_pointss():
    return get_all_extraction_points()


@extraction_points_router.put("/update/{extraction_points_id}")
def update_extraction_pointss(extraction_points_id: int, new_data: Extraction_points):
    return update_extraction_points(extraction_points=new_data, extraction_points_id=extraction_points_id)


@extraction_points_router.delete("/delete/{extraction_points_id}")
def delete_extraction_pointss(extraction_points_id: int):
    return delete_extraction_points(extraction_points_id)