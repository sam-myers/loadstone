from api import db
from api.constants import JOBS

from sqlalchemy_utils import ChoiceType


items = db.Table(
    'items',
    db.Column('item_id', db.String(20), db.ForeignKey('item.id')),
    db.Column('job_id', db.Integer, db.ForeignKey('job.id'))
)


class Job(db.Model):
    """
    A single job for any given :class:`api.models.Character` and all its items / stats

    Jobs are a *superset* of classes. For example, all of the following are jobs for simplicity

    * Archer
    * Bard
    * Blacksmith
    * Machinist
    """
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.String(100), db.ForeignKey('character.id'))
    job = db.Column(ChoiceType(JOBS))
    items = db.relationship('Item', secondary=items, backref=db.backref('jobs', lazy='select'))

    hp = db.Column(db.Integer)
    mp = db.Column(db.Integer)
    tp = db.Column(db.Integer)

    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    vitality = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    mind = db.Column(db.Integer)
    piety = db.Column(db.Integer)

    fire = db.Column(db.Integer)
    ice = db.Column(db.Integer)
    wind = db.Column(db.Integer)
    earth = db.Column(db.Integer)
    lightning = db.Column(db.Integer)
    water = db.Column(db.Integer)

    accuracy = db.Column(db.Integer)
    crit_rate = db.Column(db.Integer)
    determination = db.Column(db.Integer)

    defense = db.Column(db.Integer)
    parry = db.Column(db.Integer)
    magic_defense = db.Column(db.Integer)

    attack_power = db.Column(db.Integer)
    skill_speed = db.Column(db.Integer)

    attack_magic_potency = db.Column(db.Integer)
    healing_magic_potency = db.Column(db.Integer)
    spell_speed = db.Column(db.Integer)

    slow_resist = db.Column(db.Integer)
    silence_resist = db.Column(db.Integer)
    blind_resist = db.Column(db.Integer)
    poison_resist = db.Column(db.Integer)
    stun_resist = db.Column(db.Integer)
    sleep_resist = db.Column(db.Integer)
    bind_resist = db.Column(db.Integer)
    heavy_resist = db.Column(db.Integer)

    slashing_resist = db.Column(db.Integer)
    piercing_resist = db.Column(db.Integer)
    blunt_resist = db.Column(db.Integer)

    @property
    def level_dict(self):
        return {
            JOBS.MARAUDER: self.character.lvl_marauder,
            JOBS.GLADIATOR: self.character.lvl_gladiator,
            JOBS.PUGILIST: self.character.lvl_pugilist,
            JOBS.LANCER: self.character.lvl_lancer,
            JOBS.ARCHER: self.character.lvl_archer,
            JOBS.ROGUE: self.character.lvl_rogue,
            JOBS.CONJURER: self.character.lvl_conjurer,
            JOBS.THAUMATURGE: self.character.lvl_thaumaturge,
            JOBS.ARCANIST: self.character.lvl_arcanist,

            JOBS.CARPENTER: self.character.lvl_carpenter,
            JOBS.BLACKSMITH: self.character.lvl_blacksmith,
            JOBS.ARMORER: self.character.lvl_armorer,
            JOBS.GOLDSMITH: self.character.lvl_goldsmith,
            JOBS.LEATHERWORKER: self.character.lvl_leatherworker,
            JOBS.WEAVER: self.character.lvl_weaver,
            JOBS.ALCHEMIST: self.character.lvl_alchemist,
            JOBS.CULINARIAN: self.character.lvl_culinarian,
            JOBS.BOTANIST: self.character.lvl_botanist,
            JOBS.FISHER: self.character.lvl_fisher,
            JOBS.MINER: self.character.lvl_miner,

            JOBS.WARRIOR: self.character.lvl_marauder,
            JOBS.PALADIN: self.character.lvl_gladiator,
            JOBS.MONK: self.character.lvl_pugilist,
            JOBS.DRAGOON: self.character.lvl_lancer,
            JOBS.BARD: self.character.lvl_archer,
            JOBS.WHITEMAGE: self.character.lvl_conjurer,
            JOBS.BLACKMAGE: self.character.lvl_thaumaturge,
            JOBS.SUMMONER: self.character.lvl_arcanist,
            JOBS.SCHOLAR: self.character.lvl_arcanist,
            JOBS.NINJA: self.character.lvl_rogue,

            JOBS.DARKNIGHT: self.character.lvl_darknight,
            JOBS.ASTROLOGIAN: self.character.lvl_astrologian,
            JOBS.MACHINIST: self.character.lvl_machinist
        }

    @property
    def level(self):
        """


        :return: The job's level derived from the character's class levels
        """
        return self.level_dict[self.job]

    @property
    def as_dict(self):
        """


        :return: Dictionary of the the class' values for easier JSON serialization
        """
        item_list = list(map(lambda s: s.as_dict, self.items))

        return {
            'job': self.job.value,
            'level': self.level,
            'items': item_list,
            'stats': {
                'hp': self.hp,
                'mp': self.mp,
                'tp': self.tp
            },
            'attributes': {
                'strength': self.strength,
                'dexterity': self.dexterity,
                'vitality': self.vitality,
                'intelligence': self.intelligence,
                'mind': self.mind,
                'piety': self.piety
            },
            'properties': {
                'offensive': {
                    'accuracy': self.accuracy,
                    'critical_hit_rate': self.crit_rate,
                    'determination': self.determination
                },
                'defensive': {
                    'defense': self.defense,
                    'parry': self.parry,
                    'magic_defense': self.magic_defense
                },
                'physical': {
                    'attack_power': self.attack_power,
                    'skill_speed': self.skill_speed
                },
                'mental': {
                    'attack_magic_potency': self.attack_magic_potency,
                    'healing_magic_potency': self.healing_magic_potency,
                    'spell_speed': self.spell_speed
                }
            },
            'resistances': {
                'elemental': {
                    'fire': self.fire,
                    'ice': self.ice,
                    'wind': self.wind,
                    'earth': self.earth,
                    'lightning': self.lightning,
                    'water': self.water
                },
                'status': {
                    'slow': self.slow_resist,
                    'silence': self.silence_resist,
                    'blind': self.blind_resist,
                    'poison': self.poison_resist,
                    'stun': self.stun_resist,
                    'sleep': self.sleep_resist,
                    'bind': self.bind_resist,
                    'heavy': self.heavy_resist
                },
                'physical': {
                    'slashing': self.slashing_resist,
                    'piercing': self.piercing_resist,
                    'blunt': self.blunt_resist
                }
            }
        }

    def __repr__(self):
        # return '<Job job={}>'.format(self.job)
        return '<Job job={job} charid={charid}>'.format(
            job=self.job.value,
            charid=self.character_id
        )
