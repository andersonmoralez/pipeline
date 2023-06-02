from typing import Dict
import requests as req

class HttpResquester:
    def __init__(self) -> None:
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    def request_from_page(self) -> Dict[int, str]:
        res = req.get(self.__url, timeout=5)

        return {
            "status_code": res.status_code,
            "html": res.text
        }
