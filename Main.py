from menu_eventos import menu_eventos
from menu_participantes import menu_participantes

def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Eventos - Comunidade Tech ===")
        print("1. Listar eventos")
        print("2. Listar partpantes de um evento")
        print("3. Buacar participante por código")
        print("0. Sair")

        opcao = input("Escolhauma opção: ")

        if opcao == '1':
            print("Função listar eventos ainda não implementada.")
        elif opcao == '2':
            print("Função listar participantes ainda não implemetada.")
        elif opcao == '3':
            print("Função buscar participante ainda não implementada.")
        elif opcao == '0':
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()