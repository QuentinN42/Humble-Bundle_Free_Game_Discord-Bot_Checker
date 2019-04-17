"""
New library to build commands

@date: 01/04/2019
@author: Quentin Lieumont
"""
from commands.tree import Tree, Leaf
from commands.cmds import *
from sources import get_json


def build(data: dict) -> Tree:
    d = eval(data["default"])
    dico = {}
    for k, v in data["dico"].items():
        if type(v) is dict:
            v = build(v)
            dico.update({k: v})
        else:
            dico.update({k: Leaf(eval(v))})
    return Tree(d, dico)


main = build(get_json('commands/config.json'))
