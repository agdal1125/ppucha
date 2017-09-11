import os

from flask import Flask
from flask import render_template
from app.database import db_session, init_db
from app.models import User
from app import generator, hangul


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

init_db()

# How to insert entries to DB
# from database import db_session
# from models import User
# u = Users('a','b','c,'d')
# db_session.add(u) 
# db_session.commit()
#
#


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
