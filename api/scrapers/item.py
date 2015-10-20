from api.constants import USER_AGENT
from api.exceptions import InvalidRequest
from api import app, db
from api.models.item import Item

import requests
from lxml import html

# import threading


def scrape_item_by_id(lodestone_id):
    """
    .. image:: ../images/item_lodestone_id.PNG

    >>> thyrus = scrape_item_by_id('d19447e548d')
    >>> thyrus.name
    'Thyrus Zenith'
    >>> thyrus.item_level
    90

    :param lodestone_id: Alpha-numeric ID in the URL of the item's Lodestone page
    :return: New / updated :class:`api.models.Item`
    :raise ParsingException: Unexpected errors while scraping the HTML will throw
    """
    app.logger.debug('Attempting to parse items from id {}'.format(lodestone_id))

    headers = {'User-Agent': USER_AGENT}
    uri = 'http://na.finalfantasyxiv.com/lodestone/playguide/db/item/{}/'.format(lodestone_id)
    page = requests.get(uri, headers=headers)
    if page.status_code == 404:
        raise InvalidRequest('Lodestone ID does not exist')
    assert page.status_code == 200

    tree = html.fromstring(page.text)
    item = Item.query.get(lodestone_id)

    if not item:
        item = Item(id=lodestone_id)

        item.name = tree.xpath('//title/text()')[0].split('|')[0].replace('Eorzea Database:', '').strip()
        item.type = tree.xpath('//div[@class="clearfix item_name_area"]/div[@class="box left"]/text()')[2].strip()

        ilvl = int(tree.xpath('//div[@class="eorzeadb_tooltip_pt3 eorzeadb_tooltip_pb3"]/text()')[0].
                   replace('Item Level ', ''))
        item.ilvl = ilvl if ilvl else 0

        main_stats = tree.xpath('//div[@class="clearfix sys_nq_element"]/div/strong/text()')
        if main_stats:
            if item.type == "Shield":
                item.block_strength = int(main_stats[0])
                item.block_rate = int(main_stats[1])
            elif len(main_stats) == 2:
                item.defense = int(main_stats[0])
                item.magic_defense = int(main_stats[1])
            else:
                item.damage = int(main_stats[0])
                item.auto_attack = float(main_stats[1])
                item.delay = float(main_stats[2])

        basic_stats = tree.xpath('//ul[@class="basic_bonus"]/li/text()')
        for stat_string in basic_stats:
            setattr(
                item,
                stat_string.split('+')[0].strip().lower().replace(' ', '_'),  # Sanitized stat name, eg. 'vitality'
                int(stat_string.split('+')[1].strip())                        # Its value
            )

        db.session.add(item)

    return item

# class ItemThread(threading.Thread):
#
#     def __init__(self, item_id):
#         threading.Thread.__init__(self)
#         self.item_id = item_id
#         self._item = None
#
#     def run(self):
#         self._item = scrape_item_by_id(self.item_id)
#
#     def join(self, timeout=None):
#         threading.Thread.join(self)
#         return self._item
#
#     def __repr__(self):
#         return '<ItemThread item={}>'.format(
#             self._item.__repr__()
#         )
