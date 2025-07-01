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
            termo = input("Deseja filtrar por nome? (pressione Enter para listar todos): ").strip()
            if termo:
                participantes.listar_participantes_com_args(termo)
            else:
                participantes.listar_participantes_com_args()
        elif op == 2:
            participantes.cadastrar_participante()
        elif op == 3:
            participantes.remover_participante()
        elif op == 4:
            participantes.buscar_participante()
        elif op == 5:
            try:
                codigo = int(input("Digite o código do participante: "))
                novo_email = input("Digite o novo e-mail: ").strip()
                participantes.atualizar_email_participante_com_kwargs(codigo=codigo, novo_email=novo_email)
            except ValueError:
                print("Código inválido.")
        elif op == 0:
            break