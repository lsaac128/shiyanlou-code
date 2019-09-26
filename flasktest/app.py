from flask import Flask, url_for

app = Flask(__name__)
app.config.update({
    'SECRET_KEY':'a random string'
} )

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/user/<username>')
def user_index(username):
    return 'Hello {}'.format(username)

@app.route('/port/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/courses/<name>')
def courses_name(name):
    return 'Courses: {}'.format(name)

@app.route('/test')
def test():
    print(url_for('index'))
    print(url_for('user_index', username='shixiaolou'))
    print(url_for('show_post', post_id=1, _external=True))
    print(url_for('show_post', post_id=2, q='python 03'))
    print(url_for('show_post', post_id=2, q='python可以'))
    print(url_for('show_post', post_id=2, _anchor='a'))
    return 'test'

if __name__ == '__main__':
    app.run()
