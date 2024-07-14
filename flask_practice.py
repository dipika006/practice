from flask import Flask
app = Flask(__name__)
def myfun():
    return "Hello"
@app.route('/')
def print_myfun():
    result=myfun()
    return result
if __name__=='__main__':
    app.run(debug=True)

