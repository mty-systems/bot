import discord, nekos, config, random, datetime, os, requests
from discord.http import json_or_text
import aiohttp
from discord.ext import commands
from discord.ext.commands.core import command

bot = commands.Bot(command_prefix=config.prefix)
TOKEN = config.token

@bot.command()
async def test(ctx):
    await ctx.send('this works xd')

@bot.command()
async def avatar(ctx):
    embed = discord.Embed(color=0xfc03df, timestamp=datetime.datetime.utcnow())
    embed.set_author(name=ctx.author.name, url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
    embed.set_image(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def stats(ctx):
    async with aiohttp.ClientSession() as sesh:
        async with sesh.get("https://osu.mty.systems/api/get_player_count") as api:
            stats = await api.json()

    embed=discord.Embed(title="Current server stats", url="https://mty.systems/", color=0xfc03df)
    embed.add_field(name='Online usercount', value=f"{stats['counts']['online']}",  inline=False)
    embed.add_field(name='Total usercount', value=f"{stats['counts']['total']}",  inline=False)
    await ctx.send(embed=embed)   

@bot.event
async def on_ready():
    print(f'\x1b[35m\n Logged in as {bot.user}\n\x1b[0m')

bot.run(TOKEN)

