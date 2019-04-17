"""
The file where all commands are builds

@date: 01/04/2019
@author: Quentin Lieumont
"""


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
    def act(cls):
        return cls.__name__.lower()

    @classmethod
    def test_perm(cls, context: Context) -> str:
        """
        return the permission error, "" if no error
        :param context: Context
        :return error: str
        """
        raise NotImplementedError()

    @classmethod
    def permeated(cls, context: Context) -> bool:
        if cls.test_perm(context) is "":
            return True
        else:
            return False
