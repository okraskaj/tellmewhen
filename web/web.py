import os
from dotenv import load_dotenv
load_dotenv()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('/Users/janek/private/hackathon_projects/tellmewhen/web/tellmewhen-pk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tellmewhen-app.firebaseio.com'
})


def listener(event):
    print(event.event_type)  # can be 'put' or 'patch'
    print(event.path)  # relative to the reference, it seems
    print(event.data)  # new data at /reference/event.path. None if deleted


firebase_admin.db.reference('users').listen(listener)

# ref = db.reference('users')
# print(ref.get())

# firebase = pyrebase.initialize_app(config)
# # print(os.getenv("FIREBASE_API_KEY"))
#
# db = firebase.database()
# print(firebase.requests.get())
# print(db.get("tellmewhen-app"))
