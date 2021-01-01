import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
SPECIAL_CHAR = os.getenv('SPECIAL_CHAR')
ROUNDS = int(os.getenv('ROUNDS'))
