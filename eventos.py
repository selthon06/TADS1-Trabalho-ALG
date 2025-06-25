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


#def remover_evento():
#    print('\n--- Remover Evento ---')
#    nome = input("Digite o nome do evento que deseja remover: ")
#    for evento in eventos:
#        if evento["nome"].lower() == nome.lower():
#            eventos.remove(evento)
#            print(f"Evento '{nome}' removido com sucesso!.")
#            return
#    print("Evento não encontrado.")


def buscar_evento_por_nome():
    print('\n--- Buscar Evento ---')
    nome = input("Digite o nome do evento: ")
    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            print(f"Nome: {evento['nome']} | Data: {evento['data']} | Tema: {evento['tema']}")
            print("Participantes:", evento["participantes"])
            return
    print("Evento não encontrado.")



def adicionar_participante_evento():
    print('\n--- Adicionar Participante a Evento ---')
    nome_evento = input("Nome do evento: ")
    try:
        codigo_part = int(input("Código do participante: "))
    except ValueError:
        print("Código inválido!")
        return

    evento_encontrado = None
    for evento in eventos:
        if evento["nome"].lower() == nome_evento.lower():
            evento_encontrado = evento
            break

    if not evento_encontrado:
        print("Evento não encontrado.")
        return

    for participante in participantes:
        if participante["codigo"] == codigo_part:
            if codigo_part not in evento_encontrado["participantes"]:
                evento_encontrado["participantes"].append(codigo_part)
                print("Participante adicionado com sucesso.")
            else:
                print("Participante já está inscrito neste evento.")
            return

    print("Participante não encontrado.")



def listar_participantes_evento():
    print('\n--- Participantes de um Evento ---')
    nome_evento = input("Digite o nome do evento: ")

    for evento in eventos:
        if evento["nome"].lower() == nome_evento.lower():
            if not evento["participantes"]:
                print("Nenhum participante inscrito nesse evento.")
                return

            print(f"Participantes do evento '{evento['nome']}':")
            for codigo in evento["participantes"]:
                # Buscar dados do participante pelo código
                participante = next((p for p in participantes if p["codigo"] == codigo), None)
                if participante:
                    print(f" - {participante['nome']} (Código: {participante['codigo']})")
                else:
                    print(f" - Participante com código {codigo} não encontrado.")
            return

    print("Evento não encontrado.")
