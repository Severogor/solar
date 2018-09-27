#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiohttp import web
from json.decoder import JSONDecodeError
from ..authorization import authorization, authorize

###############################
# New vacancy creation handler
# PUT /vacancy
###############################


@authorization
async def additem(request):
    """Vacancy creation handler
        request: aiohttp.web_request.Request object

        returns: aiohttp.web_response.Response object (failure) or raises aiohttp.web_exceptions.HTTPFound exception (success)
    """

    # Acquire new data
    try:
        item = await request.json()

    # 400 Bad Request
    except JSONDecodeError:
        return web.Response(status=400)

    cursor = await request.app['db'].cursor()
    SQL = request.app["sql"]

    # Simplified insert data (psycopg2 driver automatically escapes data)
    try:
        await cursor.execute(SQL["INSERT"], item)

    # 400 Bad Request
    except KeyError:
        return web.Response(status=400)

    request.app['db'].commit()
    # Get newly created row ID
    row = await cursor.fetchone()
    item = dict(row)

    # Spec should define the necessity to return data (200) or make a redirect (302)
    raise web.HTTPFound(location=request.app.router['view'].url_for(id=str(item['id'])))
    # return web.json_response(item)

