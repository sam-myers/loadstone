from api import app, db
from api.constants import USER_AGENT, JOB_IDS
from api.exceptions import InvalidRequest
from api.models.character import Character
from api.models.job import Job
from api.scrapers.item import scrape_item_by_id
from api.scrapers.free_company import scrape_free_company_by_id


from asyncio import get_event_loop, wait
from requests import get
from lxml import html


def scrape_character_by_id(lodestone_id):
    """
    .. image:: ../images/character_lodestone_id.PNG

    >>> mina = scrape_character_by_id('8774791')
    >>> mina.free_company_name
    'Zanarkand'

    :param lodestone_id: Numeric ID in the URL of the character's Lodestone page
    :return: New / updated :class:`api.models.Character`
    :raise InvalidRequest: Character of given ID cannot be found
    """
    app.logger.debug('Attempting to parse character id {}'.format(lodestone_id))

    headers = {'User-Agent': USER_AGENT}
    uri = 'http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(lodestone_id)
    page = get(uri, headers=headers)
    if page.status_code == 404:
        raise InvalidRequest('Lodestone ID does not exist')
    assert page.status_code == 200

    # Populate Character
    char = Character.query.get(lodestone_id)
    if not char:
        char = Character(id=lodestone_id)

    tree = html.fromstring(page.text)

    char.name = tree.xpath('//title/text()')[0].split('|')[0].strip()
    char.free_company_name = tree.xpath('//dd[@class="txt_name"]/a[contains(@href, "")]/text()')[0]
    char.free_company_id = \
        tree.xpath('//dd[@class="txt_name"]/a[contains(@href, "")]')[0].attrib['href'].split('/')[3]
    char.server = tree.xpath('//h2//span/text()')[0].strip()[1:-1]

    scrape_free_company_by_id(char.free_company_id)

    info = tree.xpath('//dd[@class="txt_name"]/text()')
    _, _, char.city_state, grand_company = info
    char.grand_company_name, char.grand_company_rank = grand_company.split('/')

    info = tree.xpath('//div[@class="chara_profile_title"]')
    species, _, gender = info[0].text.split('/')
    char.species = species.strip()
    char.gender = 'Female' if ord(gender.strip()) == 9792 else 'Male'

    class_list_from_html = tree.xpath('//td/text()')

    def level_from_index(index):
        level = class_list_from_html[index*3+1]

        def parse_level(html_level):
            if html_level == '-':
                return 0
            else:
                return int(html_level)
        return parse_level(level)

    # Populate classes
    char.lvl_gladiator = level_from_index(0)
    char.lvl_pugilist = level_from_index(1)
    char.lvl_marauder = level_from_index(2)
    char.lvl_lancer = level_from_index(3)
    char.lvl_archer = level_from_index(4)
    char.lvl_rogue = level_from_index(5)
    char.lvl_conjurer = level_from_index(6)
    char.lvl_thaumaturge = level_from_index(7)
    char.lvl_arcanist = level_from_index(8)

    char.lvl_darknight = level_from_index(9)
    char.lvl_machinist = level_from_index(10)
    char.lvl_astrologian = level_from_index(11)

    char.lvl_carpenter = level_from_index(12)
    char.lvl_blacksmith = level_from_index(13)
    char.lvl_armorer = level_from_index(14)
    char.lvl_goldsmith = level_from_index(15)
    char.lvl_leatherworker = level_from_index(16)
    char.lvl_weaver = level_from_index(17)
    char.lvl_alchemist = level_from_index(18)
    char.lvl_culinarian = level_from_index(19)

    char.lvl_miner = level_from_index(20)
    char.lvl_botanist = level_from_index(21)
    char.lvl_fisher = level_from_index(22)

    db.session.add(char)

    # Find current job
    job_images = tree.xpath('//div[@id="class_info"]/div[@class="ic_class_wh24_box"]/img')
    job_image_id = job_images[0].attrib['src'].split('?')[1]
    job_id = JOB_IDS[job_image_id]

    job = Job.query.filter_by(character_id=lodestone_id, job=job_id).first()
    if not job:
        job = Job(character_id=lodestone_id, job=job_id)

    # Populate stats
    job.hp, job.mp, job.tp = tree.xpath('//div[@id="param_power_area"]/ul/li/text()')

    job.strength, job.dexterity, job.vitality, job.intelligence, job.mind, job.piety = \
        tree.xpath('//ul[@class="param_list_attributes"]/li/span/text()')

    job.fire, job.ice, job.wind, job.earth, job.lightning, job.water = \
        tree.xpath('//ul[@class="param_list_elemental"]/li/span[@class="val"]/text()')

    job.accuracy, job.crit_rate, job.determination, \
        job.defense, job.parry, job.magic_defense, \
        job.attack_power, job.skill_speed, \
        job.attack_magic_potency, job.healing_magic_potency, job.spell_speed, \
        job.slow_resist, job.silence_resist, job.blind_resist, job.poison_resist, \
        job.stun_resist, job.sleep_resist, job.bind_resist, job.heavy_resist, \
        job.slashing_resist, job.piercing_resist, job.blunt_resist = \
        tree.xpath('//ul[@class="param_list"]/li/span[@class="right"]/text()')

    db.session.add(job)
    char.jobs.append(job)
    db.session.commit()

    # Populate items
    html_item_list = tree.xpath('//div[@class="item_detail_box"]/div/div/div/div/a')
    item_ids = map(lambda x: x.attrib['href'].split('/')[5], html_item_list)

    async def scrape_item(item_id):
        job.items.append(scrape_item_by_id(item_id))

    get_event_loop().run_until_complete(wait([
        scrape_item(item_id) for item_id in item_ids
    ]))

    db.session.commit()

    return char
