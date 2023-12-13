from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String  # Add these lines


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(200))

    def __repr__(self):
        return f'<Todo {self.id}>'


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    description = request.form['description']

    if title and description:  # Check if both fields are not empty
        new_todo = Todo(title=title, description=description)
        db.session.add(new_todo)
        db.session.commit()
    else:
        return render_template('index.html', alert_message="Title and Description are required fields!")

    return redirect(url_for('index'))


@app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update(todo_id):
    todo = Todo.query.get_or_404(todo_id)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('update.html', todo=todo)

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

