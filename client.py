import discord
from constants import SPECIAL_CHAR, ROUNDS
from asyncio import TimeoutError
from player import Player
from game import Game
import asyncio
import re
import currency_converter
import embed_creator


class GameClient(discord.Client):
    channel: discord.TextChannel
    game: Game
    started: bool

    def __init__(self):
        super().__init__()
        self.started = False

    async def on_ready(self) -> None:
        print(f'We have logged in as {self.user}')

    async def on_message(self, message: discord.Message) -> None:
        if message.author.id == self.user.id:
            return
        if message.content.startswith(f'{SPECIAL_CHAR}new') and not self.started:
            self.channel = message.channel
            await self.channel.send(
                'Setting up your game. This may take a second...')
            self.game = Game()
            await self.channel.send(
                f"Type '{SPECIAL_CHAR}join' to join the game.")
            await self.channel.send(
                f"Once all players have joined, type '{SPECIAL_CHAR}start' to start.")
        if hasattr(self, 'game') and message.channel == self.channel and message.content.startswith(SPECIAL_CHAR + 'join') and not self.started:
            if self.game.add_player(message.author):
                await self.channel.send(
                    f"{message.author.display_name} has joined the game.")
        if hasattr(self, 'game') and message.channel == self.channel and message.content.startswith(SPECIAL_CHAR + 'start') and not self.started:
            if self.game.has_players():
                self.started = True
                for i in range(ROUNDS):
                    await self._play_round(i)
                    self.game.update_scores(i)
                    await self._end_round(i)
                await self._end_game()
            else:
                await self.channel.send("Can't start a game with no players!")

    async def _play_round(self, round_num: int) -> None:
        await self.channel.send(embed=embed_creator.get_product_embed(round_num + 1, self.game.products[round_num]))
        tasks = []
        for player in self.game.players:
            tasks.append(self._record_guess(player, round_num))

        await asyncio.gather(*tasks)

    async def _record_guess(self, player: Player, round_num: int) -> None:
        await player.send(f"Enter your guess for Round {round_num + 1}.")
        await player.send("Accepted formats: 25, 3.14, 79.00")

        def check(m: discord.Message) -> bool:
            if m.channel == player.get_dm_channel() and m.author.id == player.get_id():
                if re.fullmatch(r"^\d*(\.\d\d)?$", m.content):
                    return True
            return False

        try:
            message = await self.wait_for('message', check=check, timeout=60)
        except TimeoutError:
            return

        guess = currency_converter.string_to_cents(message.content)
        player.record_guess(round_num, guess)
        await player.send(f"Your guess of {message.content} for Round {round_num + 1} has been recorded.")

    async def _end_round(self, round_num: int) -> None:
        answer = currency_converter.cents_to_string(self.game.products[round_num].price)
        await self.channel.send(f"The correct answer for Round {round_num + 1} was {answer}")
        await self.channel.send(embed=embed_creator.get_scores_embed(self.game.get_scores()))
        await asyncio.sleep(2)

    async def _end_game(self) -> None:
        names_to_scores = self.game.get_scores()
        winners = [names_to_scores[0][0]]
        for i in range(1, len(self.game.get_scores())):
            if names_to_scores[i][1] == names_to_scores[0][1]:
                winners.append(names_to_scores[i][0])
            else:
                break
        if len(winners) == 1:
            await self.channel.send(f"{winners[0]} has won the game.")
            await self.channel.send(f"{winners[0]} is fabulous.")
            await self.channel.send("""⊂_ヽ
　 ＼＼ _
　　 ＼(　•-•) F
　　　 <　⌒ヽ A
　　　/ 　 へ＼ B
　　 /　　/　＼＼ U
　　 ﾚ　ノ　　 ヽ_つ L
　　/　/ O
　 /　/| U
　(　(ヽ S
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
`ノ )　 Lﾉ
(_／""")
        else:
            winners = ''
            for name in winners:
                winners = winners + name + ', '
            winners = winners[0:-2]
            await self.channel.send(winners + " have won the game.")
            await self.channel.send(winners + " are fabulous.")
            await self.channel.send("""⊂_ヽ
　 ＼＼ _
　　 ＼(　•-•) F
　　　 <　⌒ヽ A
　　　/ 　 へ＼ B
　　 /　　/　＼＼ U
　　 ﾚ　ノ　　 ヽ_つ L
　　/　/ O
　 /　/| U
　(　(ヽ S
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
`ノ )   Lﾉ
(_／""")
        self.started = False
        self.game.reset_game()
        await self.channel.send(f"Type '{SPECIAL_CHAR}start' to start a new game with the same players.")
        await self.channel.send(f"Type '{SPECIAL_CHAR}new' to set up a new game with different players.")
