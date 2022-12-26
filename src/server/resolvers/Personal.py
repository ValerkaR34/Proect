from server.sql_base.models import Personal
from server.sql_base.Rescript import base_worker


def new_personal(personal: Personal):
    n = base_worker.execute(f"""INSERT INTO Personal (name, surname, rating, post_id, salary,chart) 
                                    VALUES(?,?,?,?,?,?) RETURNING id;""",
                            (personal.name, personal.surname, personal.rating, personal.post_id,  personal.salary, personal.chart))
    return n


def update_personal(personal: Personal, personal_id: int):
    update_id = base_worker.execute(f"""update Personal set (name, surname, rating, post_id, salary,chart) = (?,?,?,?,?,?) where id=(?);""",
                                    (personal.name, personal.surname,  personal.rating, personal.post_id, personal.salary, personal.chart, personal_id))
    return update_id


def get_all_personal():
    return base_worker.execute(query="SELECT id, name, surname, rating, post_id, salary,chart  FROM Personal", many=True)


def delete_personal(personal_id: int):
    return base_worker.execute(query="DELETE FROM Personal WHERE id=? ",
                               args=(personal_id,))


def get_personal(personal_id: int):
    return base_worker.execute(query="SELECT id, name, surname, rating, post_id, salary,chart  FROM Personal WHERE id=?", args=(personal_id,))