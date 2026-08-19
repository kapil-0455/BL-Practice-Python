class Monster:
    def __init__(self , name , health , attack , reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.reward = reward

    def battle_score(self):
        return self.reward + (self.health / 10) - self.attack