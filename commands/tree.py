"""
The tree where commands can be attach

@date: 13/04/2019
@author: Quentin Lieumont
"""
from commands.cmd import Command, Context
from typing import Type


class Tree:
    def __init__(self, default: Type[Command], branches: dict):
        """
        A tree with branches, when ran, check if you can go down, else run the default command

        :param default: the method holder called if this is the final command
        :param branches: a dict of activators and subcommands
        """
        self.default = default
        self.branches = branches

    # ==/!=/in defs

    def __eq__(self, other) -> bool:
        """
        equal ?
        :param other:
        :return: Bool
        """
        if type(other) == type(self):
            if self.branches == other.branches and self.default == other.default:
                return True
        return False

    def __ne__(self, other) -> bool:
        """
        not equal ?
        :param other:
        :return: Bool
        """
        return not self == other

    def __contains__(self, item: str):
        """
        if string can match with a command
        :param item:
        :return: bool
        """
        return item in self.branches.keys()

    # +/- defs

    def __add__(self, new_dict: dict):
        """
        Add some commands to this tree

        =========Warning===========
         Not commutative operation
        ===========================

        :param new_dict: An other Tree
        :return:
        """
        self.branches.update(new_dict)
        return self

    def __sub__(self, key_to_remove: str):
        self.branches.pop(key_to_remove)
        return self

    # The run command

    def run(self, args: list, context: Context):
        if len(args) is 0:
            return self.default.run(context)
        elif args[0] in self.branches.keys():
            context.path.append(args[0])
            return self.branches[args[0]].run(args[1:], context)
        else:
            context.remains = args
            return self.default.run(context)


class Leaf(Tree):
    def __init__(self, default: Type[Command]):
        """
        Last level command container
        """
        super().__init__(default, {})

    # ==/!=/in same as Tree

    # +/-
    def __add__(self, new_dict: dict):
        """
        Add some commands to this tree

        =========Warning===========
         Not commutative operation
        ===========================

        :param new_dict: An other Tree
        :return:
        """
        return Tree(self.default, new_dict)

    # The run command

    def run(self, args: list, context: Context):
        context.remains = args
        if self.default.permeated(context):
            return self.default.run(context)
        else:
            return self.default.test_perm(context)
