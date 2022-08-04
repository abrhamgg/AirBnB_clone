#!/usr/bin/python3
"""
method to link BaseModel to FileStorage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
