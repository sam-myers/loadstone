from api import app, db
from api.scrapers.item import scrape_item_by_id

from flask.json import jsonify


@app.route('/scrape/item/<string:lodestone_id>')
def scrape_item(lodestone_id):
    item = scrape_item_by_id(lodestone_id)
    return jsonify(item.as_dict)
