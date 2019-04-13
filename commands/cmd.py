"""
The file where all commands are builds

@date: 01/04/2019
@author: Quentin Lieumont
"""
from commands.help import get_help


class Context:
    def __init__(self, message):
        self.msg = message
        self.path = []
        self.remains = []


class Command:
    """
    The main command class
    """
    @classmethod
    def run(cls, context: Context):
        raise NotImplementedError()

    @classmethod
    def test_perm(cls, context: Context) -> str:
        raise NotImplementedError()

    @classmethod
    def permeated(cls, context: Context) -> bool:
        if cls.test_perm(context) is "":
            return True
        else:
            return False


class Help(Command):
    @classmethod
    def run(cls, context: Context):
        return get_help(context)


class Ping(Command):
    """
    The basic ping command
    """
    @classmethod
    def run(cls, context: Context):
        return "pong"


class Bla(Command):
    """
    The basic ping command
    """
    @classmethod
    def run(cls, context: Context):
        return "bla"


class Bli(Command):
    """
    The basic ping command
    """
    @classmethod
    def run(cls, context: Context):
        return "bli"


class Blo(Command):
    """
    The basic ping command
    """
    @classmethod
    def run(cls, context: Context):
        return "blo"
