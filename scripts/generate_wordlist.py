def generate_wordlist(file_path: str, words: int) -> None:
    """Generate a sample wordlist for testing purposes.

    Args:
        file_path (str): The path to the file to save the wordlist.
        words (int): The number of words to generate.
    """
    with open(file_path, 'w') as file:
        for i in range(words):
            file.write(f"password{i}\n")
    print(f"Generated {words} sample words in {file_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python generate_wordlist.py <file_path> <words>")
    else:
        file_path = sys.argv[1]
        words = int(sys.argv[2])

        generate_wordlist(file_path, words)
