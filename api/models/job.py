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
    def level(self):
        """


        :return: The job's level derived from the character's class levels
        """
        if self.job == JOBS.MARAUDER:
            return self.character.lvl_marauder
        elif self.job == JOBS.GLADIATOR:
            return self.character.lvl_gladiator
        elif self.job == JOBS.PUGILIST:
            return self.character.lvl_pugilist
        elif self.job == JOBS.LANCER:
            return self.character.lvl_lancer
        elif self.job == JOBS.ARCHER:
            return self.character.lvl_archer
        elif self.job == JOBS.ROGUE:
            return self.character.lvl_rogue
        elif self.job == JOBS.CONJURER:
            return self.character.lvl_conjurer
        elif self.job == JOBS.THAUMATURGE:
            return self.character.lvl_thaumaturge
        elif self.job == JOBS.ARCANIST:
            return self.character.lvl_arcanist

        elif self.job == JOBS.CARPENTER:
            return self.character.lvl_carpenter
        elif self.job == JOBS.BLACKSMITH:
            return self.character.lvl_blacksmith
        elif self.job == JOBS.ARMORER:
            return self.character.lvl_armorer
        elif self.job == JOBS.GOLDSMITH:
            return self.character.lvl_goldsmith
        elif self.job == JOBS.LEATHERWORKER:
            return self.character.lvl_leatherworker
        elif self.job == JOBS.WEAVER:
            return self.character.lvl_weaver
        elif self.job == JOBS.ALCHEMIST:
            return self.character.lvl_alchemist
        elif self.job == JOBS.CULINARIAN:
            return self.character.lvl_culinarian
        elif self.job == JOBS.BOTANIST:
            return self.character.lvl_botanist
        elif self.job == JOBS.FISHER:
            return self.character.lvl_fisher
        elif self.job == JOBS.MINER:
            return self.character.lvl_miner

        elif self.job == JOBS.WARRIOR:
            return self.character.lvl_marauder
        elif self.job == JOBS.PALADIN:
            return self.character.lvl_gladiator
        elif self.job == JOBS.MONK:
            return self.character.lvl_pugilist
        elif self.job == JOBS.DRAGOON:
            return self.character.lvl_lancer
        elif self.job == JOBS.BARD:
            return self.character.lvl_archer
        elif self.job == JOBS.WHITEMAGE:
            return self.character.lvl_conjurer
        elif self.job == JOBS.BLACKMAGE:
            return self.character.lvl_thaumaturge
        elif self.job == JOBS.SUMMONER:
            return self.character.lvl_arcanist
        elif self.job == JOBS.SCHOLAR:
            return self.character.lvl_arcanist
        elif self.job == JOBS.NINJA:
            return self.character.lvl_rogue

        elif self.job == JOBS.DARKNIGHT:
            return self.character.lvl_darknight
        elif self.job == JOBS.ASTROLOGIAN:
            return self.character.lvl_astrologian
        elif self.job == JOBS.MACHINIST:
            return self.character.lvl_machinist

    @property
    def as_dict(self):
        """


        :return: Dictionary of the the class' values for easier JSON serialization
        """
        # items = list(map(lambda x: x.as_dict, list(self.items.all()))) if len(self.items.all()) > 0 else []
        items = list(map(lambda s: s.as_dict, self.items))

        return {
            'job': self.job.value,
            'level': self.level,
            'items': items,
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
