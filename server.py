"""Server for YourFolder app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Video, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_videos():

    stats=crud.get_videos()
    
    video_id=[q[0] for q in db.session.query(Video.video_id).all()]

    channel_name=[q[0] for q in db.session.query(Video.channel_name).all()]
      
    web_title=[q[0] for q in db.session.query(Video.web_title).all()]

    youtube_title=[q[0] for q in db.session.query(Video.youtube_title).all()]

    return render_template('videos.html', video_id=video_id, channel_name=channel_name, web_title=web_title, youtube_title=youtube_title)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()