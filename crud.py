"""CRUD operations."""

from model import db, Video, connect_to_db

import datetime


def create_video(channel_name, web_title, youtube_title):
   

    video = Video(channel_name=channel_name,
                  web_title=web_title,
                  youtube_title=youtube_title)

    db.session.add(video)

    db.session.commit()

    return video

def get_videos():
    """Return all rows of video data."""

    return Video.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
