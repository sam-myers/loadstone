class InvalidRequest(Exception):

    def __init__(self, message='', status_code=403):
        super(InvalidRequest, self).__init__()
        self.message = message
        self.status_code = status_code

    @property
    def as_dict(self):
        return {
            'error': 'Invalid Request',
            'message': self.message
        }
