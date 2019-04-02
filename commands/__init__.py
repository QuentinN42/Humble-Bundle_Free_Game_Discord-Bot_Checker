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
    
    def __init__(self):
        pass

    @classmethod
    def run(cls, args):
        for sub in cls.__subclasses__():
            if args[0] in sub.act:
                return sub.run(args[1:])
        return cls.default()

    @staticmethod
    def default():
        return get_help()


class Ping(Command):
    """
    The basic ping command
    """
    act = ['ping']
    
    def run(self, args = []):
        return 'pong'


if __name__ == '__main__':
    print(Command.run(['bla', 'bli']))
