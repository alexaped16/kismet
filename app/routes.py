from app import app, db
from flask import redirect, render_template, url_for, flash

@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',  title=title)


@app.route('/activities&hours')
def activities_and_hours():
    title = 'Activities & Hours'
    return render_template('activities&hours.html',  title=title)

@app.route('/what_we_are')
def what_we_are():
    title = 'What We Are'
    return render_template('what_we_are.html',  title=title)

@app.route('/calendar')
def calendar():
    title = 'Calendar'
    return render_template('calendar.html',  title=title)