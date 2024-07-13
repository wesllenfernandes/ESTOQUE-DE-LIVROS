livros = []
while True:
        print("----- Biblioteca -----")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        print("3. Atualizar Livro")
        print("4. Listar Livros")
        print("5. Procurar Livro")
        print("6. Sair")
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            titulo = str(input("Digite o título do livro: "))
            autor = str(input("Digite o autor do livro: "))
            livro = [titulo, autor]
            livros.append(livro)
            print("Livro adicionado com sucesso!")
        elif escolha == 2:
            titulo = str(input("Digite o título do livro a ser removido: "))
            for livro in livros:
                if livro[0].lower() == titulo.lower():
                    livros.remove(livro)
                    print("Livro removido com sucesso!")
                    break
            else:
                print("Livro não encontrado.")
        elif escolha == 3:
            titulo = str(input("Digite o título do livro a ser atualizado: "))
            for livro in livros:
                if livro[0].lower() == titulo.lower():
                    novo_titulo = str(input("Digite o novo título (ou pressione Enter para manter o atual): "))
                    novo_autor = str(input("Digite o novo autor (ou pressione Enter para manter o atual): "))


                    if novo_titulo:
                        livro[0] = novo_titulo
                    if novo_autor:
                        livro[1] = novo_autor
                    print("Livro atualizado com sucesso!")
                    break
            else:
                print("Livro não encontrado.")
        elif escolha == 4:
            if not livros:
                print("Nenhum livro cadastrado.")
            else:
                for livro in livros:
                    print(f"Título: {livro[0]}, Autor: {livro[1]}")
        elif escolha == 5:
            termo = str(input("Digite o título ou autor do livro a ser procurado: ")).lower()
            encontrados = [livro for livro in livros if termo in livro[0].lower() or termo in livro[1].lower()]
            if encontrados:
                for livro in encontrados:
                    print(f"Título: {livro[0]}, Autor: {livro[1]}")
            else:
                print("Nenhum livro encontrado.")
        elif escolha == 6:
            print("Saindo do programa.")
            break
        else:
            print("Escolha inválida. Tente novamente.")