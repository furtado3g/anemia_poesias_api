from database import db,Users,Posts,Comments,SubComments,PostLikes,CommentLikes,SubCommentLikes

db.connect()
db.create_tables([Users,Posts,Comments,SubComments,PostLikes,CommentLikes,SubCommentLikes])