import discord

token = "NzEyOTk3ODYyMjEyMTA4MzI2.XsZtgw.DlSDW7PoVNYPceFv3i4akmvS0XI"


class Client(discord.Client):
    async def on_ready(self):
        print("Ready.")

    async def on_message(self, message):
        print(message)

        if not message.author == self.user:
            await message.channel.send("Hi")

        print("Message sent")


Client().run(token)
