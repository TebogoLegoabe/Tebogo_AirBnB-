import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class."""

    def setUp(self):
        """Sets up the test environment."""
        self.storage = FileStorage()

    def test_all(self):
        """Tests the `all()` method."""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Tests the `new()` method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(obj, self.storage.all())

    def test_save(self):
        """Tests the `save()` method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.storage.__file_path, "r") as f:
            objects = json.load(f)
        self.assertIn(obj, objects)

    def test_reload(self):
        """Tests the `reload()` method."""
        with open(self.storage.__file_path, "w") as f:
            json.dump({"test": "value"}, f)
        self.storage.reload()
        self.assertIn("test", self.storage.all())


if __name__ == "__main__":
    unittest.main()
