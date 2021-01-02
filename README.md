# cost_is_correct
A Discord bot with a price guessing game.

## Getting Started

### Requirements and Dependencies

* Python 3.7 or higher
* [`discord.py`](https://github.com/Rapptz/discord.py) - Python wrapper for Discord API
```sh
# Linux/macOS
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```
* Selenium - see [documentation](https://www.selenium.dev/selenium/docs/api/py/) for detailed installation instructions
```sh
pip install -U selenium
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/ed963/cost_is_correct.git
```
2. Download a [Chrome WebDriver](https://chromedriver.chromium.org/downloads), and add the executable 'chromedriver' in the root directory.

3. Set up a Discord Bot account and invite it to the server of your choice. See this [page](https://discordpy.readthedocs.io/en/latest/discord.html) for detailed instructions.

4. Create a `.env` file in the root directory, with the following template:

```
DISCORD_TOKEN=
SPECIAL_CHAR=
ROUNDS=
```
where `DISCORD_TOKEN` represents the token of your bot, `SPECIAL_CHAR` represents a special character that prepends your bot's commands, and `ROUNDS` represents the number of rounds you would like per game.

## Usage

To log in with your Discord Bot, run
```sh
python main.py
```

Then, to start a new game, type '_SPECIAL\_CHAR_ new' into a text channel, where _SPECIAL\_CHAR_ is replaced by the special character defined in your `.env` file.

## License

Distributed under the MIT License. More information can be found in `LICENSE`.