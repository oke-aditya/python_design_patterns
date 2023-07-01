from composite.base_file_system import BaseFileSystem


class Directory(BaseFileSystem):
    def __init__(self, name: str) -> None:
        self.directory_name = name
        self.file_system: list[BaseFileSystem] = []

    def add(self, file: BaseFileSystem) -> None:
        self.file_system.append(file)

    def ls(self) -> None:
        print(f"{self.directory_name} /")
        for file in self.file_system:
            file.ls()
