from .get_api_consumer import GetApiConsumer

def test_get_starships(requests_mock):
    ''' Testing get_starships method'''
    requests_mock.get('https://swapi.dev/api/starships/', status_code = 200, json={ 'some': 'thing' })
    
    api_consumer =  GetApiConsumer()
    resp = api_consumer.get_starships(page=1)
    
    print(resp)