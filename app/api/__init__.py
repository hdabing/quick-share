# -*- coding: utf-8 -*-
from flask.ext.api import status
from app import app
from manage import manage
from chat import chat

app.register_blueprint(manage, url_prefix='/api/manage')
app.register_blueprint(chat, url_prefix='/api/chat')