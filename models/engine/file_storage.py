import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def delete(self, obj=None):
        """deletes obj from __objects if it's inside
        Args:
            obj: given object
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def all(self, cls=None):
        """returns a dictionary
        Args:
            cls: class type to filter return by
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            return self.__objects
        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize JSON file objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    class_name = value.get("__class__")
                    if class_name:
                        obj_class = globals().get(class_name)
                        if obj_class:
                            obj = obj_class(**value)
                            self.__objects[key] = obj
                        else:
                            print(f"Class '{class_name}' not found.")
                    else:
                        print("Missing '__class__' attribute in JSON data.")
        except FileNotFoundError:
            pass

    def close(self):
        """Close the storage"""
        self.reload()