import requests


class AMPR:
    api = 'https://portal.ampr.org/api/v1/'

    def __init__(self, call, api_key):
        self.call = call
        self.api_key = api_key
        self.session = requests.Session()
        self.session.auth = (self.call, self.api_key)

    def _get(self, resource):
        url = self.api + resource
        return self.session.get(url).json()

    @property
    def encap(self):
        return self._get('encap')

    @property
    def encap_serial(self):
        return self._get('encapSerial')

    @property
    def endpoints(self):
        return self._get('endpoints')


if __name__ == '__main__':
    call = input('call sign: ')
    api_key = input('api key: ')
    print(AMPR(call, api_key).endpoints)
