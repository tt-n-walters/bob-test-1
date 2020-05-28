import discord
import os

token = os.environ.get("token")


class Client(discord.Client):
    async def on_ready(self):
        print("Ready.")

    async def on_message(self, message):
        print(message.content)

        if not message.author == self.user:
            await message.channel.send(message.content + "?")

        if not message.author == self.user:
            if message.content == "Hello":
                await message.channel.send("@{} Hello!".format(message.author))


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')


Client().run(token)
