#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
from config import config


conn = psycopg2.connect(config["pg_dsn"])
cursor = conn.cursor()


print("Creating tables")
with open('sql/init.sql') as f:
    cursor.execute(f.read())
    conn.commit()
print("Success (%s)" % (cursor.rowcount,))


print("Filling the database with values")
with open('sql/fill.sql') as f:
    cursor.execute(f.read())
    conn.commit()
    print("Success (%s)" % (cursor.rowcount,))


cursor.close()
conn.close()

print("Database initialized successfully")
