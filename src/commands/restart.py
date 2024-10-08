import discord, sys
class Restart():
	def __init__(self, client):
		@client.hybrid_command()
		async def restart(ctx):
			"""Restarts the bot"""
			await ctx.reply("Restarting...")
			sys.exit()
