import discord
import random
from discord.ext import commands
import requests
from os import path
import wikipedia
import urllib
import os
import ruamel.yaml
import json

if message.content.startswith('!item'):
  itemsearch = message.content[len('!item'):].strip()
  APIKey = ''
  swtorPull = request.get("http://swtordata.com:80/api/v2/items?query={}".format(itemsearch), X-Api-Key = APIKey)
  if swtorPull.status_code == 200:
    await client.send_message(message.channel, swtorPull.json()["Display Name"])
  elif swtorPull.status_code == 404:
    await client.send_message(message.channel, "ERROR: Item was not found")
  else: 
    errorcode = random.randint(0, 9999) # yes i know this is useless its just a place holder
    await client.send_message(message.channel, "ERROR: Unknown error code "+ errorcode)

@client.event
async def on_ready():
  print('Logged in as: %s#%s' % (client.user.name, client.user.id))

if __name__ == '__main__':
    client.run('x', 'x')
