from random import randint
class Monstros:
    def __init__(self, nome, tipo, poder_ataque, poder_defesa, pontos_vida, grau_evolucao, nivel):
        self.nome = nome
        self.tipo = tipo
        self.poder_ataque = poder_ataque
        self.poder_defesa = poder_defesa
        self.pontos_vida = pontos_vida
        self.grau_evolucao = grau_evolucao
        self.nivel = nivel
        self.metodo_ataque = poder_ataque * grau_evolucao * nivel * randint(1, 5)
        self.metodo_defesa = poder_defesa * grau_evolucao * nivel * randint(1, 3)




monstro1 = Monstros("Sportacus", "Ar", 5, 8, 98, 2, 5)
monstro2 = Monstros("Mjolnir", "Terra", 8, 5, 87, 3, 7)
monstro3 = Monstros("rayquaza", "ferro", 9, 9, 5000, 9, 10)
print(monstro1.nome, monstro1.tipo, monstro1.poder_ataque, monstro1.poder_defesa, monstro1.pontos_vida, monstro1.grau_evolucao, monstro1.nivel)
print(monstro2.nome, monstro2.tipo, monstro2.poder_ataque, monstro2.poder_defesa, monstro2.pontos_vida, monstro2.grau_evolucao, monstro2.nivel)
print(monstro3.nome, monstro3.tipo, monstro3.poder_ataque, monstro3.poder_defesa, monstro3.pontos_vida, monstro3.grau_evolucao, monstro3.nivel)
print(monstro1.metodo_ataque, monstro1.metodo_defesa)
print(monstro2.metodo_ataque, monstro2.metodo_defesa)
print(monstro3.metodo_ataque, monstro3.metodo_defesa)
dano = monstro1.metodo_ataque - monstro2.metodo_defesa
monstro2.pontos_vida -= dano
print(monstro2.pontos_vida)



'''print(x.nome, x.tipo)'''