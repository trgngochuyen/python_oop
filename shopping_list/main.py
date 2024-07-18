class ShoppingList():
    def __init__(self, items):
        self.items = items
    
    @classmethod
    def from_string(cls, string):
        list_of_items = [item for item in string.split(",")]
        return cls(list_of_items)