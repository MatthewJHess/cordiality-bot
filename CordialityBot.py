# bot.py
import os
import random
from re import L
from token import EQUAL
from discord.ext import commands
import discord

TOKEN = 'REDACTED'
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

description = '''description'''


class Person:
    def __init__(self, name, score):
        self.name = name
        self.score = 0
        


bot = commands.Bot(command_prefix='!', description=description, intents=intents)
people = {}
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    for member in bot.get_all_members():
        name = format(member.name)
        people[name] = people.get(name, Person(name = name, score = 0))
        print(people[format(member.name)].name)

@bot.command()
async def members(ctx):
    """Server Members."""
    x = ctx.guild.members
    for member in x:
        await ctx.send(f'{member.name} is also called {member.nick}')


@bot.command()
async def commands(ctx):
    """Lists current commands."""
    await ctx.send(f'Current commands: !members, !cordiality <nickname>, !take <nickname>, and !reward <nickname>')

@bot.command()
async def cordiality(ctx, nick):
    """Cordiality Point Checker"""
    x = ctx.guild.members
    for member in x:
        if nick == member.nick or nick == member.name:
            await ctx.send(f'{member.nick} has {people[format(member.name)].score} cordiality points')
            return
    await ctx.send(f'{nick} is not a member')
    
@bot.command()
async def reward(ctx, nick):
    """Rewards a cordiality point"""
    x = ctx.guild.members
    for member in x:
        if nick == member.nick or nick == member.name:
            people[format(member.name)].score = people[format(member.name)].score + 1
            await ctx.send(f'Rewarding {member.nick} with one cordiality point. {member.nick} now has {people[format(member.name)].score} cordiality points')
            return
    await ctx.send(f'{nick} is not a member. Please use server nickname')
    
@bot.command()
async def take(ctx, nick):
    """Takes away a cordiality point"""
    x = ctx.guild.members
    for member in x:
        if nick == member.nick or nick == member.name:
            people[format(member.name)].score = people[format(member.name)].score - 1
            await ctx.send(f'Taking one cordiality point from {member.nick}. {member.nick} now has {people[format(member.name)].score} cordiality points')
            return
    await ctx.send(f'{nick} is not a member. Please use server nickname')
    
    


bot.run(TOKEN)