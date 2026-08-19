class Player:

    def __init__(self , name , score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score 

    def __le__(self, other):
        return self.score <= other.score

    def __str__(self):
        return self.name + " " + str(self.score)