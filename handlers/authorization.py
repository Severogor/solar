#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiohttp import web
from json.decoder import JSONDecodeError
from aiohttp_session import new_session, get_session

###############################
# Authorization handlers
#  authorization  *    *
#  authorize      POST /
###############################


def authorization(f):
    """Check authorization before calling a handler
        f: handler to call in case of success

        returns: decorated function f
    """

    async def wrapper(request):

        # Get current user session
        session = await get_session(request)

        cursor = await request.app['db'].cursor()
        SQL = request.app["sql"]

        # Check actual permissions for logged-in user
        if session.get("id"):
            await cursor.execute(SQL["CHECK_PERM"], (session["id"], f.__name__))
            if cursor.rowcount:
                return await f(request)

        # No records -- Not permitted
        return web.Response(status=403)

    return wrapper


async def authorize(request):
    """Authorize user by credentials in request JSON body
        request: aiohttp.web_request.Request object

        returns: aiohttp.web_response.Response object
    """

    # Receive JSON credentials
    try:
        auth = await request.json()
        _, _ = auth['username'], auth['password']

    # 400 Bad Request
    except JSONDecodeError:
        return web.Response(status=400)

    except KeyError:
        return web.Response(status=400)

    cursor = await request.app['db'].cursor()
    SQL = request.app["sql"]

    # Simplified case; psycopg2 escapes fields
    await cursor.execute(SQL["CHECK_AUTH"], auth)

    if cursor.rowcount:
        # Start a new session
        session = await new_session(request)

        # Processing user data
        session["id"], session["username"], session["access"] = None, None, {}
        for row in cursor:
            session["access"][row["resource"]] = True
        session["id"], session["username"] = row["id"], row["role"]

        return web.json_response({"username": session["username"], "status": "Authorized"}, status=200)

    # User not found
    return web.json_response({"status": "Access denied", "reason": "No record with specified credentials", "data": auth}, status=403)

