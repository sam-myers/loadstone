def test_item_json(client):
    response = client.get('/scrape/item/cada9ec7074')

    assert response.status_code == 200
    assert response.json == {
        'id': 'cada9ec7074',
        'ilvl': 110,
        'name': 'Arachne Robe',
        'type': 'Body'
    }


def test_item_invalid_lodestone_id(client):
    response = client.get('/scrape/item/23fh032hf0oi1so3a012r1')

    assert response.status_code == 403
    assert response.json == {
        'error': 'Invalid Request',
        'message': 'Lodestone ID does not exist'
    }


def test_item_repr():
    from api.scrapers.item import scrape_item_by_id

    item = scrape_item_by_id('ec2ddbdcd47')
    assert repr(item) == '<Item lodestone_id=ec2ddbdcd47 name=Weathered Daystar Gloves type=Hands ilvl=100>'
