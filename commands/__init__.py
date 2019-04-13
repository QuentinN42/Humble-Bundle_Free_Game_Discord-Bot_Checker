"""
New library to build commands

@date: 01/04/2019
@author: Quentin Lieumont
"""
from commands.help import get_help


class Command:
    """
    The main command class
    """
    act = []
    need_run_alone = False
    can_run_alone = False

    def __init__(self):
        raise SyntaxError("{C} as no instance methods.".format(C=self.__name__))

    @classmethod
    def run(cls, args=None):
        """
        Recursive check if a command exist.
        If yes: run the run method of the subclass
        If no : run the default method of the class

        :param args: all the arguments in a list ex : ['logs', 'read', 'all']
        :return: the return of the called command
        """
        if cls.need_run_alone:
            return cls.default(args)
        if args is None and not cls.can_run_alone:
            raise AttributeError("{C} can't be run with no arguments.".format(C=cls.__name__))
        if args is None and cls.can_run_alone:
            return cls.default()

        sub: Command
        for sub in cls.__subclasses__():
            if args[0] in sub.act:
                return sub.run(args[1:])
        return cls.default(args)

    @classmethod
    def default(cls, args=None):
        return get_help(args)


class Ping(Command):
    """
    The basic ping command
    """
    act = ['ping']
    need_run_alone = True
    can_run_alone = True

    @classmethod
    def default(cls, args=None):
        return "pong"


def test_cmd(cmd):
    """
    Run all the command.
    :param cmd: an one line command
    :return: the result
    """
    if cmd is "":
        raise AttributeError("You need to enter a command")
    return Command.run(cmd.split(" "))


if __name__ == '__main__':
    print("Done")
