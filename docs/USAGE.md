### English Version

# Usage Instructions

Follow these steps to use the `dictionary_attack_tool`:

## Generate a Sample Wordlist

Generate a sample wordlist with a specified number of words:

```bash
generate_wordlist wordlist.txt 10
```

- **Output**: A file named `wordlist.txt` containing 10 sample words.

## Run a Dictionary Attack

Run a dictionary attack using a specified hash file and wordlist:

```bash
run_dictionary_attack hash.txt wordlist.txt
```

- **Input**:
  - `hash.txt`: Path to the file containing the password hash.
  - `wordlist.txt`: Path to the wordlist file.
- **Output**: The result of the dictionary attack, including any discovered passwords.

### Using Optional Rules

If you have a rules file for Hashcat, you can include it in the dictionary attack:

```bash
run_dictionary_attack hash.txt wordlist.txt rules.txt
```

- **Input**:
  - `rules.txt`: Path to the rules file.

## Run Unit Tests

To ensure everything is working correctly, run the unit tests provided with the project:

```bash
pytest
```

- **Output**: Results of the tests, indicating pass or fail status for each test case.

---

<p>&nbsp;</p>
<p>&nbsp;</p>

#### French Version

# Instructions d'Utilisation

Suivez ces étapes pour utiliser le `dictionary_attack_tool` :

## Générer une Liste de Mots de Test

Générer une liste de mots de test avec un nombre spécifié de mots :

```bash
generate_wordlist wordlist.txt 10
```

- **Sortie** : Un fichier nommé `wordlist.txt` contenant 10 mots de test.

## Lancer une Attaque par Dictionnaire

Lancer une attaque par dictionnaire en utilisant un fichier de hash et une liste de mots spécifiés :

```bash
run_dictionary_attack hash.txt wordlist.txt
```

- **Entrée** :
  - `hash.txt` : Chemin vers le fichier contenant le hash du mot de passe.
  - `wordlist.txt` : Chemin vers le fichier de la liste de mots.
- **Sortie** : Le résultat de l'attaque par dictionnaire, incluant tous les mots de passe découverts.

### Utiliser des Règles Optionnelles

Si vous avez un fichier de règles pour Hashcat, vous pouvez l'inclure dans l'attaque par dictionnaire :

```bash
run_dictionary_attack hash.txt wordlist.txt rules.txt
```

- **Entrée** :
  - `rules.txt` : Chemin vers le fichier de règles.

## Exécuter les Tests Unitaires

Pour s'assurer que tout fonctionne correctement, exécutez les tests unitaires fournis avec le projet :

```bash
pytest
```

- **Sortie** : Résultats des tests, indiquant le statut de réussite ou d'échec de chaque cas de test.

---

These versions of the `USAGE.md` file provide comprehensive instructions for using the `dictionary_attack_tool` project, ensuring that users can effectively utilize the various functionalities offered by the tool.