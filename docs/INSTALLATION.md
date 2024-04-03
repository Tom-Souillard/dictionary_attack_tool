### English Version

# Installation Instructions

Follow these steps to install the `dictionary_attack_tool`:

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Steps

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
    - On other systems, follow the instructions on the [Hashcat website](https://hashcat.net/hashcat/).

## Verifying the Installation

To verify that the installation was successful, you can run one of the included scripts:

```bash
generate_wordlist wordlist.txt 10
```

If this command executes without errors and generates a file `wordlist.txt` with 10 words, the installation was successful.

## Running Unit Tests

To ensure everything is working correctly, you can run the unit tests:

```bash
pytest
```

---

<p>&nbsp;</p>
<p>&nbsp;</p>

#### French Version

# Instructions d'Installation

Suivez ces étapes pour installer le `dictionary_attack_tool` :

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)

## Étapes

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
    - Sur d'autres systèmes, suivez les instructions sur le site web de [Hashcat](https://hashcat.net/hashcat/).

## Vérification de l'Installation

Pour vérifier que l'installation s'est déroulée avec succès, vous pouvez exécuter l'un des scripts inclus :

```bash
generate_wordlist wordlist.txt 10
```

Si cette commande s'exécute sans erreur et génère un fichier `wordlist.txt` contenant 10 mots, l'installation a été réussie.

## Exécution des Tests Unitaires

Pour s'assurer que tout fonctionne correctement, vous pouvez exécuter les tests unitaires :

```bash
pytest
```

---

These versions of the `INSTALLATION.md` file provide comprehensive instructions for installing the `dictionary_attack_tool` project, ensuring that users can set up their environment correctly and verify the installation.