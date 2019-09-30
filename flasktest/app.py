from flask import Flask, request, render_template


app = Flask(__name__)

app.config.update({
    'SECRET_KEY':'a random string'
})

@app.route('/')
def index():
    course = {
            'python':'lou+ python',
            'java':'java base',
            'bigdata':'spark sql',
            'teacher':'shixiaolou',
            'is_unique':False,
            'has_tag':True,
            'tags':['c', 'c++', 'docker']
            }
    return render_template('index.html', course=course)

@app.route('/courses/<courses_name>')
def coursesname(courses_name):
    return 'Courses:{}'.format(courses_name)

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
