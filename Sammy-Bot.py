#!/usr/bin/env python3
import discord
import asyncio
import logging
#import token
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

    '''
    async def example_func(self, author, message):
        await self.send_message(message.channel, "%s, how are you doing?" % author)

    async def join(self, author, message):
        join_link = message.content[len('$!join'):].strip()
        print("This is the join link -- %s" % join_link)
        self.accept_invite(join_link)
        self.send_message(message.channel, "The bot has Joined!")
    '''

    def bot_login_helper(self):
        self.run("Your token here")

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
        if message.content.startswith('!$purge'):
            purge_content = message.content[len('!$purge '):].strip()
            if channel.permissions_for(author).manage_messages and channel.permissions_for(self).manage_messages is True:
                if isinstance(purge_content[0:1], int):
                    purged_content = 0
                    while purge_content > 100:
                        await self.purge_from(channel, 100)
                        purge_content -=100
                        purged_content += 100
                    else:
                        await self.purge_from(channel, purge_content)
                        purged_content += purge_content
                        purge_content = 0
                        await self.send_message(channel, "{0} messages have been purged.").format(purged_content)
                # elif purge_content = member()
                else:
                    await self.purge_from(channel, 100)
                    await self.send_message(channel, "100 messages have been pruned")
            elif channel.permissions_for(author).manage_messages is False:
                await self.send_message(channel, "You do not have permission to delete messages.")
            else:
                await self.send_message(channel, "I do not have permission to delete messages.")
        if message.content.startswith('!$give roles'):
            if channel.permissions_for(author).manage_roles and channel.permissions_for(self).manage_roles is True:
                roles = message.content.strip('!$give roles ')
                await add_roles(roles)
                await self.send_message("Roles have been assigned")
            elif channel.permissions_for(author).manage_roles is False:
                await self.send_message(channel, "You do not have permission to assign roles.")
            else:
                await self.send_message(channel, "I do not have permission to assign roles.")
        if message.content.startswith('!$remove roles'):
            if channel.permissions_for(author).manage_roles and channel.permissions_for(self).manage_roles is True:
                roles = message.content.strip('!remove roles ')
                await remove_roles(roles)
                await self.send_message("Roles have been removed")
            elif channel.permissions_for(author).manage_roles is False:
                await self.send_message(channel, "You do not have permission to remove roles.")
            else:
                await self.send_message(channel, "I do not have permission to remove roles.")
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



BotClient().bot_login_helper()
