from os import stat
from matplotlib.pyplot import cla
import psycopg2
from enums import CreateEnum


class Executor:
    def __init__(self, *connection_details):
        self.connection_details = connection_details

    @property
    def connection(self):
        pass

    @connection.setter
    def connection(self, dbname, user, password, port):
        connection = psycopg2.connect(dbname, user, password, port)

    @classmethod
    def select(self):
        pass

    @classmethod
    def delete(self):
        pass

    @classmethod
    def create(self):
        pass

    @classmethod
    def drop(self):
        pass

    @classmethod
    def update():
        pass

    @classmethod
    def delete():
        pass

    @classmethod
    def alter():
        pass

    @classmethod
    def exists():
        pass

    @classmethod
    def grant():
        pass

    @classmethod
    def revoke():
        pass

    @classmethod
    def savepoint():
        pass

    @classmethod
    def commit():
        pass

    @classmethod
    def rollback():
        pass

    @classmethod
    def truncate():
        pass

    @classmethod
    def union():
        pass

    @classmethod
    def union_all():
        pass

    @classmethod
    def aggregate():
        # count, sum, avg, min, max
        pass

    @classmethod
    def join():
        # inner join, left join, right join, full join
        pass
