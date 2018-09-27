#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiohttp import web
from ..authorization import authorization, authorize

###############################
# Single vacancy removal handler
# DELETE /vacancy/{id}
###############################


@authorization
async def removeitem(request):
    """Single vacancy removal handler
        request: aiohttp.web_request.Request object

        returns: aiohttp.web_response.Response object
    """

    # Acquire requested ID
    try:
        _id = int(request.match_info["id"])

    # 400 Bad Request
    except ValueError:
        return web.Response(status=400)

    cursor = await request.app['db'].cursor()
    SQL = request.app["sql"]

    # Delete row by ID
    await cursor.execute(SQL["DELETE"], (_id,))
    request.app['db'].commit()
    # Check if specified row was found or not
    rc = cursor.rowcount

    # 404 Not Found
    if not rc:
        return web.Response(status=404)

    # Success
    return web.Response(status=200)

