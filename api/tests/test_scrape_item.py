from api.scrapers.item import scrape_item_by_id
from api import app, db

from flask.json import loads

import unittest

app.config['TESTING'] = True
db.create_all()


class ScrapeItem(unittest.TestCase):

    def test_scrape_item_by_id(self):
        item = scrape_item_by_id('d19447e548d')
        self.assertEqual('d19447e548d', item.lodestone_id)
        self.assertEqual('Thyrus Zenith', item.name)
        self.assertEqual('Two-handed Conjurer\'s Arm', item.type)
        self.assertEqual(90, item.ilvl)

    def test_item_json(self):
        with app.test_client() as client:
            response = client.get('/scrape/item/cada9ec7074')
            self.assertEqual(response.status_code, 200)

            json = loads(response.data)
            self.assertEqual(json, {
                "id": "cada9ec7074",
                "ilvl": 110,
                "name": "Arachne Robe",
                "type": "Body"
            })

    def test_invalid_lodestone_id(self):
        with app.test_client() as client:
            response = client.post('/scrape/item/23fh032hf0oi1so3a012r1')
            self.assertEqual(response.status_code, 405)
