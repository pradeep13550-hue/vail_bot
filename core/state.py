class Player:
    def __init__(self, user):
        self.id = user.id
        self.name = user.full_name
        self.role = None
        self.team = None
        self.alive = True
        self.vote = None


class GameState:
    def __init__(self):
        self.players = {}
        self.phase = "lobby"   # lobby, night, day, voting
        self.day = 0
        self.votes = {}
        self.night_actions = {}

    def alive_players(self):
        return [p for p in self.players.values() if p.alive]
