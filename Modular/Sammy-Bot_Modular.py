#!/usr/bin/env python3
import discord
import asyncio
import logging
import Mod_Commands
import token
# import requests.packages.urllib3


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# requests.packages.urllib3.disable_warnings()


class BotClient(discord.Client):
    def __init__(self, *, loop=None, **options):
        super(BotClient, self).__init__(loop=loop, **options)

    async def on_ready(self):
        # server = await self.accept_invite('instantinvitecode')
        print('Logged in as {0}\nBot id={1}\nDiscord.py v{2} Async\n-------------------------'.format(
              self.user.name, self.user.id, discord.__version__))
        await self.change_presence(game=discord.Game(name='Type !$help for info'), status=None, afk=False)

    def bot_login_helper(self):
        self.run(token.Bot)

    async def on_message(self, message):
        channel = message.channel
        author = message.author
        """
        if message.content.startswith('!$test'):
            counter = 0
            tmp = await self.send_message(message.channel, 'Calculating messages...')
            async for log in self.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1
            await self.edit_message(tmp, 'You have {0} messages.'.format(counter))
        """
        if message.content.startswith('!$invite'):
            await self.send_message(message.channel, 'This is the link to invite the bot to your server, https://discordapp.com/oauth2/authorize?client_id=238052932388519936&scope=bot&permissions=3222528')
        if message.content.startswith('!$sleep'):
            await asyncio.sleep(5)
            await self.send_message(message.channel, 'Done sleeping')
        if message.content.startswith('!$help'):
            await self.send_message(message.channel, 'This is Sammy-Bot. I am currently under development and this menu will be updated as needed.\n    The current commands are: "!$invite", "!$sleep", "!$purge" "!$give roles" and "!$help"\n    Command usage:\n        1. !$invite : This is the link to invite this bot to your server\n        2. !$sleep : makes the bot unresponsive for a few seconds\n        3. !$purge :!$purge `number of messages or user to delete messages(optional)` will remove the last 100 messages/ x number of messages or @user\'s messages among last 100, requires message permissions\n        4. !$give roles :!$give roles `member, roles` , requires manage role permissions\n        5. !$help : will display this message')
        if message.content.startswith('!$Boom'):
          if author.id ==message.server.owner.id or author.id == "138116156488679425":
            if channel.permissions_for(author).manage_roles and channel.permissions_for(self).manage_roles is True:
              #messlist = yield from client.logs_from(channel)
              async for message in client.logs_from(channel, limit=500): #messlist:
                await delete_message(message)
            elif channel.permissions_for(author).manage_roles is False:
                await self.send_message(channel, "I do not have permission to blow this channel up.")
          else:
            await self.send_message("You are not allowed to do that")
        if message.content.startswith(['!$purge', '!$give roles', '!$remove roles']):
          Mod_Commands.command(self, author, message)


BotClient().bot_login_helper()
