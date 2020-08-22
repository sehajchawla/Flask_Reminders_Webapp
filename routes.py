from app import app
from flask import render_template
from forms import AddTaskForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', current_title="Custome Title")

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
    return render_template('about.html', form=form)
