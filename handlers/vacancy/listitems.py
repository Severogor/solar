#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiohttp import web
from ..authorization import authorization, authorize

###############################
# Vacancies list view handler
# GET /vacancy
###############################


@authorization
async def listitems(request):
    """Display vacancies list handler
        request: aiohttp.web_request.Request object

        returns: aiohttp.web_response.Response object
    """

    items = []
    cursor = await request.app['db'].cursor()
    SQL = request.app["sql"]

    # Select all
    await cursor.execute(SQL["SELECT_ALL"])
    for row in cursor:
        items.append(dict(row))

    return web.json_response(items)

