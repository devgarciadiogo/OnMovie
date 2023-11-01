# OnMovie
## Sistema que recomenda filmes com base nas preferências do usuário e histórico de visualização.
Projeto de python da faculdade realizado em grupo com colegas de classe.
Créditos: Arthur Falcone / Dillan Rosa / Leonardo Ibraim / Diogo Garcia

Nosso trabalho foi referente à recomendação de filmes para usuários.

Nós utilizamos do método de encapsulamento para criar as variáveis -generos_de_filme- e -filme- para serem utilizadas em todos os métodos

Começamos com o método 'criacao_conta' em que pedimos ao usuário seu nome para utilizar depois, criamos um dicionário em cima do -generos_de_filme- para armazenar os generos de filme que o usuário gosta e então fizemos uma mini-biblioteca com as recomendações que nós mesmos pesquisamos e achamos adequados. Uma pequena base de dados.

Com isso, pudemos criar um loop de input que requisita do usuário seu genero de filme preferido e qual filme favorito desse genero.

Depois concatenamos os dois no dicionário criado anteriormente -generos_de_filme- para ser utilizado no próximo método

No método -recomendacao- nós fizemos a utilização mais uma vez das variáveis criadas no começo do programa com 10 condicionais fazendo conexão com as escolhas específicas do usuário, assim, se ele digitou 1, para o gênero 'Comédia', serão feitas indicações baseadas na nossa mini-biblioteca e impressas de maneira formatada para que ele possa somente ver o painel.

Ao final do programa, ou melhor, ao começo do programa, fizemos a chamada da variável 'conta' que faz uso da Função 'Main', nesse caso, não precisamos colocar parâmetros definidos.

Fizemos então a chamada do método criacao_conta para pedir ao usuário Gênero de filme e Filme favorito.

E então utilizamos do método recomendacao para indicar para ele os filmes mais adequados para suas escolhas.
