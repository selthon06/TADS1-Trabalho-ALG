def listar_eventos():
    print('\n--- Lista de Eventos ---')
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    for idx, evento in enumerate(eventos, start=1):
        print(f"{idx}. Nome: {evento['nome']} | Data: {evento['data']} | Tema: {evento['tema']} | Participantes: {len(evento['participantes'])}")