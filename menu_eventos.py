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
        print('(8) - Relatório: Participantes mais ativos')
        print('(9) - Eventos com menos de 2 participantes')
        print('(10) - Remover participantes duplicados por evento')
        print('(11) - Filtrar eventos por tema')
        print('(12) - Filtrar eventos por faixa de datas')
        print('(13) - Atualizar tema de um evento')
        print('(14) - Relatório: Quantidade de eventos por tema')
        print('(0) - Voltar')

        try:
            op = int(input("Digite uma opção: "))
            if op < 0 or op > 14:
                print("Opção inválida!")
                continue
        except ValueError:
            print("Digite um número válido.")
            continue

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
        elif op == 8:
            eventos.participantes_mais_ativos()
        elif op == 9:
            eventos.eventos_com_poucos_participantes()
        elif op == 10:
            eventos.remover_participantes_duplicados()
        elif op == 11:
            eventos.filtrar_eventos_por_tema()
        elif op == 12:
            eventos.filtrar_eventos_por_data()
        elif op == 13:
            eventos.atualizar_tema_evento()
        elif op == 14:
            eventos.eventos_por_tema()
        elif op == 0:
            break