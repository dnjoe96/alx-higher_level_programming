#!/usr/bin/python3
""" Module for the base class """
import json
import turtle


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """The contructor for the base class

        Arg:
            id (int): The id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the json string representation of a list of dictionaries

        Arg:
            list_dictionaries (list): list of dictornaries
        """
        if list_dictionaries is None:
            return "[]"
        for one in list_dictionaries:
            if type(one) is not dict:
                raise TypeError("All elements of the list must be \
                        dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json representation of a list of objs to file

        Arg:
            list_objs (list): The list of objs
        """
        filename = str(cls.__name__) + ".json"
        with open(filename, 'w') as f:
            if len(list_objs) == 0 or list_objs is None:
                f.write("[]")
            else:
                dlist = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(dlist))

    def from_json_string(json_string):
        """Returns the list of the JSON string representation

        Arg:
            json_string (str): json str.
        """
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
        """returns an instance with all attributes already set.

        Args:
            **kwargs (dict): Key-value pair of instance attributes.
        """
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances, reading json attributes
        from file <cls name>.json
        """
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
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """Drawing the shapes from the list with the turtle module

        Args:
            list_rectangles (list) - list of rectangle objects
            list_squares (list) - list of squares
        """
        # turtle.left(90)
        for one in list_rectangles:
            w = one.width
            h = one.height
            turtle.setpos(one.x, one.y)

            pos = turtle.pos()
            # print("start at ", pos)
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
            pos = turtle.pos()
            # print("end at ", pos)
            # turtle.setpos(abs(pos[0]) + w, abs(pos[1]) + 0)

        for one in list_squares:
            s = one.size

            turtle.setpos(one.x, one.y)
            pos = turtle.pos()
            # print("start at ", pos)
            turtle.forward(s)
            turtle.left(90)
            turtle.forward(s)
            turtle.left(90)
            turtle.forward(s)
            turtle.left(90)
            turtle.forward(s)
            turtle.left(90)
            pos = turtle.pos()
            # print("end at ", pos)
            # turtle.setpos(abs(pos[0]) + w, abs(pos[1]) + 0)
