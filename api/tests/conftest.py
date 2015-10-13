import pytest


@pytest.fixture(scope='module')
def app():
    from api import app
    return app
