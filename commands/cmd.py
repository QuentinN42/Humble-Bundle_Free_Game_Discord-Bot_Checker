"""
The file where all commands are builds

@date: 01/04/2019
@author: Quentin Lieumont
"""
from sources import get_json
from discord.message import Message


class Context:
    def __init__(self, message: Message):
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
    def _test(cls, mode: str, cmd: str, json: dict, role: str, first_cmd: str = "") -> bool:
        """
        test if cmd is in role perms or in inherit perms
        :param cmd:
        :param role:
        :return:
        """
        if mode not in json.keys():
            raise SyntaxError("Unrecognised mode")
        if first_cmd == "":
            first_cmd = cmd
        if cmd in json[mode][role]["this_role"]:
            return True
        else:
            for herit in json[mode][role]["inherit"]:
                if herit == first_cmd:
                    raise SyntaxError("Recursive definition in permissions")
                elif cls._test(mode, cmd, json, herit, cmd):
                    return True
        return False

    @classmethod
    def test_perm(cls, context: Context) -> str:  # < --- role perms missing
        """
        return the permission error, "" if no error
        :param context: Context
        :return error: str
        """
        if cls._test("user", cls.act(), get_json("commands/perm.json"), context.msg.author.id):
            return ""

    @classmethod
    def permeated(cls, context: Context) -> bool:
        if cls.test_perm(context) is "":
            return True
        else:
            return False
