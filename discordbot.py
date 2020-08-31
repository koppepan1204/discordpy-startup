import discord
from discord.ext import commands

import os
import time
import random  

bot = commands.Bot(command_prefix="!")
token = os.environ['DISCORD_BOT_TOKEN']

import ctypes
import ctypes.util
 
print("ctypes - Find opus:")
a = ctypes.util.find_library('opus')
print(a)
 
print("Discord - Load Opus:")
b = discord.opus.load_opus(a)
print(b)
 
print("Discord - Is loaded:")
c = discord.opus.is_loaded()
print(c)

@bot.command()
async def ult(ctx):
    """指定された音声ファイルを流します。"""
    voice_state = ctx.author.voice

    if (not voice_state) or (not voice_state.channel):
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return

    channel = voice_state.channel

    await channel.connect()
    print("connected to:",channel.name)
 
    rand = random.randint(1,4)
    
    if rand == 1:
        ffmpeg_audio_source = discord.FFmpegPCMAudio("phoenix.mp3")
        sleeptime = 2
    elif rand == 2:
        ffmpeg_audio_source = discord.FFmpegPCMAudio("sage.mp3")
        sleeptime = 2
    elif rand == 3:
        ffmpeg_audio_source = discord.FFmpegPCMAudio("sova.mp3")
        sleeptime = 1
    elif rand == 4:
        ffmpeg_audio_source = discord.FFmpegPCMAudio("brimstone.mp3")
        sleeptime = 7
        
    voice_client = ctx.message.guild.voice_client

    voice_client.play(ffmpeg_audio_source)
    
    time.sleep(sleeptime)
    
    await voice_client.disconnect()

bot.run(token)
