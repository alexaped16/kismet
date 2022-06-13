from app import app, db
from flask import redirect, render_template, url_for, flash


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',  title=title)

@app.route('/activities')
def activities():
    title = 'Activities'
    return render_template('activities.html',  title=title)

@app.route('/what_we_are')
def what_we_are():
    title = 'What We Are'
    return render_template('what_we_are.html',  title=title)

@app.route('/calendar_and_events')
def calendar_and_events():
    title = 'Calendar and Events'
    return render_template('calendar_and_events.html',  title=title)

@app.route('/join_the_community')
def join_the_community():
    title = 'Join The Community'

    return render_template('join_the_community.html', title=title)




@app.route('/DJ')
def DJ():
    title = 'DJ'
    return render_template('DJ.html',  title=title)

@app.route('/WD')
def WD():
    title = 'WD'
    return render_template('WD.html',  title=title)

@app.route('/PIP')
def PIP():
    title = 'PIP'
    return render_template('PIP.html',  title=title)

@app.route('/CC')
def CC():
    title = 'CC'
    return render_template('CC.html',  title=title)

@app.route('/VM')
def VM():
    title = 'VM'
    return render_template('VM.html',  title=title)








