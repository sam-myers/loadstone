import pytest

from api.tests.test_character import mina


@pytest.fixture
def mina_whm(mina):
    from api.constants import JOBS
    return mina.jobs.filter_by(job=JOBS.WHITEMAGE).first()


def test_scrape_character_job_data(mina_whm):
    assert mina_whm.level == 50
    assert mina_whm.piety == 376


def test_job_repr(mina_whm):
    assert repr(mina_whm) == '<Job job=White Mage charid=8774791>'


def test_job_contains_item():
    from api.scrapers.character import scrape_character
    from api.constants import JOBS
    mina = scrape_character('8774791')
    whm = mina.jobs.filter_by(job=JOBS.WHITEMAGE).first()
    circlet = next(filter(lambda i: i.name == 'Platinum Circlet of Healing', whm.items))

    assert circlet.defense == 38
