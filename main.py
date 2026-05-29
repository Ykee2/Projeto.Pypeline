# main.py
def saudacao(nome: str) -> str:
    `Retorna uma saudacao segura.
    if not isinstance(nome, str):
        raise TypeError('Nome deve ser uma string')
    return f'Ola, {nome}! Bem-vindo ao sistema.'


def calcular_media(notas: list) -> float:
    Calcula a media de uma lista de notas.`
    if not notas:
        raise ValueError('Lista de notas nao pode ser vazia')
    return sum(notas) / len(notas)


if _name_ == '_main_':
    print(saudacao('Aluno FATEC'))
    print(f'Media: {calcular_media([8.5, 9.0, 7.5])}')
