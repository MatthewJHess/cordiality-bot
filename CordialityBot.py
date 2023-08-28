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
rows = []
update = []

description = '''description'''
#data = open("data.csv","w+") as csvfile:

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
    with open("data.csv","r+", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvreader = csv.reader(csvfile, delimiter=',')
        csvreader = list(csvreader)
        r = 0;
        n = 0; #keep track of any new entries added
        for row in csvreader:
            if csvreader[r][0] == []: break
            name = csvreader[r][0]
            score = int(csvreader[r][1])
            people[name] = people.get(name, Person(name = name, score = score))
            people[name].score = score
            print(f'{people[name].name} has {people[name].score} points')
            update.append([people[name].name,people[name].score])
            r = r+1
        old = 0
        for member in bot.get_all_members():
            name = format(member.name)
            p=0
            for person in people:
                #print(f'{name} equals {people[person].name}?')
                if name == people[person].name:
                    old = 1
                p = p+1
            people[name] = people.get(name, Person(name = name, score = 0))
            if old == 0:
                rows.append([people[format(name)].name,people[format(member.name)].score])
                update.append([people[format(name)].name,people[format(member.name)].score])
                n = 1;
            old = 0
        if n == 1: csvwriter.writerows([''] + rows)
        
@bot.command()
async def members(ctx):
    '''Server Members.'''
    x = ctx.guild.members
    for member in x:
        await ctx.send(f'{member.name} is also called {member.nick}')


@bot.command()
async def commands(ctx):
    '''Lists current commands'''
    await ctx.send(f'Current commands: !members, !cordiality <nickname>, !take <nickname>, and !reward <nickname>')

@bot.command()
async def cordiality(ctx, nick):
    '''Cordiality Point Checker'''
    x = ctx.guild.members
    for member in x:
        if nick == member.nick:
            await ctx.send(f'{member.nick} has {people[format(member.name)].score} cordiality points')
            return
        elif nick == member.name:
            await ctx.send(f'{member.name} has {people[format(member.name)].score} cordiality points')
            return
    await ctx.send(f'{nick} is not a member')
    
@bot.command()
async def reward(ctx, nick):
    '''Rewards a cordiality point'''
    x = ctx.guild.members
    error = 1
    for member in x:
        if nick == member.nick:
            print(member.nick)
            people[format(member.name)].score = people[format(member.name)].score + 1
            await ctx.send(f'Rewarding {member.nick} with 1 cordiality point. {member.nick} now has {people[format(member.name)].score} cordiality points')
            error = 0
        elif nick == member.name:
            people[format(member.name)].score = people[format(member.name)].score + 1
            await ctx.send(f'Rewarding {member.name} with 1 cordiality point. {member.name} now has {people[format(member.name)].score} cordiality points')
            error = 0
        i=0
        for row in update:
            if update[i][0] == member.name: update[i][1] = people[format(member.name)].score
            i=i+1
    if error == 1: 
            await ctx.send(f'{nick} is not a member. Please use server nickname')
            return
    with open("data.csv","w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerows(update)
        
    
    
@bot.command()
async def take(ctx, nick):
    '''Takes away a cordiality point'''
    x = ctx.guild.members
    error = 1
    for member in x:
        if nick == member.nick:
            print(member.nick)
            people[format(member.name)].score = people[format(member.name)].score - 1
            await ctx.send(f'Taking 1 cordiality point from {member.nick}. {member.nick} now has {people[format(member.name)].score} cordiality points')
            error = 0
        elif nick == member.name:
            people[format(member.name)].score = people[format(member.name)].score - 1
            await ctx.send(f'Taking 1 cordiality point from {member.name}. {member.name} now has {people[format(member.name)].score} cordiality points')
            error = 0
        i=0
        for row in update:
            if update[i][0] == member.name: update[i][1] = people[format(member.name)].score
            i=i+1
    if error == 1: 
            await ctx.send(f'{nick} is not a member. Please use server nickname')
            return
    with open("data.csv","w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerows(update)

bot.run(TOKEN)
