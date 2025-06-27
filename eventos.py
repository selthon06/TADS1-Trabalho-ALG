from datetime import datetime

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


def temas_mais_frequentes():
    print('\n--- Temas mais frequentes ---')
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    temas = {}
    for evento in eventos:
        tema = evento["tema"].strip().lower()
        temas[tema] = temas.get(tema, 0) + 1

    # Ordenar por qtde (do maior para o menor)
    temas_ordenados = sorted(temas.items(), key=lambda x: x[1], reverse=True)

    for tema, qtd in temas_ordenados:
        print(f"Tema: {tema.capitalize()} | Total de eventos: {qtd}")


def participantes_mais_ativos():
    print('\n--- Participantes mais ativos ---')
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    contagem = {}

    for evento in eventos:
        for codigo in evento["participantes"]:
            contagem[codigo] = contagem.get(codigo, 0) + 1

    if not contagem:
        print("Nenhum participante inscrito em eventos.")
        return

    participantes_ordenados = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    for codigo, qtd in participantes_ordenados:
        participante = next((p for p in participantes if p["codigo"] == codigo), None)
        if participante:
            print(f"{participante['nome']} (Código: {codigo}) - {qtd} evento(s)")
        else:
            print(f"Código {codigo} - {qtd} evento(s)")


def eventos_com_poucos_participantes():
    print('\n--- Eventos com menos de 2 participantes ---')
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    encontrados = False
    for evento in eventos:
        if len(evento["participantes"]) < 2:
            print(f"- {evento['nome']} ({len(evento['participantes'])} participante(s))")
            encontrados = True

    if not encontrados:
        print("Todos os eventos têm dois ou mais participantes.")


def remover_participantes_duplicados():
    print('\n--- Remoção de participantes duplicados por evento ---')
    total_corrigidos = 0

    for evento in eventos:
        participantes_antes = len(evento["participantes"])
        # Remove duplicados usando set, mantendo a ordem
        participantes_unicos = list(dict.fromkeys(evento["participantes"]))
        evento["participantes"] = participantes_unicos
        participantes_depois = len(participantes_unicos)

        removidos = participantes_antes - participantes_depois
        if removidos > 0:
            print(f"- {evento['nome']}: {removidos} duplicata(s) removida(s)")
            total_corrigidos += removidos

    if total_corrigidos == 0:
        print("Nenhuma duplicata encontrada.")
    else:
        print(f"Total de {total_corrigidos} duplicata(s) removida(s) no sistema.")


def filtrar_eventos_por_tema():
    print('\n--- Filtrar eventos por tema ---')
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    tema_busca = input("Digite o tema para filtrar: ").strip().lower()
    encontrados = [evento for evento in eventos if evento['tema'].strip().lower() == tema_busca]

    if encontrados:
        print(f"\nEventos com tema '{tema_busca}':")
        for evento in encontrados:
            print(f"- {evento['nome']} | Data: {evento['data']}")
    else:
        print("Nenhum evento encontrado com esse tema.")


def filtrar_eventos_por_data():
    print('\n--- Filtrar eventos por faixa de datas ---')
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    try:
        data_inicio = input("Digite a data inicial (dd/mm/aaaa): ")
        data_fim = input("Digite a data final (dd/mm/aaaa): ")

        data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim, "%d/%m/%Y")

        print(f"\nEventos entre {data_inicio.date()} e {data_fim.date()}:")

        encontrados = False
        for evento in eventos:
            data_evento = datetime.strptime(evento["data"], "%d/%m/%Y")
            if data_inicio <= data_evento <= data_fim:
                print(f"- {evento['nome']} | Data: {evento['data']} | Tema: {evento['tema']}")
                encontrados = True

        if not encontrados:
            print("Nenhum evento encontrado nesse intervalo.")

    except ValueError:
        print("Formato de data inválido. Use dd/mm/aaaa.")



def atualizar_tema_evento():
    print('\n--- Atualizar Tema de Evento ---')
    nome = input("Digite o nome do evento: ").strip()
    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            novo_tema = input("Digite o novo tema: ").strip()
            evento["tema"] = novo_tema
            print("Tema atualizado com sucesso.")
            return
    print("Evento não encontrado.")


def eventos_por_tema():
    print('\n--- Relatório: Quantidade de eventos por tema ---')
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    contagem = {}
    for evento in eventos:
        tema = evento["tema"].strip().lower()
        contagem[tema] = contagem.get(tema, 0) + 1

    print("Tema(s) e quantidade de eventos:")
    for tema, qtd in contagem.items():
        print(f"- {tema.capitalize()}: {qtd} evento(s)")


def taxa_media_participacao_por_tema():
    print('\n--- Relatório: Taxa média de participação por tema ---')
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    temas = {}
    for evento in eventos:
        tema = evento["tema"].strip().lower()
        qtd_participantes = len(evento["participantes"])
        if tema not in temas:
            temas[tema] = {"total_eventos": 0, "total_participantes": 0}
        temas[tema]["total_eventos"] += 1
        temas[tema]["total_participantes"] += qtd_participantes

    for tema, dados in temas.items():
        media = dados["total_participantes"] / dados["total_eventos"]
        print(f"{tema.capitalize()}: {media:.1f} participantes por evento")