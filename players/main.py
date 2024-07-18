class Player:
    MAX_HEARTS = 3
    def __init__(self, name) -> None:
        self.name = name
        self.hearts = Player.MAX_HEARTS
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.name} {self.hearts}"
    
    def lose(self):
        if self.hearts > 1:
            self.hearts -= 1
            print(f"You lost, But you {self.hearts} more hearts")
        else:
            print("Game Over!")