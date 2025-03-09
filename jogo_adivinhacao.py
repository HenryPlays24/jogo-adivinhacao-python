import random

class JogoAdivinhacao():
    def __init__(self, minimo = 1, maximo = 10):
        self.minimo = minimo
        self.maximo = maximo
        self.numero_secreto = random.randint(minimo, maximo)
        self.tentativas = 1

def nivel(self):
    print('Bem-vindo ao Jogo de Adivinhção! Escolha uma dificuldade: ')
    while True:
        dificuldade = input("Digite uma dificuldade: facil; medio; dificil: ").strip().lower()
        if dificuldade == "facil":
            self.tentantivas = 5
            print('Você escolheu o modo fácil!')
            break
        elif dificuldade == "medio":
            self.tentativas = 3
            print('Você escolheu o modo médio!')
            break
        elif dificuldade == "dificil":
            self.tentativas = 1 
            print('Você escolheu o modo difícil!')
            break
        else:
            print('Esse modo não existe, volte e escolha novamente!')

    def jogar(self):
        while self.tentativas > 0:
            try:
                numero_escolhido = int(input("Escolha um número de 1 a 10: "))
                if numero_escolhido < self.minimo or numero_escolhido > self.maximo:
                    print(f'Por favor, escolha uma número que esteja no intervalo de tempo de {self.minimo} a {self.maximo}!')
                    continue         
            except ValueError:
                print('Error: Escolha um valor númerico válido!')
                continue

            if numero_escolhido == self.nummero_secreto:
                print(f'Você acertou! Encontrou o Número Secreto: {self.numero_secreto}')
                return
            elif numero_escolhido < self.numero_secreto:
                print('O Número Secreto é maior!')
            else:
                print('O Número Secreto é menor!')

            self.tentativas -= 1
            if self.tentativas > 0:
                print(f'Você ainda tem mais {self.tentativas} para conseguir vencer!')
            else:
                print(f'Tentativas esgotadas! O Número Secreto era: {self.numero_secreto}')

while True:
    jogo = JogoAdivinhacao()
    jogo.nivel()
    jogo.jogar()

    jogar_novamente = input("Você quer jogar novamente? (S/N)").strip().lower()
    if jogar_novamente == 's':
        print('Ótimo! Então vamos para mais um novo jogo!')
        continue
    else:
        print('Que pena, então até próxima!')
        break
