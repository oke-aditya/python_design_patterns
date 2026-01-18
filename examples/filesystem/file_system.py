# Trick here is to create a Tree Like Node and structure
# Else you will set yourself up for big trap later on

# Do not think of "Files" and "Directories" as completely different things. Think of them both as Nodes.
# A Directory is a Node that holds children.
# A File is a Node that holds content/size.

# Memory Hook: "Find the Parent." If I want to create /a/b/file.txt, I need to find the node for b.

# Step C: "The Last Mile" Once you have the Parent Node (b), the logic is easy:

# Add: parent.children["file.txt"] = new Node(...)

# Delete: del parent.children["file.txt"]

# Get: return parent.children["file.txt"].size

class Node:
    def __init__(self, name, is_file=False) -> None:
        self.name = name
        self.is_file = is_file

        # for files
        self.size = 0
        self.content = ""

        # for directories
        self.children = {}


class FileSystem:
    def __init__(self) -> None:
        # Root directory /
        self.root = Node("/", is_file=False)
    
    def _traverse(self, path_parts):
        """
        Helper: Returns the Directory node containing the target file/folder.
        Input: ["root", "dir", "file1.txt"] -> Returns Node("dir")
        """
        curr = self.root
        # Go up to the last part (parent directory)
        for part in path_parts[:-1]:
            if part not in curr.children:
                curr.children[part] = Node(part, is_file=False)
            curr = curr.children[part]

            # Sanity check
            if curr.is_file:
                return False
            
        return curr
    
    def add_file(self, path, size):
        """
        Adds a file at the specified path with the given size.

        path will always be absolute, starting with / (e.g., /etc/config/test.txt).

        If the file already exists, return False.

        If the parent directories do not exist, create them automatically.

        Return True if successful.
        """

        parts = path.split('/')
        filename = path.split('/')[-1]

        parent = self._traverse(parts)
        if not parent:
            return False

        # File already exists
        if filename in parent.children:
            return False

        # Create a new file
        new_file = Node(filename, is_file=True)
        new_file.size = size
        parent.children[filename] = new_file
        return True
    
    def get_file_size(self, path):
        """
        Returns the size of the file at path as a string.

        If the file does not exist, return "" (empty string).
        
        :param self: Description
        :param path: Description
        """

        parts = path.split("/")
        file_name = path.split("/")[-1]
        parent = self._traverse(parts) 
        
        if not parent or file_name not in parent.children:
            return ""
        
        target = parent.children[file_name]
        if not target.is_file:
            return ""
        
        return str(target.size)
    
    def move_file(self, source_path: str, dest_path: str) -> bool: 
        """
        Moves a file or directory from source to destination.

        If source doesn't exist, return False.

        If destination directory doesn't exist, return False.

        If a file/dir with the same name already exists at destination, return False.

        Return True on success.
        """
        def get_parent_filename(path):
            parts = path.split("/")
            name = parts[-1]
            parent = self._traverse(parts)
            return parent, name

        src_parent, src_name = get_parent_filename(source_path)
        dest_parent, dest_name = get_parent_filename(dest_path)

        if not src_parent or src_name not in src_parent.children:
            # Source does not exist
            return False 
        

        if not dest_parent:
            # Target does not exist
            return False
        
        if not dest_name in dest_parent.children:
            # Destination already has file folder with this name
            return False
        
        # Node to move
        target_node = src_parent.children[src_name]
        target_node.name = dest_name
        dest_parent.children[dest_name] = target_node

        del src_parent.children[src_name]
        return True


    def get_largest_n(self, n: int)-> list[str] :
        """
        Returns the n largest files in the entire system formatted as "name(size)".

        If sizes are equal, sort alphabetically.
        
        """

        all_files = []
        def dfs(node, current_path):
            if node.is_file:
                all_files.append((-node.size, node.name))
            else:
                for child_name, child_node in node.children.items():
                    dfs(child_node, current_path + "/" + child_name)

        # Start collection from root
        dfs(self.root, "")
        
        # Sort: Primary key is size (desc), Secondary is name (asc)
        all_files.sort() 
        
        # Format output: "name(size)"
        result = []
        for i in range(min(n, len(all_files))):
            size = -all_files[i][0] # Flip size back to positive
            name = all_files[i][1]
            result.append(f"{name}({size})")
            
        return result

        