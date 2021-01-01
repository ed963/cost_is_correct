from client import GameClient
from constants import DISCORD_TOKEN


if __name__ == '__main__':
    game_client = GameClient()
    game_client.run(DISCORD_TOKEN)
