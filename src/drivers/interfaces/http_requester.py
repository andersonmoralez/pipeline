from abc import ABC, abstractmethod
from typing import Dict


class HttpResquesterInterface(ABC):

    @abstractmethod
    def request_from_page(self) -> Dict[int, str]:
        pass
