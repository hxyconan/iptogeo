# models.py

class Lookup(object):
    def __init__(self, ip=None):
        super(Lookup, self).__init__()
        self._ip = ip
        self._data = {
            self._ip: {
                'latitude': None,
                'longitude': None,
                'city': None,
                'state': None,
                'country_code': None,
                'country': None,
                'postal_code': None,
                'time_zone': None,
                'continent': None,
                'host': None,
            }
        }

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data[self._ip] = value


