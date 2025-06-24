from dados_participantes import participantes

def listar_participantes():
    print('\n--- Lista de Participantes ---')
    if not participantes:
        print("Nenhum participante cadastrado.")
        return

    for p in participantes:
        print(f"Código: {p['codigo']} | Nome: {p['nome']} | Email: {p['email']}")