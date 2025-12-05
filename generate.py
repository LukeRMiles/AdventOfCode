import sys
from pathlib import Path

def generate_file(year, day, part):
    folder = Path(str(year))

    if not folder.exists():
        folder.mkdir()
        init_file = folder / "__init__.py"
        init_file.write_text("")

    file_name = folder / f"day{day}_part{part}.py"

    if file_name.exists():
        print(f"File {file_name} already exists.")
        return

    template = f'''from utils import *

def solution(lines : list[str]):
    total = 0

    return total

if __name__ == "__main__":
    lines = read_input("{year}/day{day}_input.txt")

    print(solution(lines))
'''
    file_name.write_text(template)
    print(f"Created {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generator.py <year> <day> <part>")
        sys.exit(1)

    year, day, part = map(int, sys.argv[1:])

    generate_file(year, day, part)