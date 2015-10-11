from api import app, db
from api.scrapers.item import scrape_item_by_id

from flask.json import jsonify


@app.route('/')
def hello_world():
    app.logger.debug('Hello World')
    return 'Hello World!'


@app.route('/migrate')
def migrate():
    app.logger.warning('Migration requested...')
    db.create_all()
    return 'Migration processed'


@app.route('/scrape/item/<string:lodestone_id>')
def scrape_item(lodestone_id):
    item = scrape_item_by_id(lodestone_id)
    return jsonify(item.as_dict)
