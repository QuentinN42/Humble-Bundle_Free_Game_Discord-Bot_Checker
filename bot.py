"""
Main Bot script

@date: 15/03/2019
@author: Quentin Lieumont
"""
import discord
from discord.ext.commands import Bot
import asyncio

import secrets
import sources
from checker import main as check


bot = Bot(command_prefix = "!")


async def run_checker():
    await bot.wait_until_ready()
    while not bot.is_closed:
        f = open("ping_roles.txt", "r")
        pinged_roles = f.read()
        f.close()
        f = open("channel.txt", "r")
        channel = f.read()
        f.close()
        if channel != '' and pinged_roles != '':
            games = check()
            for game in games:
                msg = "Hello {pinged}, checkout this free game:\n".format(pinged = pinged_roles[:-1])
                msg+= game.link
                await bot.send_message(bot.get_channel(channel), msg, embed = game.picture)
        await asyncio.sleep(10)


@bot.event
async def on_ready():
    print("Logged in !")


@bot.event
async def on_message(message):
    print("Message from " + str(message.author) + ":")
    print(message.content)
    if (message.author != bot.user) and message.content:
        if message.content[0] == '!':
            if message.content[1:].lower() in sources.channel:
                msg = "List of channels :\n"
                for c in message.author.server.channels:
                    msg += "`{c}` with id ```{id}``` \n".format(c = c, id = c.id)
                await bot.send_message(message.channel, msg)
            elif message.content[1:].lower() in sources.role_list:
                msg = "List of roles :\n"
                for r in message.author.server.roles:
                    msg += "`{role}` with id ```{id}``` \n".format(role = r, id = r.id)
                await bot.send_message(message.channel, msg)
            elif message.content[1:].split(" ")[0].lower() in sources.set_role:
                role_id = message.content[1:].split(" ")[1]
                f = open("ping_roles.txt", "a")
                f.write(str(role_id)+",")
                f.close()
                msg = "{} added to the `ping_role` list.".format(role_id)
                await bot.send_message(message.channel, msg)
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
                    msg+= "List of roles in this file :\n"
                    msg+= "\n".join(roles)
                await bot.send_message(message.channel, msg)
            elif message.content[1:].lower() in sources.here:
                f = open("channel.txt", "w")
                f.write(message.channel.id)
                f.close()
                print("-- channel set to {}--".format(message.channel.id))
                await bot.send_message(message.channel, "Channel set :)")
            else:
                await bot.send_message(message.channel, "Erreur ...", embed = sources.error_pict)


bot.loop.create_task(run_checker())
bot.run(secrets.BOT_TOKEN)
