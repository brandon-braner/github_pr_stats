from typing import Dict, Union
from urllib.parse import urlparse, parse_qs


def get_query_string(url) -> Dict:
    parsed_url = urlparse(url)
    return parse_qs(parsed_url.query)


def get_query_string_value(url: str, key: str, return_first_value: bool = True) -> Union[str, list]:
    query_string = get_query_string(url).get(key)
    return query_string[0] if return_first_value else query_string
