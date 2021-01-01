class Product:
    name: str
    img_path: str
    price: int

    def __init__(self, name: str, img_path: str, price: int) -> None:
        self.name = name
        self.img_path = img_path
        self.price = price
