import dados_participantes

def listar_participantes_com_args(*filtros):
    print('\n--- Lista de Participantes ---')
    if not dados_participantes.participantes:
        print("Nenhum participante cadastrado.")
        return

    for p in dados_participantes.participantes:
        if filtros:
            if not any(filtro.lower() in p["nome"].lower() for filtro in filtros):
                continue
        print(f"Código: {p['codigo']} | Nome: {p['nome']} | Email: {p['email']}")

def cadastrar_participante():
    print('\n--- Cadastro de Novo Participante ---')
    try:
        codigo = int(input("Código do participante: "))
    except ValueError:
        print("Código inválido.")
        return

    for p in dados_participantes.participantes:
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

    dados_participantes.participantes.append(novo_participante)
    print("Participante cadastrado com sucesso.")

def remover_participante():
    print('\n--- Remover Participante ---')
    try:
        codigo = int(input("Informe o código do participante: "))
    except ValueError:
        print("Código inválido.")
        return

    for p in dados_participantes.participantes:
        if p["codigo"] == codigo:
            dados_participantes.participantes.remove(p)
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

    for p in dados_participantes.participantes:
        if p["codigo"] == codigo:
            print(f"Nome: {p['nome']} | Email: {p['email']} | Preferências: {', '.join(p['preferencias'])}")
            return

    print("Participante não encontrado.")

def atualizar_email_participante_com_kwargs(**kwargs):
    print('\n--- Atualizar E-mail de Participante ---')
    codigo = kwargs.get("codigo")
    novo_email = kwargs.get("novo_email")

    if not isinstance(codigo, int) or not novo_email:
        print("Parâmetros inválidos.")
        return

    for p in dados_participantes.participantes:
        if p["codigo"] == codigo:
            p["email"] = novo_email
            print("E-mail atualizado com sucesso.")
            return

    print("Participante não encontrado.")