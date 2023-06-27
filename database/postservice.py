from models import Post, PostPhoto, PostComment, db
from datetime import datetime


def get_all_posts_db():
    posts = Post.query.all()
    if posts:
        return posts
    return False


def get_all_photo_db():
    photos = PostPhoto.query.all()
    if photos:
        return photos
    return False


def get_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    if post:
        return post
    return False


def delete_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()

    if post:
        db.session.delete(post)
        db.session.commit()
    return False


def change_post_text_db(post_id, new_text):
    post = Post.query.filter_by(post_id=post_id).first()

    if post:
        post.post_text = new_text
        post.post_date = datetime.now()
        db.session.commit()
    return False


def add_comment_post_db(post_id, comment_user_id, comment_text):
    post_comment = PostComment.query.filter_by(post_id=post_id).first()
    post_comment.comment_text = comment_text
    post_comment.user_id = comment_user_id
    post_comment.comment_date = datetime.now()
    db.session.commit()
