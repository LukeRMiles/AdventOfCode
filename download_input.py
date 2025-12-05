import requests
import sys
from pathlib import Path

SESSION_FILE = Path(__file__).resolve().parent / ".aoc_session"

def get_session_token():
    if not SESSION_FILE.exists():
        raise FileNotFoundError(f"Session file not found: {SESSION_FILE}")
    return SESSION_FILE.read_text().strip()

def fetch_input(year, day):
    session = get_session_token()

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    resp = requests.get(
        url,
        cookies = {"session" : session},
        headers = {"User-Agent": "github.com/LukeRMiles/AdventOfCode by lukemiles765@gmail.com"}
    )
    resp.raise_for_status()

    folder = Path(str(year))
    if not folder.exists():
        folder.mkdir()
        init_file = folder / "__init__.py"
        init_file.write_text("")

    output_file = folder / f"day{day}_input.txt"
    output_file.write_text(resp.text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python download_input.py <year> <day>")
        sys.exit(1)

    year, day = map(int, sys.argv[1:])

    fetch_input(year, day)