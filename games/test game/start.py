from alcolympics_tui import GameSession, GameStats
def start_game(gamesession: GameSession):
    game_stats = {}
    for player in gamesession.players:
        game_stats[player] = GameStats()
        game_stats[player].games_played = 1
        game_stats[player].klunkar_druckna = 1
        game_stats[player].klunkar_givna = 2
        game_stats[player].Ws = 1
        game_stats[player].Ls = 0
    return game_stats
