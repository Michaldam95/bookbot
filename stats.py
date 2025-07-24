import string

def word_count(text: str) -> int:
    return len(text.split())

def letter_count(text: str) -> dict[str, int]:
    """
    Count occurrences of each character in the input string (case‐insensitive).
    Returns a dict mapping each character to its integer count.
    """
    lower_text = text.lower()
    letter_set = {x for x in lower_text}
    let_occure = {x: lower_text.count(x) for x in letter_set}
    return let_occure

def dict_to_str(d: dict[str: int]) -> str:
    return ", ".join(f"''{key}': {val}'" for key,val in d.items())

def print_report(word_count: int, letter_counts: dict[str, int], book_path: str):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"'Found {word_count} total words'")
    print("--------- Character Count -------")
    # Only show letters, sorted alphabetically
    for letter in sorted(string.ascii_lowercase + "æâêëô"):
        if letter in letter_counts:
            print(f"'{letter}: {letter_counts[letter]}'")
    print("============= END ===============")
    
