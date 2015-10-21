from api import app
from api.scrapers.item import scrape_item_by_id
from api.scrapers.character import scrape_character_by_id
from api.exceptions import InvalidRequest
from api.models.item import Item

from flask.json import jsonify

from functools import wraps
import re


def restful_api(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            json = f(*args, **kwargs)
        except InvalidRequest as e:
            return jsonify(e.as_dict), e.status_code
        return jsonify(json.as_dict)
    return decorated


@app.route('/scrape/item/<string:lodestone_id>')
@restful_api
def get_item(lodestone_id):
    if not re.match(r'^[0-9a-z]+$', lodestone_id):
        raise InvalidRequest('Illegal characters in requested ID')

    return scrape_item_by_id(lodestone_id)


@app.route('/scrape/character/<string:lodestone_id>')
@restful_api
def get_character(lodestone_id):
    if not re.match(r'^[0-9]+$', lodestone_id):
        raise InvalidRequest('Illegal characters in requested ID')

    return scrape_character_by_id(lodestone_id)
