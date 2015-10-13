from api import db


class Item(db.Model):
    """
    A weapon, armor, shield, accessory, or soul stone.

    Generated and added to DB by :func:`scrapers.character.scrape_item_by_id`.
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

    damage = db.Column(db.Integer)
    auto_attack = db.Column(db.Float)
    delay = db.Column(db.Integer)

    defense = db.Column(db.Integer)
    magic_defense = db.Column(db.Integer)

    block_strength = db.Column(db.Integer)
    block_rate = db.Column(db.Integer)

    vitality = db.Column(db.Integer)
    mind = db.Column(db.Integer)
    determination = db.Column(db.Integer)
    spell_speed = db.Column(db.Integer)
    accuracy = db.Column(db.Integer)
    critical_hit_rate = db.Column(db.Integer)
    piety = db.Column(db.Integer)

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
            'ilvl': self.ilvl
        }
