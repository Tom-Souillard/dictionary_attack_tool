import subprocess
from typing import Optional


def run_hashcat(hash_file: str, wordlist: str, rules_file: Optional[str] = None) -> str:
    """Run Hashcat with the provided parameters to perform a dictionary attack.

    Args:
        hash_file (str): The path to the hash file.
        wordlist (str): The path to the wordlist file.
        rules_file (Optional[str]): The path to the rules file, if any.

    Returns:
        str: The output from the Hashcat command.
    """
    command = ['hashcat', '-a', '0', '-m', '0', hash_file, wordlist]
    if rules_file:
        command.extend(['-r', rules_file])

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"An error occurred while running Hashcat: {e}"
