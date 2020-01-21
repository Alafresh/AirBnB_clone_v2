#!/usr/bin/python3
""" The file that will be used to store in MYSQL with sqlalchemy"""

from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
import os
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """the storage engine for mySQL using MYsqlALchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the engine"""
        user = os.getenv("HBNB_MYSQL_USER")
        psswd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, psswd, host, db),
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        class_list = ["State", "City", "User", "Place", "Review"]
        class_info = {}
        if cls:
            for data in self.__session.query(eval(cls)).all():
                info = type(data).__name__ + '.' + data.id
                class_info[info] = data
        else:
            for classes in class_list:
                for data in self.__session.query(eval(classes)).all():
                    info = type(data).__name__ + '.' + data.id
                    class_info[info] = data
        return class_info

    def new(self, obj):
        """adds a new object to the database,
        keep im mind is not yet commited"""
        self.__session.add(obj)

    def save(self):
        """saves everything made in the session to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes the  object if it exist"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates the sesssion so we can make changes"""
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        session = scoped_session(session_maker)
        self.__session = session()

    def close(self):
        self.__session.close()
