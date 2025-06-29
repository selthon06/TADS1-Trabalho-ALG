
from datetime import datetime
from dados_eventos import eventos
from dados_participantes import participantes

eventos = []
participantes = []

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

def remover_evento():
    print('\n--- Remover Evento ---')
    nome = input("Digite o nome do evento que deseja remover: ")
    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            eventos.remove(evento)
            print(f"Evento '{nome}' removido com sucesso!.")
            return
    print("Evento nÃ£o encontrado.")

def buscar_evento_por_nome():
    print('\n--- Buscar Evento ---')
    nome = input("Digite o nome do evento: ")
    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            print(f"Nome: {evento['nome']} | Data: {evento['data']} | Tema: {evento['tema']}")
            print("Participantes:", evento["participantes"])
            return
    print("Evento nÃ£o encontrado.")

def adicionar_participante_evento():
    print('\n--- Adicionar Participante a Evento ---')
    nome_evento = input("Nome do evento: ")
    try:
        codigo_part = int(input("CÃ³digo do participante: "))
    except ValueError:
        print("CÃ³digo invÃ¡lido!")
        return
    evento_encontrado = next((e for e in eventos if e["nome"].lower() == nome_evento.lower()), None)
    if not evento_encontrado:
        print("Evento nÃ£o encontrado.")
        return
    participante = next((p for p in participantes if p["codigo"] == codigo_part), None)
    if not participante:
        print("Participante nÃ£o encontrado.")
        return
    if codigo_part not in evento_encontrado["participantes"]:
        evento_encontrado["participantes"].append(codigo_part)
        print("Participante adicionado com sucesso.")
    else:
        print("Participante jÃ¡ estÃ¡ inscrito neste evento.")

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
                participante = next((p for p in participantes if p["codigo"] == codigo), None)
                if participante:
                    print(f" - {participante['nome']} (CÃ³digo: {participante['codigo']})")
                else:
                    print(f" - Participante com cÃ³digo {codigo} nÃ£o encontrado.")
            return
    print("Evento nÃ£o encontrado.")

def temas_mais_frequentes():
    print('\n--- Temas mais frequentes ---')
    if not eventos:
        print("Nenhum evento cadastrado.")
        return
    temas = {}
    for evento in eventos:
        tema = evento["tema"].strip().lower()
        temas[tema] = temas.get(tema, 0) + 1
    temas_ordenados = sorted(temas.items(), key=lambda x: x[1], reverse=True)
    for tema, qtd in temas_ordenados:
        print(f"Tema: {tema.capitalize()} | Total de eventos: {qtd}")

def participantes_mais_ativos():
    print('\n--- Participantes mais ativos ---')
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
            print(f"{participante['nome']} (CÃ³digo: {codigo}) - {qtd} evento(s)")
        else:
            print(f"CÃ³digo {codigo} - {qtd} evento(s)")

def eventos_com_poucos_participantes():
    print('\n--- Eventos com menos de 2 participantes ---')
    encontrados = False
    for evento in eventos:
        if len(evento["participantes"]) < 2:
            print(f"- {evento['nome']} ({len(evento['participantes'])} participante(s))")
            encontrados = True
    if not encontrados:
        print("Todos os eventos tÃªm dois ou mais participantes.")

def remover_participantes_duplicados():
    print('\n--- RemoÃ§Ã£o de participantes duplicados por evento ---')
    total_corrigidos = 0
    for evento in eventos:
        participantes_antes = len(evento["participantes"])
        participantes_unicos = list(dict.fromkeys(evento["participantes"]))
        evento["participantes"] = participantes_unicos
        removidos = participantes_antes - len(participantes_unicos)
        if removidos > 0:
            print(f"- {evento['nome']}: {removidos} duplicata(s) removida(s)")
            total_corrigidos += removidos
    if total_corrigidos == 0:
        print("Nenhuma duplicata encontrada.")
    else:
        print(f"Total de {total_corrigidos} duplicata(s) removida(s) no sistema.")