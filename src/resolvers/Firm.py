from sql_base.models import Firms
from sql_base.Rescript import base_worker


def new_firms(firms: Firms):
    n = base_worker.execute(f"""INSERT INTO Firms (Name, Rights) 
                                    VALUES(?,?) RETURNING id;""",
                            (firms.Name, firms.Rights))
    return n


def update_firms(firms: Firms, firms_id: int):
    update_id = base_worker.execute(f"""update Firms set (Name, Rights) = (?,?) where id=(?);""",
                                    (firms.Name, firms.Rights, firms_id))
    return update_id


def get_all_firms():
    return base_worker.execute(query="SELECT id, Name, Rights FROM Firms", many=True)


def delete_firms(firms_id: int):
    return base_worker.execute(query="DELETE Firms WHERE id=? ",
                               args=(firms_id,))


def get_firms(firms_id: int):
    return base_worker.execute(query="SELECT id, Name, Rights FROM Firms WHERE id=?", args=(firms_id,))