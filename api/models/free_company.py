from api import db


class FreeCompany(db.Model):
    """
    Free Company which contains at least one :class:`api.models.Character` and its associated stats
    Generated and added to DB by :func:`api.scrapers.free_company.scrape_free_company_by_id`.
    """

    id = db.Column(db.String(200), primary_key=True, unique=True)
    """
    Numeric ID unique for each free company
    Used to scrape the free company's info from Lodestone, see below.
    .. image:: ../../images/free_company_lodestone_id.PNG
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

    members_id = db.relationship('Character', backref='free_company', lazy='dynamic')
    """
    Members of the free company
    :type: :class:`api.models.Character`
    """

    tag = db.Column(db.String(20))
    """
    :type: String
    """

    formed = db.Column(db.DateTime())
    """
    :type: DateTime
    """

    rank = db.Column(db.Integer)
    """
    Reward rank (max 8). See `wiki <http://ffxiv.consolegameswiki.com/wiki/Free_Company#Free_Company_Entitlements>`_.
    :type: Int
    """

    weekly_rank = db.Column(db.Integer)
    """
    World standings (previous week)
    :type: Int
    """

    monthly_rank = db.Column(db.Integer)
    """
    World standings (previous month)
    :type: Int
    """

    slogan = db.Column(db.String(200))
    """
    :type: String
    """

    @property
    def as_dict(self):
        """
        :return: Dictionary of the the class' values for easier JSON serialization
        """

        return {
            'lodestone_id': self.id,
            'name': self.name,
            'server': self.server,
            'tag': self.tag,
            'date_formed': self.formed,
            'rank': self.rank,
            'weekly_rank': self.weekly_rank,
            'monthly_rank': self.monthly_rank,
            'slogan': self.slogan
        }

    def __repr__(self):
        return '<FreeCompany name={} id={}>'.format(
            self.name,
            self.id
        )
