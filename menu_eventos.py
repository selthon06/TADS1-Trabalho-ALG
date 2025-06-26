import eventos



def menu_eventos():
    while True:
        print('\n========= MENU DE EVENTOS =========')
        print('(1) - Listar eventos')
        print('(2) - Cadastrar novo evento')
        print('(3) - Remover evento')
        print('(4) - Buscar evento por nome')
        print('(5) - Adicionar participante a evento')
        print('(6) - Listar participantes de um evento')
        print('(7) - Relatório: Temas mais frequentes')
        print('(0) - Voltar')
        op = ler_opcao(6)

        if op == 1:
            eventos.listar_eventos()
        elif op == 2:
            eventos.cadastrar_evento()
        elif op == 3:
            eventos.remover_evento()
        elif op == 4:
            eventos.buscar_evento_por_nome()
        elif op == 5:
            eventos.adicionar_participante_evento()
        elif op == 6:
          eventos.listar_participantes_evento()
        elif op == 7:
    eventos.temas_mais_frequentes()
        elif op == 0:
            break