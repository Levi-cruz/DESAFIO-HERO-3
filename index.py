'''   ## Objetivo:

Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades:

- nome
    - idade
        - tipo (ex: guerreiro, mago, monge, ninja )

além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:

    - exibir a mensagem: "o {tipo} atacou usando {ataque}")
        - aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe
            - e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

se mago -> no ataque exibir (usou magia)
    se guerreiro -> no ataque exibir (usou espada)
        se monge -> no ataque exibir (usou artes marciais)
            se ninja -> no ataque exibir (usou shuriken)
## Saída
    Ao final deve se exibir uma mensagem:

- "o {tipo} atacou usando {ataque}"
  ex: mago atacou usando magia
  guerreiro atacou usando espada    '''


class heroi:
    def __init__(self):
        herois = ['Guerreiro', 'Mago', 'Ninja', 'Monge']
        for i, heroi in enumerate(herois, start=1):
            print(f"[{heroi}] --> {i}")
        escolha = input('Escolha o número correspondente ao tipo do herói: ')
        if escolha == '1':
            self.tipo = 'Guerreiro'
        elif escolha == '2':
            self.tipo = 'Mago'
        elif escolha == '3':
            self.tipo = 'Ninja'
        elif escolha == '4':
            self.tipo = 'Monge'
        else:
            print("Escolha inválida. Definindo o tipo para 'Guerreiro'.")
        self.tipo = 'Guerreiro'
        self.nome = input('Digite o nome do herói: ')


    def atacar(self):
        if self.tipo == "Guerreiro":
            ataque = "espada"
        elif self.tipo == "Mago":
            ataque = "magia"
        elif self.tipo == "Ninja":
            ataque = "shuriken"
        elif self.tipo == "Monge":
            ataque = "artes marciais"
        else:
            ataque = "atacou"
        print(f"O {self.tipo} {self.nome} atacou usando {ataque}!")

# Criando um objeto da classe Heroi com entrada do usuário
heroi = heroi()

# Chamando o método atacar
heroi.atacar()
