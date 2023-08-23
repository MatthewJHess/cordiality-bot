# bot.py
import os
import random
from token import EQUAL
from discord.ext import commands
import discord


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

description = '''description'''


class Person:
    #name = ''
    score = 0


bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    #guild = bot.user.get_guild(payload.guild_id)
    #x = ctx.guild.members
    #for member in x:
     #   await discord.ext.commands.Context.send(member.name)


@bot.command(description='For when you wanna settle the score some other way')
async def members(ctx):
    """Server Members."""
    x = ctx.guild.members
    for member in x:
        await ctx.send(member.name)


@bot.command()
async def commands(ctx):
    """Repeats a message multiple times."""
    await ctx.send(f'Current commands: !members, !cordiality <username>, !take <username>, and !reward <username>')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def cordiality(ctx, name):
    """Cordiality Point Checker"""
    x = ctx.guild.members
    for member in x:
        if name == member.name:
            await ctx.send(f'{name} has 0 cordiality points')
            return
    await ctx.send(f'{name} is not a member')
    
@bot.command()
async def reward(ctx, name):
    """Rewards a cordiality point"""
    x = ctx.guild.members
    for member in x:
        if name == member.name:
            await ctx.send(f'Rewarding {name} with one cordiality point')
            return
    await ctx.send(f'{name} is not a member')
    
@bot.command()
async def take(ctx, name):
    """Takes away a cordiality point"""
    x = ctx.guild.members
    for member in x:
        if name == member.name:
            await ctx.send(f'Taking one cordiality point from {name}')
            return
    await ctx.send(f'{name} is not a member')
    
    


#bot.run()

