import requests

class GetApiConsumer:
    
    @classmethod
    def get_starships(self, page: int) -> any:
        params = { 'page':page }
        resp = requests.get('https://swapi.dev/api/starships/', params=params, verify=False)

        return resp.json()
