from sql_base import models
from sql_base.Resources import base_worker


def check_login(user: models.User) -> int:
    query = "SELECT post FROM users WHERE login = ? AND password = ?"
    post_id = base_worker.execute(query, (user.login, user.password), many=False)
    return post_id

def new_user(user: models.User) -> int:
    new_pol = base_worker.execute(f"""INSERT INTO User (login, password, phone_number) 
                                    VALUES(?,?,?) RETURNING id;""",
                                    (user.login, user.password, user.phone_number))


def update_user(user: models.User) -> int:
    update_id = base_worker.execute(f"""UPDATE user SET login=(?), password=(?), phone_number=(?) WHERE id = {user} RETURNING id;""",
                                     (user.login, user.password, user.phone_number))
    return update_id