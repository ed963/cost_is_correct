from discord import User, DMChannel
from typing import Dict


class Player:
    """A class that represents a player in the game.

    === Attributes ===
    score : int
        the player's score
    guesses :  Dict[int, int]
        a dictionary mapping a round number to the player's guess for that
        round (guess is recorded in cents)
    """
    _user_obj: User
    score: int
    guesses: Dict[int, int]

    def __init__(self, user_obj: User) -> None:
        """Initialize a new Player object corresponding to the given Discord
        User.

        Parameters
        ----------
        user_obj : User
            The Discord User object corresponding to the Player
        """
        self._user_obj = user_obj
        self.score = 0
        self.guesses = {}

    def get_name(self) -> str:
        """Return the display name of this player.

        Returns
        -------
        str
            The display name of this player
        """
        return self._user_obj.display_name

    def record_guess(self, round_num: int, guess: int) -> None:
        """Record this player's guess for a given round.

        Parameters
        ----------
        round_num : int
            The round of the guess
        guess : int
            The player's guess (in cents)
        """
        self.guesses[round_num] = guess

    async def send(self, content: str) -> None:
        """Send a Discord direct message to this player.

        Parameters
        ----------
        content : str
            The contents of the message to be sent
        """
        await self._user_obj.send(content)

    def get_dm_channel(self) -> DMChannel:
        """Return the Discord direct message associated with this player.

        Returns
        -------
        DMChannel
            The Discord direct message associated with this player
        """
        return self._user_obj.dm_channel

    def get_id(self) -> int:
        """Return the unique identifier associated with this player.

        Returns
        -------
        int
            This player's unique identifier
        """
        return self._user_obj.id
