def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo '{nome}' criado com sucesso!")
