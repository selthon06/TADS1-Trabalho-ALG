from dados_participantes import participantes

def listar_participantes():
    print('\n--- Lista de Participantes ---')
    if not participantes:
        print("Nenhum participante cadastrado.")
        return

    for p in participantes:
        print(f"Código: {p['codigo']} | Nome: {p['nome']} | Email: {p['email']}")



def cadastrar_participante():
    print('\n--- Cadastro de Novo Participante ---')
    try:
        codigo = int(input("Código do participante: "))
    except ValueError:
        print("Código inválido.")
        return

    for p in participantes:
        if p["codigo"] == codigo:
            print("Já existe um participante com esse código.")
            return

    nome = input("Nome completo: ")
    email = input("E-mail: ")
    preferencias = input("Preferências temáticas (separadas por vírgula): ").split(',')

    novo_participante = {
        "codigo": codigo,
        "nome": nome,
        "email": email,
        "preferencias": [pref.strip() for pref in preferencias]
    }

    participantes.append(novo_participante)
    print("Participante cadastrado com sucesso.")


def remover_participante():
    print('\n--- Remover Participante ---')
    try:
        codigo = int(input("Informe o código do participante: "))
    except ValueError:
        print("Código inválido.")
        return

    for p in participantes:
        if p["codigo"] == codigo:
            participantes.remove(p)
            print("Participante removido.")
            return

    print("Participante não encontrado.")



def buscar_participante():
    print('\n--- Buscar Participante ---')
    try:
        codigo = int(input("Informe o código do participante: "))
    except ValueError:
        print("Código inválido.")
        return

    for p in participantes:
        if p["codigo"] == codigo:
            print(f"Nome: {p['nome']} | Email: {p['email']} | Preferências: {', '.join(p['preferencias'])}")
            return

    print("Participante não encontrado.")


