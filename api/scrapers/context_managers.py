from api import app
from api.constants import USER_AGENT
from api.exceptions import InvalidRequest

from lxml import html
from requests import get


class HTMLFromLoadstone(object):

    def __init__(self, url):
        self.url = url

    def __enter__(self):
        app.logger.debug('Attempting to parse url {}'.format(self.url))

        headers = {'User-Agent': USER_AGENT}
        page = get(self.url, headers=headers)
        if page.status_code == 404:
            raise InvalidRequest('Lodestone ID does not exist')
        assert page.status_code == 200

        return html.fromstring(page.text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
