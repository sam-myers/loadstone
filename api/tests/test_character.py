def test_character_json(client):
    response = client.get('/scrape/character/8774791')

    assert response.status_code == 200
    assert response.json == {
        'name': 'Mina Loriel',
        'lodestone_id': '8774791',
        'server': 'Zalera',
        'species': 'Miqo\'te',
        'city_state': 'Gridania',
        'gender': 'Female',
        'grand_company': {
            'name': 'Order of the Twin Adder',
            'rank': 'Second Serpent Lieutenant'
        },
        'free_company': {
            'lodestone_id': '9229142273877347770',
            'name': 'Zanarkand'
        }
    }


def test_character_invalid_lodestone_id(client):
    response = client.get('/scrape/character/91238298371293791287391827317314422')

    assert response.status_code == 403
    assert response.json == {
        'error': 'Invalid Request',
        'message': 'Lodestone ID does not exist'
    }


def test_character_repr():
    from api.scrapers.character import scrape_character_by_id

    item = scrape_character_by_id('4746459')
    assert repr(item) == '<Character name=Zael Strife id=4746459>'
