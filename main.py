'''
Consultando o código das atividades que você já fez, faça funções que (é necessário chamar as funções e mostrar o
resultado na tela):
tenha como entrada um número e exiba o seu quadrado.
'''
import random


def quadrado(a):
    return a**2

'''
Ler 3 valores e escrever o maior deles.

'''

def maior_valor():
    valores = []
    for i in range(3):
        valores.append(int(input('Insira um valor inteiro: ')))

    valores.sort(reverse=True)
    return valores[0]

'''
leia do teclado as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo.
(Valores inválidos: 0 e números negativos).
'''


def area_retangulo():
    base = float(input('Insira o valor da base : '))
    altura = float(input('Insira o valor da altura : '))
    return base * altura



'''

Crie um vetor de int vetA com tamanho 5 e mostre na tela os valores de seus elementos;

'''

def vetor():
    vetB = []
    for i in range(5):
        vetB.append(random.randint(1, 50))
        yield vetB[i]


'''
Maçãs verdes custam R$ 12,20 por quilo. Cada uma pesa em torno de 130g. Faça um programa que tenha como entrada a
quantidade de maçãs e mostre o valor em reais.
'''

def valor_macas(un=1):
    valor_g = 12.20
    maca = .130

    return round(un * maca * valor_g, 2)



'''

A jornada de trabalho mensal de um funcionário na empresa X é de 160 horas. O funcionário que trabalhar mais de
160 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que 
leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, 
que deverá ser acrescido das horas extras, caso tenham sido trabalhadas.

'''

class Salario:
    def __init__(self, ):
        self.horas_trabalhadas = []
        self.salario_hora = -1
        self.salario_mes = -1
        self.hora_extra_50 = 1.5
    def set_salario_hora(self):
        while True:
            self.salario_hora = float(input('Insira o valor do salario por hora : \n'))
            if self.salario_hora <=0:
                print('Salario não pode ser negativo ou zero')
            else:
                return self.salario_hora

    def set_horas_trabalhadas(self):
        for n in range(4):
            while True:
                hora = int(input(f'Insira o valor de horas trablhadas na semana {n+1}: \n'))
                if hora < 0 or hora > 50:
                    print('O número de horas por semana não pode ser negativo e '
                          'não pode ultrapassar 50 horas por semana.')
                else:
                    self.horas_trabalhadas.append(hora)
                    break

        return self.horas_trabalhadas

    def calcular_salario(self):
        salario_total = 0
        for i in range(len(self.horas_trabalhadas)):
            if self.horas_trabalhadas[i] <= 40:
                salario_total += self.salario_hora * 40
            else:
                salario_total += ((self.horas_trabalhadas[i] - 40) * self.salario_hora) * self.hora_extra_50
                salario_total += self.salario_hora * 40

        self.salario_mes = salario_total
        return self.salario_mes




'''
leia do teclado uma distância em metros e mostre na tela o seu valor convertido em quilômetros.
(Valores inválidos: números negativos).
'''
class Distancia:
    """
    Trata o valor da distancia fornecida
    """
    def __init__(self):
        self.distancia = -1

    def set_distancia(self):
        """
        Usuario insere um valor float referente a uma distancia que seja >=0
        """
        while self.distancia < 0:
            self.distancia = float(input('Insira um valor da distancia: \n'))
            if self.distancia < 0:
                print('Valores inválidos: números negativos\n')

    def converter_metro(self):
        """
        Converte o valor em metros.
        :return: retorna um float do valor em metros
        """
        metros = self.distancia * 1000
        return metros

    def converter_kilometros(self):
        """
        Converte o valor em kilometros.
        :return: retorna um float do valor em kilometros
        """
        kilometros = self.distancia / 1000
        return kilometros




'''
Crie uma list de int vetB com tamanho 5, insira um inteiro com entrada do teclado para cada um dos elementos e mostre
na tela os seus valores após a inserção dos elementos.

'''

def vetor2():
    vetB = []
    for i in range(5):
        vetB.append(int(input('Insira um valor inteiro:')))
        print(vetB[i])

vetor2()