"""
New movies start at 1600
Win probability: 1 / (10 ** ((opponent's rating - my rating) / 400) + 1)
Scoring: 1 for a win, 0 for a loss, 0.5 for a draw
New rating: old rating + (k constant * (scoring point - win probability))
K constant: 8-16 for local, 24-32 for regional, etc. We can just use 20.
Every movie should "fight" every other movie only once (to begin?).
    Any new movie added should go down the list fighting every other movie.
"""


import sys
import json
import pprint


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
            winner = raw_input('Who wins? A or B or T (tie): ')
            winner = winner.lower()

            wp_a = win_probability(movie_a['rank'], movie_b['rank'])
            wp_b = win_probability(movie_b['rank'], movie_a['rank'])

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

    pprint.pprint(movies)


def win_probability(me, them):
    return 1 / (10 ** ((them - me) / 400) + 1)


def new_rating(old, wp, point):
    k = 20
    return old + (k * (point - wp))


if __name__ == '__main__':
    sys.exit(main())
