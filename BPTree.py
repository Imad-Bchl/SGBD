from BPTreeNode import BPTreeNode

class BPTree:
    def __init__(self, ordre=3):
        self.ordre = ordre  # Ordre du B+Tree
        self.racine = BPTreeNode(is_feuille=True)  # Le nœud racine est initialement une feuille

    def inserer(self, cle, valeur):
        """Insère une clé et sa valeur dans le B+Tree."""
        racine = self.racine
        if len(racine.keys) == (self.ordre - 1):  # Si la racine est pleine, il faut la fractionner
            nouvelle_racine = BPTreeNode(is_feuille=False)  # Nouvelle racine qui n'est pas une feuille
            nouvelle_racine.children.append(self.racine)  # L'ancienne racine devient un enfant
            self.fractionner_enfant(nouvelle_racine, 0, self.racine)  # Fractionne l'ancienne racine
            self.racine = nouvelle_racine  # Met à jour la racine
        self._inserer_non_plein(self.racine, cle, valeur)

    def _inserer_non_plein(self, noeud, cle, valeur):
        """Insère une clé dans un nœud non plein."""
        if noeud.is_feuille:
            # Insérer dans une feuille
            i = 0
            while i < len(noeud.keys) and cle > noeud.keys[i]:
                i += 1
            if i < len(noeud.keys) and noeud.keys[i] == cle:
                # Ajouter la valeur à une clé existante
                noeud.children[i].append(valeur)
            else:
                # Insérer une nouvelle clé et sa valeur
                noeud.keys.insert(i, cle)
                noeud.children.insert(i, [valeur])
        else:
            # Insérer dans un nœud interne
            i = len(noeud.keys) - 1
            while i >= 0 and cle < noeud.keys[i]:
                i -= 1
            i += 1
            if len(noeud.children[i].keys) == (self.ordre - 1):  # Si l'enfant est plein, fractionne-le
                self.fractionner_enfant(noeud, i, noeud.children[i])
                if cle > noeud.keys[i]:
                    i += 1
            self._inserer_non_plein(noeud.children[i], cle, valeur)

    def fractionner_enfant(self, parent, index, enfant):
        """F   ractionne un nœud plein en deux."""
        if not enfant.keys:
            raise ValueError("Impossible de fractionner un nœud avec une liste de clés vide.")
    
        nouveau_noeud = BPTreeNode(is_feuille=enfant.is_feuille)
        milieu = len(enfant.keys) // 2
    
        # Enregistrer la clé médiane avant de modifier `enfant.keys`
        cle_median = enfant.keys[milieu]
    
        # Transférer les clés et les enfants au nouveau nœud
        nouveau_noeud.keys = enfant.keys[milieu + 1:]
        enfant.keys = enfant.keys[:milieu]
    
        if enfant.is_feuille:
            # Pour les feuilles, déplacer les enfants (valeurs)
            nouveau_noeud.children = enfant.children[milieu + 1:]
            enfant.children = enfant.children[:milieu]
        else:
            # Pour les nœuds internes, déplacer les enfants
            nouveau_noeud.children = enfant.children[milieu + 1:]
            enfant.children = enfant.children[:milieu + 1]
    
        # Insérer la clé médiane dans le parent
        parent.keys.insert(index, cle_median)
        parent.children.insert(index + 1, nouveau_noeud)

    def rechercher(self, cle):
        """Recherche une clé dans le B+Tree et retourne ses valeurs associées."""
        return self._rechercher(self.racine, cle)

    def _rechercher(self, noeud, cle):
        """Recherche récursive dans un nœud donné."""
        i = 0
        while i < len(noeud.keys) and cle > noeud.keys[i]:
            i += 1
        if i < len(noeud.keys) and cle == noeud.keys[i]:
            if noeud.is_feuille:
                return noeud.children[i]  # Retourne les valeurs associées
        if noeud.is_feuille:
            return None  # Clé non trouvée
        return self._rechercher(noeud.children[i], cle)
