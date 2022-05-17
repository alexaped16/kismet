from app import app, db
from flask import redirect, render_template, url_for, flash
from app.models import joinTheCommunity
from app.forms import joinTheCommunity

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

@app.route('/calendar_and_events')
def calendar_and_events():
    title = 'Calendar and Events'
    return render_template('calendar_and_events.html',  title=title)

@app.route('/join_the_community', methods=['POST', 'GET'])
def join_the_community():
    form = joinTheCommunity()
    title = 'Join The Community'
    if form.validate_on_submit():
        email = form.email.data   
        message = form.message.data

        new_message = joinTheCommunity(email=email, message=message)
        
        flash(f"Thank you for your message (:  We will be in touch shortly! ", "success")
        return redirect(url_for('index'))

    return render_template('join_the_community.html', title=title, form=form)