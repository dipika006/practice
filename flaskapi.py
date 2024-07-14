from flask import Flask, request, redirect
app=Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to flask api!'

@app.route('/<username>')
def say_hello(username):
    return f'Hello {username}!'

@app.route('/add')
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    c=a+b
    return {'sum': c}

@app.route('/profile')
def profile():
    return {'firstname': 'Dipika', 'lastname': 'Dhara'}

@app.route('/login', methods=['POST'])
def post_json():
    username = request.json.get('username')
    return {'username': f'Login request for user {username}!'}

@app.route('/login1', methods=['POST'])
def post_form_data():
    username = request.form.get('username')
    return {'username': f'Login request for user {username}!'}

@app.route('/goto-google')
def redirect_me():
    return redirect('https://www.google.com')

if __name__=='__main__':
    app.run(debug=True,port=8002)