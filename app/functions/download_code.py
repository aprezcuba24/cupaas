import requests
import os
import shutil
from app.kafka import pipe
from app.config import CODE_DOWLOAND_PAHT
from zipfile import ZipFile


def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, "wb") as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


@pipe
async def download_code(data, **kwargs):
    commit_hash = data["commit_hash"]
    project_folder = f"{CODE_DOWLOAND_PAHT}/{commit_hash}"
    if os.path.isdir(project_folder):
        shutil.rmtree(project_folder)
    folder = f"{project_folder}_downoload"
    zip_file = f"{folder}.zip"
    download_url(data["zip_url"], zip_file)
    with ZipFile(zip_file, "r") as zObject:
        zObject.extractall(path=folder)
    project_folder_donwload = f"{folder}/{os.listdir(folder)[0]}"
    shutil.move(project_folder_donwload, project_folder)
    os.remove(zip_file)
    os.rmdir(folder)
    return {
        **data,
        **{
            "project_code": project_folder,
        },
    }
