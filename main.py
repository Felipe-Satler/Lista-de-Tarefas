from utilidade import *
from arquivo import *

arq = 'lista_de_tarefas.txt'

if not ArquivoExiste(arq):
    criarArquivo(arq)

if __name__ == "__main__":
    main()
