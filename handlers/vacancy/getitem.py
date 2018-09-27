#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiohttp import web
from ..authorization import authorization, authorize

###############################
# Single vacancy display handler
# GET /vacancy/{id}
###############################


@authorization
async def getitem(request):
    """Single vacancy display handler
        request: aiohttp.web_request.Request object

        returns: aiohttp.web_response.Response object
    """

    # Acquire requested ID
    try:
        _id = int(request.match_info['id'])

    # 400 Bad Request
    except ValueError:
        return web.Response(status=400)

    cursor = await request.app['db'].cursor()
    SQL = request.app["sql"]

    # Select a record by ID
    items = []
    await cursor.execute(SQL["SELECT_ID"], (_id,))
    for row in cursor:
        items.append(dict(row))

    try:
        return web.json_response(items[0])

    # 404 Not Found
    except IndexError:
        return web.Response(status=404)

