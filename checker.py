"""
Check if there is some free game on Humble Bundle

@date: 15/03/2019
@author: Quentin Lieumont
"""
from sources import Game, url, outputfile
import os


def get_data():
    """
    Request the html page
    :return bool:
        True -> Success
        False-> Fail
    """
    test = os.system(f"phantomjs getPage.JS {url} > {outputfile}")
    if test == 0:
        return True
    else:
        return False


def get_body():
    """
    remove page <head> ... </head>
    :return str: the body
    """
    f = open(outputfile, "r")
    line = f.readline()
    while "<body" not in line:
        line = f.readline()
    line = f.readline()
    body = ""
    while "</body" not in line:
        body += line
        line = f.readline()
    return body


def get_all_games_raw():
    """
    Parse the body and get the UL from the page
    
    Return the table of raw games
    :return list(str): all <li>...</li> in the UL
    """
    body = get_body()
    ul_end = '</ul>\n</div></div>\n\n  <div class="js-loading-overlay overlay'
    ul = body.split('<ul class="entities-list')[1].split(ul_end)[0]
    return ul.split('<li class="entity-block-container')[1:]


def get_all_games():
    """
    get all raw games and put them into the Game() class
    """
    games = []
    for raw_game in get_all_games_raw()[:-1]:
        link = (
            "https://www.humblebundle.com" + raw_game.split('href="')[1].split('"')[0]
        )
        picture = raw_game.split("<img ")[1].split('src="')[1].split('"')[0]
        name = raw_game.split('<span class="entity-title">')[1].split("</span>")[0]
        price = raw_game.split('<span class="price">')[1].split("</span>")[0]
        discount = raw_game.split('<span class="store-discount">')[1].split("</span>")[
            0
        ]
        games.append(Game(name, discount, price, link, picture))
    return games


def get_free_games(game_list: list):
    """
    check if there is some free games
    
    :param game_list: list of the games
    :return: list of free games
    """
    return [game for game in game_list if game.discount == "-100%"]


def main(verbose: bool = False):
    """
    The main function
    
    :return:
    """
    if verbose:
        print("\tgetting web page")
    test = get_data()
    if test:
        if verbose:
            print(f"\tweb page successfully pulled")
        all_games = get_all_games()
        if verbose:
            print(f"\t{len(all_games)} game(s)")
        free_games = get_free_games(all_games)
        if verbose:
            print(f"\t{len(free_games)} free game(s)")
        return free_games
    else:
        if verbose:
            print(f"\tcan't pull the page :/")
        return False


if __name__ == "__main__":
    pass
    # gs = main(True)
    # for g in gs:
    #   print(g)
