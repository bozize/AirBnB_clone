#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel:
    """

    For this BaseModel we have.

    Artributes:
    id:the id of the BaseModel unique one.
    created_at: the time the model is created.
    updated_at; the time the model is updated.

    """
    def __init__(self, *args, **kwargs):
        """
        initializes the basemodel.

        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                            )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                            )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of BaseModel instance.

        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, str(self.__dict__)
                )

    def save(self):
        """
        Records when instance of BaseModel is updated.

        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns the dixtionary representation of the dict.

        """
        bs_dict = self.__dict__.copy()
        bs_dict["__class__"] = self.__class__.__name__
        bs_dict["created_at"] = self.created_at.isoformat()
        bs_dict["updated_at"] = self.updated_at.isoformat()
        return bs_dict
