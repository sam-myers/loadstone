import pytest


@pytest.fixture(scope='module')
def app():
    from api import app, db
    app.config['TESTING'] = True
    db.create_all()

    return app


@pytest.fixture(scope='module')
def mina(app):
    from api.scrapers.character import scrape_character_by_id
    return scrape_character_by_id('8774791')


@pytest.fixture(scope='module')
def thyrus():
    from api.scrapers.item import scrape_item_by_id
    return scrape_item_by_id('d19447e548d')


@pytest.fixture(scope='module')
def mina_whm(mina):
    from api.constants import JOBS
    return mina.jobs.filter_by(job=JOBS.WHITEMAGE).first()
