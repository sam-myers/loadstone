import pytest


@pytest.fixture(scope='module')
def app():
    from api import app, db
    from api.models.job import Job
    from api.models.character import Character
    from api.models.item import Item

    app.config['TESTING'] = True
    db.create_all()

    return app


@pytest.fixture(scope='module')
def mina():
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