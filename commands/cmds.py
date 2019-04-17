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

    @classmethod
    def test_perm(cls, context: Context) -> str:
        return ""


class Ping(Command):
    """
    The basic ping command
    """
    @classmethod
    def run(cls, context: Context):
        return "pong"

    @classmethod
    def test_perm(cls, context: Context) -> str:
        return ""


class Bla(Command):
    """
    test command
    """
    @classmethod
    def run(cls, context: Context):
        return "bla"

    @classmethod
    def test_perm(cls, context: Context) -> str:
        return ""


class Bli(Command):
    """
    test command
    """
    @classmethod
    def run(cls, context: Context):
        return "bli"

    @classmethod
    def test_perm(cls, context: Context) -> str:
        return "Not permitted"


class Blo(Command):
    """
    test command
    """
    @classmethod
    def run(cls, context: Context):
        return "blo"

    @classmethod
    def test_perm(cls, context: Context) -> str:
        return ""
