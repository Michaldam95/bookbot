import stats
import sys


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    content = get_book_text(path_to_book)
    word_co = stats.word_count(content)
    letter_co = stats.letter_count(content)
    stats.print_report(word_co, letter_co, path_to_book)

main()