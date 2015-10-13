from api import db


class Character(db.Model):
    id = db.Column(db.String(100), primary_key=True, unique=True)
    """
    Unique for each item.

    Used to scrape the item's info from Lodestone, see below.

    .. image:: ../../images/character_lodestone_id.PNG

    :type: String
    """

    name = db.Column(db.String(100))
    """
    :type: String
    """

    server = db.Column(db.String(100))
    """
    :type: String
    """

    species = db.Column(db.String(100))
    """
    :type: String
    """

    gender = db.Column(db.String(20))
    """
    :type: String
    """

    city_state = db.Column(db.String(100))
    """
    :type: String
    """

    free_company_name = db.Column(db.String(100))
    """
    :type: String
    """

    free_company_id = db.Column(db.String(100))
    """
    :type: String
    """

    grand_company_name = db.Column(db.String(100))
    """
    :type: String
    """

    grand_company_rank = db.Column(db.String(100))
    """
    :type: String
    """

    lvl_archer = db.Column(db.Integer)
    lvl_lancer = db.Column(db.Integer)
    lvl_marauder = db.Column(db.Integer)
    lvl_pugilist = db.Column(db.Integer)
    lvl_rogue = db.Column(db.Integer)
    lvl_arcanist = db.Column(db.Integer)
    lvl_conjurer = db.Column(db.Integer)
    lvl_thaumaturge = db.Column(db.Integer)
    lvl_astrologian = db.Column(db.Integer)
    lvl_darknight = db.Column(db.Integer)
    lvl_machinist = db.Column(db.Integer)
    lvl_alchemist = db.Column(db.Integer)
    lvl_armorer = db.Column(db.Integer)
    lvl_blacksmith = db.Column(db.Integer)
    lvl_carpenter = db.Column(db.Integer)
    lvl_culinarian = db.Column(db.Integer)
    lvl_gladiator = db.Column(db.Integer)
    lvl_goldsmith = db.Column(db.Integer)
    lvl_leatherworker = db.Column(db.Integer)
    lvl_weaver = db.Column(db.Integer)
    lvl_botanist = db.Column(db.Integer)
    lvl_fisher = db.Column(db.Integer)
    lvl_miner = db.Column(db.Integer)

    def __repr__(self):
        return '<Character name={name} id={id}>'.format(
            name=self.name,
            id=self.id
        )

    @property
    def as_dict(self):
        """
        :return: Dictionary of the the class' values for easier JSON serialization

        :rtype: Dictionary
        """
        # jobs = list(map(lambda x: x.as_dict, list(self.job_set.all()))) if len(self.job_set.all()) > 0 else []

        return {
            'name': self.name,
            'lodestone_id': self.id,
            'server': self.server,
            'species': self.species,
            'gender': self.gender,
            'city_state': self.city_state,
            'free_company': {
                'name': self.free_company_name,
                'lodestone_id': self.free_company_id
            },
            'grand_company': {
                'name': self.grand_company_name,
                'rank': self.grand_company_rank
            },
            # 'jobs': jobs,
        }
