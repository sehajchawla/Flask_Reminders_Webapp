from app import app
from flask import render_template
from forms import AddTaskForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', current_title="Custome Title")

@app.route('/about')
def about():
    form = AddTaskForm()
    return render_template('about.html', form=form)
