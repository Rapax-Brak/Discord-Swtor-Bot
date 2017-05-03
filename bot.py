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



@client.event
async def on_ready():
  print('Logged in as: %s#%s' % (client.user.name, client.user.id))

if __name__ == '__main__':
    client.run('x', 'x')
