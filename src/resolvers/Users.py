from sql_base.models import User
from sql_base.Rescript import base_worker


def check_login(user: User):
    query = "SELECT post_id FROM User WHERE login = ? AND password = ?"
    post_id = base_worker.execute(query, (user.login, user.password), many=False)
    return post_id


def new_user(user: User):
    n = base_worker.execute(f"""INSERT INTO User (login, password, post_id) 
                                    VALUES(?,?,?) RETURNING id;""",
                            (user.login, user.password, user.post_id))
    return n


def update_user(user: User, User_id: int):
    update_id = base_worker.execute(f"""update User set (login, password, post_id) = (?, ?, ?) where id=(?);""",
                                    (user.login, user.password,  user.post_id, User_id))
    return update_id


def get_all_user():
    return base_worker.execute(query="SELECT id, login, post_id  FROM User", many=True)


def delete_user(user_id: int):
    return base_worker.execute(query="DELETE User WHERE id=? ",
                               args=(user_id,))


def get_user(user_id: int):
    return base_worker.execute(query="SELECT id, login, password, post_id FROM User WHERE id=?", args=(user_id,))