from peewee import *
import datetime
db = SqliteDatabase('database.db')

class Users(Model):
    name = CharField()
    username = CharField()
    password = CharField()
    joindate = DateTimeField(default=datetime.datetime.now)
    birthday = DateField()
    perfil_image = CharField()
    is_superuser= BooleanField(default=False)
    email = CharField() 

    class Meta:
        database = db

class Posts(Model):
    title = CharField()
    body = TextField()
    aditional_image = CharField()
    author = ForeignKeyField(Users)
    
    class Meta:
        database = db

class Comments(Model):
    comment = CharField()
    comment_author = ForeignKeyField(Users)

    class Meta:
        database = db
    
class SubComments(Model):
    parent_comment = ForeignKeyField(Comments)
    comment = CharField()

    class Meta:
        database = db

class PostLikes(Model):
    post = ForeignKeyField(Posts)
    user = ForeignKeyField(Users)

    class Meta:
        database = db

class CommentLikes(Model):
    comment = ForeignKeyField(Comments)
    user = ForeignKeyField(Users)

    class Meta:
        database = db

class SubCommentLikes(Model):
    comment = ForeignKeyField(Comments)
    user = ForeignKeyField(Users)

    class Meta:
        database = db