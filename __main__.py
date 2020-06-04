import discord
from discord.ext import commands
import os
import random

token = "NzEyOTk3ODYyMjEyMTA4MzI2.Xse-lw.qcNw4kBBQDUJceBE5G_vEeUU8HU"
# token = os.environ.get("token")
# print("Using token " + token)

bot = commands.Bot(command_prefix='$')


@bot.command()
async def test(context):
    await context.send("Hello")


@bot.command()
async def kill(context):
    await context.send("Bob is dead.")
    await bot.close()


class Client(discord.Client):
    async def on_ready(self):
        print("Ready.")
        print(self.guilds[0].roles)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "Hello":
            await message.channel.send("<@!{}> Hello!".format(message.author.id))

        for command in commands:
            if message.content.startswith(command):
                await self.command(
                    command=command,
                    guild=message.guild,
                    channel=message.channel,
                    author=message.author,
                    mentions=message.mentions,
                    content=message.content
                )
                break
        else:
            await message.channel.send(message.content + "?")

    async def command(self, **kwargs):
        command = kwargs["command"]
        guild = kwargs["guild"]
        channel = kwargs["channel"]
        author = kwargs["author"]
        if not command in commands:
            await channel.send("Invalid command")
            return
        command = commands[command]
        if command in roles:
            required_role_name = roles[command]
            required_role = self.get_role_by_name(guild, required_role_name)
        else:
            required_role = None
        if not required_role or self.check_user_role(required_role, author):
            await command(**kwargs)
        else:
            await channel.send(f"{required_role_name} required.")

    def get_role_by_name(self, guild, role_name):
        for role in guild.roles:
            print(role)
            print(type(role))
            if role.name == role_name:
                return role
        print("None found")
        return "No role found."

    def check_user_role(self, role, user):
        return user in role.members


# bob = Client()


async def kick_user(guild=None, target=None, **kwargs):
    await guild.kick(target)


async def kick_mentions(guild=None, mentions=None, **kwargs):
    for user in mentions:
        await kick_user(guild, user)


async def random_int(channel=None, **kwargs):
    await channel.send(random.randint(0, 100))


async def close(channel, **kwargs):
    await channel.send("Bob is dead.")
    await bob.logout()


commands = {
    # "&kick": kick_user,
    "&kick": kick_mentions,
    "&random": random_int,
    "&kill": close
}
roles = {
    kick_mentions: "Executioner",
}

# bob.run(token)
bot.run(token)
