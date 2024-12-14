from BPTree import BPTree
from BPTreeNode import BPTreeNode

class Database:

    def __init__(self, name):
        self.name = name
        # Dictionnaire pour stocker les tables
        # Clé : Nom de la table, Valeur : Instance de la classe Relation
        self.tables = {}
        self.indexes = {}  # Stores indexes for each table



     # Getter pour le nom de la base de données
    def get_name(self):
        return self.name

    # Setter pour le nom de la base de données
    def set_name(self, name):
        if not name:
            raise ValueError("Le nom de la base de données ne peut pas être vide.")
        self.name = name

    # Getter pour les tables
    def get_tables(self):
        return self.tables

    # Setter pour les tables (rarement utilisé, mais disponible si nécessaire)
    def set_tables(self, tables):
        if not isinstance(tables, dict):
            raise ValueError("Les tables doivent être un dictionnaire.")
        self.tables = tables
        
        
    def create_index(self, relation, column, order):
        """CREATEINDEX command."""
        index_key = f"{relation}.{column}"
        self.indices[index_key] = BPTree(order=order)
        print(f"Index created for {relation} on column {column} with order {order}.")

    def insert_record(self, relation, column, key, record_id):
        """Insert a record into the specified index."""
        index_key = f"{relation}.{column}"
        if index_key in self.indices:
            self.indices[index_key].insert(key, record_id)
        else:
            print(f"No index found for {relation} on column {column}.")

    def select_index(self, relation, column, key):
        """SELECTINDEX command."""
        index_key = f"{relation}.{column}"
        if index_key in self.indices:
            result = self.indices[index_key].search(key)
            if result:
                print(f"Records with {column}={key}: {result}")
            else:
                print(f"No records found with {column}={key}.")
        else:
            print(f"No index found for {relation} on column {column}.")