from server.sql_base.models import Extraction_points
from server.sql_base.Rescript import base_worker


def new_extraction_points(extraction_points: Extraction_points):
    n = base_worker.execute(f"""INSERT INTO Extraction_points (status,condition,Firm_Id) 
                                    VALUES(?,?,?) RETURNING id;""",
                            (extraction_points.status, extraction_points.condition, extraction_points.Firm_Id))
    return n


def update_extraction_points(extraction_points: Extraction_points, extraction_points_id: int):
    update_id = base_worker.execute(f"""update Extraction_points set (status, condition, Firm_Id ) = (?,?,?) where id=(?);""",
                                    (extraction_points.status, extraction_points.condition,  extraction_points.Firm_Id, extraction_points_id))
    return update_id


def get_all_extraction_points():
    return base_worker.execute(query="SELECT id, status, condition, Firm_Id  FROM  Extraction_points ", many=True)


def delete_extraction_points(extraction_points_id: int):
    return base_worker.execute(query="DELETE FROM  Extraction_points WHERE id=? ",
                               args=(extraction_points_id,))


def get_extraction_points(extraction_points_id: int):
    return base_worker.execute(query="SELECT id,  status, condition, Firm_Id   FROM Extraction_points  WHERE id=?", args=(extraction_points_id,))