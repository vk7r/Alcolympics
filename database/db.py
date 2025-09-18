import os
from tinydb import TinyDB, Query
from datetime import datetime

# Initialize database with absolute path
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, 'data')
os.makedirs(data_dir, exist_ok=True)
db_path = os.path.join(data_dir, 'game.json')
db = TinyDB(db_path)
Player = Query()

# ----------------------------
# CRUD Operations
# ----------------------------

def add_player(name, klunkar_druckna=0, klunkar_givna=0, Ws=0, Ls=0, games_played=0):
    """Add a new player entry for today. Name+Date must be unique."""
    today = datetime.today().strftime('%Y-%m-%d')
    if db.search((Player.name == name) & (Player.date == today)):
        print(f"Player '{name}' already has an entry today.")
        return False

    player = {
        "name": name,
        "klunkar_druckna": klunkar_druckna,
        "klunkar_givna": klunkar_givna,
        "Ws": Ws,
        "Ls": Ls,
        "games_played": games_played,
        "date": today
    }
    db.insert(player)
    return True

def get_player(name, date=None):
    """Get a player entry for a specific date (default today)."""
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')
    result = db.search((Player.name == name) & (Player.date == date))
    return result[0] if result else None

def get_player_history(name):
    """Get all entries for a player across dates."""
    return db.search(Player.name == name)

def update_player(name, date=None, klunkar_druckna=None, klunkar_givna=None, Ws=None, Ls=None, games_played=None):
    """Update stats for a player on a specific date (default today)."""
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')
    player = get_player(name, date)
    if not player:
        print(f"No entry for '{name}' on {date}.")
        return False

    updates = {}
    if klunkar_druckna is not None:
        updates["klunkar_druckna"] = klunkar_druckna
    if klunkar_givna is not None:
        updates["klunkar_givna"] = klunkar_givna
    if Ws is not None:
        updates["Ws"] = Ws
    if Ls is not None:
        updates["Ls"] = Ls
    if games_played is not None:
        updates["games_played"] = games_played

    if updates:
        db.update(updates, (Player.name == name) & (Player.date == date))
        return True
    return False

def delete_player(name, date=None):
    """Delete a player entry for a specific date (default today)."""
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')
    if db.search((Player.name == name) & (Player.date == date)):
        db.remove((Player.name == name) & (Player.date == date))
        return True
    return False

# ----------------------------
# Helper / Game API Functions
# ----------------------------

def player_exists(name, date=None):
    """Check if player has an entry for a specific date."""
    return get_player(name, date) is not None

def increment_stats(name, klunkar_druckna=0, klunkar_givna=0, Ws=0, Ls=0, games_played=0, date=None):
    """Increment stats for a player on a specific date."""
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')
    player = get_player(name, date)
    if not player:
        print(f"No entry for '{name}' on {date}. Cannot increment.")
        return False

    new_stats = {
        "klunkar_druckna": player["klunkar_druckna"] + klunkar_druckna,
        "klunkar_givna": player["klunkar_givna"] + klunkar_givna,
        "Ws": player["Ws"] + Ws,
        "Ls": player["Ls"] + Ls,
        "games_played": player.get("games_played", 0) + games_played
    }
    db.update(new_stats, (Player.name == name) & (Player.date == date))
    return True

def reset_player_stats(name, date=None):
    """Reset stats for a player on a specific date (default today)."""
    return update_player(name, date, klunkar_druckna=0, klunkar_givna=0, Ws=0, Ls=0, games_played=0)

# ----------------------------
# Leaderboard / Stats Functions
# ----------------------------

def all_entries():
    """Return all player entries in DB."""
    return db.all()

def total_stats_for_player(name):
    """Aggregate stats across all entries for a player."""
    entries = get_player_history(name)
    totals = {"klunkar_druckna": 0, "klunkar_givna": 0, "Ws": 0, "Ls": 0, "games_played": 0}
    for p in entries:
        totals["klunkar_druckna"] += p["klunkar_druckna"]
        totals["klunkar_givna"] += p["klunkar_givna"]
        totals["Ws"] += p["Ws"]
        totals["Ls"] += p["Ls"]
        totals["games_played"] += p.get("games_played", 0)
    return totals

def leaderboard_by_wins(top_n=10):
    """Return top N players by total wins (aggregated across all dates)."""
    players = {}
    for entry in db.all():
        name = entry["name"]
        players[name] = players.get(name, 0) + entry["Ws"]
    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
    return sorted_players[:top_n]

def leaderboard_by_klunkar_druckna(top_n=10):
    """Return top N players by total klunkar druckna."""
    players = {}
    for entry in db.all():
        name = entry["name"]
        players[name] = players.get(name, 0) + entry["klunkar_druckna"]
    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
    return sorted_players[:top_n]

def leaderboard_by_games_played(top_n=10):
    """Return top N players by total games played."""
    players = {}
    for entry in db.all():
        name = entry["name"]
        players[name] = players.get(name, 0) + entry.get("games_played", 0)
    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
    return sorted_players[:top_n]

def show_all_time_goat():
    """Return the player who is the all-time GOAT (highest klunkar_druckna)."""
    players = {}
    for entry in db.all():
        name = entry["name"]
        players[name] = players.get(name, 0) + entry["klunkar_druckna"]
    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
    return sorted_players[0] if sorted_players else None

def entries_today():
    """Return all player entries added today."""
    today = datetime.today().strftime('%Y-%m-%d')
    return [p for p in db.all() if p["date"] == today]

def top_players_today_by_wins(top_n=10):
    """Top players by wins today only."""
    today_entries = entries_today()
    players = {}
    for entry in today_entries:
        name = entry["name"]
        players[name] = players.get(name, 0) + entry["Ws"]
    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
    return sorted_players[:top_n]
