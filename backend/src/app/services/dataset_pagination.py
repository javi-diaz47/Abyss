import pandas as pd

from app.utils.pagination import pagination


def dataset_pagination(df: pd.DataFrame, page: int, offset: int):
    start, end = pagination(page, offset, len(df))
    return df[start:end]
