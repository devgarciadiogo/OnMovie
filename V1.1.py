import os


class Main:
  '''
  Cria-se variáveis para todo o programa na Main, Encapsulamento
  '''
  def __init__(self, generos_de_filme, filme):
    self.generos_de_filme = generos_de_filme
    self.filme = filme

  '''
  Mini-Biblioteca e pedir ao usuário generos favoritos e filmes vistos recentemente
  '''
  def criacao_conta(self):
    nome = input("Insira seu nome: ")
    self.generos_de_filme = {}
    self.filme = {
      "1":"Nome: Mistério em Paris\n\nIMDb: 5,8/10\n\nDireção: Jeremy Garelick\n______________________\n\nNome: Gente Grande\n\nIMDb: 6/10\n\nDireção: Dennis Dugan\n______________________\n\nNome: Minha Mãe é Uma Peça 3\n\nIMDb: 7,1/10\n\nDireção: Susana Garcia",

      "2":"Nome: Batman\n\nIMDb: 7,8/10\n\nDireção: Matt Reeves\n______________________\n\nNome: Até o último homem\n\nIMDb: 8.1/10\n\nDireção: Mel Gibson\n______________________\n\nNome: Oppenheimer\n\nIMDb: 8,5/10\n\nDireção: Christopher Nolan",

      "3":"Nome: Como eu era antes de você\n\nIMDb: 7,4/10\n\nDireção: Thea Sharrock\n______________________\n\nNome: Diário de uma paixão\n\nIMDb: 7,8/10\n\nDireção: Nick Cassavetes\n______________________\n\nNome: Amor ao primeiro beijo \n\nIMDb: 5.7/10\n\nDireção: Alauda Ruiz de Azúa",

      "4":"Nome: Aladdin\n\nIMDb: 6,9/10\n\nDireção: Guy Ritchie\n______________________\n\nNome: A Bela e a Fera\n\nIMDb: 7,1/10\n\nDireção: Bill Condon\n______________________\n\nNome: A Pequena Sereia\n\nIMDb: 7,2/10\n\nDireção: Rob Marshall",

      "5":"Nome: Coringa\n\nIMDb: 8,4/10\n\nDireção: Todd Phillips\n______________________\n\nNome: O Silêncio dos Inocentes\n\nIMDb: 8,6/10\n\nDireção: Jonathan Demme\n______________________\n\nNome: A Origem\n\nIMDb: 8,8/10\n\nDireção: Cristopher Nolan",

      "6":"Nome: IT: a coisa\n\nIMDb: 7,3/10\n\nDireção: Andy Muschietti\n______________________\n\nNome: A Freira\n\nIMDb: 5,3/10\n\nDireção: Corin Hardy\n______________________\n\nNome: M3gan\n\nIMDb: 6,4/10\n\nDireção: Gerard Johnstone",

      "7":"Nome: Stephen Curry: Subestimado\n\nIMDb: 7,3/10\n\nDireção: Peter Nicks\n______________________\n\nNome: Democracia em Vertigem\n\nIMDb: 7,3/10\n\nDireção: Petra Costa\n______________________\n\nNome: Pré-Histórico\n\nIMDb: 8,4/10\n\nDireção: Russel T. Davies",

      "8":"Nome: Godzilla vs Kong\n\nIMDb: 6,3/10\n\nDireção: Adam Wingard\n______________________\n\nNome: Venom\n\nIMDb: 6,6/10\n\nDireção: Ruben Fleischer\n______________________\n\nNome: Pantera Negra\n\nIMDb: 7,3/10\n\nDireção: Ryan Coogler",

      "9":"Nome: Avatar: O caminho da Água\n\nIMDb: 7,6/10\n\nDireção: James Cameron\n______________________\n\nNome: Doutor Estranho no Multiverso da Loucura\n\nIMDb: 6,9/10\n\nDireção: Sam Raimi\n______________________\n\nNome: As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa\n\nIMDb: 6,9/10\n\nDireção: Andrew Adamson",

      "10":"Nome: Cruella\n\nIMDb: 7,3/10\n\nDireção: Craig Gillespie\n______________________\n\nNome: Homem-Aranha: Sem Volta pra Casa\n\nIMDb: 8,2/10\n\nDireção: Jon Watts\n______________________\n\nNome: Jumanji: Bem-Vindo à Selva\n\nIMDb: 6,9/10\n\nDireção: Jake Kasdan"
    }
    while True:
      generos = input('''
      \nGêneros de filme:
      \n1) Comédia
      \n2) Drama
      \n3) Romance
      \n4) Musical
      \n5) Suspense
      \n6) Terror
      \n7) Documentário
      \n8) Ficção Científica
      \n9) Fantasia
      \n10) Aventura
      \n\nInsira seus favoritos! Para concluir insira 0: ''')
      if generos == "0":
        break
      vistos_filmes = str(input(f"\n{nome}, Insira seus filme favorito desse genero:"))
      os.system('clear')
      self.generos_de_filme[generos] = vistos_filmes
      print("Filmes escolhidos: \n",self.generos_de_filme)
      
  '''
  Método recomendação para acessar e imprimir os dicionários criados anteriormente 
  '''
  def recomendacao(self):
    os.system('clear')
    if "1" in self.generos_de_filme:
      print(f"\nVisto que gostou de:\n\n{self.generos_de_filme['1']}\n\nRecomendo os filmes:\n")
      print(self.filme["1"])
      print("\n______________________\n")
    if "2" in self.generos_de_filme:
      print(f"\nVisto que gostou de:\n\n{self.generos_de_filme['2']}\n\nRecomendo os filmes:\n")
      print(self.filme["2"])
      print("\n______________________\n")
    if "3" in self.generos_de_filme:
      print(f"\nVisto que gostou de:\n\n{self.generos_de_filme['3']}\n\nRecomendo os filmes:\n")
      print(self.filme["3"])
      print("\n______________________\n")
    if "4" in self.generos_de_filme:
      print(f"\nVisto que gostou de:\n\n{self.generos_de_filme['4']}\n\nRecomendo os filmes:\n")
      print(self.filme["4"])
      print("\n______________________\n")
    if "5" in self.generos_de_filme:
      print(f"\nVisto que gostou de:\n\n{self.generos_de_filme['5']}\n\nRecomendo os filmes:\n")
      print(self.filme["5"])
      print("\n______________________\n")
    if "6" in self.generos_de_filme:
      print(f"\nVisto que gostou de:\n\n{self.generos_de_filme['6']}\n\nRecomendo os filmes:\n")
      print(self.filme["6"])
      print("\n______________________\n")
    if "7" in self.generos_de_filme:
      print(f"\nVisto que gostou de:\n\n{self.generos_de_filme['7']}\n\nRecomendo os filmes:\n")
      print(self.filme["7"])
      print("\n______________________\n")
    if "8" in self.generos_de_filme:
      print(f"\nVisto que gostou de:\n\n{self.generos_de_filme['8']}\n\nRecomendo os filmes:\n")
      print(self.filme["8"])
      print("\n______________________\n")
    if "9" in self.generos_de_filme:
      print(f"\nVisto que gostou de:\n\n{self.generos_de_filme['9']}\n\nRecomendo os filmes:\n")
      print(self.filme["9"])
      print("\n______________________\n")
    if "10" in self.generos_de_filme:
      print(f"\nVisto que gostou de:\n\n{self.generos_de_filme['10']}\n\nRecomendo esses filmes:\n")
      print(self.filme["10"])
      print("\n______________________\n")

  '''  
  Chamadas de funções para execução do programa
  '''
conta = Main(0,0)
conta.criacao_conta()
conta.recomendacao()