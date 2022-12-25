from sql_base.models import Resourses
from sql_base.Rescript import base_worker


def new_resourses(resourses: Resourses):
    n = base_worker.execute(f"""INSERT INTO Resourses (price, date_time, view) 
                                    VALUES(?,?,?) RETURNING id;""",
                            (resourses.price, resourses.date_time, resourses.view))
    return n


def update_resourses(resourses: Resourses, resourses_id: int):
    update_resourses = base_worker.execute(f"""update Resourses set (price, date_time, view) = (?,?,?) where id=(?);""",
                                    (resourses.price, resourses.date_time,  resourses.view, resourses_id))
    return update_resourses


def get_all_resourses():
    return base_worker.execute(query="SELECT id, price, date_time, view  FROM Resourses", many=True)


def delete_resourses(resourses_id: int):
    return base_worker.execute(query="DELETE Resourses WHERE id=? ",
                               args=(resourses_id,))


def get_resourses(resourses_id: int):
    return base_worker.execute(query="SELECT id, price, date_time, view   FROM Resourses WHERE id=?", args=(resourses_id,))