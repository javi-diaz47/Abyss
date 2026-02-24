def get_file_extesion(filename: str) -> str:
    i = filename.rfind(".")
    return filename[i + 1 :]
