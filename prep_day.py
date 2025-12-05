import sys

from download_input import fetch_input
from generate import generate_file

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python prep_day.py <year> <day>")
        sys.exit(1)
    
    year, day = map(int, sys.argv[1:])

    generate_file(year, day, 1)
    generate_file(year, day, 2)
    fetch_input(year, day)
    
    print("Files created.")