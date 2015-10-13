from enum import Enum


USER_AGENT = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"


class JOBS(Enum):
    MARAUDER = 'Marauder'
    GLADIATOR = 'Gladiator'
    PUGILIST = 'Pugilist'
    LANCER = 'Lancer'
    ARCHER = 'Archer'
    ROGUE = 'Rogue'
    CONJURER = 'Conjurer'
    THAUMATURGE = 'Thaumaturge'
    ARCANIST = 'Arcanist'

    CARPENTER = 'Carpenter'
    BLACKSMITH = 'Blacksmith'
    ARMORER = 'Armorer'
    GOLDSMITH = 'Goldsmith'
    LEATHERWORKER = 'Leatherworker'
    WEAVER = 'Weaver'
    ALCHEMIST = 'Alchemist'
    CULINARIAN = 'Culinarian'
    BOTANIST = 'Botanist'
    FISHER = 'Fisher'
    MINER = 'Miner'

    WARRIOR = 'Warrior'
    PALADIN = 'Paladin'
    MONK = 'Monk'
    DRAGOON = 'Dragoon'
    BARD = 'Bard'
    NINJA = 'Ninja'

    WHITEMAGE = 'White Mage'
    BLACKMAGE = 'Black Mage'
    SUMMONER = 'Summoner'
    SCHOLAR = 'Scholar'

    DARKNIGHT = 'Dark Knight'
    ASTROLOGIAN = 'Astrologian'
    MACHINIST = 'Machinist'


# TODO Add ids for other jobs
JOB_IDS = {
    '1367039495': JOBS.WHITEMAGE
}
