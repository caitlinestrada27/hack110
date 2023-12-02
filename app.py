from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/create-todo')
def create_todo():
    return render_template("create-todo.html")
 
if __name__ == '__main__':
    app.run(debug=True)