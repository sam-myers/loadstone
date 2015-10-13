from api import app
from api.scrapers.item import scrape_item_by_id
from api.scrapers.character import scrape_character_by_id
from api.exceptions import InvalidRequest

from flask.json import jsonify

from functools import wraps


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
def scrape_item(lodestone_id):
    return scrape_item_by_id(lodestone_id)


@app.route('/scrape/character/<string:lodestone_id>')
@restful_api
def scrape_character(lodestone_id):
    return scrape_character_by_id(lodestone_id)
