#!/usr/bin/python3
import json
from pathlib import Path


class FileStorage:
    """Class that serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = Path(__file__).parent / "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary `__objects`."""
        return self.__objects

    def new(self, obj):
        """Sets in `__objects` the `obj` with key `<obj class name>.id`."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes `__objects` to the JSON file (path: `__file_path`)."""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to `__objects` (only if the JSON file `__file_path` exists; otherwise, do nothing. If the file doesn't exist, no exception should be raised)."""
        if self.__file_path.is_file():
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
