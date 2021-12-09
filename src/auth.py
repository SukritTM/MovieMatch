import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from werkzeug.security import check_password_hash, generate_password_hash

from src.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['cpassword']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Blank password is not valid'
        elif confirm != password:
            error = 'Passwords do not match'
        elif db.execute('SELECT uid FROM user WHERE username = ?', (username,)).fetchone():
            error = f'user {username} is already taken'
        
        if not error:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)', (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        
        flash (error)
    
    return render_template('register.html')

@bp.route('/login', methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        user = db.execute('SELECT * FROM user WHERE username = ?', (username,)).fetchone()

        if not user:
            error = 'Username is incorrect'
        elif not check_password_hash(user['password'], password):
            error = 'incorrect password'
        
        if not error:
            session.clear()
            session['user-id'] = user['uid']
            return redirect(url_for('page.movie_handler'))
        
        flash(error)
    
    return render_template('login.html')

@bp.before_app_request
def load_user():
    user_id = session.get('user-id')

    if not user_id:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM user WHERE uid = ?', (int(user_id), )).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapper(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapper