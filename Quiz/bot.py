import os

import discord
import random
import mysql.connector as ms

from datetime import datetime

TOKEN = "NzU5MzA2OTUxMTIwOTEyMzg0.X27ltA.KY1J5FsqH4cLd_NAbNdfBwe90yM"
GUILD = "Abhivyakti"

client = discord.Client()

impo = {
    "!start": [
        ["PROJECT ALIBI"],
        "LEVEL1",
        """Where is the b2xkIEphY29iIFRvbWUgU2Nob29sIGZvciBCb3lzIGFuZCB0aGUgVW5pdGVkIFN0YXRlcyBOYXZhbCBUcmFpbmluZyBDZW50ZXIgb24gQmFpbmJyaWRnZSBpcyBsb2NhdGVk? You can find it with and around these Y29vcmRpbmF0ZXM.
MzkuNjAzNjQ2LC03Ni4xMDczNS4=\nhttps://ibb.co/PM3LCvS
""",
    ],
    "!396036467610735": [
        ["LEVEL1"],
        "LEVEL2",
        "Welcome To Level 2: \n A school, well that is weird.. you make your way to the building in question posing as members from the health department, how original..but the log files say that an actual inspection was scheduled around the same time, you are led to the different sections of the school and find yourself lost in the big building, but nothing of interest is found.. apart from an old hard drive, there are two files present in it, one with a password and another free to browse, they are interlinked perhaps.. \n abhivyakti-evolve.com/Alibi/Befall.txt \n https://ibb.co/SyyRQLX",
    ],
    "!peabodyandstearns": [
        ["LEVEL2"],
        "LEVEL3",
        "Welcome To Level 3: Having secured access to the file, you find out that the virus is still in development and its market value is being estimated at over a billion dollars, attached to it is a list of ingredients involved, most of them in a native language, further development leads to the discovery that most of these are in mandarin and the only group which can facilitate a transportation at this scale is (---data redacted---), the teams in china are contacted to report all suspicious activity and a case quickly surfaces,the body of a high ranking man is found, he is reported to be a reputed carrier known for the transport of illegal goods across borders… \n (851a^3 - 2553 a^2 + 1702a) \n https://ibb.co/fFXDLZQ",
    ],
    "!vau": [
        ["LEVEL3"],
        "LEVEL4",
        "Welcome To Level 4:\n Making your way to the Xinjiang area, one of the most controversial areas in mainland china, you feel mesmerized by the sights and smells the place has to offer. In one such unique eatery, you find a kind looking old lady shuffling through the crowd, her dog the only thing allowing the blind woman to navigate. As you move forward to help her cross the street, she suddenly moves towards you and shoves a rather shady object in your hand before resuming her original stance, the escort gives you a short nod and points towards one of the less hostile looking areas.. you take the cue and follow him for a while before reaching a flower shop and settling in, opening the package, you find it has seemingly random pieces of paper.the escort tells you this is what he spent his childhood doing, Tangram, the puzzle famous to the chinese mainland looks at you as you look at it.0ne piece of the puzzle has the following lines written on it- \n “sometimes,it is the literal meaning of things that takes us forward” What do you make of this puzzle, little one.",
    ],
    "!nighjara": [
        ["LEVEL4"],
        "LEVEL5a",
        """Welcome To Level 5: \n Snooping in on people is probably not a very good idea, and when you are a potential pivot for the forces to turn , well… the national police agency sends in two men after 7 hours of gruesome work and you are taken to the local seminar hall to attend a speech by Madellyn Stillwell, one of the last people who are not handed their scripts by the PR department… the speech goes on for about 30 minutes when you find yourself in the middle of a blackout, it lasts for about 90 seconds and you hear a little more than a murmur among the audience, they are probably accustomed to this stuff, although they are not accustomed to seeing a woman tied to a chair and what seems like plastic explosives across her torso… and as much as you are sure that shit wont get crazier, a guy from the audience steps forward, removes his shirt and joins the crew on stage, you curse under your breath, trust us, we don’t understand half the shit going in here too…
Anyways, the only thing that makes the man stand out apart from his lack of clothing are the words written across his chest….
THE JUDGEMENT OF PARIS
There has to be something here, anything to buy time,,,maybe a way to steer the vigilantes off course,,, think think think…. wait, whats that, the 2 guys have managed to subdue the crew on stage, it looks more like that they were waiting to surrender… but now is not the time to think, you rush to Stillwelll and find a digital message across the device, 
“god looked down on the fairest of them all, and put on another ,Morgan freeman movie”
How do you conquer your 7 deadly sins????
Time runs short, and so does Stillwell’s temper…
""",
    ],
    "!nightjarb": [
        ["LEVEL4"],
        "LEVEL5b",
        """Welcome To Level 5: \n Solving the Tanagram leads to an address, surprising that you were eating pizza off of a papa johns a few days back without money and are here now… you don’t find it surprising that the house is abandoned, probably in haste by the looks of it . however you do manage to get hold of the vehicle responsible for transporting the contents, perhaps the facility underestimated the scope of your genius…..
> waning moon, day-3 
Henry The Hound is my favourite, I saw a boy shove a cigarette up his nose, only if I had a way to make him see how good the mascot is… I swear to god these emotions are hard to control…

> waning moon, day-6 (different year)
I don’t see Henry in the park anymore, I am scared to go there, I still love the final float during those times.



These were the only pieces clearly legible in the old diary that you manage to get your hands on, you retire to a local motel and call it a night, but a question still tingles your mind….

Wtf is a float? More importantly, what is the final float?
""",
    ],
    "!chastity": [
        ["LEVEL5a"],
        "LEVEL6",
        """Welcome To Level 6:\nSit back, take a deep breath, we honestly did not know you would get this far, maybe you are worth more than what our recruitment department  calculated, here’s an assignment, solve it and we take you more seriously- 

What comes intel after tiktok?
""",
    ],
    "!birthdaycake": [
        ["LEVEL5b"],
        "LEVEL6",
        """Welcome To Level 6:\nSit back, take a deep breath, we honestly did not know you would get this far, maybe you are worth more than what our recruitment department  calculated, here’s an assignment, solve it and we take you more seriously- 

What comes intel after tiktok?
""",
    ],
    "!processarchitectureoptimization": [
        ["LEVEL6"],
        "LEVEL7",
        """GOVERNMENT INTELLIGENCE PAIRED WITH THE INFORMATION COLLECTED PROVIDE THE HISTORY OF ‘THE FACILITY’ AND THEIR IDEOLOGY,ALTHOUGH THEIR ULTIMATE GOAL IS UNCLEAR AND A MYSTERIOUS ELEMENT IS PRESENT, THIS NEEDS TO BE FURTHER BROKEN DOWN.\n https://ibb.co/VW6RYbG""",
    ],
    "!blackplague": [
        ["LEVEL7"],
        "LEVEL8",
        """With one of the alias of the founder given in the document, the government 
agencies find out about a seed deposit in the Svalbard Seed Vault under this name. Upon 
arriving and then going to the vault location, the teams are rammed by a hostile jeep. They 
have very less time to decode the sat com code to call for help. 

The sat com is not with instructions, and operates in Chinese. The chasing jeep is gaining on your vehicle. In order to save your life, try to send a signal. You have limited time. Think about it fast!

Here’s a hint. Go beyond language in your message. Think about something universal.
Choose your path (a or b) while entering the answer for eg !youranswera for a and !youranswerb for b, Both of the participants should enter the same path.Your first choice will be counted.
""",
    ],
    "!saveousoulsa": [
        ["LEVEL8"],
        "LEVEL9a",
        """The team successfully manage to send the SOS message to the authorities, and the police arrive just in time to drive the attackers off. The team gets back on track and reaches the seed vault. When the team reach the vault they were looking for, they find out that it is locked. They must decode the passcode for the safe. The vault keepers don’t know the password themselves, so they can’t be of much help. What do you think is the passcode to the safe? The poster on the safe might be a clue.\nhttps://ibb.co/Z1HpNtM
""",
    ],
    "!saveoursoulsb": [
        ["LEVEL8"],
        "LEVEL9b",
        """The team does not manage to get the signal out, and gets kidnapped. In the hideout, they find a small burner phone that is left carelessly by the kidnappers within their reach. After managing to secure it, you must unlock it to send a message. It’s a regular 4 digit passcode. 10000 potential answers, only one right. Get on it, NOW!\nhttps://ibb.co/4gQB4rK""",
    ],
    "!quentintarantino": [
        ["LEVEL9a"],
        "LEVEL10a",
        """As it turns out, the safe opens. The seeds, turn out to be mustard seeds. Talk about seeds of doubt, turning out to be seeds of failure. The vault keepers chuckle as they go out of the room and you are asked to return back to the HQ. Upon arriving back, you received an envelope. After opening it, it seems like it has something written on it, but not obvious. Can you decode this? I think you better do, you can’t mess up twice in a row and get away with it. Look into the letter.

REIPD DNA JCPUREIDE
ARW DNA CEPAE
RICME DNA NPSIMTUENH

18 7 8
45 12 4
117 6 4
""",
    ],
    "!0908": [
        ["LEVEL9b"],
        "LEVEL10b",
        """Voila! The phone opens, and you send a message to the HQ to come save you. And come save you they do. They burst in the door and shoot on sight on the kidnappers. In the resultant shooting, the main suspect is killed, but you do manage to get a name out of their conversation, a name worth the lives of 2 people, Jean-Claude Duvalier.you sigh as they escort you to a vehicle waiting outside. Talk about recklessness. Searching the battered room for evidences, you find a computer. You must enter the password to get inside. Do it fast.

USELYSS
RGTEA PSTECAIOTNECX
VIBIISELN ANM

31 16 9
101 4 4
12 5 9
""",
    ],
    "!resistancemustfall": [
        ["LEVEL10a"],
        "LEVEL11",
        """You manage to crack open the computer. Hoping to find some extra information about the name you just overhead, you dissect the whole computer. Turns out, there’s nothing more than some mathematical papers on the “wonderful golden ratio”. But scrolling through, you also find a cryptic set of words. Try to decode this. This may provide a clue about the person who kidnapped you. 

ŉŕŕőŔěĐĐŕŊŏŚŖœōďńŐŎĐłōŊŃŊŒ
https://tinyurl.com/y3sa6fwq """,
    ],
    "!mourningislate": [
        ["LEVEL10b"],
        "LEVEL11",
        """You manage to crack open the computer. Hoping to find some extra information about the name you just overhead, you dissect the whole computer. Turns out, there’s nothing more than some mathematical papers on the “wonderful golden ratio”. But scrolling through, you also find a cryptic set of words. Try to decode this. This may provide a clue about the person who kidnapped you. 

ŉŕŕőŔěĐĐŕŊŏŚŖœōďńŐŎĐłōŊŃŊŒ
https://tinyurl.com/y3sa6fwq""",
    ],
    "!tian": [
        ["LEVEL11"],
        "LEVEL12",
        """The team members reach the jeep manufacturers main outlet in Tianjin, China. The city looks to be old and full of culture, with Chinese temples in every directions. You reach the main office of Tian, a relatively new up and coming brand which makes armored jeeps for VIPs. The outlet manager hands you the list of all the bulk purchases made within the last 10 years, but the list is incomplete. The complete list is in the companies hard drive, whose key the manager doesn't seem to know. Decode the hard drive to get access to the list. Think hard. You don’t much about the brand or the city for that matter. Start from the obvious, and work your way into the past.""",
    ],
    "!shangdi": [
        ["LEVEL12"],
        "LEVEL13",
        """Further investigating on the jeep rental firm and the clues that you have managed to gather so far, you find that the complete list actually had just one name of importance, something that the other teams had come across earlier at a different location entirely “Jean-Claude Duvalier”. a simple google search leads to a surprising discovery, the foundation splits the teams, one goes to the homeground of the mysterious figure Jean-Claude and the other stay put to further investigate other carriers through which the virus might have been transported. (!haiti for Haiti and !wuhan for Wuhan,You know the drill!)""",
    ],
    "!haiti": [
        ["LEVEL13"],
        "LEVEL13a",
        """https://tinyurl.com/y57mqbpo
https://www.youtube.com/watch?v=T73WhWTawCE
""",
    ],
    "!wuhan": [
        ["LEVEL13"],
        "LEVEL13b",
        """You get ready to move to Wuhan for further investigation,hoping that all of this would start making sense and you will finally be able to go home with the money and power that the alibi foundation has promised, even though you are tired, a can of RedCow and a short nap make you feel a little better. The reports of an unknown disease spreading have started to circulate but you don’t trust Reddit and its memes to a degree where you feel worried, you should be worried though, because the airport demands has been put under a lockdown and all passengers are being checked. The personnel accompanying you looks tense and places a picture in your hand before going to the washroom. He says “the picture is important, it lets our allies know us”, a statement from your mission brief tell you. Your turn at the security check is about to come and the other guy has still not come back… you pray to the whatever god you believe as you are asked to step forward. The officer at the station gives the picture in your hand a look and you are brought to your knees almost immediately, his thick arm tight around your neck.. two more officers come forward and take you to an unnamed room in a different section of the airport. You find the first officer looking at you from across the other end of the table you are positioned at. Maybe he wants you to say something.. your mind rushes to the picture and you find yourself inside your mind, zoning out might be helpful, for your life may depend on it.\nhttps://ibb.co/rmPfGJR""",
    ],
    "!veroniqueroy": [
        ["LEVEL13a"],
        "LEVEL14a",
        """Finally!, you gain access to the presidents phone and the only thing of value apart from his Billy Joel collection are his call recordings with a contact named Moriarty, the number used cannot be traced and files show that it was never issued…

Duration- 45:58 

-----start by talking about politics, football and random things, their families, the country---
However, a change in tone is noticed after some time, conversation following is marked-

Moriarty- So, what are you doing these days (sniffs), for passing the time.. you know our days grow short,right?

Jean- Yeah, been watching this movie called don’t go in the woods.. musical horror….loved the idea, bad implementation

Moriarty- Death by music could be so beautiful

Jean- ill drink to that, oh shit… mom’s here, gotta go


______line cuts_________


Our people say he was talking about someone, what could it be???
""",
    ],
    "!auverssuroise": [
        ["LEVEL13b"],
        "LEVEL14a",
        """As soon as you say the words, a look of worry washes over the man’s face, he motions to an attendant and a medical kit along with a small portion of food is brought in. A small conversation leads to you finding he too is a dungeons and dragons fan…anyways, he hands you a crude looking map which was found on the body of one of the personnel killed a few days ago while he was working on the case of the facility. This is a piece of a document that he acquired when the suspect fled after a fistfight. What do you make of this??\nhttps://ibb.co/Tr4LQVG""",
    ],
    "!johnfogarty": [
        ["LEVEL14a"],
        "LEVEL15",
        '''You enter the name John Fogarty into the secondary layer of firewall. And BOOM! You are in. You see information, that no one else would want you to see. It seems like there is something shadier going on. The document you see sends your to a link on drive. And there, you see a password protected document called “The Truth behind ALIBI”. Do you want to open it? I thought so too. Get on decoding. The story picks up now. There is mystery ahead. The password? What could it be? Start from the very beginning. Did you leave some leads behind? Some names that you didn’t care about?\nhttps://ibb.co/qRtXS8K"''',
    ],
    "!johncollier": [["LEVEL15"], "LEVELBREAK", """COMING SOON!"""],
    "!sorryfam": [
        ["LEVELBREAK"],
        "LEVEL16",
        """https://tinyurl.com/y3u78wqe\nhttps://ibb.co/vYsTb5C\nI am a raymond wearer and a big fan of Robert Schumann\nāččĉČÓÈÈčĂćĒĎċąÇüĈĆÈĒÌþýđćčÏ""",
    ],
    "!staugustine": [["LEVEL16"], "LEVELBREAK", """cOMMinG sOON!"""],
}

keys = [i for i in impo.keys()]
print(keys)


@client.event
async def on_ready():
    channel = client.get_channel(759718690190000158)
    await channel.send("May the force be with you!")
    print(f"Connected to Server!")


@client.event
async def on_member_join(member):
    rol = message.author
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to my Discord server!")
    await rol.add_roles(discord.utils.get(rol.guild.roles, name="I AM NEW"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.channel) == "answers":
        rol = message.author
        await message.channel.purge(limit=None, check=lambda msg: not msg.pinned)
        if message.content in keys:
            req_role = [i.name for i in rol.roles][-1]
            if req_role == "US":
                req_role = [i.name for i in rol.roles][-2]
            for mop in impo[message.content][0]:
                if mop in req_role:
                    new_role = impo[message.content][1]
                    now = datetime.now()
                    await rol.remove_roles(
                        discord.utils.get(rol.guild.roles, name=req_role)
                    )
                    await rol.add_roles(
                        discord.utils.get(rol.guild.roles, name=new_role)
                    )
                    await message.author.send(impo[message.content][2])
                    a = ms.connect(
                        host="logs.c7xtjtjv8ph3.ap-south-1.rds.amazonaws.com",
                        port=3306,
                        user="shubh",
                        passwd="shubh2003",
                        use_pure=True,
                        db="logs",
                    )
                    a.autocommit = True
                    cursor = a.cursor()
                    current_time = now.strftime("%H:%M:%S")
                    cursor.execute(
                        f'insert into Event_Logs values("{rol}","{req_role}","{current_time}");'
                    )
                    channel = client.get_channel(759364619163664423)
                    await channel.send(
                        f"*Time is money and someone just opened a bank, a team have reached*  **{new_role}** *, step up your game now*!"
                    )
        elif message.content == "!ping":
            await rol.send(f"My ping is {client.latency * 1000}ms")
        elif message.content == "!purge":
            rol = message.author
            if "US" in [i.name for i in rol.roles]:
                await message.channel.purge(
                    limit=None, check=lambda msg: not msg.pinned
                )
    elif message.content == "!ping":
        rol = message.author
        await rol.send(f"My ping is {client.latency*1000} ms")
        await rol.send(f"My ping is {client.latency*1000} ms")
    elif message.content == "!purge":
        rol = message.author
        if "US" in [i.name for i in rol.roles]:
            await message.channel.purge(limit=None, check=lambda msg: not msg.pinned)
    else:
        return
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        "I'm the human form of the 💯 emoji.",
        "Bingpot!",
        (
            "Cool. Cool cool cool cool cool cool cool, "
            "no doubt no doubt no doubt no doubt."
        ),
        "Please Sarge, just come. Do it for me. Do it for love.",
        "But my point is this: I don't care what time it is. I'm always happy to be here. Nine-Nine! Nine-Niiine! A-Noine-Noine! I'm gonna keep doing it until you guys chime in. A-Noine-Noine!",
        "Time for waiting is over. Now is the time for groin-stomping.",
        'Sarge, with all due respect, I am gonna completely ignore everything you just said." - Jake Peralta, Season Two, "Hostages',
        'The English language can not fully capture the depth and complexity of my thoughts, so I’m incorporating emojis into my speech to better express myself. Winky face." - Gina Linetti, Season One, "Charges and Specs',
        "A place where everybody knows your name is hell. You’re describing hell",
        "Cool, cool, cool, cool, cool. No doubt, no doubt, no doubt.",
        "If I die, turn my tweets into a book.",
        "I asked them if they wanted to embarrass you, and they instantly said yes.",
        "Great, I’d like your $8-est bottle of wine, please.",
        "Captain Wuntch. Good to see you. But if you’re here, who’s guarding Hades?",
        "I’m playing Kwazy Cupcakes, I’m hydrated as hell, and I’m listening to Sheryl Crow. I’ve got my own party going on.",
        "Anyone over the age of six celebrating a birthday should go to hell.",
        "Captain, turn your greatest weakness into your greatest strength. Like Paris Hilton RE: her sex tape.",
        "Jake, piece of advice: just give up. It’s the Boyle way. It’s why our family crest is a white flag."
        'Sarge, with all due respect, I am gonna completely ignore everything you just said." - Jake Peralta, Season Two, "Hostages',
        'The English language can not fully capture the depth and complexity of my thoughts, so I’m incorporating emojis into my speech to better express myself. Winky face." - Gina Linetti, Season One, "Charges and Specs',
        "A place where everybody knows your name is hell. You’re describing hell",
        "Cool, cool, cool, cool, cool. No doubt, no doubt, no doubt.",
        "If I die, turn my tweets into a book.",
        "I asked them if they wanted to embarrass you, and they instantly said yes.",
        "Great, I’d like your $8-est bottle of wine, please.",
        "Captain Wuntch. Good to see you. But if you’re here, who’s guarding Hades?",
        "I’m playing Kwazy Cupcakes, I’m hydrated as hell, and I’m listening to Sheryl Crow. I’ve got my own party going on.",
        "Anyone over the age of six celebrating a birthday should go to hell.",
        "Captain, turn your greatest weakness into your greatest strength. Like Paris Hilton RE: her sex tape.",
        "Jake, piece of advice: just give up. It’s the Boyle way. It’s why our family crest is a white flag.",
    ]

    if message.content == "!99":
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


client.run(TOKEN)