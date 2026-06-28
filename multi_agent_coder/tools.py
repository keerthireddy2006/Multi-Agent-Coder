import os

def create_folder(folder_name: str) -> str:
    os.makedirs(folder_name, exist_ok=True)
    return f"Created folder {folder_name}"

def create_file(file_path: str, content: str) -> str:
    # Auto-create parent directories if they don't exist
    parent_dir = os.path.dirname(file_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Created {file_path}"

def read_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[Errno 2] No such file or directory: '{file_path}'"

def edit_file(file_path: str, content: str) -> str:
    # Auto-create parent directories if they don't exist
    parent_dir = os.path.dirname(file_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Updated {file_path}"

def list_files(directory: str = ".") -> list[str]:
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return []