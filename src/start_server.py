
from server.sql_base.Rescript import base_worker
from server.myrout import routersval
import fastapi

base_worker.create_base('../sql/pyt.sql')

app = fastapi.APIRouter()

[app.include_router(myrout) for myrout in routersval]