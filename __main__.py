import discord
import os

token = os.environ.get("token")


class Client(discord.Client):
    async def on_ready(self):
        print("Ready.")

    async def on_message(self, message):
        print(message)

        if not message.author == self.user:
            await message.channel.send("Hi")

        print("Message sent")


Client().run(token)
