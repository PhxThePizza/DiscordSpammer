import discord

TOKEN = input("Discord token: ")
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        x = input("What do you want to send? ")
        for guild in self.guilds:
            try:
                for text_channel in guild.text_channels:
                    try:
                        await text_channel.send(f"{x}")
                        print(f'Message sent to {guild.name}')
                    except Exception as e:
                        print(f'Error sending message to {guild.name}: {e}')
            except Exception as e:
                print(f'Error processing guild {guild.name}: {e}')
        await self.close()
client = MyClient()
client.run(TOKEN)