"""
The file where all commands are builds

@date: 01/04/2019
@author: Quentin Lieumont
"""
from sources import get_json


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
    def _get_perms(cls) -> dict:
        """
        get witch role/user are allowed to use this command
        :return: the dict of allowed role, allowed user
        """
        json = get_json("commands/perms.json")
        rl = []
        ul = []

        for role in json["role"]:
            if role["this_role"] == cls.act():  # < --- missing inherit
                rl.append(role)

        for user in json["user"]:
            if user["this_user"] == cls.act():  # < --- missing inherit
                rl.append(user)

        return {"role": rl, "user": ul}

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
