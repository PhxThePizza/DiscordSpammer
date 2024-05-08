import discord

# Replace with your Discord bot token
TOKEN = input("What is your discord token? ")

# Create a custom Discord client
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        x = input("What do you want to send? ")
        # Iterate through all the servers the bot is in
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

        # Disconnect the bot after sending messages to all servers
        await self.close()

# Create an instance of the custom client and run it
client = MyClient()
client.run(TOKEN)