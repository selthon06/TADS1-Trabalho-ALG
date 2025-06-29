from menu_eventos import menu_eventos
from menu_participantes import menu_participantes

def menu_principal():
    while True:
        print("\n=== Sistema de Gerenciamento de Eventos - Comunidade Tech ===")
        print("1. Menu de Eventos")
        print("2. Menu de Participantes")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_eventos()
        elif opcao == '2':
            menu_participantes()
        elif opcao == '0':
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()