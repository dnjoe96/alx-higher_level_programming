#!/usr/bin/python3
""" Module for the base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ The contructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        for one in list_dictionaries:
            if type(one) is not dict:
                raise TypeError("All elements of the list must be dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = str(cls.__name__) + ".json"
        with open(filename, 'w') as f:
            if len(list_objs) == 0 or list_objs is None:
                f.write("[]")
            else:
                dlist = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(dlist))

    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            obj = json.loads(json_string)
            if type(obj) is list:
                return obj
            else:
                return [obj]
    
    @classmethod
    def create(cls, **dictionary):
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        try:
            filename = cls.__name__ + ".json"
            with open(filename) as f:
                item = f.read()
        except FileNotFoundError:
            return []

        dlist = Base.from_json_string(item)

        return [cls.create(**obj) for obj in dlist] 

    @classmethod
    def save_to_file_csv(cls, list_objs):
        pass

    @classmethod
    def load_from_file_csv(cls):
        pass
