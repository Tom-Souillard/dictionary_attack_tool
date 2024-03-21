from dictionary_attack_tool.hashcat_wrapper import run_hashcat

if __name__ == "__main__":
    import sys

    if len(sys.argv) not in [3, 4]:
        print("Usage: python run_dictionary_attack.py <hash_file> <wordlist> [<rules_file>]")
    else:
        hash_file = sys.argv[1]
        wordlist = sys.argv[2]
        rules_file = sys.argv[3] if len(sys.argv) == 4 else None

        output = run_hashcat(hash_file, wordlist, rules_file)
        print(output)
