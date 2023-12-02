from flask import Flask, render_template
from helpers import todo

app: Flask = Flask(__name__)
todo_list: list[todo] = []
todo_count: int = 0

from flask import Flask, render_template, request

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/create-todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        global todo_list
        global todo_count
                
        title: str = request.form['title']
        description: str = request.form['description']

        if title == '':
            return render_template("create-todo.html")

        new_todo: todo = todo(todo_count, title, description)
        todo_list.append(new_todo)

        todo_count += 1

        return render_template("success.html", title=title, description=description)
    return render_template("create-todo.html")

@app.route('/view-todo-list')
def view_todo_list():
    return render_template('view-list.html', todo_list=todo_list)
 
@app.route('/iron-man', methods=["GET", "POST"])
def iron_man():
    return render_template('iron-man.html')

@app.route('/hulk', methods=["GET", "POST"])
def hulk():
    return render_template('hulk.html')

@app.route('/iron-man-2', methods=["GET", "POST"])
def iron_man_2():
    return render_template('iron-man-2.html')

@app.route('/thor', methods=["GET", "POST"])
def thor():
    return render_template('thor.html')

@app.route('/captain_america_1', methods=["GET", "POST"])
def captain_america():
    return render_template('captain-america-1.html')

@app.route('/avengers-1', methods=["GET", "POST"])
def avengers_1():
    return render_template('avengers-1.html')

@app.route('/iron-man-3', methods=["GET", "POST"])
def iron_man_3():
    return render_template('iron-man-3.html')

@app.route('/thor-2', methods=["GET", "POST"])
def thor_2():
    return render_template('thor-2.html')

@app.route('/captain-america-2', methods=["GET", "POST"])
def captain_america_2():
    return render_template('captain-america-2.html')

@app.route('/gotg', methods=["GET", "POST"])
def gotg():
    return render_template('gotg.html')

@app.route('/avengers-2', methods=["GET", "POST"])
def avengers_2():
    return render_template('avengers-2.html')

# @app.route('/ant-man', methods=["GET", "POST"])
# def ant_man():
#     return render_template('ant-man.html')

@app.route('/captain-america-3', methods=["GET", "POST"])
def captain_america_3():
    return render_template('captain-america-3.html')

@app.route('/doctor-strange', methods=["GET", "POST"])
def doctor_strange():
    return render_template('doctor-strange.html')

@app.route('/gotg-2', methods=["GET", "POST"])
def gotg_2():
    return render_template('gotg-2.html')

@app.route('/spider-man-1', methods=["GET", "POST"])
def spider_man_1():
    return render_template('spider_man_1.html')

@app.route('/thor-3', methods=["GET", "POST"])
def thor_3():
    return render_template('thor-3.html')

@app.route('/black-panther', methods=["GET", "POST"])
def black_panther():
    return render_template('black_panther.html')

@app.route('/avengers-3', methods=["GET", "POST"])
def avengers_3():
    return render_template('avengers_3.html')

# @app.route('/ant-man-2', methods=["GET", "POST"])
# def ant_man():
#     return render_template('ant-man-2.html')

@app.route('/captain-marvel', methods=["GET", "POST"])
def captain_marvel():
    return render_template('captain-marvel.html')

@app.route('/avengers-4', methods=["GET", "POST"])
def avengers_4():
    return render_template('avengers-4.html')

@app.route('/spider-man-2', methods=["GET", "POST"])
def spider_man_2():
    return render_template('spider-man-2.html')

if __name__ == '__main__':
    app.run(debug=True)