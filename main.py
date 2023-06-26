from flask import Flask, render_template
from comment.comment_api import comment_bp
from hashtag.hashtag_api import hastag_bp
from photo.photo_api import photo_bp
from posts.posts_api import post_bp
from user.user_api import user_bp

app = Flask(__name__)


@app.route('/')
def test_api():

    return render_template('test.html')


app.register_blueprint(comment_bp)
app.register_blueprint(hastag_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(post_bp)
app.register_blueprint(user_bp)

app.run()
