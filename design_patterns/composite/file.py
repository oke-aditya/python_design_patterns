from composite.base_file_system import BaseFileSystem


class File(BaseFileSystem):
    def __init__(self, name) -> None:
        self.name = name

    def ls(self) -> None:
        print(f"{self.name}")
