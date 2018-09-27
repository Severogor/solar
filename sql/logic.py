#!/usr/bin/python3
# -*- coding: utf-8 -*-

###############################
# Database logic definitions
###############################


SQL = {
    # Authorization
    "CHECK_AUTH": 'SELECT id, role, resource FROM role LEFT JOIN access USING(id) WHERE (role, password) = (%(username)s, %(password)s);',
    # Check permissions
    "CHECK_PERM": 'SELECT id, role, resource FROM role LEFT JOIN access USING(id) WHERE (id, resource) = (%s, %s);',
    # Select all vacancies
    "SELECT_ALL": 'SELECT * FROM vacancy ORDER BY id;',
    # Select exact vacancy
    "SELECT_ID": 'SELECT * FROM vacancy WHERE id = %s;',
    # Create new vacancy
    "INSERT": 'INSERT INTO vacancy (vacancy, salary, experience, city) VALUES (%(vacancy)s, %(salary)s, %(experience)s, %(city)s) RETURNING *;',
    # Delete exact vacancy
    "DELETE": 'DELETE FROM vacancy WHERE id = %s RETURNING id;'
}


