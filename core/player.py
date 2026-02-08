class Player:
    def __init__(self, user):
        self.id = user.id
        self.name = user.full_name
        self.role = None
        self.team = None
        self.alive = True
        self.vote = None
