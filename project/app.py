from flask import Flask, render_template
from helpers import todo

app: Flask = Flask(__name__)
todo_list: list[todo] = []
todo_count: int = 0

@app.route("/")
def index():
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True)