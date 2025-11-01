from textwrap import wrap
from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


def select_season(console: Console) -> str:
    seasons = [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
    ]

    choice_inputs = {"choice": "season",
                     "max_number": 7}

    return choose_input(console, choice_inputs, seasons)


def select_nationality(console: Console) -> str:
    countries = [
        "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK",
        "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"
    ]

    choice_inputs = {"choice": "nationality",
                     "max_number": 20}

    return choose_input(console, choice_inputs, countries)


def choose_input(console: Console, choice_inputs: dict, values) -> str:
    """
    The choice is a dictionary containing:
    - choice: str = what is being chosen (e.g., "season" or "nationality")
    - max_number: int = maximum number of choices available
    """

    choice = choice_inputs["choice"]
    max_number = choice_inputs["max_number"]

    console.print(f"\n[bold cyan]Choose {choice}:[/bold cyan]")

    formatted = " / ".join(f"[bold]{i}.[/bold] [white]{v}[/white]" for i,
                           v in enumerate(values, start=1))
    console.print(formatted)

    while True:
        try:
            console.print(f"\nGive {choice} [bold](1-{max_number})[/bold] ")
            choice = int(input("number: "))
            if 1 <= choice <= len(values):
                return values[choice - 1]
            else:
                console.print("[red]Wrong number. Please try again.[/red]")
        except ValueError:
            console.print(f"[red]Give a number between 1-{max_number}.[/red]")


def main():

    console = Console()
    season = select_season(console)
    nationality = select_nationality(console)

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    if not players:
        console.print(
            f"[bold red]Could not find players for {nationality} in season {season}.[/bold red]")
        return

    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold yellow")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    console.print(table)


if __name__ == "__main__":
    main()
