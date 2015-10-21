import pytest


@pytest.fixture(scope='module')
def app():
    from api import app, db
    app.config['TESTING'] = True
    db.create_all()

    return app
