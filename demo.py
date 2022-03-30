from typing import Dict, List, TypedDict

import requests

s = requests.Session()


class Drink(TypedDict):
    id: int
    name: str
    abv: float


def beer_by_food(food: str) -> List:
    url = 'https://api.punkapi.com/v2/beers?food='
    r = s.get(url + food)
    return r.json()


def parse_data(api_data: Dict) -> Dict:
    beer: Drink = {
        'id': api_data['id'],
        'name': api_data['name'],
        'abv': api_data['abv'],
    }
    return beer


def parse_id_to_list(api_main: List) -> List[int]:
    id_list = [item['id'] for item in api_main]
    return id_list


if __name__ == '__main__':
    other_list = ['food', 'drink']
    beers = beer_by_food('burger')
    # for drink in beers:
    #    print(parse_data(drink))

    print(parse_id_to_list(beers))
