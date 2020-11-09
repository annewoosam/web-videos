"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb web_videos')

os.system('createdb web_videos')

model.connect_to_db(server.app)

model.db.create_all()


# Create video table's initial data.

with open('data/video.json') as f:

    video_data = json.loads(f.read())

video_in_db = []

for video in video_data:
    channel_name, web_title, youtube_title= (
                                   video['channel_name'],
                                   video['web_title'],
                                   video['youtube_title'])

    db_video = crud.create_video(
                                 channel_name,
                                 web_title,
                                 youtube_title)

    video_in_db.append(db_video)
