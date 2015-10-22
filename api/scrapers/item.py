from api import db
from api.models.item import Item
from api.scrapers.context_managers import HTMLFromLoadstone


def scrape_item(lodestone_id):
    """
    .. image:: ../images/item_lodestone_id.PNG

    >>> thyrus = scrape_item('d19447e548d')
    >>> thyrus.name
    'Thyrus Zenith'
    >>> thyrus.item_level
    90

    :param lodestone_id: Alpha-numeric ID in the URL of the item's Lodestone page
    :return: New / updated :class:`api.models.Item`
    :raise ParsingException: Unexpected errors while scraping the HTML will throw
    """
    item = Item.query.get(lodestone_id)
    if not item:

        url = 'http://na.finalfantasyxiv.com/lodestone/playguide/db/item/{}/'.format(lodestone_id)
        with HTMLFromLoadstone(url) as html:

            item = Item(id=lodestone_id)

            item.name = html.xpath('//title/text()')[0].split('|')[0].replace('Eorzea Database:', '').strip()
            item.type = html.xpath('//div[@class="clearfix item_name_area"]/div[@class="box left"]/text()')[2].strip()

            ilvl = int(html.xpath('//div[@class="eorzeadb_tooltip_pt3 eorzeadb_tooltip_pb3"]/text()')[0].
                       replace('Item Level ', ''))
            item.ilvl = ilvl if ilvl else 0

            main_stats = html.xpath('//div[@class="clearfix sys_nq_element"]/div/strong/text()')
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

            basic_stats = html.xpath('//ul[@class="basic_bonus"]/li/text()')
            for stat_string in basic_stats:
                setattr(
                    item,
                    stat_string.split('+')[0].strip().lower().replace(' ', '_'),  # Sanitized stat name, eg. 'vitality'
                    int(stat_string.split('+')[1].strip())                        # Its value
                )

            db.session.add(item)

    return item
