from typing import List, Tuple, Dict
from player import Player
from product import Product
from product_extractor import get_product_info
from discord import User
from constants import ROUNDS


class Game:
    players: List[Player]
    products: List[Product]

    def __init__(self) -> None:
        self.players = []
        self.products = []
        product_info = get_product_info(ROUNDS)
        for tup in product_info:
            self.products.append(Product(*tup))

    def add_player(self, user: User) -> bool:
        if user.id not in {player.get_id() for player in self.players}:
            self.players.append(Player(user))
            return True
        else:
            return False

    def has_players(self) -> bool:
        return len(self.players) > 0

    def get_scores(self) -> List[Tuple[str, int]]:
        names_and_scores = []
        for player in self.players:
            names_and_scores.append((player.get_name(), player.score))
        names_and_scores.sort(reverse=True, key=lambda x: x[1])
        return names_and_scores

    def update_scores(self, round_num: int) -> None:
        answer = self.products[round_num].price
        for player in self.players:
            if round_num in player.guesses:
                player.score += self._calculate_score(player.guesses[round_num], answer)

    def _calculate_score(self, guess: int, answer: int) -> int:
        if guess == answer:
            return 200
        else:
            return max(100 - (abs(answer - guess) * 100) // answer, 0)

    def reset_game(self) -> None:
        self.products.clear()
        product_info = get_product_info(ROUNDS)
        for tup in product_info:
            self.products.append(Product(*tup))
        for player in self.players:
            player.score = 0
            player.guesses.clear()
