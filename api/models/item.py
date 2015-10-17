from api import db


class Item(db.Model):
    """
    A weapon, armor, shield, accessory, or soul stone

    Generated and added to DB by :func:`api.scrapers.item.scrape_item_by_id`.
    """

    id = db.Column(db.String(20), primary_key=True, unique=True)
    """
    Unique for each item.

    :type: String
    """

    name = db.Column(db.String(100))
    """
    :type: String
    """

    type = db.Column(db.String(40))
    """
    Examples:

    - Body
    - Soul Crystal
    - Necklace
    - Two-handed Conjurer's Arm

    :type: String
    """

    ilvl = db.Column(db.Integer)
    """
    iLevel

    :type: Int
    """

    damage = db.Column(db.Integer, default=0)
    auto_attack = db.Column(db.Float, default=0.0)
    delay = db.Column(db.Integer, default=0)

    defense = db.Column(db.Integer, default=0)
    magic_defense = db.Column(db.Integer, default=0)

    block_strength = db.Column(db.Integer, default=0)
    block_rate = db.Column(db.Integer, default=0)

    vitality = db.Column(db.Integer, default=0)
    mind = db.Column(db.Integer, default=0)
    determination = db.Column(db.Integer, default=0)
    spell_speed = db.Column(db.Integer, default=0)
    accuracy = db.Column(db.Integer, default=0)
    critical_hit_rate = db.Column(db.Integer, default=0)
    piety = db.Column(db.Integer, default=0)

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        self.damage = 0
        self.auto_attack = 0
        self.delay = 0

        self.defense = 0
        self.magic_defense = 0

        self.block_strength = 0
        self.block_rate = 0

        self.vitality = 0
        self.mind = 0
        self.determination = 0
        self.spell_speed = 0
        self.accuracy = 0
        self.critical_hit_rate = 0
        self.piety = 0

    def __repr__(self):
        return '<Item lodestone_id={} name={} type={} ilvl={}>'.format(
            self.id,
            self.name,
            self.type,
            self.ilvl
        )

    @property
    def as_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'type': self.type,
            'ilvl': self.ilvl,
            'stats': {
                'damage': self.damage,
                'auto_attack': self.auto_attack,
                'delay': self.delay,

                'defense': self.defense,
                'magic_defense': self.magic_defense,

                'block_rate': self.block_rate,
                'block_strength': self.block_strength,

                'vitality': self.vitality,
                'mind': self.mind,
                'determination': self.determination,
                'spell_speed': self.spell_speed,
                'accuracy': self.accuracy,
                'critical_hit_rate': self.critical_hit_rate,
                'piety': self.piety
            }
        }
