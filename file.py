import os
from pathlib import Path

from type import Item


def _check_file(path: str):
    if os.path.isfile(path):
        return True
    return False


def _create_db_file(path: str):
    Path(path).touch()


def get_data_from_file(path: str = 'db.txt') -> list[Item]:
    if not _check_file(path):
        _create_db_file(path)

    with open(path, '+rb') as f:
        file_data = f.read().decode('UTF-8')

    if file_data == '':
        return []

    list_of_data = file_data.split('\n')
    transform_data = []

    for i in list_of_data:
        data = i.split('|')
        transform_data.append(
            Item(
                full_name=data[0],
                phone=data[1],
                email=data[2],
                address=data[3]
            )
        )
    return []


def set_data_to_file(data: list[str], path: str = 'db.txt'):
    if not _check_file(path):
        _create_db_file(path)

    with open(path, 'a') as f:
        f.write('\n' + '|'.join(data))
