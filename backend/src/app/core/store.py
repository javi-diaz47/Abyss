from collections import defaultdict
import secrets
from typing import List
from pandas import DataFrame


class Store:
    """Cache Manager to store user dataframes in memory for fast access"""

    def __init__(self) -> None:
        self.store = defaultdict(DataFrame)

    def get(self, key) -> DataFrame:
        if key not in self.store:
            raise KeyError(f"{key} not found in cache store")

        return self.store[key]

    def set(self, df: DataFrame) -> str:
        id = secrets.token_urlsafe()
        self.store[id] = df
        return id

    def getAll(self) -> List[str]:
        return list(self.store.keys())
