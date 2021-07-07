from flask import request, render_template, redirect, make_response
from flask.helpers import url_for
from poker_quiz import app
from services.quiz import poker_test
import services.registration as reg
import services.login
from config import SECRET_KEY
from utils import get_hash256, str_to_b64


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        re_password = request.form['re_password']
        email = request.form['email']

        if not reg.check_username_format(username):
            return render_template('registration.html', username=username,
                                   email=email,
                                   error=reg.error.username_format)

        if not reg.check_email_format(email):
            return render_template('registration.html', username=username,
                                   email=email,
                                   error=reg.error.email_format)

        if not reg.check_password_format(password):
            return render_template('registration.html', username=username,
                                   email=email,
                                   error=reg.error.password_format)

        if not reg.is_same_password(password, re_password):
            return render_template('registration.html', username=username,
                                   email=email,
                                   error=reg.error.passwords_not_equals)

        # Creating hash of user password before add to database.
        hashed_password = get_hash256(str_to_b64(password)+SECRET_KEY)

        if not reg.add_new_user(username=username,
                                email=email,
                                password=hashed_password):
            return render_template('registration.html', username=username,
                                   email=email,
                                   error=reg.error.username_is_same)

        return redirect(url_for('index'))


@app.route('/')
def index():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    if services.login.check_username(username, password):
        return render_template('index.html',
                               numbers_of_questions=len(poker_test))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = get_hash256(str_to_b64(password)+SECRET_KEY)
        if services.login.check_username(username, hashed_password):
            response = make_response(redirect(url_for('index')))
            response.set_cookie('username', username)
            response.set_cookie('password', hashed_password)
            return response
    return render_template('login.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    if not services.login.check_username(username, password):
        return redirect(url_for('login'))

    if len(poker_test) == 0:
        correct = len(poker_test.list_of_correct)
        incorrect = len(poker_test.list_of_incorrect)
        poker_test.reset_test()
        return render_template('result.html', correct=correct,
                               incorrect=incorrect)

    if request.method == 'POST':
        answer = request.form['answer']
        q = poker_test.pop()

        if q.check_answer(answer):
            poker_test.add_to_correct(q)
        else:
            poker_test.add_to_incorrect(q)
        return redirect(url_for('test'))

    return render_template('test.html', question=poker_test[-1])
