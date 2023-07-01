from composite.directory import Directory
from composite.file import File


if __name__ == "__main__":
    games_directory = Directory("Movies")

    gta = File("gta5")
    fifa = File("fifa")

    steam_directory = Directory("Steam")
    factorio = File("factorio")
    steam_directory.add(factorio)

    games_directory.add(gta)
    games_directory.add(fifa)
    games_directory.add(steam_directory)

    games_directory.ls()
