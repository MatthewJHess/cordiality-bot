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
#data = open("data.csv","w+") as csvfile:

class Person:
    def __init__(self, name, score):
        self.name = name
        self.score = 0
        
'''class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def setup_hook(self) -> None:
        # Register the persistent view for listening here.
        # Note that this does not send the view to any message.
        # In order to do this you need to first send a message with the View, which is shown below.
        # If you have the message_id you can also pass it as a keyword argument, but for this example
        # we don't have one.
        self.add_view(Person())'''
 
 
# reading csv file
#with open("data.csv","w+") as csvfile:

fields = ['Name', 'Score']
 
# data rows of csv file
rows = []
 

 
# writing to csv file
'''with open("data.csv","w+") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(rows)'''




bot = commands.Bot(command_prefix='!', description=description, intents=intents)
people = {}
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    with open("data.csv","w+") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvreader = csv.reader(csvfile, delimiter=',')
        r = 0;
        for member in bot.get_all_members():
            name = format(member.name)
            people[name] = people.get(name, Person(name = name, score = rows[format(r),1])))
            rows.append([people[format(name)].name,people[format(member.name)].score])
            r=r + 1
            #print(people[format(member.name)].name)
            print(format(r))
        csvwriter.writerows(rows)

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
    for member in x:
        if nick == member.nick:
            people[format(member.name)].score = people[format(member.name)].score + 1
            await ctx.send(f'Rewarding {member.nick} with 1 cordiality point. {member.nick} now has {people[format(member.name)].score} cordiality points')
            return
        elif nick == member.name:
            people[format(member.name)].score = people[format(member.name)].score + 1
            await ctx.send(f'Rewarding {member.name} with 1 cordiality point. {member.name} now has {people[format(member.name)].score} cordiality points')
            return
    await ctx.send(f'{nick} is not a member. Please use server nickname')
    
@bot.command()
async def take(ctx, nick):
    '''Takes away a cordiality point'''
    x = ctx.guild.members
    for member in x:
        if nick == member.nick:
            people[format(member.name)].score = people[format(member.name)].score - 1
            await ctx.send(f'Taking 1 cordiality point from {member.nick}. {member.nick} now has {people[format(member.name)].score} cordiality points')
            return
        elif nick == member.name:
            people[format(member.name)].score = people[format(member.name)].score - 1
            await ctx.send(f'Taking 1 cordiality point from {member.name}. {member.name} now has {people[format(member.name)].score} cordiality points')
            return
    await ctx.send(f'{nick} is not a member. Please use server nickname')
    
    


bot.run(TOKEN)

