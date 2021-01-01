from product import Product
from discord import Embed
from typing import List, Tuple


def get_product_embed(round_num: int, product: Product) -> Embed:
    embed = Embed(title=f'Round {round_num}', description=product.name)
    embed.set_image(url=product.img_path)
    return embed


def get_scores_embed(name_to_score: List[Tuple[str, int]]) -> Embed:
    embed = Embed(title='Scores')
    for pair in name_to_score:
        embed.add_field(name=pair[0], value=str(pair[1]), inline=False)
    return embed
