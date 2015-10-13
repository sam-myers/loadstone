def test_scrape_item_by_id():
    from api.scrapers.item import scrape_item_by_id

    item = scrape_item_by_id('d19447e548d')

    assert item.lodestone_id == 'd19447e548d'
    assert item.name == 'Thyrus Zenith'
    assert item.type == 'Two-handed Conjurer\'s Arm'
    assert item.ilvl == 90