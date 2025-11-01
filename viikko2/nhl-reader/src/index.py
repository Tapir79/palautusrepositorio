from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


def select_season(console: Console) -> str:
    """Returns the selected season as a string."""
    seasons = [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
    ]

    choice_inputs = {"choice": "season", "max_number": 7}

    return choose_input(console, choice_inputs, seasons)


def select_nationality(console: Console) -> str:
    """Returns the selected nationality as a string."""
    countries = [
        "USA",
        "FIN",
        "CAN",
        "SWE",
        "CZE",
        "RUS",
        "SLO",
        "FRA",
        "GBR",
        "SVK",
        "DEN",
        "NED",
        "AUT",
        "BLR",
        "GER",
        "SUI",
        "NOR",
        "UZB",
        "LAT",
        "AUS",
    ]

    choice_inputs = {"choice": "nationality", "max_number": 20}

    return choose_input(console, choice_inputs, countries)


def get_number_input(console: Console, choice, max_number: int) -> int | None:
    """Ask for number input and handle invalid entries."""
    console.print(f"\nGive {choice} [bold](1-{max_number})[/bold] ")
    try:
        return int(input("number: "))
    except ValueError:
        console.print(f"[red]Give a number between 1-{max_number}.[/red]")
        return None


def validate_choice(console: Console, number: int | None, values) -> int | None:
    """Return chosen value if valid, otherwise None."""
    if number is None:
        return None
    if 1 <= number <= len(values):
        return values[number - 1]
    console.print("[red]Wrong number. Please try again.[/red]")
    return None


def insert_number(console: Console, choice, values, max_number: int) -> int | None:
    """Combines input and validation."""
    number = get_number_input(console, choice, max_number)
    return validate_choice(console, number, values)


def loop_choice(console: Console, values, choice, max_number):
    """Loops until a valid choice is made."""
    while True:
        result = insert_number(console, choice, values, max_number)
        if result is not None:
            return result


def show_choices(console: Console, values):
    """Display choices to the user."""
    formatted = " / ".join(
        f"[bold]{i}.[/bold] [white]{v}[/white]" for i, v in enumerate(values, start=1)
    )
    console.print(formatted)


def choose_input(console: Console, choice_inputs: dict, values) -> str:
    """Handle user choice flow."""
    choice = choice_inputs["choice"]
    max_number = choice_inputs["max_number"]
    console.print(f"\n[bold cyan]Choose {choice}:[/bold cyan]")
    show_choices(console, values)
    return loop_choice(console, values, choice, max_number)


def fetch_players(season: str, nationality: str):
    """Fetch players from API by season and nationality."""
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    return stats.top_scorers_by_nationality(nationality)


def create_table(season: str, nationality: str) -> Table:
    """Create a table for player stats."""
    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold yellow")
    return table


def add_players_to_table(table: Table, players):
    """Add player rows to table."""
    for p in players:
        table.add_row(p.name, p.team, str(p.goals),
                      str(p.assists), str(p.points))


def show_error(console: Console, nationality: str, season: str):
    """Display error message when no players found."""
    console.print(
        f"[bold red]Could not find players for {nationality} in season {season}.[/bold red]"
    )


def create_table_viewer(players, season: str, nationality: str, console: Console):
    """Initialize the NHL player stats viewer."""
    if not players:
        show_error(console, nationality, season)
    else:
        table = create_table(season, nationality)
        add_players_to_table(table, players)
        console.print(table)


def main():
    """Main function to run the NHL player stats viewer."""
    console = Console()
    season = select_season(console)
    nationality = select_nationality(console)
    players = fetch_players(season, nationality)
    create_table_viewer(players, season, nationality, console)


if __name__ == "__main__":
    main()
