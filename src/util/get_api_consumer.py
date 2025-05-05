import requests

class GetApiConsumer:
    '''Get info API'''
    @classmethod
    def get_starships(self, page: int) -> any:
        '''Get starships from API'''
        params = { 'page':page }
        resp = requests.get('https://swapi.dev/api/starships/', 
                            params=params, 
                            verify=False,
                            timeout=10)

        return resp.json()
