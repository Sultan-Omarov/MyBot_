import discord
import time
import random

from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$ping'):
        await message.channel.send('pong(Тест)')
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$help'):
        await message.channel.send("Команды, которые доступны вам : $hello,$bye,$pass,$flipcoin")
    elif message.content.startswith('$flipcoin'):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send('Я незнаю такую команду')

client.run("Ваш токен")
