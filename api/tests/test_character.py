def test_scrape_character_by_id_basic_data(mina):
    assert mina.id == '8774791'
    assert mina.name == 'Mina Loriel'
    assert mina.species == 'Miqo\'te'
    assert mina.gender == 'Female'


def test_scrape_character_adds_to_database(mina):
    from api.models.character import Character

    m = Character.query.filter_by(name='Mina Loriel').first()
    assert m.id == mina.id


def test_character_json(client):
    response = client.get('/scrape/character/8774791')

    assert response.status_code == 200
    assert response.json['name'] == 'Mina Loriel'
    assert response.json['grand_company']['name'] == 'Order of the Twin Adder'


def test_character_invalid_lodestone_id(client):
    response = client.get('/scrape/character/91238298371293791287391827317314422')

    assert response.status_code == 403
    assert response.json == {
        'error': 'Invalid Request',
        'message': 'Lodestone ID does not exist'
    }


def test_character_illegal_lodestone_id(client):
    response = client.get('/scrape/character/123abc')

    assert response.status_code == 403
    assert response.json == {
        'error': 'Invalid Request',
        'message': 'Illegal characters in requested ID'
    }


def test_character_repr():
    from api.scrapers.character import scrape_character_by_id

    item = scrape_character_by_id('4746459')
    assert repr(item) == '<Character name=Zael Strife id=4746459>'
