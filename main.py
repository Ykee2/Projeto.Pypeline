import sqlite3


def saudacao(nome: str) -> str:
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string")
    return f"Ola, {nome}! Bem-vindo ao sistema."


def calcular_media(notas: list) -> float:
    if not notas:
        raise ValueError("Lista de notas nao pode ser vazia")
    return sum(notas) / len(notas)


def buscar_usuario_vulneravel(user_id):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
    return cursor.fetchone()


if _name_ == "_main_":
    print(saudacao("Aluno FATEC"))
    print(f"Media: {calcular_media([8.5, 9.0, 7.5])}")
