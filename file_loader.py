from pathlib import Path


def load_file(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError("File does not exist")

    if path.suffix.lower() != ".txt":
        raise ValueError("Only .txt files are supported")

    content = path.read_text(encoding="utf-8").strip()

    if not content:
        raise ValueError("File is empty")

    return content
