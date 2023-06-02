from typing import Dict
import requests as req

class HttpResquester:
    def __init__(self) -> None:
        self.__url = 'http://web.archive.org/web/20200329014303/https://www.nga.gov/collection/artists.html'

    def request_from_page(self) -> Dict[int, str]:
        res = req.get(self.__url, timeout=5)

        return {
            "status_code": res.status_code,
            "html": res.text
        }