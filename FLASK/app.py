from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'#Database location
#/// - relative path
#//// - absolute path
db = SQLAlchemy(app) # Initializing the database
# In Python Shell, we run: 1. from app import db 2. db.create_all()

# In Flask, certain objects like db don't work on their own &therefore 
# they need to know which Flask app they belong to,
# especially when you're outside of a running request (like in a Python shell).
# The app.app_context() part is necessary in Flask to bind the app
# to the current thread before running database operations.


# Creating a model for the database
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) #nullable - no nulls
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id 
@app.route('/', methods=['POST', 'GET'])#adding methods that the route can accept(default is GET)
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = ToDo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your new task"
    else:
        tasks = ToDo.query.order_by(ToDo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = ToDo.query.get_or_404(id) #returns 404 - item not found
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that task"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = ToDo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your task"
    else:
        return render_template('update.html', task=task)
if __name__ == "__main__":
    app.run(debug=True)


