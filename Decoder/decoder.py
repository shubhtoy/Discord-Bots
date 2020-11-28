import os

import discord
import random
import mysql.connector as ms

TOKEN = "NzU5NDIzNzU1MjA1MzQ1MzUx.X29SfA.b7-dvmQ5qi35VAnLVx50Ce842Qs"
GUILD = "Abhivyakti"
hint_list = {
    "LEVEL10a": {
        1: """Un jumble the words (obviously) and then use the numbers given to locate your answer. The numbers are almost like co-ordinates, just figure out the order."""
    },
    "LEVEL10b": {
        1: "Un jumble the words (obviously) and then use the numbers given to locate your answer. The numbers are almost like co-ordinates, just figure out the order."
    },
    "LEVEL11": {
        1: "Read the paper. Find something. And use something that we have given to you in the server, that you haven't used yet"
    },
    "LEVEL12": {
        1: "Read about all the information points given in the question. Then just try something that means the same, but it isn't the same thing."
    },
    "LEVEL13a": {
        1: '''"When I am exiled, I want the love of my life to stay with me"'''
    },
    "LEVEL13b": {1: '''"The lamentations of the dead are the songs of the living"'''},
    "LEVEL14a": {
        1: """"I am of the opinion that watching movies can be very helpful", although my mum never let's me watch them"""
    },
    "LEVEL14b": {
        1: '''"How do you profit off a disease, how do monopolise a disease"'''
    },
}

client = discord.Client()


@client.event
async def on_ready():

    channel = client.get_channel(759424288138068038)
    await channel.send("May the force be with you!")
    print(f"Connected to Server!")


def decoder(encoded, key):
    try:
        final_ = ""
        y = key
        key_ = (y % 26) * (y % 15)
        for j in encoded:
            for a in j:
                if a == "|":
                    final_ += " "
                else:
                    n = ord(a)
                    new = 0, key
                    new = n - key_
                    final_ += chr(new)
        return final_
    except:
        return "ERROR"


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.channel) == "decoder":
        await message.channel.purge(limit=None, check=lambda msg: not msg.pinned)
        if "$k:" in message.content:
            txt = message.content.split(" $k:")
            try:
                finp = decoder(txt[0], int(txt[1]))
            except:
                finp = "Error"
            await message.author.send(f"Decoded:{finp}")
        elif message.content == "!ping":
            await message.author.send(f"My ping is {round(client.latency * 1000)}ms")
    elif str(message.channel) == "hints":
        if message.content == "!hint" and "PRODIGY" in [
            i.name for i in message.author.roles
        ]:
            await message.channel.purge(limit=None, check=lambda msg: not msg.pinned)
            a = ms.connect(
                host="logs.c7xtjtjv8ph3.ap-south-1.rds.amazonaws.com",
                port=3306,
                user="shubh",
                passwd="shubh2003",
                db="logs",
            )
            a.autocommit = True
            c = a.cursor()
            rol = message.author
            curr_role = [i.name for i in rol.roles][-1]
            c.execute(f'select hint_no,level from hint_logs where name="{rol}";')
            res = c.fetchall()
            if len(res) != 0:
                if res[0][1] == curr_role:
                    try:
                        c.execute(
                            f"update hint_logs set hint_no={res[0][0]+1} where name='{rol}';"
                        )
                        await rol.send(
                            f"**{res[0][1]} : {res[0][0]+1} : {hint_list[curr_role][res[0][0]+1]}**"
                        )
                        with open("hint_log.txt", "a+") as qw:
                            qw.write(f"{rol}:{curr_role}:{[res[0][0]+1]}")
                            qw.write("\n")
                    except:
                        await rol.send(
                            "*YOU HAVE EXHAUSTED ALL YOUR HINTS FOR THIS LEVEL*"
                        )
                else:
                    try:
                        await rol.send(
                            f"**{curr_role} : 1 : {hint_list[curr_role][1]}**"
                        )
                        c.execute(
                            f'update hint_logs set level="{curr_role}",hint_no=1 where name="{rol}";'
                        )
                        with open("hint_log.txt", "a+") as qw:
                            qw.write(f"{rol}:{curr_role}:1")
                            qw.write("\n")
                    except:
                        await rol.send("*THERE ARE NO HINTS AVAILABLE FOR THIS LEVEL*")
            else:
                try:
                    await rol.send(f"**{curr_role} : 1 : {hint_list[curr_role][1]}**")
                    c.execute(f'insert into hint_logs values("{rol}","{curr_role}",1);')
                    with open("hint_log.txt", "a+") as qw:
                        qw.write(f"{rol}:{curr_role}:1")
                        qw.write("\n")
                except:
                    await rol.send("*THERE ARE NO HINTS AVAILABLE FOR THIS LEVEL--*")

    elif str(message.channel) == "text":
        rol = message.author
        if message.content == "!iamready" and "I AM NEW" in [
            i.name for i in message.author.roles
        ]:
            await message.channel.purge(limit=1, check=lambda msg: not msg.pinned)
            await rol.add_roles(
                discord.utils.get(rol.guild.roles, name="PROJECT ALIBI")
            )


client.run(TOKEN)