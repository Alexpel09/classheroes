class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
      
    def atacar(self, inimigo):
        if self.tipo == "mago":
            print(f"{self.nome} usou magia e atacou {inimigo.nome}!")
        elif self.tipo == "guerreiro":
            print(f"{self.nome} usou espada e atacou {inimigo.nome}!")
        elif self.tipo == "monge":
            print(f"{self.nome} usou artes marciais e atacou {inimigo.nome}!")
        elif self.tipo == "ninja":
            print(f"{self.nome} usou shuriken e atacou {inimigo.nome}!")

# Criando heróis de diferentes tipos
mago = Heroi("Preston", 1000, "mago")
guerreiro = Heroi("Capitão Caverna", 40, "guerreiro")
monge = Heroi("Ang", 33, "monge")
ninja = Heroi("Nabu San", 28, "ninja")

# Fazendo os heróis atacarem
mago.atacar(guerreiro)
guerreiro.atacar(monge)
monge.atacar(ninja)
ninja.atacar(mago)



mago.atacar(guerreiro)
guerreiro.atacar(monge)
monge.atacar(ninja)
ninja.atacar(mago)