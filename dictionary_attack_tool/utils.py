from typing import List

def load_wordlist(file_path: str) -> List[str]:
    """Load a wordlist from a file.

    Args:
        file_path (str): The path to the wordlist file.

    Returns:
        List[str]: A list of words from the wordlist.
    """
    with open(file_path, 'r') as file:
        wordlist = [line.strip() for line in file if line.strip()]
    return wordlist

def save_hash(file_path: str, hash_str: str) -> None:
    """Save a hash to a file.

    Args:
        file_path (str): The path to the file where the hash will be saved.
        hash_str (str): The hash string to save.
    """
    with open(file_path, 'w') as file:
        file.write(hash_str)
