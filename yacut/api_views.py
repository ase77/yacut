import re

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URL_map
from .views import get_unique_short_id


@app.route('/api/id/<string:short_url>/', methods=['GET'])
def get_url(short_url):
    url = URL_map.query.filter_by(short=short_url).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    data = url.to_dict()
    return jsonify({'url': data['url']}), 200


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if ('custom_id' not in data or
            data['custom_id'] == '' or
            data['custom_id'] is None):
        data['custom_id'] = get_unique_short_id()
    if URL_map.query.filter_by(short=data['custom_id']).first() is not None:
        custom_id = data['custom_id']
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
    if (re.match('^[a-zA-Z0-9_]*$', data['custom_id']) is None or
            len(data['custom_id']) > 16):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    url = URL_map()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201
