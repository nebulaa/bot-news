import discord
import os
import requests
import json
from dotenv import load_dotenv
from newsapi import NewsApiClient
import json


load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

newsapi = NewsApiClient(os.getenv('API_Key'))

client = discord.Client(intents=intents)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('!quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('!ai'):
        ai = newsapi.get_everything(q='AI OR deeplearning OR Machine learning', language='en', page_size=1, sort_by='publishedAt')
        p_dict = json.dumps(ai,sort_keys=True, indent=4)
        await message.channel.send(p_dict)

    if message.content.startswith('!sec'):
        ai = newsapi.get_everything(q='cybersecurity', language='en', page_size=1, sort_by='publishedAt')
        p_dict = json.dumps(ai,sort_keys=True, indent=4)
        await message.channel.send(p_dict)

    if message.content.startswith('!vg'):
        ai = newsapi.get_everything(q='video games', language='en', page_size=1, sort_by='publishedAt')
        p_dict = json.dumps(ai,sort_keys=True, indent=4)
        await message.channel.send(p_dict)
    
    if message.content.startswith('!test'):

        data = newsapi.get_everything(q='AI', language='en', page_size=5, sort_by='publishedAt')
        # data = json.dumps(test, sort_keys=True, indent=4)
        Title = json.dumps(data['articles'][0]['title'],sort_keys=True, indent=4)
        Title2 = json.dumps(data['articles'][1]['title'],sort_keys=True, indent=4)
        Title3 = json.dumps(data['articles'][2]['title'],sort_keys=True, indent=4)
        Title4 = json.dumps(data['articles'][3]['title'],sort_keys=True, indent=4)
        Title5 = json.dumps(data['articles'][4]['title'],sort_keys=True, indent=4)

        URL = json.dumps(data['articles'][0]['url'],sort_keys=True, indent=4)
        URL2 = json.dumps(data['articles'][1]['url'],sort_keys=True, indent=4)
        URL3 = json.dumps(data['articles'][2]['url'],sort_keys=True, indent=4)
        URL4 = json.dumps(data['articles'][3]['url'],sort_keys=True, indent=4)
        URL5 = json.dumps(data['articles'][4]['url'],sort_keys=True, indent=4)

        p1 = f"News 1 = {Title} {URL}\n"
        p1 += f"News 2 = {Title2} {URL2}\n"
        p1 += f"News 3 = {Title3} {URL3}\n"
        p1 += f"News 4 = {Title4} {URL4}\n"
        p1 += f"News 5 = {Title5} {URL5}\n"
        await message.channel.send(p1)

client.run(os.getenv('TOKEN'))
