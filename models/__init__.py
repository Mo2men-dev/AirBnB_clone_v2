#!/usr/bin/python3
"""This module instantiates the storage file/db"""
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "file":
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

storage.reload()
