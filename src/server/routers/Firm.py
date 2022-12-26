import fastapi
from server.sql_base.models import Firms
from server.resolvers.Firm import new_firms,  update_firms, get_all_firms,  delete_firms, get_firms

firm_router = fastapi.APIRouter(prefix="/firms", tags=["Firms"])


@firm_router.get("/")
def start_page():
    return ""


@firm_router.post("/new/")
def new_firm(firm: Firms):
    return new_firms(firm)


@firm_router.get("/get/{firm_id}")
def gets_firm(firm_id: int):
    return get_firms(firm_id)


@firm_router.get("/get/")
def get_all_firm():
    return get_all_firms()


@firm_router.put("/update/{firm_id}")
def update_firm(firm_id: int, new_data: Firms):
    return update_firms(firms=new_data, firms_id=firm_id)


@firm_router.delete("/delete/{firm_id}")
def delete_firm(firm_id: int):
    return delete_firms(firm_id)