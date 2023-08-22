import discord
from discord.ext import commands

class Service:
    def __init__(self, dependency):
        self.dependency = dependency

    def do_something(self):
        self.dependency.do_something_else()

class Bot(commands.Bot):
    def __init__(self, token, prefix):
        super().__init__(command_prefix=prefix)
        self.token = token
        self.services = []

    def add_service(self, service):
        self.services.append(service)

    async def on_ready(self):
        print(f'Logged in as {self.user.name}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        for service in self.services:
            service.do_something()

bot = Bot(token='MTA5NjU1MDU4ODA5Mjc4ODc5Ng.G3jMHl.j0mxKEnssalbVbV-Usvgug2l36qosPjSdmwyTY', prefix='!')
service = Service(dependency=SomeDependency())
bot.add_service(service)
bot.run(bot.token)
