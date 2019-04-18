"""
The file where all commands are defined

@date: 01/04/2019
@author: Quentin Lieumont
"""
from commands.help import get_help
from commands.cmd import Command, Context


class Help(Command):
    """
    help me '_'
    """
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
    test command
    """
    @classmethod
    def run(cls, context: Context):
        return "bla"


class Bli(Command):
    """
    test command
    """
    @classmethod
    def run(cls, context: Context):
        return "bli"


class Blo(Command):
    """
    test command
    """
    @classmethod
    def run(cls, context: Context):
        return "blo"
