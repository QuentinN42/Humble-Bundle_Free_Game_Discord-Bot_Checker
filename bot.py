"""
Main Bot script

@date: 15/03/2019
@author: Quentin Lieumont
"""
from discord.ext.commands import Bot
from discord.ext import tasks
import asyncio

import secrets
import sources
from checker import main as check


bot = Bot(command_prefix="!")


@tasks.loop(seconds=10)
async def run_checker():
    print("loop launched")
    with open("ping_roles.txt", "r") as f:
        pinged_roles = f.read()
    with open("channel.txt", "r") as f:
        channel = f.read()
    presented_games: list = sources.get_json("presented_games.json")
    print(presented_games)
    print(channel, pinged_roles)
    if channel != '' and pinged_roles != '':
        print("checker launched")
        games = check()
        print("games parsed")
        for game in games:
            print(f"-> {game.name}")
            if game.name not in presented_games:
                presented_games.append(game.name)
                msg = f"Hello {pinged_roles[:-1]}, checkout this free game:\n"
                msg += game.link
                print(f" | ch: {channel}")
                print(f" | msg:\n{msg}\n")
                sources.write_json("presented_games.json", presented_games)
                await bot.get_channel(int(channel)).send(msg, embed=game.picture)
            else:
                print("    Nope")


@bot.event
async def on_ready():
    print("Logged in !")
    run_checker.start()


@bot.event
async def on_message(message):
    print("Message from " + str(message.author) + ":")
    print(message.content)
    if (message.author != bot.user) and message.content:
        if message.content[0] == '!':
            if message.content[1:].lower() in sources.channel:
                msg = "List of channels :\n"
                for c in message.author.server.channels:
                    msg += "`{c}` with id ```{id}``` \n".format(c=c, id=c.id)
                await message.channel.send(msg)
            elif message.content[1:].lower() in sources.role_list:
                msg = "List of roles :\n"
                for r in message.author.server.roles:
                    msg += "`{role}` with id ```{id}``` \n".format(role=r, id=r.id)
                await message.channel.send(msg)
            elif message.content[1:].split(" ")[0].lower() in sources.set_role:
                role_id = message.content[1:].split(" ")[1]
                f = open("ping_roles.txt", "a")
                f.write(str(role_id)+",")
                f.close()
                msg = "{} added to the `ping_role` list.".format(role_id)
                await message.channel.send(msg)
            elif message.content[1:].split(" ")[0].lower() in sources.remove_role:
                role_id = message.content[1:].split(" ")[1]
                f = open("ping_roles.txt", "r")
                roles = f.read().split(",")
                f.close()
                if role_id in roles:
                    roles.remove(role_id)
                    f = open("ping_roles.txt", "w")
                    f.write(",".join(roles)+",")
                    f.close()
                    msg = "{} remved from the `ping_role` list.".format(role_id)
                else:
                    msg = "{} is not in the `ping_role` list.\n".format(role_id)
                    msg += "List of roles in this file :\n"
                    msg += "\n".join(roles)
                await message.channel.send(msg)
            elif message.content[1:].lower() in sources.here:
                with open("channel.txt", "w") as f:
                    f.write(str(message.channel.id))
                print("-- channel set to {}--".format(message.channel.id))
                await message.channel.send("Channel set :)")
            else:
                await message.channel.send("Erreur ...", embed=sources.error_pict)


bot.run(secrets.BOT_TOKEN)
