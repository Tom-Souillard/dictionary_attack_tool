### English Version

# Dictionary Attack Tool

Welcome to the `dictionary_attack_tool` project. This professional-grade Python tool is designed to perform dictionary attacks on password hashes using the powerful Hashcat engine. It includes comprehensive scripts and utilities to facilitate efficient and effective dictionary attacks for security testing purposes.

## Features

- Perform dictionary attacks on password hashes
- Utilize Hashcat for efficient password cracking
- Generate sample wordlists for testing
- Load and manage wordlists and hash files
- Easy to extend and customize

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Tom-Souillard/dictionary_attack_tool.git
    cd dictionary_attack_tool
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install the package in editable mode**:
    ```bash
    pip install -e .
    ```

5. **Install Hashcat**:
    - On Debian/Ubuntu:
      ```bash
      sudo apt-get install hashcat
      ```

## Usage

### Generate a Sample Wordlist

Generate a sample wordlist with a specified number of words:

```bash
generate_wordlist wordlist.txt 10
```

- **Output**: A file named `wordlist.txt` containing 10 sample words.

### Run a Dictionary Attack

Run a dictionary attack using a specified hash file and wordlist:

```bash
run_dictionary_attack hash.txt wordlist.txt
```

- **Input**:
  - `hash.txt`: Path to the file containing the password hash.
  - `wordlist.txt`: Path to the wordlist file.
- **Output**: The result of the dictionary attack, including any discovered passwords.

### Run Unit Tests

To ensure everything is working correctly, run the unit tests provided with the project:

```bash
pytest
```

- **Output**: Results of the tests, indicating pass or fail status for each test case.

## Documentation

For detailed usage and customization instructions, please refer to the [documentation](docs/USAGE.md).

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting a pull request.

---

<p>&nbsp;</p>
<p>&nbsp;</p>

### French Version

# Outil d'Attaque par Dictionnaire

Bienvenue dans le projet `dictionary_attack_tool`. Cet outil Python de qualité professionnelle est conçu pour effectuer des attaques par dictionnaire sur des hashes de mots de passe en utilisant le puissant moteur Hashcat. Il comprend des scripts et des utilitaires complets pour faciliter des attaques par dictionnaire efficaces à des fins de tests de sécurité.

## Fonctionnalités

- Effectuer des attaques par dictionnaire sur des hashes de mots de passe
- Utiliser Hashcat pour un craquage de mot de passe efficace
- Générer des listes de mots de test
- Charger et gérer des listes de mots et des fichiers de hash
- Facile à étendre et à personnaliser

## Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)

### Étapes

1. **Cloner le dépôt** :
    ```bash
    git clone https://github.com/Tom-Souillard/dictionary_attack_tool.git
    cd dictionary_attack_tool
    ```

2. **Créer et activer un environnement virtuel** (optionnel mais recommandé) :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    ```

3. **Installer les packages Python requis** :
    ```bash
    pip install -r requirements.txt
    ```

4. **Installer le package en mode édition** :
    ```bash
    pip install -e .
    ```

5. **Installer Hashcat** :
    - Sur Debian/Ubuntu :
      ```bash
      sudo apt-get install hashcat
      ```

## Utilisation

### Générer une Liste de Mots de Test

Générer une liste de mots de test avec un nombre spécifié de mots :

```bash
generate_wordlist wordlist.txt 10
```

- **Sortie** : Un fichier nommé `wordlist.txt` contenant 10 mots de test.

### Lancer une Attaque par Dictionnaire

Lancer une attaque par dictionnaire en utilisant un fichier de hash et une liste de mots spécifiés :

```bash
run_dictionary_attack hash.txt wordlist.txt
```

- **Entrée** :
  - `hash.txt` : Chemin vers le fichier contenant le hash du mot de passe.
  - `wordlist.txt` : Chemin vers le fichier de la liste de mots.
- **Sortie** : Le résultat de l'attaque par dictionnaire, incluant tous les mots de passe découverts.

### Exécuter les Tests Unitaires

Pour s'assurer que tout fonctionne correctement, exécutez les tests unitaires fournis avec le projet :

```bash
pytest
```

- **Sortie** : Résultats des tests, indiquant le statut de réussite ou d'échec de chaque cas de test.

## Documentation

Pour des instructions détaillées sur l'utilisation et la personnalisation, veuillez consulter la [documentation](docs/USAGE.md).

## Licence

Ce projet est sous licence Apache License 2.0. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contribuer

Les contributions sont les bienvenues ! Veuillez lire les lignes directrices de [CONTRIBUTING](CONTRIBUTING.md) avant de soumettre une demande de tirage.