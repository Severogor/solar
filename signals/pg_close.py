#!/usr/bin/python3
# -*- coding: utf-8 -*-

###############################
# Shutdown signal handler
###############################


async def pg_close(app):
    """Shutdown signal handler for closing the database connection
        app: application coroutine object
    """

    await app["db"].close()

