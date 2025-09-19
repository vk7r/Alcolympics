import sys
import time
import os
import importlib.util
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text
from rich.prompt import Confirm

from artifacts.BarkaOlympicsV2 import main as barka_main

# Import database functions
sys.path.append(os.path.join(os.path.dirname(__file__), 'database'))
import database.db as db

class GameSession:
    def __init__(self):
        self.players = []
        self.stats = {}

class GameStats:
    def __init__(self):
        self.klunkar_druckna = 0
        self.klunkar_givna = 0
        self.Ws = 0
        self.Ls = 0
        self.games_played = 0



console = Console()

# Global game session object
game_session = GameSession()

def discover_games():
    """Discover available games in the games folder"""
    games_folder = os.path.join(os.path.dirname(__file__), 'games')
    games = []
    
    if not os.path.exists(games_folder):
        return games
    
    for item in os.listdir(games_folder):
        game_path = os.path.join(games_folder, item)
        if os.path.isdir(game_path):
            start_file = os.path.join(game_path, 'start.py')
            if os.path.exists(start_file):
                games.append(item)
    
    return sorted(games)

def start_game(game_name):
    """Start a game by importing and running its start_game function"""
    try:
        # Path to the game's start.py file
        game_folder = os.path.join(os.path.dirname(__file__), 'games', game_name)
        start_file = os.path.join(game_folder, 'start.py')
        
        # Import the game module
        spec = importlib.util.spec_from_file_location(f"{game_name}_game", start_file)
        game_module = importlib.util.module_from_spec(spec)
        
        # Add the game folder to sys.path temporarily so the game can import other modules
        original_path = sys.path.copy()
        sys.path.insert(0, game_folder)
        
        try:
            spec.loader.exec_module(game_module)
            
            # Call the game's start_game function
            if hasattr(game_module, 'start_game'):
                game_stats = game_module.start_game(game_session)
                
                # Update the database with the game results
                if game_stats:
                    for player, stats in game_stats.items():
                        try:
                            db.increment_stats(
                                player,
                                klunkar_druckna=stats.klunkar_druckna,
                                klunkar_givna=stats.klunkar_givna,
                                Ws=stats.Ws,
                                Ls=stats.Ls,
                                games_played=stats.games_played
                            )
                        except Exception as e:
                            console.print(f"[red]Error updating stats for {player}: {e}[/red]")
                
                return True
            else:
                console.print(f"[red]Error: {game_name} doesn't have a start_game function[/red]")
                return False
                
        finally:
            # Restore original sys.path
            sys.path = original_path
            
    except Exception as e:
        console.print(f"[red]Error loading game '{game_name}': {e}[/red]")
        return False

def fancy_welcome():
    # Larger Olympic rings ASCII art with better spacing
    olympic_rings = Text(style="bold")
    
    # Add extra vertical spacing
    olympic_rings.append("\n\n")
    
    # Line 1
    olympic_rings.append("    .,::OOO::,.", "bright_blue")
    olympic_rings.append("     .,ooOOOoo,.", "black")
    olympic_rings.append("     .,::OOO::,.\n", "bright_red")

    
    # Line 2
    olympic_rings.append("    .:'         `:.", "bright_blue")
    olympic_rings.append(" .8'         `8. ", "black")
    olympic_rings.append(".:'         `:.\n", "bright_red")
    
    # Line 3
    olympic_rings.append("    :\"           \":", "bright_blue")
    olympic_rings.append(" 8\"           \"8 ", "black")
    olympic_rings.append(":\"           \":\n", "bright_red")
    
    # Line 4 (interlocking part)
    olympic_rings.append("    :,        ", "bright_blue")
    olympic_rings.append(".,:", "yellow")
    olympic_rings.append("::", "bright_blue")
    olympic_rings.append("\"\"::,.", "yellow")
    olympic_rings.append("     .,:", "green")
    olympic_rings.append("o8", "black")
    olympic_rings.append("OO::,.", "green")
    olympic_rings.append("        ,:\n", "bright_red")
    
    # Line 5 (interlocking part)
    olympic_rings.append("     :,,    ", "bright_blue")
    olympic_rings.append(".:'", "yellow")
    olympic_rings.append(" ,:", "bright_blue")
    olympic_rings.append("   8o ", "black")
    olympic_rings.append("`:. ", "yellow")
    olympic_rings.append(".:'", "green")
    olympic_rings.append(" o8   ", "black")
    olympic_rings.append(":, ", "bright_red")
    olympic_rings.append("`:.", "green")
    olympic_rings.append("    ,,:\n", "bright_red")
    
    # Line 6 (interlocking part)
    olympic_rings.append("     `^OOoo", "bright_blue")
    olympic_rings.append(":\"", "yellow")
    olympic_rings.append("O^'     ", "bright_blue")
    olympic_rings.append("`^88oo", "black")
    olympic_rings.append(":\"", "green")
    olympic_rings.append("8^'", "black")
    olympic_rings.append("     `^O\":ooOO^'\n", "bright_red")
    
    # Line 7
    olympic_rings.append("    :,           ,:", "yellow")
    olympic_rings.append(" :,", "green")
    olympic_rings.append("           ,:\n", "green")
    
    # Line 8
    olympic_rings.append("    :,,       ,,:", "yellow")
    olympic_rings.append("   :,,", "green")
    olympic_rings.append("       ,,:\n", "green")
    
    # Line 9
    olympic_rings.append("    `^Oo,,,oO^'     ", "yellow")
    olympic_rings.append("`^OOoooOO^'\n", "green")
    
    # Add extra spacing after rings
    olympic_rings.append("\n\n")
    
    # Larger drink emojis with more spacing
    drinks_art = "    🍺      🍷      🍸      🍻    "
    
    # Larger title with ASCII art
    title_art = """
╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                     ║
║     █████╗ ██╗      ██████╗ ██████╗ ██╗  ██╗   ██╗██████╗  ███╗   ███╗██████╗ ██╗ ██████╗███████╗   ║
║    ██╔══██╗██║     ██╔════╝██╔═══██╗██║  ╚██╗ ██╔╝██╔══██╗ ████╗ ████║██╔══██╗██║██╔════╝██╔════╝   ║
║    ███████║██║     ██║     ██║   ██║██║   ╚████╔╝ ██████╔╝ ██╔████╔██║██████╔╝██║██║     ███████╗   ║
║    ██╔══██║██║     ██║     ██║   ██║██║    ╚██╔╝  ██╔═══╝  ██║╚██╔╝██║██╔═══╝ ██║██║     ╚════██║   ║
║    ██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║   ██║      ██║ ╚═╝ ██║██║     ██║╚██████╗███████║   ║
║    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝╚══════╝   ║
║                                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""
    
    term_width = console.size.width
    term_height = console.size.height
    
    # Create the panel with larger padding
    panel = Panel(
        Align.center(
            olympic_rings + Text.from_markup(f"\n[center]{drinks_art}[/center]\n") + 
            Text.from_markup(f"[bold deep_pink2]{title_art}[/bold deep_pink2]"),
            vertical="middle"
        ),
        title="🥇🥇🥇 [bold hot_pink3]ALCOLYMPICS[/bold hot_pink3] 🥇🥇🥇",
        subtitle="[bold]by Alcohol Enjoyers[/bold]",
        border_style="hot_pink3",
        padding=(3, 15),
        width=term_width,
        height=term_height-1,
        style="on grey11"
    )
    
    console.clear()
    console.print(panel, justify="center")

    # Wait for any key press (not Enter) to continue
    def wait_key():
        try:
            # Unix
            import termios
            import tty
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        except (ImportError, AttributeError):
            # Windows fallback
            import msvcrt
            msvcrt.getch()

    wait_key()

def main_menu():
    console.clear()
    
    # Larger menu with better spacing
    menu_text = """
    
    ╔════════════════════════════════════════════╗
    ║                                            ║
    ║           [bold cyan]1.[/bold cyan]  START PLAYING                ║
    ║                                            ║
    ║           [bold cyan]2.[/bold cyan]  VIEW LEADERBOARD             ║
    ║                                            ║
    ║           [bold cyan]3.[/bold cyan]  EXIT                         ║
    ║                                            ║
    ╚════════════════════════════════════════════╝
    
    """
    
    menu_panel = Panel(
        Align.center(
            menu_text,
            vertical="middle"
        ),
        title="[bold hot_pink3]═══ MAIN MENU ═══[/bold hot_pink3]",
        border_style="hot_pink3",
        width=70,
        height=20,
        padding=(2, 5),
        style="on grey11"
    )
    console.print("\n\n")
    console.print(menu_panel, justify="center")
    console.print("\n")
    
    while True:
        choice = Prompt.ask("[bold hot_pink3]>>> Select an option (1-3)[/bold hot_pink3]", 
                          choices=["1", "2", "3", "-1"], show_choices=False)
        if choice == "1":
            start_playing()
            break
        elif choice == "2":
            view_leaderboard()
            break
        elif choice == "3":
            console.print("\n[bold hot_pink3]Thanks for playing! Goodbye! 🍻[/bold hot_pink3]\n")
            sys.exit()
        elif choice == "-1":
            barka_main()
            break


def start_playing():
    console.clear()
    console.print("\n\n\n")
    
    # Show initial message
    console.print(Panel(
        Align.center(
            "\n\n[bold hot_pink3]🎮 GAME STARTING SOON! 🎮[/bold hot_pink3]\n\n"
            "[bold]Get ready for the ultimate drinking game experience![/bold]\n\n",
            vertical="middle"
        ), 
        border_style="hot_pink3",
        width=80,
        height=12,
        padding=(2, 5),
        style="on grey11"
    ), justify="center")
    
    time.sleep(3)
    
    # Progress bar animation
    console.print("\n")
    loading_chars = ["🍺", "🍷", "🍸", "🍻", "🥃", "🍶"]
    for i in range(21):  # 0 to 20 for percentage
        progress = "█" * i + "░" * (20 - i)
        char = loading_chars[i % len(loading_chars)]
        percentage = i * 5
        console.clear()
        loading_text = f"[bold hot_pink3]{char} Loading... {percentage}% [{progress}][/bold hot_pink3]"
        console.print(loading_text, justify="center", end="")
        time.sleep(0.15)
    
    console.print("\n\n")
    
    # Final message
    final_panel = Panel(
        Align.center(
            "\n[bold hot_pink3]🎉 Ready to play! 🎉[/bold hot_pink3]\n\n",
            vertical="middle"
        ),
        border_style="hot_pink3",
        width=50,
        height=8,
        padding=(1, 3),
        style="on grey11"
    )
    console.clear()
    console.print(final_panel, justify="center")
    
    time.sleep(2)

    if not game_session.players:
        add_players()

    # Start main game loop
    main_game_loop()

def add_players():
    """Add players to the current game session"""
    console.clear()
    
    console.print(Panel(
        Align.center(
            "\n[bold hot_pink3]🎮 ADD PLAYERS 🎮[/bold hot_pink3]\n\n"
            "[bold]Enter player names for this game session[/bold]\n",
            vertical="middle"
        ),
        border_style="hot_pink3",
        width=70,
        height=10,
        padding=(2, 5),
        style="on grey11"
    ), justify="center")
    
    game_session.players = []
    while True:
        if game_session.players:
            player_list = ", ".join(game_session.players)
            console.print(f"\n[bold hot_pink3]Current players:[/bold hot_pink3] {player_list}")
        
        name = Prompt.ask("\n[bold hot_pink3]Enter player name (or 'done' to finish)[/bold hot_pink3]", show_choices=False)
        
        if name.lower() == 'done':
            if len(game_session.players) < 1:
                console.print("[bold red]You need at least 1 player to start![/bold red]")
                continue
            break
        
        if name and name not in game_session.players:
            game_session.players.append(name)
            # Add player to database if they don't exist today
            if (db.add_player(name)):
                console.print(f"[green]✓ Added {name}[/green]")
                game_session.stats[name] = GameStats()
            else:
                console.print(f"[yellow]⚠ {name} already exists in today's database, continuing on same stats[/yellow]")
                game_session.stats[name] = GameStats()
                # If player exists, load their stats from DB
                existing = db.get_player(name)
                if existing:
                    game_session.stats[name].klunkar_druckna = existing.get("klunkar_druckna", 0)
                    game_session.stats[name].klunkar_givna = existing.get("klunkar_givna", 0)
                    game_session.stats[name].Ws = existing.get("Ws", 0)
                    game_session.stats[name].Ls = existing.get("Ls", 0)
                    game_session.stats[name].games_played = existing.get("games_played", 0)
        elif name in game_session.players:
            console.print("[red]Player already added![/red]")
    
    console.print(f"\n[bold green]✓ {len(game_session.players)} players ready to play![/bold green]")
    time.sleep(2)

def game_selection_menu():
    """Display available games menu with dynamically discovered games"""
    console.clear()
    
    # Discover available games
    available_games = discover_games()
    console.print(f"[dim]DEBUG: Found {len(available_games)} games: {available_games}[/dim]")
    
    if not available_games:
        console.print(Panel(
            Align.center(
                "\n[bold red]❌ NO GAMES FOUND ❌[/bold red]\n\n"
                "[bold]No games were found in the games folder![/bold]\n"
                "[dim]Make sure games are properly installed in subfolders with start.py files[/dim]\n",
                vertical="middle"
            ),
            border_style="red",
            width=70,
            height=12,
            padding=(2, 5),
            style="on grey11"
        ), justify="center")
        
        input("\n[bold hot_pink3]Press Enter to return to main menu...[/bold hot_pink3]")
        return False
    
    # Build dynamic menu
    menu_text = "\n\n═════════════════════════════════════════════════════════\n\n"
    for i, game in enumerate(available_games, 1):
        # Format game name (capitalize and replace underscores with spaces)
        display_name = game.replace('_', ' ').title()
        menu_text += f"[bold cyan]{i}.[/bold cyan]  {display_name}\n\n"
    manage_option = len(available_games) + 1
    back_option = len(available_games) + 2
    menu_text += "\n\n════════════════════════════════════════════\n\n"
    menu_text += f"[bold cyan]{manage_option}.[/bold cyan]  MANAGE PLAYERS\n\n"
    menu_text += f"[bold cyan]{back_option}.[/bold cyan]  BACK TO MAIN MENU\n\n"
    menu_text += "═════════════════════════════════════════════════════════\n\n"
    
    games_panel = Panel(
        Align.center(
            menu_text,
            vertical="middle"
        ),
        title="[bold hot_pink3]═══ SELECT GAME ═══[/bold hot_pink3]",
        border_style="hot_pink3",
        width=80,
        height=30 + len(available_games) * 2,
        padding=(2, 5),
        style="on grey11"
    )
    
    # Show current players
    if game_session.players:
        player_list = ", ".join(game_session.players)
        console.print(f"\n[bold hot_pink3]Players:[/bold hot_pink3] {player_list}\n")
    
    console.print(games_panel, justify="center")
    
    # Create valid choices list
    valid_choices = [str(i) for i in range(1, len(available_games) + 3)]
    
    while True:
        choice = Prompt.ask(f"[bold hot_pink3]>>> Select a game (1-{len(available_games) + 2})[/bold hot_pink3]", 
                          choices=valid_choices, show_choices=False)
        
        choice_num = int(choice)
        
        if choice_num <= len(available_games):
            # Start the selected game
            selected_game = available_games[choice_num - 1]
            console.clear()
            console.print(f"\n[bold hot_pink3]🎮 Starting {selected_game.replace('_', ' ').title()}... 🎮[/bold hot_pink3]\n")
            time.sleep(1)
            
            success = start_game(selected_game)
            
            if success:
                console.print(f"\n[bold green]✅ {selected_game.replace('_', ' ').title()} completed successfully![/bold green]")
                console.print("[dim]Player stats have been updated in the database.[/dim]")
            else:
                console.print(f"\n[bold red]❌ Error running {selected_game.replace('_', ' ').title()}[/bold red]")
            
            time.sleep(2)
            return True
        elif choice_num == manage_option:
            manage_players()
            console.clear()
            return True
        else:
            return False

def manage_players():
    while True:
        console.clear()
        player_list = ", ".join(game_session.players) if game_session.players else "[none]"
        panel = Panel(
            Align.center(
                f"\n[bold hot_pink3]MANAGE PLAYERS[/bold hot_pink3]\n\n"
                f"[bold]Current players:[/bold] {player_list}\n\n"
                "[bold cyan]1.[/bold cyan] Add player\n"
                "[bold cyan]2.[/bold cyan] Remove player\n"
                "[bold cyan]3.[/bold cyan] Restart session (remove all)\n"
                "[bold cyan]4.[/bold cyan] Back to game menu\n",
                vertical="middle"
            ),
            border_style="hot_pink3",
            width=70,
            height=16,
            padding=(2, 5),
            style="on grey11"
        )
        console.print(panel, justify="center")
        choice = Prompt.ask("[bold hot_pink3]>>> Select an option (1-4)[/bold hot_pink3]", choices=["1","2","3","4"], show_choices=False)
        if choice == "1":
            name = Prompt.ask("[bold hot_pink3]Enter new player name[/bold hot_pink3]", show_choices=False)
            if name and name not in game_session.players:
                game_session.players.append(name)
                if db.player_exists(name):
                    console.print(f"[yellow]⚠ {name} already exists in today's database, continuing on same stats[/yellow]")
                    game_session.stats[name] = GameStats()
                    existing = db.get_player(name)
                    if existing:
                        game_session.stats[name].klunkar_druckna = existing.get("klunkar_druckna", 0)
                        game_session.stats[name].klunkar_givna = existing.get("klunkar_givna", 0)
                        game_session.stats[name].Ws = existing.get("Ws", 0)
                        game_session.stats[name].Ls = existing.get("Ls", 0)
                        game_session.stats[name].games_played = existing.get("games_played", 0)
                else:
                    game_session.stats[name] = GameStats()
                    console.print(f"[green]✓ Added {name}[/green]")
                    db.add_player(name)
            else:
                console.print("[red]Player already exists or invalid![/red]")
            time.sleep(2)
        elif choice == "2":
            if not game_session.players:
                console.print("[red]No players to remove![/red]")
                time.sleep(1)
                continue
            name = Prompt.ask("[bold hot_pink3]Enter player name to remove[/bold hot_pink3]", choices=game_session.players)
            if name in game_session.players:
                game_session.players.remove(name)
                console.print(f"[yellow]Removed {name}[/yellow]")
                time.sleep(1)
        elif choice == "3":
            confirm = Confirm.ask("[bold red]Are you sure you want to restart the session? This will remove all players![/bold red]")
            if confirm:
                game_session.players = []
                console.print("[red]Session restarted. All players removed.[/red]")
                time.sleep(1)
                add_players()
                main_game_loop()
                break
        elif choice == "4":
            if not game_session.players:
                console.print("[red]You must have at least one player to continue![/red]")
                time.sleep(1)
                continue
            break

def main_game_loop():
    """Main game loop"""
    while True:     
        # Game selection menu
        continue_playing = game_selection_menu()
        
        if not continue_playing:
            # Ask if they want to start a new session or return to main menu
            new_session = Confirm.ask("\n[bold hot_pink3]Start a new game session?[/bold hot_pink3]")
            if new_session:
                game_session.players = []  # Reset players
                add_players()
                continue
            else:
                break  # Return to main menu
    
    # Return to main menu
    main_menu()

def view_leaderboard():
    console.clear()
    console.print("\n\n")
    
    # Larger leaderboard table with better spacing
    table = Table(
        title="\n🏆 LEADERBOARD 🏆\n", 
        show_header=True, 
        header_style="bold hot_pink3",
        box=None,  # Remove box for cleaner look
        padding=(1, 3),  # Add padding between columns
        width=80
    )
    
    table.add_column("RANK", style="bold yellow", justify="center", width=15)
    table.add_column("PLAYER", style="bold white", justify="center", width=25)
    table.add_column("WINS", style="bold hot_pink3", justify="center", width=15)
    table.add_column("GAMES PLAYED", style="bold", justify="center", width=15)
    table.add_column("DRINKS TAKEN", style="bold cyan", justify="center", width=15)
    table.add_column("DATE", style="bold magenta", justify="center", width=25)
    try:
        # Get leaderboard data from database
        wins_leaderboard = db.leaderboard_by_wins(10)
        games_data = db.leaderboard_by_games_played(10)
        drinks_data = db.leaderboard_by_klunkar_druckna(10)
        
        # Convert to dictionaries for easier lookup
        games_dict = dict(games_data)
        drinks_dict = dict(drinks_data)
        
        # Create leaderboard entries
        leaderboard = []
        medals = ["🥇", "🥈", "🥉"]
        
        for i, (name, wins) in enumerate(wins_leaderboard):
            rank_display = f"{medals[i]} {i+1}" if i < 3 else f"  {i+1}"
            games = games_dict.get(name, 0)
            drinks = drinks_dict.get(name, 0)
            # Get the latest date for this player
            history = db.get_player_history(name)
            if history:
                latest_entry = max(history, key=lambda x: x["date"])
                date = latest_entry["date"]
            else:
                date = "-"
            leaderboard.append((rank_display, name, str(wins), str(games), str(drinks), date))
    
    except Exception as e:
        # Fallback to placeholder data if database is empty or has issues
        leaderboard = [
            ("🥇 1st", "Alice", "42", "7", "15", "2023-10-01"),
            ("🥈 2nd", "Bob", "37", "6", "12", "2023-09-28"),
            ("🥉 3rd", "Charlie", "29", "5", "10", "2023-09-25"),
            ("  4th", "David", "24", "4", "8", "2023-09-20"),
            ("  5th", "Eve", "18", "3", "6", "2023-09-15"),
        ]
    
    if not leaderboard:
        leaderboard = [("--", "No players yet!", "0", "0", "0", "-")]
    for rank, name, wins, games, drinks, date in leaderboard:
        table.add_row(rank, name, wins, games, drinks, date)
    
    # Center the table in a panel
    leaderboard_panel = Panel(
        Align.center(table),
        border_style="hot_pink3",
        padding=(2, 5),
        width=100,
        style="on grey11"
    )
    
    console.print(leaderboard_panel, justify="center")
    console.print("\n\n[bold hot_pink3]>>> Press Enter to return to the main menu...[/bold hot_pink3]")
    input()
    main_menu()

if __name__ == "__main__":
    fancy_welcome()
    main_menu()