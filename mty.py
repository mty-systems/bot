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

@bot.command()
async def vote(ctx):
    embed=discord.Embed(title="Vote for mty.systems", url="https://topg.org/osu-private-servers/server-632412", color=0xfc03df)
    embed.add_field(name='How do I vote?', value='You can find the vote page by simply pressing on the Vote for mty.systems text above! Everything else should be self explanatory',  inline=False)
    embed.add_field(name='Reasons to vote', value='Thanks for your enthusiasm in our server! Voting helps our server grow so everyone will have more people to compete against and befriend!',  inline=False)
    await ctx.send(embed=embed)

@tasks.loop(seconds=30)
async def channelupdate():
    async with aiohttp.ClientSession() as sesh:
        async with sesh.get("https://osu.mty.systems/api/get_player_count") as api:
            stats2 = await api.json()

    channel = await bot.fetch_channel(putidhere);
    await channel.edit(name=f"Online users: {stats2['counts']['online']}")
    channel2 = await bot.fetch_channel(putidhere);
    await channel2.edit(name=f"Total users: {stats2['counts']['total']}")

@bot.event
async def on_ready():
    os.system('clear')
    await bot.change_presence(activity=discord.Game(name="on mty.systems!"))
    print(f'\x1b[35m\n Logged in as {bot.user}\n\x1b[0m')
    await channelupdate.start()

bot.run(TOKEN)

