from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, HasAtLeast, Not, Or, PlaysIn

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(20, "assists"),
    #     PlaysIn("PHI")
    # )

    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )
    # Chad Ruhwedel        NYR          0  + 1  = 1
    # Zac Jones            NYR          1  + 10 = 11
    # Brennan Othmann      NYR          0  + 2  = 2
    # Matthew Robertson    NYR          0  + 0  = 0
    # Gabe Perreault       NYR          0  + 0  = 0
    # Connor Mackey        NYR          0  + 0  = 0

    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))
    # 899

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    for player in stats.matches(matcher):
        print(player)

    # William Nylander     TOR          45 + 39 = 84
    # Mitch Marner         TOR          27 + 75 = 102
    # Leon Draisaitl       EDM          52 + 54 = 106
    # Connor McDavid       EDM          26 + 74 = 100
    # Nikita Kucherov      TBL          37 + 84 = 121
    # Nathan MacKinnon     COL          32 + 84 = 116

    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("COL"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    print("----")
    for player in stats.matches(matcher):
        print(player)

    # David Pastrnak       BOS          43 + 63 = 106
    # Aleksander Barkov    FLA          20 + 51 = 71
    # Cale Makar           COL          30 + 62 = 92
    # Sam Reinhart         FLA          39 + 42 = 81
    # Nathan MacKinnon     COL          32 + 84 = 116

if __name__ == "__main__":
    main()
