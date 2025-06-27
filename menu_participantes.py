import participantes

def menu_participantes():
    while True:
        print('\n========= MENU DE PARTICIPANTES =========')
        print('(1) - Listar participantes')
        print('(2) - Cadastrar novo participante')
        print('(3) - Remover participante')
        print('(4) - Buscar participante por código')
        print('(5) - Atualizar e-mail de participante')
        print('(0) - Voltar')

        try:
            op = int(input("Digite uma opção: "))
            if op < 0 or op > 5:
                print("Opção inválida!")
                continue
        except ValueError:
            print("Digite um número válido.")
            continue

        if op == 1:
            participantes.listar_participantes()
        elif op == 2:
            participantes.cadastrar_participante()
        elif op == 3:
            participantes.remover_participante()
        elif op == 4:
            participantes.buscar_participante()
        elif op == 5:
            participantes.atualizar_email_participante()
        elif op == 0:
            break