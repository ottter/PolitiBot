import time
import datetime

server_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
bot_prefix = '.'
discord_game_played = f'{bot_prefix}help for info'
bot_description = 'Political Shitposter'
discord_token = 'NjU3MTE3MTQ5NjEyOTk4NjU3.XfsiSw.DMYcS8Mi2uSn4j9-wHzLD6V9RJk'

startup_extensions = ['cogs.admin', 'cogs.trump', 'cogs.crypto_tracker']
