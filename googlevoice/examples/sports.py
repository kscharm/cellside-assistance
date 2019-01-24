import nflgame

games = nflgame.games(2015, week=9)
for game in games:
    print(game.nice_score())