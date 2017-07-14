import re
import models
from app import db

def lookup(ip):
    """ Look up a single IP address in the MaxMind database
    """
    lookup = models.Lookup(ip=ip)

    # Validate the IP address
    if valid_ip(ip):
        try:
            db_data = db.city(ip) #Execute the ip to geo actual function
        except Exception, e:
            lookup.data = {
                'ip': ip,
                'error': 'Couldn\'t find address in database'
            }
        else: # If found, then will do
            lookup.data = {
                'ip': ip,
                'latitude': db_data.location.latitude,
                'longitude': db_data.location.longitude,
                'city': db_data.city.name,
                'state': db_data.subdivisions.most_specific.iso_code,
                'country_code': db_data.country.iso_code,
                'country': db_data.country.name,
                'postal_code': db_data.postal.code,
                'time_zone': db_data.location.time_zone,
                'continent': db_data.continent.name,
                'host': hostname(ip)[0]
            }
    else:
        lookup.data = {
            'ip': ip,
            'error': 'I don\'t think this is a valid address'
        }

    # Return the dictionary value without key name
    return lookup.data[ip]


def hostname(ip):
    """ Attempts a reverse lookup of the hostname.
        There does exist a GeoIP2 domain database but it's not free.
    """
    try:
        return socket.gethostbyaddr(ip)
    except Exception:
        return None, None, None


def valid_ip(ip):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return True
    else:
        return False
