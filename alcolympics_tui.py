import sys
import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

console = Console()

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
    ║           [bold cyan]1.[/bold cyan]  START PLAYING              ║
    ║                                            ║
    ║           [bold cyan]2.[/bold cyan]  VIEW LEADERBOARD           ║
    ║                                            ║
    ║           [bold cyan]3.[/bold cyan]  EXIT                       ║
    ║                                            ║
    ╚════════════════════════════════════════════╝
    
    """
    
    menu_panel = Panel(
        Align.center(
            menu_text,
            vertical="middle"
        ),
        title="[bold green]═══ MAIN MENU ═══[/bold green]",
        border_style="green",
        width=60,
        height=20,
        padding=(2, 5)
    )
    console.print("\n\n")
    console.print(menu_panel, justify="center")
    console.print("\n")
    
    while True:
        choice = Prompt.ask("[bold yellow]>>> Select an option (1-3)[/bold yellow]", 
                          choices=["1", "2", "3"], default="1")
        if choice == "1":
            start_playing()
            break
        elif choice == "2":
            view_leaderboard()
            break
        elif choice == "3":
            console.print("\n[bold red]Thanks for playing! Goodbye! 🍻[/bold red]\n")
            sys.exit()

def start_playing():
    console.clear()
    console.print("\n\n\n")
    console.print(Panel(
        Align.center(
            "\n\n[bold green]🎮 GAME STARTING SOON! 🎮[/bold green]\n\n"
            "[yellow]Get ready for the ultimate drinking game experience![/yellow]\n\n"
            "[dim](Feature coming soon...)[/dim]\n\n",
            vertical="middle"
        ), 
        border_style="magenta",
        width=80,
        height=15,
        padding=(2, 5)
    ), justify="center")
    time.sleep(3)
    main_menu()

def view_leaderboard():
    console.clear()
    console.print("\n\n")
    
    # Larger leaderboard table with better spacing
    table = Table(
        title="\n🏆 LEADERBOARD 🏆\n", 
        show_header=True, 
        header_style="bold blue",
        box=None,  # Remove box for cleaner look
        padding=(1, 3),  # Add padding between columns
        width=80
    )
    
    table.add_column("RANK", style="bold yellow", justify="center", width=15)
    table.add_column("PLAYER", style="bold white", justify="center", width=25)
    table.add_column("SCORE", style="bold magenta", justify="center", width=20)
    table.add_column("GAMES", style="bold cyan", justify="center", width=20)
    
    # Placeholder data with medals for top 3
    leaderboard = [
        ("🥇 1st", "Alice", "42", "7"),
        ("🥈 2nd", "Bob", "37", "6"),
        ("🥉 3rd", "Charlie", "29", "5"),
        ("  4th", "David", "24", "4"),
        ("  5th", "Eve", "18", "3"),
    ]
    
    for rank, name, score, games in leaderboard:
        table.add_row(rank, name, score, games)
    
    # Center the table in a panel
    leaderboard_panel = Panel(
        Align.center(table),
        border_style="blue",
        padding=(2, 5),
        width=100
    )
    
    console.print(leaderboard_panel, justify="center")
    console.print("\n\n[bold cyan]>>> Press Enter to return to the main menu...[/bold cyan]")
    input()
    main_menu()

if __name__ == "__main__":
    fancy_welcome()
    main_menu()