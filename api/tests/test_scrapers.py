def test_scrape_item_by_id():
    from api.scrapers.item import scrape_item_by_id

    item = scrape_item_by_id('d19447e548d')

    assert item.id == 'd19447e548d'
    assert item.name == 'Thyrus Zenith'
    assert item.type == 'Two-handed Conjurer\'s Arm'
    assert item.ilvl == 90


def test_scrape_character_by_id():
    from api.scrapers.character import scrape_character_by_id

    name = scrape_character_by_id('8774791')

    assert name.id == '8774791'
    assert name.name == 'Mina Loriel'
    assert name.species == 'Miqo\'te'
    assert name.gender == 'Female'
