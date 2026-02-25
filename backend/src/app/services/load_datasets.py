import pandas as pd

from app.core.constants import STORAGE_DIR
from app.exeptions.file_exeptions import FileInvalidExtension
from app.utils.file_utils import get_file_extesion


def load_dataset(filename: str) -> pd.DataFrame:
    path = STORAGE_DIR / filename

    if path.exists():
        file_ext = get_file_extesion(filename)
        match file_ext:
            case "csv":
                df = pd.read_csv(path)
                return df
            case _:
                raise FileInvalidExtension(
                    f"File extension {file_ext} is not currently supported"
                )

    raise FileNotFoundError()
