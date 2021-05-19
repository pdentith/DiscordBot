# bot.py
import os
import discord
import random
import requests
import json
from dotenv import load_dotenv
from random import randrange

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
KEY = os.getenv('TENOR_KEY')
MEME_KEY = os.getenv('MEME_API_KEY')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the homeland of our Lord and Savior Brain Urbano, may you never be paired against him in a tournament.'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #ToDo hook this up to a db and allow uploading new quotes from bot
    urbano_quotes = [
        'Urbano is the human form of the 💯 emoji.',
        'Urbano just got scheduled to do a Ted Talk on winning',
        'When asked about Spock\'s attempt to use the Vulcan Nerve Pinch, Urbano was heard saying \'It kinda tickled a bit\'',
        'Urbano has created a cologne called Alpha4me',
        'By the time you finish reading this statement, Urbano will have made it to the the finals or an old school tournament.',
        'Elon Musk has a picture of him with Brian Urbano in his home.',
        'Ron Jeremy calls Urbano when he needs a wingman',
        'Every deck Urbano plays is called The Deck',
            'I asked 20 friends to come over to my place.'
            'They all said no.'
            'I told them Urbano would be there.'
            'Now 40 people are coming.'
            'Now I gotta figure out how to get Brian there.'
            '---Michael J Butzen'
        ,
        'When Urbano plays video games he has to level is character down after first logging in or it won’t be a challenge.',
        'Urbano’s dci number is 1.',
        'Urbano puts on more clinics than Home Depot',
        'Jay-Z composed his hit classic “Big Pimpin” after a run in with Brian Urbano at a red lobster',
        'Urbano walked into a rest area to piss.  When he walked out, it was an LGS.,',
        'I once sold some cards to Urbano because I wanted those cards to start winning  some games.',
        'Urbano didn’t choose shops, shops choose him to improve its win rate',
        'When Urbano casts psiblast, the target takes 4 damage and he GAINS 2 life.',
        'Brian is tired of us normal people',
        'Urbano once took Pete, squire of Urbano and Savage, admirer of Urbano to a late night Chinese dinner and then he let them sleep at his house. house. He\'s a nice guy .',
        'I once slept in the same building as urbano. I woke up a wiser man',
        'Urbano once won an old school tournament piloting a ham sandwich',
        'When Urbano walks into a bar an old school tournament breaks out',
        'when Urbano mulligans he keeps 8, and it\'s legal',
        'Urbano had volcanic island left out of alpha just to make it interesting.',
        'When Urbano mulligans, it’s just to give you the idea that you have an advantage.',
        'When wizards was releasing the Legends expansion they had to get Urbano’s approval due to potential copyright infringement',
        'Hymn to Tourach was originally Hymn to Urbano during play test but it scared too many players',
        'Brian Urbano once held a Juzam Djinn in two fingers',
        'When Richard Garfield goes to sleep every night, he checks his closet for Brian Urbano',
        'Brian taught Chuck Norris karate',
        'Urbano never asks if his spells resolve, he stares at his opponent until they do the right thing',
        'Urbano doesn’t shuffle his deck, the cards assemble themselves out of both fear and respect',
        'Urbano traded an alpha farmstead for his house.',
        'Icy Manipulator’s alpha test card name was “Brian Urbano”',
        'When urbano casts animate dead the creature gets +1/+0',
        'Nicol Bolas picks up Urbano’s dry cleaning',
        'Whenever urbano loses a child is cured of cancer, unfortunately he never loses.',
        'Urbano doesn’t sleep.  He orb flips.',
        'I heard Richard Garfield thought of magic the gathering after having a conversation with Brian Urbano',
        'Urbano is more of an end boss in real life than End bosses are in video games'
        'Last Christmas Santa asked Urbano for an Alpha Chaos Orb',
        'When Urbano gets paid, it is in alpha dual lands',
        'Urbano isn\'t on a quest for Urza\'s Chalice, the Chalice is on a quest to be held by Urbano',
        'When Urbano touchs a modern magic card it turns to Alpha',
        'Urbano\'s house smells like alpha card stock',
        'Urbano says playng white is "a crutch for bad players"',
        'Mark Rosewater has Urbano on speedail',
        'I once looked in Urbano\'s eyes, I instantly knew I was a lesser man',
        'Urbano always hits Yathzee',
        'Urbano\'s like pizza, even when he is bad he is good',
        'Last Halloween, Richard Garfield dressed up as Brian Urbano and carried an alpha deck around',
        'Urbano knew dual lands were better than Shivan Dragonin 6th grade',
        'Urbano considers beta "pauper"',
        'The chief export of Urbano is pain'
        ]

    print(message.content)

    if 'boss' in message.content.lower() or 'urbano' in message.content.lower():
        response = random.choice(urbano_quotes)
        await message.channel.send(response)

    if message.content.lower().startswith('gif'):
        cmd = message.content.split()[0].replace("gif","")
        if len(message.content.split()) > 1:
            wSpaces = message.content.split(' ', 1)
            parameters = wSpaces[1].replace(' ', '+')
            #parameters = message.content.split()[1:]
            print(parameters)
        
        ploads = {'key':KEY, 'q': parameters, 'media_filter': 'basic'} 
        r = requests.get('https://g.tenor.com/v1/search',params=ploads)
        print(r)
        python_obj = json.loads(r.content)
        #default is 20 gifs returned
        x = randrange(20)
        response = python_obj['results'][x]['media'][0]['gif']['url']
        await message.channel.send(response)
    
    if message.content.lower().startswith('wonka'):
        a=Switcher()
        querystring = a.string_to_meme('wonka', message.content)
        b=MemeApi()
        b.RequestAndSendMeme(querystring)
        await message.channel.send(file=discord.File('my_image.png'))

    if message.content.lower().startswith('xx'):
        a=Switcher()
        querystring = a.string_to_meme('xx', message.content)
        b=MemeApi()
        b.RequestAndSendMeme(querystring)
        await message.channel.send(file=discord.File('my_image.png'))

    if message.content.lower().startswith('distracted'):
        a=Switcher()
        querystring = a.string_to_meme('distracted', message.content)
        b=MemeApi()
        b.RequestAndSendMeme(querystring)
        await message.channel.send(file=discord.File('my_image.png'))
    
    if message.content.lower().startswith('bano'):
        a=Switcher()
        querystring = a.string_to_meme('Bano', message.content)
        b=MemeApi()
        b.RequestAndSendMeme(querystring)
        await message.channel.send(file=discord.File('my_image.png'))

    if message.content.lower().startswith('aliens'):
        a=Switcher()
        querystring = a.string_to_meme('Aliens', message.content)
        b=MemeApi()
        b.RequestAndSendMeme(querystring)
        await message.channel.send(file=discord.File('my_image.png'))

    if message.content.startswith('/commands'):
        response = 'gif <words to gif> \n Urbano, urbano, boss returns Urbano quote \n Meme words \n Format <meme_word> <top text> / <bottom tet> \n Bano \n wonka \n Aliens \n distracted \n XX'
        await message.channel.send(response)
 
class Switcher(object):
    def string_to_meme(self, argument, message):
        method_name = str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid meme")
        # Call the method as we return it
        return method(message)
 
    def wonka(self, message):
        c=MemeApi()
        return c.ProcessMessage("wonka", "Condescending-Wonka" ,message, 50)
    
    def distracted(self, message):
        c=MemeApi()
        return c.ProcessMessage("distracted", "Distracted-Boyfriend" ,message, 60)
 
    def xx(self,message):
        c=MemeApi()
        return c.ProcessMessage("xx", "The-Most-Interesting-Man-In-The-World" ,message, 40)

    def Bano(self,message):
        c=MemeApi()
        return c.ProcessMessage("bano", "MadUrbano" ,message, 50)

    def Aliens(self,message):
        c=MemeApi()
        return c.ProcessMessage("aliens", "Ancient-Aliens" ,message, 50)

class MemeApi(object): 
    def RequestAndSendMeme(self, querystring):
        url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"
        headers = {
            'x-rapidapi-key': MEME_KEY,
            'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        #await message.channel.send(response.content)
        file = open("my_image.png", "wb")
        file.write(response.content)
        file.close()
        return 1

    def ProcessMessage(self, originalCommand, memeName ,message, font):
        cmd = message.lower().split()[0].replace(originalCommand,"")
        text = message.lower().split(originalCommand)[1]
        print(text)
        top_text = ""
        bottom_text =""
        if len(message.split()) > 1:
            if '/' in text:
                x= text.split("/", 1)
                print(x)
                top_text = x[0]
                bottom_text = x[1:]
            else:   
                top_text = text
        return {"meme": memeName,"bottom":bottom_text,"top":top_text,"font":"Impact","font_size":font}

client.run(TOKEN)