class Pizza:
    def __init__(self, name: str, ingredients: [str]):
        self.name = name
        self.ingredients = ingredients

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.ingredients == other.ingredients




