#!/usr/bin/python3
"""
This used to create unique instance of file storage.
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
