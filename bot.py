from discord.ext import commands

bot = commands.Bot(command_prefix='?')

bot.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'singapore'
    }
]

@bot.event
async def on_ready():
    print('Bot is ready to play music.')
    bot.load_extension('dismusic')
    
    

bot.run("ODgzMTUzNTQ2NjgwMzY1MDc3.YTFy1Q.IYkiueofwZeBahb2j1ihK_nZtYg")