"""
New library to build commands

@date: 01/04/2019
@author: Quentin Lieumont
"""
from commands.tree import Tree, Leaf
from commands.cmd import *

bt = Tree(Bla, {"bli": Leaf(Bli), "Blo": Leaf(Blo)})
main = Tree(Help, {"ping": Leaf(Ping), "bla": bt})
