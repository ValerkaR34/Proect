from sql_base import models
from sql_base import base_worker


def check_login(user: models.User) -> int:
    query = "SELECT post FROM users WHERE login = ? AND password = ? AND phone_number = ?"
    post_id = base_worker.execute(query, (user.login, user.password, user.phone_number), many=False)
    return post_id