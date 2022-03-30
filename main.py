from typing import List, Dict, TypedDict

import requests

s = requests.Session()


# p3
class Beer(TypedDict):
    id: int
    name: str
    abv: float


# p1 less hints
def beer_by_food(food: str) -> List:
    url = 'https://api.punkapi.com/v2/beers?food='
    r = s.get(url + food)
    return r.json()


# p1 less hints
def parse_data(api_data: Dict) -> Beer:
    # try adding another key in
    beer: Beer = {
        'id': api_data['id'],
        'name': api_data['name'],
        'abv': api_data['abv'],
    }
    return beer


# p2 - lets say we want a list of IDs (try expecting a Dict)
def parse_to_id_list(api_data: List) -> List[int]:
    id_list = [item['id'] for item in api_data]
    return id_list


# p1 less hints
if __name__ == '__main__':
    beers = beer_by_food('burger')
    #for drink in beers:
    #    print(parse_data(drink))

    print(parse_to_id_list(beers))