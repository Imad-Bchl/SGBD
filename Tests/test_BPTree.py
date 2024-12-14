
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from BPTree import BPTree

def test_bptree():
    print("=== Tester BPTree ===")

    # Étape 1 : Créer un B+Tree avec ordre=3
    print("\nÉtape 1 : Créer un B+Tree avec ordre=3")
    arbre = BPTree(ordre=3)
    print("B+Tree initialisé.")

    # Étape 2 : Insérer des clés et des valeurs
    print("\nÉtape 2 : Insérer des clés et des valeurs")
    cles_a_inserer = [
        (10, "Enregistrement1"),
        (20, "Enregistrement2"),
        (5, "Enregistrement3"),
        (6, "Enregistrement4"),
        (12, "Enregistrement5"),
        (30, "Enregistrement6"),
        (7, "Enregistrement7"),
        (17, "Enregistrement8")
    ]
    print("\n")
    for cle, valeur in cles_a_inserer:
        arbre.inserer(cle, valeur)
        print(f"Inséré clé={cle}, valeur={valeur}")
    
    print("Root keys:", arbre.racine.keys)
    for child in arbre.racine.children:
        print("Child keys:", child.keys)

        
    

    # Étape 3 : Rechercher des clés
    print("\nÉtape 3 : Rechercher des clés dans le B+Tree")
    cles_a_rechercher = [6, 15, 17, 30, 35]
    for cle in cles_a_rechercher:
        resultat = arbre.rechercher(cle)
        if resultat:
            print(f"Clé {cle} trouvée avec les valeurs : {resultat}")
        else:
            print(f"Clé {cle} non trouvée.")
    
    
    
if __name__ == "__main__":
    test_bptree()
