import subprocess
from typing import Optional


def run_hashcat(hash_file: str, wordlist: str, rules_file: Optional[str] = None) -> str:
    """Run Hashcat to perform a dictionary attack on a password hash.

    Args:
        hash_file (str): The path to the file containing the password hash.
        wordlist (str): The path to the wordlist file.
        rules_file (Optional[str]): The path to the rules file for Hashcat (optional).

    Returns:
        str: The output from Hashcat.
    """
    command = ['hashcat', '-a', '0', '-m', '0', hash_file, wordlist]
    if rules_file:
        command.extend(['-r', rules_file])

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    import sys

    if len(sys.argv) not in [3, 4]:
        print("Usage: python dictionary_attack.py <hash_file> <wordlist> [<rules_file>]")
    else:
        hash_file = sys.argv[1]
        wordlist = sys.argv[2]
        rules_file = sys.argv[3] if len(sys.argv) == 4 else None

        output = run_hashcat(hash_file, wordlist, rules_file)
        print(output)
