import sqlite3

def create_connection():
    conn = sqlite3.connect('expenses.db', check_same_thread=False)
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS compras_diversas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            descricao TEXT,
            valor_total REAL,
            valor_pessoa1 REAL,
            valor_pessoa2 REAL
        )
    ''');

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS compras_parceladas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            descricao TEXT,
            valor_total REAL,
            total_parcelas INTEGER,
            parcelas_pagas INTEGER,
            parcelas_restantes INTEGER,
            valor_pessoa1 REAL,
            valor_pessoa2 REAL
        )
    ''');

    conn.commit()
    conn.close()