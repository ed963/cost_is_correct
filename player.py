from discord import User, DMChannel
from typing import Dict


class Player:
    _user_obj: User
    score: int
    guesses: Dict[int, int]

    def __init__(self, user_obj: User) -> None:
        self._user_obj = user_obj
        self.score = 0
        self.guesses = {}

    def get_name(self) -> str:
        return self._user_obj.display_name

    def record_guess(self, round_num: int, guess: int) -> None:
        self.guesses[round_num] = guess

    async def send(self, content: str) -> None:
        await self._user_obj.send(content)

    def get_dm_channel(self) -> DMChannel:
        return self._user_obj.dm_channel

    def get_id(self) -> int:
        return self._user_obj.id
