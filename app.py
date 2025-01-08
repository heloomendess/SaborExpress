import os

restaurantes = ['Almanara', 'Madero', 'Outback']

def exibir_nome_programa():
    print("""
    𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
    """)

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_restaurante():
    os.system('cls')
    exibir_subtitulo('Cadastrar Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    os.system('cls')
    exibir_subtitulo('Listar Restaurantes')
    for restaurante in restaurantes:
        print(f'{restaurante}')
    print()
    voltar_menu_principal()

def voltar_menu_principal():
    input('\nPressione Enter para voltar para o menu principal.')
    main()        


def finalizar_app():
    os.system('cls')
    exibir_subtitulo('Finalizar app')

def opcao_invalida():
    print('Opção inválida. Tente novamente.')
    voltar_menu_principal()
       

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()       
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()    

