#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiohttp import web

from handlers.authorization import authorize, authorization
from handlers.vacancy.getitem import getitem
from handlers.vacancy.listitems import listitems
from handlers.vacancy.additem import additem
from handlers.vacancy.removeitem import removeitem


# Routing table definition
routes = [
    web.route('POST', '/', authorize),
    web.route('GET', '/vacancy', listitems, name = 'list'),
    web.route('GET', '/vacancy/{id}', getitem, name = 'view'),
    web.route('PUT', '/vacancy', additem, name = 'new'),
    web.route('DELETE', '/vacancy/{id}', removeitem, name = 'remove')
]

