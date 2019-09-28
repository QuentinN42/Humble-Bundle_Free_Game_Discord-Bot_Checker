"""
Usefull thinks...

@date: 15/03/2019
@author: Quentin Lieumont
"""
import discord
import json


def get_json(link: str):
    return json.load(open(link, "r"))


def write_json(link: str, data) -> None:
    _json = json.dumps(data, sort_keys=True, indent=4, separators=(",", ": "))
    with open(link, "w") as f:
        for l in _json.split("\n"):
            f.write(l)


# all commands
channel = ["channel", "ch"]
here = ["here", "h"]
role_list = ["rolelist", "rl"]
set_role = ["setrole", "set"]
remove_role = ["removerole", "rm"]


url = "https://www.humblebundle.com/store/search?sort=discount"
outputfile = "tmp.html"


error_pict_url = "https://pbs.twimg.com/profile_images/607860484830859264/AQuZ4ODc.png"
error_pict = discord.Embed().set_image(url=error_pict_url)


class Game:
    def __init__(self, name, discount, price, link, picture_url=None):
        self.name = name
        self.discount = discount
        self.price = price
        self.link = link
        self.picture_url = "".join(picture_url.split("amp;"))
        self.picture = discord.Embed().set_image(url=self.picture_url)

    def __eq__(self, other):
        if type(other) == type(self):
            return self.name == other.name
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "{} at {} ({} discount)".format(self.name, self.price, self.discount)
