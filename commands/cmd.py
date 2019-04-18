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
        if role in json[mode].keys():
            if cmd in json[mode][role]["perm"]:
                return True
            else:
                for herit in json[mode][role]["inherit"]:
                    if herit == first_cmd:
                        raise SyntaxError("Recursive definition in permissions")
                    elif cls._test(mode, cmd, json, herit, cmd):
                        return True
        return False

    @classmethod
    def test_perm(cls, context: Context) -> str:
        """
        return the permission error, "" if no error
        :param context: Context
        :return error: str
        """
        user = context.msg.author
        json = get_json("commands/perm.json")
        if cls._test("user", cls.act(), json, str(user.id).zfill(4)):
            return ""
        elif True in [cls._test("role", cls.act(), json, str(r.id).zfill(4)) for r in user.roles]:
            return ""
        else:
            return "You can't run this command :/"

    @classmethod
    def permeated(cls, context: Context) -> bool:
        if cls.test_perm(context) is "":
            return True
        else:
            return False
