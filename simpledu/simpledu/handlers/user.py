from flask import Blueprint, render_template
from simpledu.models import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('<username>')
def index(username):
    if str(username) == session.query(User).filter(User.username==str(username)):

        return render_template('user/detail.html', username=username)
    else:
        return '404'