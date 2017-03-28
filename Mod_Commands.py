#!/usr/bin/env python3

import discord

client = discord.Client()


def command(bot, author, message):
  if message.content.startswith('!$purge'):
    purge_content = message.content.strip('!$purge ')
    if channel.permissions_for(author).manage_messages and channel.permissions_for(client).manage_messages is True:
      if isinstance(purge_content[0:1], int):
        purged_content = 0
        while purge_content > 100:
          await client.purge_from(channel, 100)
          purge_content -=100
          purged_content += 100
        else:
          await client.purge_from(channel, purge_content)
          purged_content += purge_content
          purge_content = 0
          await client.send_message(channel, "{0} messages have been purged.").format(purged_content)
      # elif purge_content = member()
      else:
        await client.purge_from(channel, 100)
        await client.send_message(channel, "100 messages have been pruned")
    elif channel.permissions_for(author).manage_messages is False:
      await client.send_message(channel, "You do not have permission to delete messages.")
    else:
      await client.send_message(channel, "I do not have permission to delete messages.")
  if message.content.startswith('!$give roles'):
    if channel.permissions_for(author).manage_roles and channel.permissions_for(client).manage_roles is True:
      roles = message.content.strip('!$give roles ')
      await add_roles(roles)
      await client.send_message("Roles have been assigned")
    elif channel.permissions_for(author).manage_roles is False:
      await client.send_message(channel, "You do not have permission to assign roles.")
    else:
      await client.send_message(channel, "I do not have permission to assign roles.")
  if message.content.startswith('!$remove roles'):
    if channel.permissions_for(author).manage_roles and channel.permissions_for(client).manage_roles is True:
      roles = message.content.strip('!$remove roles ')
      await add_roles(roles)
      await client.send_message("Roles have been removed")
    elif channel.permissions_for(author).manage_roles is False:
      await client.send_message(channel, "You do not have permission to remove roles.")
    else:
      await client.send_message(channel, "I do not have permission to remove roles.")
#  if message.content.startswith('!$kill channel'):
#    await client.send_message("Are you sure you want to?")
#    killzoner = message.author
#    get_message
