from discord.ext import commands, tasks
from secrets import TOKEN
import discord, os

intents = discord.Intents.default()
intents.message_content = True
prefix = "bd."
client = commands.Bot(command_prefix=prefix, intents=intents)
client.prefix = prefix

client.targeted_links = {
	"https://www.twitter.com/": "https://fxtwitter.com/",
	"https://twitter.com/": "https://fxtwitter.com/",
	"https://www.x.com/": "https://fxtwitter.com/",
	"https://x.com/": "https://fxtwitter.com/",
	
	"https://www.instagram.com/": "https://ddinstagram.com/",
	"https://instagram.com/": "https://ddinstagram.com/",
	
	"https://www.tiktok.com/": "https://vxtiktok.com/",
	"https://tiktok.com/": "https://vxtiktok.com/",
	
	"https://www.furaffinity.net/view/": "https://fxraffinity.net/view/",
	"https://furaffinity.net/view/": "https://fxraffinity.net/view/",
}

# Import all command files from the commands folder
commands_path = f"{os.path.dirname(os.path.abspath(__file__))}/commands"
for entry in os.scandir(commands_path):
	if entry.is_file():
		string = f'from commands.{entry.name[:-3]} import {entry.name[:-3].title()}'
		exec(string)
		
		# This initializes all commands to the client
		string = f'{entry.name[:-3].title()}(client)'
		exec(string)
		
async def handle_reply(new_msg, referenced_msg):
	if (
		(not referenced_msg.author == client.user)
		or (not referenced_msg.content.startswith("-# 🛈 *Message originally from:*  "))
		or (not new_msg.mentions)
	):
		return
		
	op = referenced_msg.content.split("\n")[0].replace("-# 🛈 *Message originally from:*  ", "")
	await referenced_msg.channel.send(f"{op}, {new_msg.author.display_name} responded to your post!")
	
@client.event
async def on_message(message):
	# Return immediately when the bot sees its own message
	if message.author == client.user:
		return
		
	# Ensure legacy prefix commands still work
	await client.process_commands(message)
	
	# Handle replies
	if message.reference:
		await handle_reply(message, await message.channel.fetch_message(message.reference.message_id))
		
	# Allow for links to bypass this system if a user so chooses
	if "!http" in message.content or "<http":
		return
		
	for link in client.targeted_links:
		if link in message.content:
			text = f"-# 🛈 *Message originally from:*  {message.author.mention}\n"
			await message.channel.send(text + message.content.replace(link, client.targeted_links[link]))
			await message.delete(delay=0)
			break
			
@client.event
async def on_ready():
	# await client.tree.sync()
	print(f'We have logged in as {client.user}')
	
client.run(TOKEN)
