print("Bem Vindo á Calculadora de Frete da nossa loja!  Por favor, insira as próximas informações ")

usuario_cadastrado = input("Crie seu nome de usuario ou insira seu email: ")
senha_cadastrado = input("Crie sua senha de usuario: ")
while True:
    print('\n-----LOGIN-----')
    usuario= input("Digite seu nome de usuario ou email: ")
    senha= input("Digite sua senha: ")
    if usuario == usuario_cadastrado and senha == senha_cadastrado:
        print("\nLogin realizado com sucesso")
        break
    else:
        print('\nLogin incorreto. Tente novamente')

print("Bem Vindo! Por favor, insira as próximas informações ")

while True:
    peso_produto = float(input("Peso do seu produto em kg: "))

    if peso_produto > 0:
        break
    else:
        print("Peso inválido, digite um valor acima de 0")

estado_user= input("Digite seu estado (sigla): ").lower()

if estado_user == "pr":
    taxa = 0
elif estado_user in ["sp", "rj", "mg"]:
    taxa = 15
else:
    taxa = 36

while True:
    print('\n-----MENU-----'
          '\n 1: Calcular Frete'
          '\n 2: Ajuda com o Envio'
          '\n 3: Rastrear meu Envio')

    seletor = input("\nDigite o número da opção que deseja acessar: ")
    if seletor == "1":
        print('\n---CALCULADORA DE FRETE---\n')
        frete = (peso_produto * 15) + taxa
        print(f"Valor do frete: R$ {frete}")
        voltar = input("\nDeseja voltar ao menu? (digite s ou n): ")
        if voltar != "s":
            print("\nPrograma Encerrado")
            break
    elif seletor == "2":
     while True:
        print('\n---AJUDA COM O ENVIO---\n'
                '\n 1: Como Embalar'
                '\n 2: Quanto tempo até meu produto chegar?'
                '\n 3: Outro'
                '\n 4: Voltar')

        opcao_ajuda = input("\nEscolha uma opção: ")

        if opcao_ajuda == "1":
            print("\nUse caixas resistentes e proteção interna.")

        elif opcao_ajuda == "2":
            print("\nO prazo depende da sua região.")

        elif opcao_ajuda == "3":
            print("\nFale com o suporte da nossa loja (41)9324-3261.")

        elif opcao_ajuda == "4":
            break
    elif seletor == "3":
        print('\n----RASTREAR MEU ENVIO----')
        cpf = input("Digite seu CPF: ")
        print('\nInfelizmente não conseguimos Rastrear seu pedido.'
              '\n Voce pode rastrear seu pedido pelo site dos correios o qual te encaminharei a Seguir:'
              '\n https://rastreamento.correios.com.br/app/index.php')
        voltar = input("\nDeseja voltar ao menu? (Digite s ou n): ")
        if voltar == "n":
          print("\nPrograma Encerrado")
          break


