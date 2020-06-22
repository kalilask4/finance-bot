from typing import Dict, List, NamedTuple


class Category(NamedTuple):
    codename: str
    name: str
    is_base_expense: bool
    aliases: List[str]

class Categories:
    def __init__(self):
        self._categories = self._load_categories()


    def _load_categories(self) -> List[Category]:
        pass
