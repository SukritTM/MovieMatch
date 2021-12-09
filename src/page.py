from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
from src.db import get_db

from src.auth import login_required

bp = Blueprint('page', __name__, url_prefix='/')

@bp.route('/movie', methods=('GET', 'POST'))
@login_required
def movie_handler():
	mid = request.args.get('id', type=int)
	db = get_db()
	uid = g.user['uid']
	if not mid:
		mid = 1
	else:
		mid += 1
	
	userlist = db.execute('SELECT mid FROM watchlist WHERE uid = ?', (uid,)).fetchall()
	while exists(userlist, mid):
		mid += 1
	
	movie = db.execute('SELECT * FROM movie WHERE mid = ?', (mid,)).fetchone()
	print(movie)
	
	return render_template('movie.html', mid=mid, movie=movie)

@bp.route('/add', methods=('GET', 'POST'))
@login_required
def add():
	mid = request.args.get('id', type=int)
	uid = session.get('user-id')
	db = get_db()
	db.execute('INSERT INTO watchlist (uid, mid) VALUES (?, ?)', (uid, mid))
	db.commit()

	return redirect(url_for('page.movie_handler', id=mid))

@bp.route('/watchlist', methods=('GET', 'POST'))
@login_required
def watchlist():
	user = g.user
	db = get_db()
	movies = db.execute(
            '''SELECT m.mid, m.title, m.picture, m.genre FROM
            movie m INNER JOIN watchlist w ON m.mid = w.mid
            INNER JOIN user u on w.uid = u.uid
            where u.uid = ?''', 
            (str(user[0]),)
        ).fetchall()
	
	return render_template('watchlist.html', movies=movies)

@bp.route('/remove', methods=('GET', 'POST'))
@login_required
def wremover():
	user = g.user
	db = get_db()
	mid = request.args.get('id', type=int)
	uid = user['uid']
	print(uid, mid)

	db.execute(
		'''
		DELETE FROM watchlist
		WHERE uid = ? AND mid = ?
		
		''',
		(uid, mid)
	)
	db.commit()

	return redirect(url_for('page.watchlist'))

def exists(ulist, id):
	for row in ulist:
		if row['mid'] == id:
			return True
	
	return False