from typing import Dict, List


def my_function(my_num: int, my_str: str, my_float: float) -> Dict:
    return {
        'my_num': my_num,
        'my_str': my_str,
        'my_float': my_float,
    }


output = my_function(35, 'like this video?', 69)
print(output)