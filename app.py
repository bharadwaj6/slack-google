# -*- coding: utf-8 -*-

import os

from flask import Flask, request, Response, redirect
from pygoogle import PyGoogle


NO_PAGES = 1

app = Flask(__name__)


@app.route('/google', methods=['post'])
def google():
    '''
    Example:
        /google python list comprehension
    '''
    search_query = request.values.get('text')

    gs = PyGoogle(search_query)
    gs.pages = NO_PAGES

    urls = gs.get_result_urls()
    # need to remove | character to get links right in slack output
    titles = [t.replace('|', '') for t in gs.get_result_titles()]
    resp = dict(zip(titles, urls))

    if not resp:
        resp = 'No results found.'
    else:
        temp = []
        for k in resp:
            temp.append('<%s|%s>' % (resp[k], k))
        resp = '\n'.join(temp)

    return Response(resp, content_type='text/plain; charset=utf-8')


@app.route('/')
def hello():
    return redirect('https://github.com/bharadwaj6/slack-google')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
