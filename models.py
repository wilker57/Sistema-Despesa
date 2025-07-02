from database import create_connection

def add_compra_diversa(data, descricao, valor_total, valor_pessoa1, valor_pessoa2):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO compras_diversas (data, descricao, valor_total, valor_pessoa1, valor_pessoa2)
        VALUES (?, ?, ?, ?, ?)
    ''', (data, descricao, valor_total, valor_pessoa1, valor_pessoa2))
    conn.commit()
    conn.close()

def get_compras_diversas():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM compras_diversas')
    data = cursor.fetchall()
    conn.close()
    return data

def update_compra_diversa(id, data, descricao, valor_total, valor_pessoa1, valor_pessoa2):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE compras_diversas
        SET data=?, descricao=?, valor_total=?, valor_pessoa1=?, valor_pessoa2=?
        WHERE id=?
    ''', (data, descricao, valor_total, valor_pessoa1, valor_pessoa2, id))
    conn.commit()
    conn.close()

def delete_compra_diversa(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM compras_diversas WHERE id=?', (id,))
    conn.commit()
    conn.close()

def add_compra_parcelada(data, descricao, valor_total, total_parcelas, parcelas_pagas, parcelas_restantes, valor_pessoa1, valor_pessoa2):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO compras_parceladas (data, descricao, valor_total, total_parcelas, parcelas_pagas, parcelas_restantes, valor_pessoa1, valor_pessoa2)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data, descricao, valor_total, total_parcelas, parcelas_pagas, parcelas_restantes, valor_pessoa1, valor_pessoa2))
    conn.commit()
    conn.close()

def get_compras_parceladas():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM compras_parceladas')
    data = cursor.fetchall()
    conn.close()
    return data

def update_compra_parcelada(id, data, descricao, valor_total, total_parcelas, parcelas_pagas, parcelas_restantes, valor_pessoa1, valor_pessoa2):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE compras_parceladas
        SET data=?, descricao=?, valor_total=?, total_parcelas=?, parcelas_pagas=?, parcelas_restantes=?, valor_pessoa1=?, valor_pessoa2=?
        WHERE id=?
    ''', (data, descricao, valor_total, total_parcelas, parcelas_pagas, parcelas_restantes, valor_pessoa1, valor_pessoa2, id))
    conn.commit()
    conn.close()

def delete_compra_parcelada(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM compras_parceladas WHERE id=?', (id,))
    conn.commit()
    conn.close()