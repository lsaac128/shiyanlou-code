from flask import Flask, request


app = Flask(__name__)

app.config.update({
    'SECRET_KEY':'a random string'
})

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/httptest', methods=['get', 'post'])
def httptest():
    if request.method == 'POST':
        print('Q:', request.form.getlist('Q'))
        return 'It is a post request!'
    print('q:', request.args.get('q'))
    print('t:', request.args.get('t'))
    return 'It is a get request!'

@app.route('/user/<username>')
def user_index(username):
    return 'Hello {}'.format(username)

@app.route('/port/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/courses/<coursename>')
def courses(coursename):
    return render_template('courses.html', coursename=coursename)

@app.route('/test')
def test():
    print(url_for('courses', name='java' , _external=True))
    return 'Hello Shiyanlou!'

@app.route('/<username>')
def hello(username):
    if username == 'shiyanlou':
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
