#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet
import psycopg2
import aiopg
import base64
import sys

# HTTP requests handlers
from handlers.authorization import authorize, authorization
from handlers.vacancy.getitem import getitem
from handlers.vacancy.listitems import listitems
from handlers.vacancy.additem import additem
from handlers.vacancy.removeitem import removeitem
from sql.logic import SQL

# Routes definitions
from routes import routes

# Signal handlers
from signals.pg_close import pg_close

# Configuration
from config import config

###############################
# Simple REST server
#   (c) Severogor
#   27.09.2018
#   Personal use only
###############################


async def init():
    """Initialize web application

        returns: application coroutine object
    """

    # Base application object
    app = web.Application()
    # Session setup
    key = base64.urlsafe_b64decode(fernet.Fernet.generate_key())
    setup(app, EncryptedCookieStorage(key))
    # Routes
    app.add_routes(routes)
    # Database
    app['db'] = await aiopg.connect(config["pg_dsn"], cursor_factory=psycopg2.extras.DictCursor)
    app['sql'] = SQL
    # Shutdown signal handler
    app.on_shutdown.append(pg_close)

    return app


app = init()
web.run_app(app, host=config["host"], port=config["port"])

