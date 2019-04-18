"""
New library to build commands

@date: 01/04/2019
@author: Quentin Lieumont
"""
from commands.tree import Tree, Leaf
from commands.cmds import *
from sources import get_json
from typing import Type


def get_cmd(txt: str) -> Type[Command]:
    """
    Get a command from a txt via the act() method
    :param txt: text
    :return: Command
    """
    for cmd in Command.__subclasses__():
        if cmd.act() == txt:
            return cmd
    raise SyntaxError(txt + " not found")


def build(data: dict) -> Tree:
    d = get_cmd(data["default"])
    dico = {}
    for e in data["dico"]:
        if type(e) is dict:
            v = build(e)
            dico.update({v.default.act(): v})
        else:
            c = get_cmd(e)
            dico.update({c.act(): Leaf(c)})
    return Tree(d, dico)


main = build(get_json('commands/config.json'))

if __name__ == '__main__':
    class Message:
        def __init__(self, u):
            self.author = u


    class R:
        def __init__(self, id: int):
            self.id = id


    class U:
        def __init__(self, id: int, roles: list = []):
            self.id = id
            self.roles = roles


    r1 = R(1)
    r2 = R(2)

    u1 = U(1, [r1])
    u2 = U(2, [r2])
    u101 = U(101)
    u102 = U(102)

    c1 = Context(Message(u1))
    c2 = Context(Message(u2))
    c101 = Context(Message(u101))
    c102 = Context(Message(u102))
