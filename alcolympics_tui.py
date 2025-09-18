import sys
import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text
from rich.prompt import Confirm

# Import database functions
sys.path.append(os.path.join(os.path.dirname(__file__), 'database'))
import database.db as db

console = Console()

# Global list to store current game session players
current_players = []

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
                          choices=["1", "2", "3"], default="1")
        if choice == "1":
            start_playing()
            break
        elif choice == "2":
            view_leaderboard()
            break
        elif choice == "3":
            console.print("\n[bold hot_pink3]Thanks for playing! Goodbye! 🍻[/bold hot_pink3]\n")
            sys.exit()

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
    
    # Start main game loop
    main_game_loop()

def add_players():
    """Add players to the current game session"""
    global current_players
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
    
    current_players = []
    while True:
        if current_players:
            player_list = ", ".join(current_players)
            console.print(f"\n[bold hot_pink3]Current players:[/bold hot_pink3] {player_list}")
        
        name = Prompt.ask("\n[bold hot_pink3]Enter player name (or 'done' to finish)[/bold hot_pink3]")
        
        if name.lower() == 'done':
            if len(current_players) < 1:
                console.print("[bold red]You need at least 1 player to start![/bold red]")
                continue
            break
        
        if name and name not in current_players:
            current_players.append(name)
            # Add player to database if they don't exist today
            try:
                db.add_player(name)
                console.print(f"[green]✓ Added {name}[/green]")
            except:
                console.print(f"[yellow]⚠ {name} already exists in today's database[/yellow]")
        elif name in current_players:
            console.print("[red]Player already added![/red]")
    
    console.print(f"\n[bold green]✓ {len(current_players)} players ready to play![/bold green]")
    time.sleep(2)

def game_selection_menu():
    """Display available games menu"""
    console.clear()
    
    games_menu = """
    
    ╔════════════════════════════════════════════╗
    ║                                            ║
    ║           [bold cyan]1.[/bold cyan]  BEER PONG                    ║
    ║                                            ║
    ║           [bold cyan]2.[/bold cyan]  FLIP CUP                     ║
    ║                                            ║
    ║           [bold cyan]3.[/bold cyan]  KINGS CUP                    ║
    ║                                            ║
    ║           [bold cyan]4.[/bold cyan]  NEVER HAVE I EVER           ║
    ║                                            ║
    ║           [bold cyan]5.[/bold cyan]  BACK TO MAIN MENU           ║
    ║                                            ║
    ╚════════════════════════════════════════════╝
    
    """
    
    games_panel = Panel(
        Align.center(
            games_menu,
            vertical="middle"
        ),
        title="[bold hot_pink3]═══ SELECT GAME ═══[/bold hot_pink3]",
        border_style="hot_pink3",
        width=70,
        height=20,
        padding=(2, 5),
        style="on grey11"
    )
    
    # Show current players
    if current_players:
        player_list = ", ".join(current_players)
        console.print(f"\n[bold hot_pink3]Players:[/bold hot_pink3] {player_list}\n")
    
    console.print(games_panel, justify="center")
    
    while True:
        choice = Prompt.ask("[bold hot_pink3]>>> Select a game (1-5)[/bold hot_pink3]", 
                          choices=["1", "2", "3", "4", "5"], default="1")
        
        if choice == "1":
            play_game("Beer Pong")
            break
        elif choice == "2":
            play_game("Flip Cup")
            break
        elif choice == "3":
            play_game("Kings Cup")
            break
        elif choice == "4":
            play_game("Never Have I Ever")
            break
        elif choice == "5":
            return False  # Return to main menu
    
    return True  # Continue game loop

def play_game(game_name):
    """Play the selected game"""
    console.clear()
    
    console.print(Panel(
        Align.center(
            f"\n[bold hot_pink3]🎮 {game_name.upper()} 🎮[/bold hot_pink3]\n\n"
            f"[bold]Now playing: {game_name}[/bold]\n\n"
            f"[bold hot_pink3]Players:[/bold hot_pink3] {', '.join(current_players)}\n\n"
            "[dim](Game implementation coming soon...)[/dim]\n\n"
            "[bold]For now, manually update player stats![/bold]\n",
            vertical="middle"
        ),
        border_style="hot_pink3",
        width=80,
        height=15,
        padding=(2, 5),
        style="on grey11"
    ), justify="center")
    
    # Simulate game play - for now just increment games played
    for player in current_players:
        try:
            db.increment_stats(player, games_played=1)
        except:
            pass
    
    console.print("\n[bold green]✓ Game completed! Stats updated.[/bold green]")
    
    # Ask if they want to play another game
    play_again = Confirm.ask("\n[bold hot_pink3]Play another game?[/bold hot_pink3]")
    return play_again

def main_game_loop():
    """Main game loop - add players then game selection"""
    global current_players
    
    while True:
        # First, add players if none exist
        if not current_players:
            add_players()
        
        # Game selection menu
        continue_playing = game_selection_menu()
        
        if not continue_playing:
            # Ask if they want to start a new session or return to main menu
            new_session = Confirm.ask("\n[bold hot_pink3]Start a new game session?[/bold hot_pink3]")
            if new_session:
                current_players = []  # Reset players
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
    table.add_column("GAMES", style="bold", justify="center", width=15)
    table.add_column("DRINKS", style="bold cyan", justify="center", width=15)
    
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
            leaderboard.append((rank_display, name, str(wins), str(games), str(drinks)))
    
    except Exception as e:
        # Fallback to placeholder data if database is empty or has issues
        leaderboard = [
            ("🥇 1st", "Alice", "42", "7", "15"),
            ("🥈 2nd", "Bob", "37", "6", "12"),
            ("🥉 3rd", "Charlie", "29", "5", "10"),
            ("  4th", "David", "24", "4", "8"),
            ("  5th", "Eve", "18", "3", "6"),
        ]
    
    if not leaderboard:
        leaderboard = [("--", "No players yet!", "0", "0", "0")]
    
    for rank, name, wins, games, drinks in leaderboard:
        table.add_row(rank, name, wins, games, drinks)
    
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