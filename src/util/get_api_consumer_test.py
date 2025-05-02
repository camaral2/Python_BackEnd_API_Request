from .get_api_consumer import GetApiConsumer

def test_get_starships():
    ''' Testing get_starships method'''
    
    api_consumer =  GetApiConsumer()
    resp = api_consumer.get_starships(page=1)
    
    print(resp)