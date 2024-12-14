class BPTreeNode:
    """Representation d'un noeud d'un B+Tree."""
    def __init__(self, is_feuille=False):
        self.is_feuille = is_feuille  # Indique si le noeud est une feuille
        self.keys = []          # Liste des clés
        self.children = []      # Pointeurs vers les enfants ou les valeurs (pour les feuilles)

    