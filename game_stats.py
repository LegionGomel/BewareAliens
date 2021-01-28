class GameStats:
    """Statistics tracking for Alien Invasion game"""
    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start with inactive game
        self.game_active = False
        # High score, that not reset
        self.high_score = 0

    def reset_stats(self):
        """ititialize statistics, that change in a game"""
        self.ships_left = self.ai_settings.ship_limit
        self.game_active = True
        self.score = 0
        self.level = 1
