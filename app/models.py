# models.py

class Lookup(object):
    def __init__(self, ip=None):
        super(Lookup, self).__init__()
        self._ip = ip
        self._data = {
            self._ip: {
                'city': None,
                'continent': None,
                'country': None,
                'country_code': None,
                'host': None,
                'latitude': None,
                'longitude': None,
                'postal_code': None,
                'state': None,
                'time_zone': None,
            }
        }

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data[self._ip] = value


