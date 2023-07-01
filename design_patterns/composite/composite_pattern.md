# Composite Pattern

Object inside an object.

Break a problem into Tree like structure.

Create the tree like structure with Interfaces.

# Example

![File System Tree structure](../../images/file_system.png)

```python

from composite.directory import Directory
from composite.file import File


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


```

# Use cases

1. Design File System
2. Design Calculator

