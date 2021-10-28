
import discord
from discord.ext import commands
import random 
import json
import choice



def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix)



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f'help'))
    print('0NLINE❗')



@client.event
async def on_guild_join(guild):
      with open ('prefixes.json', 'r') as f:
            prefixes = json.load(f)
 
      prefixes[str(guild.id)] = '.'

      with open ('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
      with open ('prefixes.json', 'r') as f:
            prefixes = json.load(f)

            prefixes.pop(str(guild.id))

            with open ('prefixes.json', 'w') as f:
                  json.dump(prefixes, f, indent=4)

@client.command()
async def changeprefix(ctx, prefix):
      with open ('prefixes.json', 'r') as f:
            prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = prefix


      with open ('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

      await ctx.send(f'Prefix changed to: {prefix}')
      await ctx.message.add_reaction('❗')

@client.command()
async def K(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.message.add_reaction('❗')
    await ctx.send (f'Kicked {member.mention}')


@client.command()
async def B(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.message.add_reaction('❗')
    await ctx.send(f'Banned {member.mention}')
@client.command()
async def U(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.message.add_reaction('❗')
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction('❗')
        await ctx.send('Invaild command used type **.help** for command sheet!')
  
@client.command()
async def cls(ctx, amount=1001):
    await ctx.message.add_reaction('❗')
    await ctx.channel.purge(limit=amount)


@client.command()
async def ping(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send(f'Pong! {round (client.latency *1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def ai (ctx, *, question):
 responses = ["It is certain."
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "hmm....! yes!",
            "I SAY NO!",
            "well.. i say yes",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
 await ctx.message.add_reaction('❗')
 await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def hi(ctx):
  await ctx.message.add_reaction('❗')
  await ctx.send('Hi!, how are you')
  await ctx.send ('My name is G0_BOT')
                 


@client.command()
async def angry(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send('chill down...!!')


@client.command()
async def happy(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send('Hey! , i am happy too!!')
    await ctx.send('be happy forever!!!!!!!!')


@client.command()
async def how_to(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send('for discord bot ask the user MʀGᴏᴋᴜʟBɪɢ#9503')
    await ctx.send(
        'you just ask and tell, what name do you want for your bot and personalization!'
    )
    await ctx.send('after some time you will have a bot!!!')


@client.command()
async def sad(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send("don't worry!, be happy!")
    await ctx.send('make sure you breath in and breath out')
    await ctx.send("and erase the bad memories")


@client.command()
async def name(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send('my name is G0_BOT and made by MʀGᴏᴋᴜʟBɪɢ#9503')


@client.command()
async def spam(ctx):
    await ctx.message.add_reaction('❗')
    await ctx.send('Ok')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')
    await ctx.send('**SPAMING**')



client.run('UR API')
