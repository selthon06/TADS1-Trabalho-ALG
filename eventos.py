def listar_eventos():
    print('\n--- Lista de Eventos ---')
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    for idx, evento in enumerate(eventos, start=1):
        print(f"{idx}. Nome: {evento['nome']} | Data: {evento['data']} | Tema: {evento['tema']} | Participantes: {len(evento['participantes'])}")


def cadastrar_evento():
    print('\n--- Cadastro de Novo Evento ---')
    nome = input('Nome do evento: ')
    data = input('Data (AAAA-MM-DD): ')
    tema = input('Tema: ')

    novo_evento = {
        "nome": nome,
        "data": data,
        "tema": tema,
        "participantes": []
    }

    eventos.append(novo_evento)
    print(f"Evento '{nome}' cadastrado com sucesso!")