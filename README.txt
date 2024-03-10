# README

Ce programme est une implémentation de l'algorithme de Pollard p-1 modifié pour factoriser les modules RSA.

## Comment exécuter le programme :

1. Assurez-vous d'avoir Python installé sur votre système.
2. Téléchargez le fichier `projet_pollard_final.py` sur votre machine.
3. Ouvrez une console ou un terminal.
4. Accédez au répertoire contenant le fichier `projet_pollard_final.py`.
5. Exécutez le programme en tapant la commande suivante :

    ```
    python projet_pollard_final.py
    ```

## Fonctionnalités du programme :

Le programme comprend les fonctionnalités suivantes :

- **Factorisation d'entiers :** La fonction `pollard` permet de factoriser un nombre entier donné en utilisant l'algorithme de Pollard p-1 modifié.

- **Tests :** Le fichier `tests.py` contient des tests unitaires pour vérifier le bon fonctionnement des fonctions implémentées.

## Exemple d'utilisation :

Voici un exemple d'utilisation du programme pour factoriser un nombre entier :

```python
from projet_pollard_final import pollard

number = 123469
factors = pollard(number)
print("Factors of", number, ":", factors)
