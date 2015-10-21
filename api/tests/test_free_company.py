import pytest


@pytest.fixture
def zanarkand():
    from api.scrapers.free_company import scrape_free_company_by_id
    return scrape_free_company_by_id('9229142273877347770')


def test_scrape_free_company_basic_info(zanarkand):
    assert zanarkand.name == 'Zanarkand'
    assert zanarkand.server == 'Zalera'


def test_item_invalid_lodestone_id(client):
    response = client.get('/scrape/free_company/000000000001111111111122222222222222')

    assert response.status_code == 403
    assert response.json == {
        'error': 'Invalid Request',
        'message': 'Lodestone ID does not exist'
    }


def test_free_company_json(client):
    response = client.get('/scrape/free_company/9229142273877347770')

    assert response.status_code == 200
    assert response.json['slogan'] == 'Burning shit since 2013.'
    assert response.json['tag'] == 'CHAOS'


def test_character_illegal_lodestone_id(client):
    response = client.get('/scrape/item/123abc!')

    assert response.status_code == 403
    assert response.json == {
        'error': 'Invalid Request',
        'message': 'Illegal characters in requested ID'
    }


def test_free_company_repr(zanarkand):
    assert repr(zanarkand) == '<FreeCompany name=Zanarkand id=9229142273877347770>'
