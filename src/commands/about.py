import discord
from discord.ext import commands
class About():
	def __init__(self, client):
		@client.hybrid_command()
		async def about(ctx):
			"""Get helpful information about this bot
			"""
			response = "## 🛈 Bird Discourse - From Heliguy\n"
			response += "> I was created to fix shitty embeds that social media sites often have. I will replace a regular link you send with a better link, to make embeds actually enjoyable to interact with.\n\n"
			response += "**Supported Links:**\n"
			for link, replacement in client.targeted_links.items():
				response += f"`{link}`\n"
				
			response += f"\nMy legacy prefix is `{client.prefix}`\n"
			response += "To send a link without it being replaced, surround it with `< >`, or put `!` before it.\n"
			response += "    ex: `<https://twitter.com/thing>`\n"
			response += "    ex: `!https://twitter.com/thing`"
			await ctx.reply(response)
