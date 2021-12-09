import os

from flask import Flask
from flask.helpers import url_for
from werkzeug.utils import redirect

def create_app(test_config=None):

	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'src.sqlite')
	)

	if test_config is None:
		# load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	from . import db
	db.init_app(app)

	from . import auth
	app.register_blueprint(auth.bp)

	from . import page
	app.register_blueprint(page.bp)

	@app.route('/')
	def redir():
		return redirect(url_for('page.movie_handler'))

	@app.route('/hello')
	def hello():
		return '<h1>Hello World</h1>'
	
	return app

if __name__ == '__main__':
    app = create_app()
    app.run()