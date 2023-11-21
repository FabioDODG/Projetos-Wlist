def consultar_consultor():
    fabricantes = {
        '1': 'Confidencial',
        '2': 'Confidencial',
        '3': 'Confidencial',
        '4': 'Confidencial',
        '5': 'Confidencial',
        '6': 'Confidencial'
    }

    while True:
        print("")
        print("Opções de fabricantes:")
        for chave, valor in fabricantes.items():
            print(f"\033[96m{chave} : {valor}\033[0m")
        print("\033[91m7 : Sair\033[0m")
        print("")
        fabricante_opcao = input("Digite o número correspondente ao fabricante do produto: ")

        if fabricante_opcao == "7":
            break

        fabricante = fabricantes.get(fabricante_opcao)

        if fabricante is None:
            print("\033[91mFabricante não reconhecido.\033[0m")
        else:
            valor = float(input("Digite o valor do produto: "))

            if fabricante_opcao == "1":
                valor = round((valor * 0.51 * 1.05 * 2.2), 2)
                print("")
                print(f"Valor do mobiliário: R$ {valor:.2f}")
                print("")
                valor_vista = valor * 0.95
                print(f"Valor do mobiliário à vista : R$ {valor_vista:.2f}")

            elif fabricante_opcao == "2":
                valor = round((valor * 0.65 * 1.0325 * 1.8), 2)
                print("")
                print(f"Valor do mobiliário: R$ {valor:.2f}")
                print("")
                valor_vista = valor * 0.95
                print(f"Valor do mobiliário à vista : R$ {valor_vista:.2f}")

            elif fabricante_opcao == "3":
                valor = round((valor * 0.47 * 1.0325 * 1.8), 2)
                print("")
                print(f"Valor do mobiliário: R$ {valor:.2f}")
                print("")
                valor_vista = valor * 0.95
                print(f"Valor do mobiliário à vista: R$ {valor_vista:.2f}")

            elif fabricante_opcao == "4":
                valor = round((valor * 1.0325 * 1.8), 2)
                print("")
                print(f"Valor do mobiliário: R$ {valor:.2f}")
                print("")
                valor_vista = valor * 0.95
                print(f"Valor do mobiliário à vista: R$ {valor_vista:.2f}")

            elif fabricante_opcao == "5":
                valor = round((valor * 0.88 * 0.95 * 0.95 * 1.05 * 2.4), 2)
                print("")
                print(f"Valor do mobiliário: R$ {valor:.2f}")
                print("")
                valor_vista = valor * 0.95
                print(f"Valor do mobiliário à vista : R$ {valor_vista:.2f}")

            elif fabricante_opcao == "6":
                valor = round((valor * 1.0325 * 2.2), 2)
                print("")
                print(f"Valor do mobiliário: R$ {valor:.2f}")
                print("")
                valor_vista = valor * 0.95
                print(f"Valor do mobiliário à vista: R$ {valor_vista:.2f}")


def cadastrar_produto():
    nome_cadastro = input("Digite o nome de cadastro do produto: ")
    print("\033[96mOpções de fabricantes:\033[0m")
    print("1. Confidencial")
    print("2. Confidencial")
    print("3. Confidencial")
    print("4. Confidencial")
    print("5. Confidencial")
    print("6. Confidencial")
    print("7. Confidencial")

    fabricante_opcao = input("Digite o número correspondente ao fabricante do produto: ")

    fabricantes = {
        '1': 'Confidencial',
        '2': 'Confidencial',
        '3': 'Confidencial',
        '4': 'Confidencial',
        '5': 'Confidencial',
        '6': 'Confidencial',
        '7': 'Confidencial'
    }

    fabricante = fabricantes.get(fabricante_opcao)

    if fabricante is None:
        print("\033[91mOpção inválida de fabricante.\033[0m")
        return

    nome_original = input("Digite o nome original do produto: ")

    with open("nomes.txt", "a") as arquivo:
        arquivo.write(f"{nome_cadastro},{fabricante},{nome_original}\n")

    print("\033[92mProduto cadastrado com sucesso!\033[0m")


def incluir_valor_produto():
    try:
        nome_original_produto = input("Digite o nome original do produto: ")
        with open("nomes.txt", "r") as arquivo:
            produtos = arquivo.readlines()

        if produtos:
            produto_encontrado = False
            for i, produto in enumerate(produtos):
                valores = produto.strip().split(',')
                if len(valores) == 3 and valores[2] == nome_original_produto:
                    valor = input("Digite o novo valor do produto: ")
                    produtos[i] = f"{valores[0]},{valores[1]},{valores[2]},{valor}\n"

                    with open("nomes.txt", "w") as arquivo:
                        arquivo.writelines(produtos)

                    print("\033[92mValor do produto atualizado com sucesso!\033[0m")
                    produto_encontrado = True
                    break

            if not produto_encontrado:
                print("\033[91mProduto não encontrado. Verifique o nome original e tente novamente.\033[0m")

        else:
            print("\033[93mNenhum produto cadastrado.\033[0m")

    except FileNotFoundError:
        print("\033[93mNenhum produto cadastrado.\033[0m")

def alterar_dados_produto():
    try:
        with open("nomes.txt", "r") as arquivo:
            produtos = arquivo.readlines()

        print("""
Opções de alteração:
1. Alterar nome de cadastro
2. Alterar nome original
3. Alterar fabricante
4. Alterar valor
5. Voltar ao menu inicial
""")
        alteracao = input("Digite a opção de alteração que deseja fazer: ")

        if produtos:
            if alteracao == "4":
                nome_original_produto_alterar = input("Digite o nome original do produto que deseja alterar: ")

                produto_encontrado = False
                for i, produto in enumerate(produtos):
                    valores = produto.strip().split(',')
                    if len(valores) == 4 and valores[2] == nome_original_produto_alterar:
                        novo_valor = input("Digite o novo valor do produto: ")
                        valores[3] = novo_valor

                        produtos[i] = ','.join(valores) + '\n'

                        with open("nomes.txt", "w") as arquivo:
                            arquivo.writelines(produtos)

                        print("\033[92mDados do produto alterados com sucesso!\033[0m")
                        produto_encontrado = True
                        break

                if not produto_encontrado:
                    print("\033[91mProduto não encontrado. Verifique o nome original e tente novamente.\033[0m")
            else:
                nome_produto_alterar = input("Digite o nome de cadastro do produto que você deseja alterar: ")

                produto_encontrado = False
                for i, produto in enumerate(produtos):
                    valores = produto.strip().split(',')
                    if len(valores) == 4 and valores[0] == nome_produto_alterar:
                        if alteracao == "1":
                            novo_nome_cadastro = input("Digite o novo nome de cadastro: ")
                            valores[0] = novo_nome_cadastro
                        elif alteracao == "2":
                            novo_nome_original = input("Digite o novo nome original: ")
                            valores[2] = novo_nome_original
                        elif alteracao == "3":
                            print("\033[96mOpções de fabricantes:\033[0m")
                            print("1. Confidencial")
                            print("2. Confidencial")
                            print("3. Confidencial")
                            print("4. Confidencial")
                            print("5. Confidencial")
                            print("6. Confidencial")
                            print("7. Confidencial")

                            novo_fabricante_opcao = input("Digite o número correspondente ao novo fabricante do produto: ")
                            fabricantes = {
                                '1': 'Confidencial',
                                '2': 'Confidencial',
                                '3': 'Confidencial',
                                '4': 'Confidencial',
                                '5': 'Confidencial',
                                '6': 'Confidencial',
                                '7': 'Confidencial'
                            }
                            novo_fabricante = fabricantes.get(novo_fabricante_opcao)

                            if novo_fabricante is None:
                                print("\033[91mOpção inválida de fabricante.\033[0m")
                                return

                            valores[1] = novo_fabricante
                        produtos[i] = ','.join(valores) + '\n'

                with open("nomes.txt", "w") as arquivo:
                    arquivo.writelines(produtos)

                print("\033[92mDados do produto alterados com sucesso!\033[0m")
                produto_encontrado = True

                if not produto_encontrado:
                    print("\033[91mProduto não encontrado. Verifique o nome de cadastro e tente novamente.\033[0m")

        else:
            print("\033[93mNenhum produto cadastrado.\033[0m")

    except FileNotFoundError:
        print("\033[93mNenhum produto cadastrado.\033[0m")


def consultar_por_nome():
    try:
        with open("nomes.txt", "r") as arquivo:
            produtos = arquivo.readlines()

        if produtos:
            nome_cadastro_consulta = input("Digite o nome de cadastro do produto que deseja consultar: ")

            produto_encontrado = False
            for produto in produtos:
                valores = produto.strip().split(',')
                if len(valores) == 4 and valores[0] == nome_cadastro_consulta:
                    print("\nInformações do Produto:")
                    print(f"Nome de Cadastro: {valores[0]}")
                    print(f"Fabricante: {valores[1]}")
                    print(f"Nome Original: {valores[2]}")
                    print(f"Valor: R$ {valores[3]}")
                    produto_encontrado = True
                    break

            if not produto_encontrado:
                print("\033[91mProduto não encontrado. Verifique o nome de cadastro e tente novamente.\033[0m")

        else:
            print("\033[93mNenhum produto cadastrado.\033[0m")

    except FileNotFoundError:
        print("\033[93mNenhum produto cadastrado.\033[0m")


def consultar_por_fabricante():
    try:
        with open("nomes.txt", "r") as arquivo:
            produtos = arquivo.readlines()

        if produtos:
            print("\033[96mOpções de fabricantes:\033[0m")
            print("1. Confidencial")
            print("2. Confidencial")
            print("3. Confidencial")
            print("4. Confidencial")
            print("5. Confidencial")
            print("6. Confidencial")
            print("7. Confidencial")

            opcoes_validas = ['1', '2', '3', '4', '5', '6', '7']
            fabricante_consulta = input("Digite o número correspondente ao fabricante do produto que deseja consultar: ")

            if fabricante_consulta in opcoes_validas:
                fabricante_selecionado = selecionar_fabricante_por_numero(fabricante_consulta)
                produtos_encontrados = []

                for produto in produtos:
                    valores = produto.strip().split(',')
                    if len(valores) >= 3:
                        if valores[1] == fabricante_selecionado:
                            if len(valores) == 3:
                                produtos_encontrados.append(f"\033[32mNome de Cadastro: {valores[0]}\033[0m ||| \033[34mNome Original: {valores[2]}\033[0m ||| \033[31mFabricante: {valores[1]}\033[0m ||| \033[33mValor: R$ N/I\033[0m")
                            elif len(valores) == 4:
                                produtos_encontrados.append(f"\033[32mNome de Cadastro: {valores[0]}\033[0m ||| \033[34mNome Original: {valores[2]}\033[0m ||| \033[31mFabricante: {valores[1]}\033[0m ||| \033[33mValor: R$ {valores[3]}\033[0m")

                if produtos_encontrados:
                    print(f"\nProdutos do fabricante {fabricante_selecionado}")
                    print("=-=-=-=-=-=-=-=-=-=")
                    for produto in produtos_encontrados:
                        print(produto)
                else:
                    print("\033[91mNenhum produto encontrado para o fabricante especificado.\033[0m")
            else:
                print("\033[91mOpção inválida. Por favor, escolha um número correspondente a um fabricante.\033[0m")

        else:
            print("\033[93mNenhum produto cadastrado.\033[0m")

    except FileNotFoundError:
        print("\033[93mNenhum produto cadastrado.\033[0m")


def selecionar_fabricante_por_numero(numero):
    fabricantes = {
        '1': 'Confidencial',
        '2': 'Confidencial',
        '3': 'Confidencial',
        '4': 'Confidencial',
        '5': 'Confidencial',
        '6': 'Confidencial',
        '7': 'Confidencial'
    }
    return fabricantes.get(numero, 'Fabricante Inválido')



def selecionar_fabricante_por_numero(numero):
    fabricantes = {
        '1': 'Confidencial',
        '2': 'Confidencial',
        '3': 'Confidencial',
        '4': 'Confidencial',
        '5': 'Confidencial',
        '6': 'Confidencial',
        '7': 'Confidencial'
    }
    return fabricantes.get(numero, 'Fabricante Inválido')



def consultar_produtos():
    try:
        with open("nomes.txt", "r") as arquivo:
            produtos = arquivo.readlines()

        if produtos:
            produtos_ordenados = sorted(produtos, key=lambda x: (x.split(',')[1], x.split(',')[0]))

            fabricante_atual = None
            for produto in produtos_ordenados:
                valores = produto.strip().split(',')
                if len(valores) == 3:
                    if valores[1] != fabricante_atual:
                        fabricante_atual = valores[1]
                        print(f"\nProdutos {valores[1]}")
                        print("=-=-=-=-=-=-=-=-=-=")
                    print(f"\033[32mNome de Cadastro:\033[0m {valores[0]} ||| \033[34mNome Original:\033[0m {valores[2]} ||| \033[31mFabricante:\033[0m {valores[1]} ||| \033[33mValor:\033[0m R$ N/I")
                elif len(valores) == 4:
                    if valores[1] != fabricante_atual:
                        fabricante_atual = valores[1]
                        print(f"\nProdutos {valores[1]}")
                        print("=-=-=-=-=-=-=-=-=-=")
                    print(f"\033[32mNome de Cadastro:\033[0m {valores[0]} ||| \033[34mNome Original:\033[0m {valores[2]} ||| \033[31mFabricante:\033[0m {valores[1]} ||| \033[33mValor:\033[0m R$ {valores[3]}")

        else:
            print("\033[93mNenhum produto cadastrado.\033[0m")

    except FileNotFoundError:
        print("\033[93mNenhum produto cadastrado.\033[0m")


def main():
    try:
        while True:
            print("\nOpções:")
            print("1. - CALCULADORA -")
            print("2. - CONSULTORA -")
            print("3. - SAIR -")

            opcao1 = input("Digite a opção: ")

            if opcao1 == "1":
                consultar_consultor()
            elif opcao1 == "2":
                try:
                    while True:
                        print("""
Opções:
1. Cadastrar produto
2. Incluir valor do produto
3. Alterar dados do produto
4. Consultar por último nome de cadastro
5. Consultar por fabricante
6. Consultar todos os produtos
7. Voltar ao menu anterior
""")
                        opcao2 = input("Digite o número da opção desejada: ")

                        if opcao2 == "1":
                            cadastrar_produto()
                        elif opcao2 == "2":
                            incluir_valor_produto()
                        elif opcao2 == "3":
                            alterar_dados_produto()
                        elif opcao2 == "4":
                            consultar_por_nome()
                        elif opcao2 == "5":
                            consultar_por_fabricante()
                        elif opcao2 == "6":
                            consultar_produtos()
                        elif opcao2 == "7":
                            break
                        else:
                            print("\033[91mOpção inválida. Escolha novamente.\033[0m")
                except KeyboardInterrupt:
                    print("\nPrograma interrompido pelo usuário.")

            elif opcao1 == "3":
                print("Encerrando o programa.")
                break
            else:
                print("\033[91mOpção inválida. Escolha novamente.\033[0m")

    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")


if __name__ == "__main__":
    main()
