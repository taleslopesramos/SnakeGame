# SnakeGame
Jogo da cobrinha utilizando pygame e POO

# Instalar a lib pygame
`$ pip install pygame`

# Rodar o projeto
`$ python snake_game.py`

# Estrutura dos Arquivos
* **snake_game.py**: game main loop e lida com os inputs do usuário.  
* **snake.py**: definição da cobra a qual o usuário irá controlar.(Classe mais importante do Jogo)  
* **actions.py**: definição de ações possiveis do usuário tanto no menu quanto no jogo. (Falta implementar um menu)  
* **colors.py**: definição das cores as quais foram utilizadas no jogo.  
* **food.py**: implementação da comida a qual a cobra irá se alimentar, a comida é gerada aleatóriamente nos eixos do janela.  
* **point.py**: uma classe auxiliar para definir um ponto.  
* **globs.py**: classe de "variáveis globais", por hora só guarda as dimensões da tela.  
