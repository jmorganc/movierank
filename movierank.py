"""
TODO
"""


import MySQLdb, MySQLdb.cursors

from bottle import route, run, template, debug, static_file
import config

import sys
import json
import pprint


"""------------------------------
ROUTES
------------------------------"""
"""
Main / Index
"""
@route('/')
def index():
    return template('templates/index')


"""
Movies

TODO: Get user_id from session
"""
@route('/movies')
def index():
    con = mysql_connect()
    with con:
        c = con.cursor()
        c.execute('SELECT id, title FROM movies ORDER BY title ASC')
        movies_all = c.fetchall()
        c.execute('SELECT movie_id FROM movies_users WHERE user_id = %s', (1,))
        movies_users = c.fetchall()

    movies_nic = []
    movies_ic = []
    for movie in movies_all:
        if {'movie_id': movie['id']} in movies_users:
            movies_ic.append({'id': movie['id'], 'title': movie['title'], 'in_collection': True})
        else:
            movies_nic.append({'id': movie['id'], 'title': movie['title'], 'in_collection': False})
    movies = movies_nic + movies_ic

    return template('templates/movies', movies=movies)


"""
Static file handlers
"""
@route('/js/<filename>')
def static_js(filename):
    return static_file(filename, root='./static/js')


@route('/css/<filename>')
def static_js(filename):
    return static_file(filename, root='./static/css')


@route('/img/<filename>')
def static_js(filename):
    return static_file(filename, root='./static/img')


"""------------------------------
PRIVATE FUNCTIONS
------------------------------"""
"""
MySQL Connector
"""
def mysql_connect(host=config.opts['mysql']['host'], username=config.opts['mysql']['username'], password=config.opts['mysql']['password'], database=config.opts['mysql']['database']):
    return MySQLdb.connect(host, username, password, database, cursorclass=MySQLdb.cursors.DictCursor)


"""
"""
debug(True)
run(relaoder=True)







def main():
    movies = json.loads(open('testmovies.json', 'r').read())
    #pprint.pprint(movies)
    # Make this a class?
    # try:
    #     self.movies_json = json.loads(open('testmovies.json', 'r').read())
    # except (IOError, ValueError) as error:
    #     open('testmovies.json', 'w').write(json.dumps(self.movies_json))

    for movie_a in movies:
        for movie_b in movies:
            if movie_a['id'] == movie_b['id']:
                continue
            if movie_a['id'] in movie_b['compared'] or movie_b['id'] in movie_a['compared']:
                continue
            print '(A) {0} vs. (B) {1}'.format(movie_a['title'], movie_b['title'])
            winner = raw_input('Who wins? A or B or T (tie) or S (skip): ')
            winner = winner.lower()

            wp_a = win_probability(movie_a['rank'], movie_b['rank'])
            wp_b = win_probability(movie_b['rank'], movie_a['rank'])

            if winner == 's':
                continue
            if winner == 'a':
                nr_a = new_rating(movie_a['rank'], wp_a, 1)
                nr_b = new_rating(movie_b['rank'], wp_b, 0)
            elif winner == 'b':
                nr_a = new_rating(movie_a['rank'], wp_a, 0)
                nr_b = new_rating(movie_b['rank'], wp_b, 1)
            elif winner == 't':
                nr_a = new_rating(movie_a['rank'], wp_a, 0.5)
                nr_b = new_rating(movie_b['rank'], wp_b, 0.5)

            movie_a['compared'].append(movie_b['id'])
            movie_b['compared'].append(movie_a['id'])

            movie_a['rank'] = nr_a
            movie_b['rank'] = nr_b

    open('testmovies.json', 'w').write(json.dumps(movies))
    pprint.pprint(movies)


def win_probability(me, them):
    return 1 / (10 ** ((them - me) / 400) + 1)


def new_rating(old, wp, point):
    k = 20
    return old + (k * (point - wp))


if __name__ == '__main__':
    sys.exit(main())
