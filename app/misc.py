import shutil
from pathlib import Path

from fastapi import UploadFile


def save_upload_file(upload_file: UploadFile, destination: Path) -> None:
    upload_file.file.seek(0)

    try:
        with destination.open("wb+") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()
