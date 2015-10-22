from api import db
from api.models.free_company import FreeCompany
from api.scrapers.context_managers import HTMLFromLoadstone

import datetime
import re


def scrape_free_company_by_id(lodestone_id):
    url = 'http://na.finalfantasyxiv.com/lodestone/freecompany/{}/'.format(lodestone_id)
    with HTMLFromLoadstone(url) as tree:

        fc = FreeCompany.query.get(lodestone_id)
        if not fc:
            fc = FreeCompany(id=lodestone_id)

        _, fc.name, server = tree.xpath('//div[@class="crest_id centering_h"]/span/text()')
        fc.server = server[1:-1]
        fc.tag = tree.xpath('//td[@class="vm"]/text()')[0][1:-1]

        formed_js = str(tree.xpath('//td/script/text()')[0])
        updated_regex = re.search(r'ldst_strftime\(([0-9]+),', formed_js)
        fc.formed = datetime.datetime.fromtimestamp(int(updated_regex.group(1)))

        fc.rank = int(tree.xpath('//tr[@class="rank"]/td/text()')[0].strip())

        weekly_rank, monthly_rank, _ = tree.xpath('//tr[5]/td/text()')
        fc.weekly_rank = int(re.search(r'Rank: ([0-9]+) ', weekly_rank).group(1))
        fc.monthly_rank = int(re.search(r'Rank: ([0-9]+) ', monthly_rank).group(1))

        fc.slogan = tree.xpath('//tr[6]/td/text()')[0]

        db.session.add(fc)
        db.session.commit()

        # total_members = int(tree.xpath('//tr[3]/td/text()')[0])
        # page_num = 1
        #
        # while total_members > 0:
        #     total_members -= 50
        #     page_num += 1
        #
        #     headers = {'User-Agent': USER_AGENT}
        #     uri = 'http://na.finalfantasyxiv.com/lodestone/freecompany/{lodestone_id}/member/?page={page_num}'.format(
        #         lodestone_id=lodestone_id,
        #         page_num=page_num)
        #     page = requests.get(uri, headers=headers)
        #     assert page.status_code == 200
        #
        #     tree = html.fromstring(page.text)
        #
        #     character_ids = map(
        #         lambda x: x.attrib['href'].split('/')[3],
        #         tree.xpath('//div[@class="name_box"]/a'))
        #
        #     for character_id in character_ids:
        #         if character_id == '8774791':
        #             fc.members.add(scrape_character(character_id))
        #
        #     # Grab items from database / grab in parallel
        #     # character_threads = []
        #     # for character_id in character_ids:
        #     #     try:
        #     #         fc.members.add(Character.objects.get(lodestone_id=lodestone_id))
        #     #     except ObjectDoesNotExist:
        #     #         thread = CharacterThread(character_id)
        #     #         thread.start()
        #     #         character_threads.append(thread)
        #     # for thread in character_threads:
        #     #     fc.members.add(thread.join())

        return fc
