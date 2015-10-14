def test_scrape_character_job_data(mina_whm):
    assert mina_whm.level == 50
    assert mina_whm.piety == 376


def test_job_repr(mina_whm):
    assert repr(mina_whm) == '<Job job=White Mage charid=8774791>'
