from src.database.database import Users
from src.util.password import encrypt_password
from datetime import datetime,timedelta
from src.util.auth import create_token


class UserController:

    def __init__(self):
        None

    def create(self,  name, username, password, joindate, birthday, perfil_image, email):
        encripted_password = encrypt_password(password)
        user = Users(
            name=name,
            username=username,
            password=encripted_password,
            joindate=joindate,
            birthday=birthday,
            perfil_image=perfil_image,
            email=email
        )
        id = user.save()
        return user.get_by_id(id)

    def login(self, username, password):
        encripted_password = encrypt_password(password)
        user = Users.select().where((Users.username == username) &
                                    (Users.password == encripted_password)).first()
        expiration_date = datetime.now()
        expiration_date += +timedelta(hours=1)
        session_token = create_token({
            "name": user.name,
            "username": user.username,
            "email": user.email,
            "birthday": user.birthday.isoformat(),
            "perfil_image": user.perfil_image,
            "iat": expiration_date.isoformat()
        }, user.password)
        return {
            "session_token": session_token
        }

    def update(token, user):
        None