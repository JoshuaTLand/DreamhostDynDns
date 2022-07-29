import discord

class MyClient(discord.Client):
    def __init__(self, alerts, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.alerts = alerts

        self.errorChannelId = 1234

    async def on_ready(self):
        errorChannel = self.get_channel(self.errorChannelId)
        
        for alert in self.alerts:
            await errorChannel.send(alert)

        await self.close()


class discordBot:

    def sendAlerts(self, alerts):
        client = MyClient(alerts)
        client.run('YOURBOTSECRET')