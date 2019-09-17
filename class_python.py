#AULA 1***********************
#Python é case sensitive
print('essa é a função print')
print (2+5)
print('o resultado da soma é: ', 2+5)


#AULA 2***********************
#variáveis
#não há necessidade de declarar as variáveis

Minha_idade = 31
meu_nome = 'Max'
print('minha idade é ',Minha_idade)

type(Minha_idade)
type(meu_nome)
#type exibe o tipo de dados da variável

print('Meu nome é: ', meu_nome, 'e minha idade é: ', Minha_idade)



#variáveis globais*********************
var_global = 10

def soma(num1, num2):
    var_global = num1 + num2
    print(var_global)#na função o vaalor é o resultado da soma

print(var_global)#fora da função a variável continua com o valor 10


#AULA 2 a 5***********************
#tipos de dados de variáveis

nome = 'Max' #string
type(nome)
sobrenome = "Pinheiro"
#concatenar
nomeCompleto = nome +' '+sobrenome
print(nomeCompleto)

#comprimento de uma variável
len(nomeCompleto)

nomeCompleto[0] #índice para a primeira letra da string - array

nomeCompleto[-1] #vai percorrer de tras pra frente, neste caso retorna a última letra

#slicing - fatiar uma variável
nomeCompleto[0:2]
#o resultado será as duas primeiras letras
nomeCompleto[-2:-1]
#resultado será as duas últimas letras da palavra


#AULA 6***********************
#tipos de dados númericos

num1 = 2 #int
num2 = 5.5 #float

#condição if
if num2 > num1:
    print('é maior')
else:
     print('é menor')

#**********importar módulos

#math é um módulo matemático
import math #o módulo possui várias funções
#exemplo:
math.sqrt(16) #raiz quadrada de 16


#recebendo dados do usuário
nome = input('Digite seu nome:')
print(nome)
#input retorna um dado do tipo string

#conversão de tipos de dados
num1 = int(input('Digite um número:'))
num2 = int(input('digite o segundo número:'))
resultado = num1 + num2
print(resultado)

#AULA 8***********************
#listas e tuplas

#tuplas***********************************
meses = ('janeiro', 'fevereiro', 'março')
#as tuplas são imutávies

len(meses)#tamanho da tupla

'maio' in meses#resultado falso

lista = list(meses)#converte a tupla em lista
tupla = tuple(lista)#converte a lista em tupla

#adicionando dados à lista
lista = ['a', 'b', 'c']
l.insert('d', 0)
print(l)
#['d', 'a', 'b', 'c']

lista += 'e'
#['d', 'a', 'b', 'c', 'e']

lista2 = [1,2,3,4]
lista3 = lista + lista2
#['d', 'a', 'b', 'c', 'e', 1, 2, 3, 4]

#removendo item
lista3.remove(4)#['a', 'b', 'c', 'd', 'e', 1, 2, 3]
#remove o item e não o indice, remove o primeiro item da lista

#dir
dir(lista3)#verifica todos os atributos(__add__) e métodos disponíveis para o objeto
help(lista3.count)#ajuda/instruções do método

#organizando as listas #sort
lista4 = [3,2,5,9]
#[2, 3, 5, 9]

lista5 = [3, 2, 5, 9, 'x']
#quando há mix de tipos de dados não é possível ordenar

#ordenar string
lista_texto = ['x', 'b', 'a', 'e']
lista_texto.sort()
#['a', 'b', 'e', 'x']

#sorted
l_number = [1,2,3]
sorted(l_number)
#[1, 2, 3]


#listas***********************************
alunos = ['maria', 'joao', 'jose']

#add um item a uma lista:
alunos.append('ricardo')
print(alunos) #resultado ['maria', 'joao', 'jose', 'ricardo']

#para add um item na 2ª posição, por exemplo
alunos.insert(1, 'paula')
print(alunos) #resultado ['maria', 'paula', 'joao', 'jose', 'ricardo']

#mostrar índice da lista
alunos.index("joao")

#contar quantos itens tem 
alunos.count("maria")

#alterar a ordem dos itens da lista
alunos.reverse()

#ordenar a lista
alunos.sort()

#remover itens da lista
alunos.pop(1) #exclui o 2º elemento
alunos.remove('paula')#exclui o elemento específico

#concatenar
alunos2 = ['joana', 'jorge']
totalAlunos = alunos + alunos2
print(totalAlunos)#resultado ['joao', 'maria', 'ricardo', 'joana', 'jorge']

indice = 2
print(totalAlunos[indice]) #resultado 'ricardo'

#exercício 8
#criar uma tupla para guardar meses do ano
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho','agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
data_nasc = input('Qual a sua data de nascimento?')
mes = data_nasc[3:4]
print('você nasceu no mês de ', meses[int(mes)-1])





# conversão para float num2 = float(input('digite o segundo número:'))

#AULA 10***********************
#DICIONÁRIOS
#os itens de um dicionário são sempre formados por um par: uma chave e um valor
#a chave não é uma variável
joao = {'nome':'joao',
        'sobrenome': 'pereira',
        'profissão': 'programador python',
        'filhos': ['pedro', 'maria']
        }
# type(joao)
# resultado: class 'dict'
print(joao) #resultado {'nome': 'joao', 'sobrenome': 'pereira', 'profissão': 'programador python', 'filhos': ['pedro', 'maria']}
print(joao['profissão']) #resultado: 'programador python'

len(joao) #resultado: 4
del joao['filhos'] #exclui os filhos

joao['profissão'] = 'aposentado' #resultado substitui 'programdor python' por 'aposentado'

'sobrenome' in joao #o resultado será true

joao.keys()#mostra as chaves
joao.values()#mostra os valores
joao.items()#mostra conjunto chave/valor

#percorrendo um dicionário
for x,y in dicionario.items():
    print(x,y)


#looping for

for x in joao:
    print(x) #resultado:nome, sobrenome, profissão

for x in joao:
    print(x+' :'+joao[x])#resultado
                            #nome: joao
                            #sobrenome: pereira
                            # profissão: aposentado

#método get
joao.get('nome', 'esta informação não consta no cadastro')#caso não ache o 'nome', caso contrário retorna a msg
#resultado: 'joao'
joao.get('idade', 'esta informação não consta no cadastro')

#adicionando itens
joao['filhos'] = ['pedro','maria']
joao['filhos'].append('jorge')
print(joao['filhos'])#resultado: 'pedro', 'maria', 'jorge'

#apagando todas as informações de um dicionário. exclui apenas o conteúdo
joao.clear()
print(joao)#resultado: ''

#AULA 11***********************
#DICIONÁRIOS - método get

cores = {'branco': 'white',
         'vermelho': 'red',
         'verde': 'green'
    }
cor = input('Qual cor deseja traduzir:').lower()
#lower() transformará tudo o que for digitado em minúsculo
traducao = cores.get(cor, 'Cor não localizada')#primeiro parametro a variavel pesquisada
#segundo parâmetro a msg caso não encontre
print(traducao)


##verificar se um item é alfabetíco
str.isalpha()#retorno True or False
for x in lista_texto:
    if x.isalpha() and x not in conjunto:
        print(x)



#AULA 12 **********************
#if, elif e else

idade = 18
if idade == 18:
    print('é 18')
    print('isso ainda está dentro do if')
print('não é 18')
#no if a edentação diz o que está dentro ou fora da condição

if idade > 18:
    print('maior que 18')
else:
    print('é diferente de 18')

if idade > 18:#se
    print('maior que 18')
elif idade == 18:  #senão se
        print('é 18')
else:
    print('menor que 18')

#operador diferente
if idade != 18:
    print('é diferente de 18')

#vazio ou zero são considerados falsos
#qq valor diferente disso é considerado verdadeiro
y = 0
if y:
    print('verdadeiro')
else:
    print('falso')





#AULA 13 **********************
#sexo = input('Digite o sexo M ou f:').lower()#lower se a pessoa digitar minusculo ou maiuscula

idade = int(input('digite a idade: '))
sexo = input('Digite o sexo M ou f:').lower()

if sexo == 'm':
    if idade < 18:
        print('homem menor de idade')
    else:
        print('homem maior de idade')

elif sexo == 'f':
    if idade < 18:
        print('mulher menor de idade')
    else:
        print('mulher maior de idade')
else:
    print('erro na entrada de dados')

#operador mod
x=4.5
y=2
print(x%y)#0.5

#operadores logicos and e or

if idade == 18 and sexo == 'm':
    print('18 anos e masculino')

if idade == 18 or sexo != 'f':
    print('ou tem 18 anos ou é masculino')

#AULA 14 **********************


#AULA 15 **********************
#while

x = 0
pessoas = []#isso é uma lista vazia

while x < 4:
    nome = input('Qual o seu nome?')
    x += 1
    pessoas.append(nome)#append vai adicionando elementos à lista

print(pessoas)


x = 0
pessoas = []#isso é uma lista vazia

while 'joao' not in pessoas:
    nome = input('Qual o seu nome?')
    x += 1
    pessoas.append(nome)#append vai adicionando elementos à lista

print(pessoas)

#para while, pode ser add um continue ou break
#o continue faz com que volte ao início do loop sem executar o que está abaixo
#o break força a saída do loop



x = 0
pessoas = []#isso é uma lista vazia

while 'joao' not in pessoas:
    nome = input('Qual o seu nome?')
    if nome == 'joao':
        break
    x += 1
    pessoas.append(nome)#append vai adicionando elementos à lista

print(pessoas)

#aula 16*******************************************
#loop for

compras = ['arroz', 'feijão', 'carne']#isso é uma lista

for i in compras:
    print(i)#resultado arroz, feijao e carne
#***********
nome = 'max'

for i in nome:
    print(i)#resultado m, a, x
#***********
vendas = [100, 200, 300]

total = 0

for i in vendas:
    total += i
    
print(total)#resultado 600
#***********

#dicionário
cores = {'verde': 'green',
         'branco': 'white',
         'vermelho': 'red'}

for i in cores:
    print(i)#resultado verde, branco e vermelho

cores = {'verde': 'green',
         'branco': 'white',
         'vermelho': 'red'}

for i in cores:
    print(cores[i])#resultado green, white e red

#***********

compras = [['arroz', 'feijão', 'carne'], ['sabonete', 'xampoo']]#isso é uma lista de lista

for i in compras:
    print(i)
#resultado
##['arroz', 'feijão', 'carne']
##['sabonete', 'xampoo']

for i in compras:
    for item in i:
        print(item)

#resultado
##arroz
##feijão
##carne
##sabonete
##xampoo

for i in range(0,10):
    print(i)

##resultado
##0
##1
##2
##3
##4
##5
##6
##7
##8
##9

#aula 17*******************************************
#Exercícios loops


repetir = 's'
fatura = []
total = 0

while repetir == 's':
    produto = input('Digite o nome do produto:')
    preco = float(input('Digite o valor do produto:'))
    fatura.append([produto,preco])
    total += preco
    repetir = input('Deseja comprar mais algum produto? S ou N').lower()

for i in fatura:
    print(i[0], '-', i[1])

#aula 18*******************************************
#Validação de dados

repetir = 's'
fatura = []
total = 0
valid_preco = False

while repetir == 's':
    produto = input('Digite o nome do produto:')
    try:#tenta realizar a operação
        preco = float(preco)

        if preco <= 0:
            print('o preço precisa ser maior que zero')
        else:
            valid_preco = True
    except:#se não conseguir realizar a operação
        print("Formato de preço inválido. Use apenas números e separe centavos com '.'")

##    while valid_preco == False:
##        preco = float(input('Digite o valor do produto:'))

    fatura.append([produto,preco])
    total += preco
    repetir = input('Deseja comprar mais algum produto? S ou N').lower()

for i in fatura:
    print(i[0], '-', i[1])


#aula 20*******************************************
#Funções

def nomedafunção():
    #comandos
    #comandos
#comandos fora da função


def mensagem():
    print('essa é uma função')

mensagem()#chamada da função

#***********

def mensagem(user):
    print('seja bem vindo, ', user, '!')

nome = input('qual o seu nome?').title() #title coloca primeira letra em maiúsculo

mensagem(nome) #resultado seja bem vindo, fulano!

#***********
def imc(peso, altura):
    valor_imc = peso / (altura*altura)
    return(valor_imc)
#fim da função

if imc(74, 1.82) > 32:
    print('obesidade')
else: print('tá de boa')


#aula 21e 22*******************************************
#Exercícios Funções

def imc(peso, altura):#calcula o imc
    imc = peso/ (altura*altura)
    return imc

def class_imc(sexo, peso, altura):
    valor_imc = imc(peso, altura)

    if sexo == 'm':
        if valor_imc < 20.7:
            return "Abaixo do peso"
        elif valor_imc >= 20.7 and valor_imc < 26.4:
            return "Peso Normal"
        elif valor_imc >= 26.4 and valor_imc < 27.8:
            return "Marginalmente acima do peso"
        elif valor_imc >= 27.8 and valor_imc < 31.1:
            return "Acima do peso ideal"
        elif valor_imc >= 31.1:
            return "Obesidade"
    else: return "erro de Cálculo"

    if sexo == 'm':
        if valor_imc < 19.1:
            return "Abaixo do peso"
        elif valor_imc >= 19.1 and valor_imc < 25.8:
            return "Peso Normal"
        elif valor_imc >= 25.8 and valor_imc < 27.3:
            return "Marginalmente acima do peso"
        elif valor_imc >= 27.3 and valor_imc < 32.3:
            return "Acima do peso ideal"
        elif valor_imc >= 32.3:
            return "Obesidade"
    else: return "erro de Cálculo"

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite seu sexo: M ou F').lower()
    if sexo != 'm' and sexo != 'f':
        print('valor inválido. digite M ou F.')
    else:
        valid_sexo = True
        print('\n')#pular linha

valid_peso = False
while valid_peso == False:
    peso = input('Digite o peso ex. 76.5')
    try:
        peso = float(peso)#converter pra float
        if peso <= 0 or peso > 350:
            print('Valor inválido. Número não pode ser 0 ou negativo nem acima de 350')
        else: valid_peso = True
        print('\n')#pular linha
    except:
        print('Use apenas números e separe os decimais com .')
        
        

valid_altura = False
while valid_altura == False:
    altura = input('Digite a altura ex. 1.8')
    try:
        altura = float(altura)#converter pra float
        if altura <= 0 or altura > 3:
            print('Valor inválido. Número não pode ser 0 ou negativo nem acima de 3')
        else: valid_altura = True
        print('\n')#pular linha
    except:
        print('Use apenas números e separe os decimais com .')
        
v_imc = str(imc(peso, altura))#converter em string para reduzir o número de casas decimais
c_imc = class_imc(sexo, peso, altura)

print('O seu imc é: ', v_imc[0:5])#slicing para reduzir o número de casas decimais
print('A sua classificação é ', c_imc)


#aula 23*******************************************
#criar e conectar módulos
#CONECTAR PROGRAMAS

import Nomedoarquivo as apelido

##comandos
#comandos

#chamada da função
Nomedoarq.Nomedafuncao


#aula 24*******************************************
#Módulos built-in
#módulos dos python

import math #módulo para operações matemáticas

math.ceil(3.2)#arredonda pra cima
math.floor(3.7)#arredondar pra baixo
math.fsum([1,2,3])#soma
vendas = [100,200,300]
math.fsum(vendas)
math.sqrt(16)#raiz quadrada


#*********************************
import time #módulo para hora e data

time.localtime()
hora = time.localtime().tm_hour
minuto = time.localtime().tm_min

print('Hora certa: ', hora, minuto)

time.clock()#mostra a quanto tempo a função foi chamada

inicio = time.clock()
fim = time.clock()
tempo = round(fim - inicio, 2)
#a função round arredonda as casas decimais, neste caso em duas casas


#aula 25*******************************************
#Módulos built-in
#módulos dos python

import random #módulo para número aleatórios

random.randint(0,10) #pega números de 0 a 10, neste caso

#****************criando um gerador de números - pra mega Sena
import random
def megasena():
    jogo = []
    while len(jogo) < 6:#enquanto jogo for menor que 6 - leg é comprimento, neste caso a qtd de elementos da lista
        num = random.randint(1,60)#escolher qq número entre 1 e sessenta
        if num in jogo:
            continue
        else:
            jogo.append(num)
    print(sorted(jogo))#sorted, função nativa do python - ordena lista

megasena() #chamada da função

#opção mais fácil
import random as r
num_sorteados = r.sample(range(0,80),6)
sorted(num_sorteados)


#***********
alunos = ['joao', 'maria', 'pedro']
random.choice(alunos)#escolhe elementos, aleatoriamente na lista
#numpy tb oferece método para a escolha de um número aleatório
np.random.choice([0,1,2])

#***********
random.sample(alunos, 2)#pega 2 elementos da lista


#aula 26*******************************************
#PIP gerenciador de comandos

pygames -> página para games em python

wxpython -> para estrutura de programas - layout visual inface com usuário

sqlalchemy -> para tratar com base de dados

beautiful soup documentantation - para web screping - para extrair conteúdos da internet

scypi.org 

#aula 26*******************************************

#montar um gráfico com módulo matplotlib.pyplot
#após a chamada da bliclioteca, incluir o comando abaixo para garantir que o gráfico será executado no jupyter e não em outra janela
%matplotlib notebook
%matplotlib inline

x = ['a', 'b', 'c', 'd', 'e']#RÓTULOS
y = [1,2,3,4,5]#VALORES

plt.xticks(x,y)#sticks cria legendas. 
plt.show()

#salvar img com matplot
# store to file
plt.savefig("img/us_wine.png", format="png")

#criando um gráfico de linhaimport 
matplotlib.pyplot as plt
%matplotlib inline
x = [1,3,5]
y = [1,4,6]
plt.plot(x,y)
plt.ylabel('eixo Y')
plt.xlabel('eixo x')
plt.title('título')
plt.show()

#gráfico barras
plt.bar(x,y, label ='barras', color = 'r')

#gráfico barras duplo
plt.bar(x,y, label ='barras', color = 'r')
plt.bar(x2,y2, label ='barras2', color = 'y')

#histograma
plt.hist(x,y)

#scatter - pontinhos
plt.scartter(x,y)

#pizza
fatias = [7,2,2,13]
atividades = ['dormir', 'comer', 'trabalhar', 'passear']
cores = ['c','m', 'r', 'k']
plt.pie(fatias, labels=atividades, colors = cores)
plt.show()

#vários tipos de gráficos subplots aula MATPLOTLIB GRÁFICOS A PARTIR DO NUMPY da DSA - curso python fundamentos 04:06'

#gráficos 3d from mpl_toolkits.mplot.azes3d import axes3D


#SciPy - scientific python

#Livro Python Básico*******************************************
#for - página 49
nomes = ['jose', 'maria', 'pedro']
for i in nomes:
    print(i)
#resultado: jose, maria e pedro

dicionario = {'nome':'max', 'profissão': 'analista'}
for i in dicionario.keys():
    print(i)#resultado: nome e profissão

for i in dicionario.values():
    print(i)#resultado: max e analista

for i in dicionario:
    print(i)#resultado: nome e profissão

for i in range(5):
    print(i)#resultado 0,1,2,3,4

for i in range(3, 10):
    print(i)#resultado 3,4,5,6,7,8,9

#break**************
# sai completamente do loop
for i in range(3, 10):
    if i == 5:
        break
    print(i)#resultado: 3,4

#contando a quantidade de itens de um dicionário
len(list(times['Times']))


#continue**************
#não executa mais nada naquele ciclo e parte para o próximo
for i in range(3, 10):
    if i == 5:
        continue
    print(i)#resultado: 3,4,5,6,7,8,9

#Livro Python Básico*******************************************
#while - página 53


i=0
while i < 5:
    print(i)
    i += 1
    #resultado 0,1,2,3,4


while True:
    nome = input("Digite o seu nome ou sair para sair:")
    if nome.lower() == "sair":
        break
    else:
        print("Nome digitado %s!" % nome.capitalize())

#lower() transforma tudo em minúsculo
#upper() transformatudo em maiúsculo
#capitalize() transforma a primeira letra em maíuscula, demais serão colocadas em minúsculo


#Livro Python Básico*******************************************
#funções - página 56

#função sem retorno e sem parâmetros
def imprime():
    print("Imprimiu")
imprime()#resultado: imprimiu


#função com retorno e com parâmetros
def cal(num):
    valor = num * 2
    return valor

base = 10
print(cal(base))#resultado: 20

#ou
def cal(num):
    valor = num * 2
    return valor
print(cal(10))#resultado: 20

#ou
def meunome(nome, idade):
    print("Meu nome é %s e tenho %d anos!" % (nome, idade))

meunome(nome="Max", idade=38)

def meunome(nome, idade):
    print("Meu nome é %s e tenho %d anos!" % (nome, idade))

meunome(idade=38, nome="Max")

#argumento *args e **kwargs
# *args com esse pode-se acessar os parâmetros como uma lista
# 1 * define que não se sabe quantos parâmetros serão passados. Serão passados quantos parâmetros quanto o necessário
#**kwrags pode-se acessar os parâmetros como um dicionário

def print_tudo_2_vezes(*args):
    for parametro in args:
        print(parametro + "! " + parametro + "!")
    print_tudo_2_vezes("Olá", "Python", "Felipe")
    > Olá! Olá!
    > Python! Python!
    > Felipe! Felipe!

def print_info(**kwargs):
for parametro, valor in kwargs.items():
print(parametro + " - " + str(valor))
print_info(nome="Felipe", idade=30, nacionalidade="Brasil")
> nacionalidade - Brasil
> nome - Felipe
> idade - 30

#Livro Python Básico*******************************************
#módulo - página 60

def meunome(nome, idade):
    print("Meu nome é %s e tenho %d anos!" % (nome, idade))

#meunome(idade=38, nome="Max")


#importando apenas a função que deseja-se usar:

from nomedomodulo import nomedafuncao


#Livro Python Básico*******************************************
#datas - página 67

from datetime import date

print(date.today())

hoje = date.today()

hoje2 = hoje.day, hoje.month
print("hojé é: %d-%d" % hoje2)

#Python para Iniciantes - Udemy*******************************************
#aula 11
#pass, break econtinue

num = 10
While True:
    num=num-1
    if (num==4):
        continue#continua a execução do código
    print(num)
    if (num==3):
        break#interrompe a execução
pass#apenas passa a frente sem interferir em nenhuma parte do código
    
    
#Curso Python Web Scraping*******************************************
#aula 8 - meu primeiro web scraping

from urllib.request import urlopen
http = urlopen("http://www.google.com")
print(http.read())

#O python oferece duas excelentes ferramentas para realizar as tarefas
#requests da biblioteca urllib para carregar as páginas e
#beautifulSoup para realizar a análise das informações 

#Curso Python Web Scraping*******************************************
#aula 9 - EXPRESSÕES REGULARES

#o módulo re do Python fornece suporte a expressões regulares
#exemplo

variavel = re.funcao(padrao, string, flag)
#padrao = expressões regulares
#string é o texto onde está sendo procurado

import re

texto = ("bb Esta é uma aula de Pythoon. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula.")

#*******SEARCH************************
#search procura o padrão dentro do texto
#search retorna A PRIMEIRA OCORRÊNCIA ENCONTRADA - retorna a POSIÇÃO
resultado = re.search("Esta", texto)#resultado;<re.Match object; span=(0, 4), match='Esta'>
# span(0, 4), significa a partir da primeira posição e menor que a 4ª
print(resultado)


import re
padrao = "Esta"
texto = ("Esta é uma aula de Pythoon. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula.")

resultado = re.search(padrao, texto)

print(resultado)#resultado: None - no caso o pardrão era igual a abacaxi

#*******GROUP************************
#PARA RETORNAR O CONTEÚDO USA A FUNÇÃO group
print(resultado.group())#resultado: Esta


#*******CARACTERES ESPECIAIS - PONTO ".")************************
#ELE IRÁ ENCONTRAR QUALQUER(o 1º caracter)CARACTER EXCETO O ENTER. Para localizar enter usar DOTALL
import re
padrao = "."
texto = ("Esta é uma aula de Pythoon. Esta aula é sobre Expressões Regulares. "
         "Espero que goste desta aula 9999 528.")
resultado = re.search(padrao, texto)
print(resultado.group())#RESULTADO: E

#*******CARACTERES ESPECIAIS - circonflexo "^")************************
#LOCALIZA UM PADRÃO NO INÍCIO DO TEXTO
padrao = "^Esta"
#RESULTADO: Esta

#*******CARACTERES ESPECIAIS - cifrão "$")************************
#localiza o padrão do final do texto
padrao = "aula$"
#Resultado: aula.

#*******CARACTERES ESPECIAIS - contrabarra "\")************************
#Permite usar caracteres especiais como se fossem comum
padrao = "\."


#*******CARACTERES ESPECIAIS - COLCHETES "[]")************************
#RANGE DE CARACTERES
padrao = "\."

#*******CARACTERES ESPECIAIS - findall************************
#função que retorna todas as ocorrências
padrao = "[aéeP]"
resultado = re.findall(padrao, texto)
print(resultado)#resultado: ['a', 'é', 'a', 'a', 'a', 'e', 'P', 'a', 'a', 'a', 'é', 'e', 'e', 'e', 'e', 'a', 'e', 'e', 'e', 'e', 'e', 'a', 'a', 'a']


padrao = "[A-Z]"
resultado = re.findall(padrao, texto)
print(resultado)#resultado: ['E', 'P', 'E', 'E', 'R', 'E']

padrao = "[0-9]"
resultado = re.findall(padrao, texto)
print(resultado)#resultado: ['9', '9', '9', '9', '5', '2', '8']

#* retorna uma ou mais ocorrência "a*"
#+
# ? diz que aquele padrão não é obrigatório
padrao = ([0-9{2}][\.]?[0-9]{3})#diz que o ponto não é obrigatório
#\d busca por caractesres numéricos
#\D traz todos os caracteres que NÃO são números
#\s qq caracter de espaçamento "[\t\n\r\f\v]"
#\S qq caractere que NÃO SEJA DE  ESPAÇAMENTO
#\w caractere alfanumériico ou sublinhado "[a-zA-Z0-9_]"
#\W caractere que não seja alfanumérico ou sublinhado "[^a-zA-Z0-9_]"
#{} quantidade de ocorrência
padrao = "\d{2}"# localiza caracteres números com dois dígitos
# | ou lógico
# () grupo de expressões
padrao = "(a) | (\d)"#localizar a ou números

padrao = re.compile("e", re.IGNORECASE)#vai localizar todas as ocorrências, independente se maiúscula ou minúscula


#expressões regulares  re.sub ======================================================
#substituir caracteres
texto = '# - texto para, teste de / caracteres'
print(texto)## - texto para, teste de / caracteres
import re
texto = re.sub("[a-zA-Z0-9_]", '', texto)
print(texto)## -  ,   / 





#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 11 - Servidor web python
#no cmd, para iniciar o servidor web nativo do python
python -m http.server


#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 12 - EXECUTANDO O BeautifulSoup

#executar o servidor pelo cmd
pytho -m http.server

#importar a bliblioteca
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://localhost:8000/teste.html')#carrega o arquivo
bsObj = BeautifulSoup(html.read(), "html.parser")#ler o arquivo

print(bsObj.h1)#imprime o primeiro h1
print(bsObj.title)#imprime o títula da pág
print(bsObj.find_all("h1")#imprime todas as tags h1

for link in bsObj.find_all('a'):
      print(link)

for link in bsObj.find_all('a'):
      print(link.get('href'))



#a requests executa requisições GET e obtem o código HTML das páginas




#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 14 - Mais sobre o BeautifulSoup

# get_text = retorna todo o texto de uma página
print(bsObj.get_text())

# .tag a primeira ocorrência da tag informada
print(bsObj.title)#mostrará o conteúdo da primeira tag title informada

# .tag.name = retorno o nome da tag
# .tag['atributo']
print(bsObj.body['class'])
print(bsObj.button['type'])

#id
print(bsObj.find(id='descrição'))

#biblioteca para expressões regulares
import re

#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 15 - Mais sobre o BeautifulSoup

#expressões regulares ajudam quando há um padrão do que pretende-se localizar


#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 17 - Biblioteca LXML

#lendo arquivo xml
import lxml import etree

funcionarios = etree.parse("funcionarios.xml")#ler arquivo

#imprimindo arquivo
print(funcionarios.find("funcionario"))#aqui será impresso o objeto funcionário
#o objeto(tag) funcionário pertence ao arquivo

print(funcionarios.getroot().find("funcionario"))

#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 18 - Instalando Scrapy



#lxml precisa de algumas bibliotecas C, sendo assim é necessário intalar o Visual C++ 14.0
#end: http://landinhub.visualstudio.com/visual-cpp-build-tools
#1º passo instalar Visual C++

#2º passo instalar o Scrapy no CMD
# $ pip install scrapy

#3º passo importa bibliteca scrapy via cmd
#python
#import scrapy
#scrapy version

#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 19 - Trabalhando com Scrapy - parte 1

#1º configirar projeto scrapy cmd:
      #$ scrapy startproject nome_do_projeto
      
#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 19 - Trabalhando com Scrapy - parte 2

#trabalhando com scrapy shell
#abrindo o scrapy shell cmd
#scrapy shell "http://paginaquequeremosabrir.com"
    
      
#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 20 - Trabalhando com Scrapy - parte 3 - gerando arquivos

#$ scrapy crawl nome_da_classe -o nomedoarquivo.formato

#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 21 - Trabalhando com Scrapy - parte 4 - seguindo links

#1. criar o projeto $ scrapy starproject nomedoprojeto
#2. abrir o projeto
import scrapy
class QuotesSpider (scrapy.Spider):
      name = "citacoes"
      star_urls = ['http://quotes.toscrape.com/page/1/']

#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 24 - APIs - parte 1

#testar métodos: get, post, put e delete de apis: https://hurl.it


#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 25 - APIs - parte 2

#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 26 - APIs - parte 3

#apis google
#https://console.developers.google.com

#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 27 - Armazenando arquivos


#baixar arquivos à partir de qq qualquer url
#urllib.request.urlretrieve

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

site = "http://www.destemperados.com.br"
html = urlopen(site+'receitas')
bsobj = BeautifulSoup(html)
imagemLocation = bsObj.find("a", {"title": "Destemperados"}).find("img") ["src"] urlretrive(site+imagemLocation, "teste.jpg")

#xiste a biblioteca csv para trabalhar (ler e escrever) com arquivos csv

#para ler arquivos dicionários: utilizar DictReader

import csv

estado = []
with open("estados.csv", encoding="utf-8") as arq:
      reader = csv.DictReader(arq)
      for linha in reader:
      print(linha['Nome'] + " - " + linha['Capital'])

#para escrever utilizando dicionário

import csv

try:
      arq = open("pessoas.cvs", "w", newline="")
      cabecalho = ["nome", "sobrenome"]
      writer = csv.DictWriter(arq, fieldnames=cabecalho)
      whiter.writeheader()
      writer.writerow("nome": "Max", "sobrenome":"Pinheiro")
final:
      arq.close()

#escrevendo linha a linha
with open('arquivo.csv', 'w') as arq:
      writer = csv.writer(arq)
      writer.writerow('primeira', 'segunda')
      writer.writerow(20, 10)

#transformando um arquivo csv em uma lista
with open('arquivo.csv', 'r') as arq:
      leitor = csv.reader(arq)
      dados_lista = list(leitor)
print(dados_lista)

#scraping em tabela html e salvando em csv


#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 31 - Conectando ao banco MySQL com MYSQL connector/Python

#importando o connector - só dá certo caso, no momento da instalação, tenha habilitado a instalação do connector

import mysql.connector

#2ª opção baixar o conector direto do site do MySQL
#3ª forma usando o pip
pip install mysql-connector-python

#acessar mysql usando o python

import mysql.connector

conexao = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='agenda')

conexao.close()

#outra forma de conexão

from mysql.connector import connection

conexao = connection.MySQLConnection(user='root', password='1234', host='127.0.0.1', database='agenda')

conexao.close()

#os dois métodos são válidos

#tratando erros

import mysql.connector
from mysql.connector import error code

try:
      con = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='agenda')
except mysql.connector.Error as erro
      if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('acesso negado')
      elif erro.errno == errorcode.ER_BAD_DB_ERROR:
          print('BANCO DE DADOS NÃO EXISTE')
      else:
          print(erro)
else:
      con.close()



#usando kwargs **

import mysql.connector
    #criando um dicionário
config = {'user': 'root',
          'password': '1234',
          'host':'127.0.0.1',
          'database':'agenda'
    }
conexao = mysql.connector.connect(**config)
conexao=close()


#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 32 - Executando instruções SQL com Python

#importando o MySQL connector/Python
import mysql.connector

#criando o objeto de conexão através do connect com os parâmetros:
#usuário, senha, servidor e base de dados
#o connect retorna um objeto MySQLConnection
conexao = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='agenda')

#criando um cursor
#cursor é uma estrutura de controle que permite percorrer
#registros, além de facilitar a adição e remoção de registros do banco de dados
cursor = conexao.cursor()
#montando uma string com insert
inserir_contato = ("insert into contatos (nome, telefone, celular) values ('Pateta', '(61)1251 1212', '(21) 2154 12155')")
#executando o comando insert
cursor.execute(inserir_contato)
#gravando a informação permanentemente
conexao.commit()
#fechando o cursor
cursor.close()
#fechando a conexão
conexao.close()

#pode ser utilizado uma tupla para passar os dados
inserir = 'insert into contatos (nome, telefone, celular) values (%s, %s, %s)'
dados = ('tio patinhas', '(61)9999-8888', '(61)5555-1111')
cursor.execute(inserir, dados)


#pode também ser usado um dicionário
inserir = 'insert into contatos (nome, telefone, celular) values (%(a)s, %(b)s, %(c)s)'
dados = {'a':'tio patinhas',
         'b'':(61)9999-8888',
         'c':'(61)5555-1111'}
cursor.execute(inserir, dados)

#para realizar uma consulta e mostrar os dados
import mysql.connector
conexao = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='agenda')
cursor = conexao.cursor()
consulta = ("select nome, telefone, celular from nometabela where nome like 'M%'")
cursor.execute(consulta)

for (nome, telefone, celular) in cursor:
      print(f"Nome: {nome}, telefone: {telefone}, celular: {celular}")
cursor.close()
conexao.close()


#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 33 - Armazenando conteúdo do scraping em MySQL

#importando as biblios para conexão
from urllib.request import urlopen
from bs4 import Beatifulsop
import randomimport mysql.connector
import re

dados_conexao = {"user": "root", "password":"1234", "host": "127.0.0.1", "database": "dados"}
conexao = mysql.connector.connect(**dados_conexao)
cursor = conexao.cursor()
def gravar (titulo, url, conteudo):
      cursor.execute("insert into paginas (titulo, url, conteudo) values (%s,%s,%s)", (titulo, url, conteudo))
      conexao.commit()

#fazendo o scraping
def getLinks ()


#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 34 - Lendo documentos - leitura de arquivo de texto

#para a leitura do arquivo
from urllib.request import urlopen
pagina - urlopen('endereco.txt')
print(pagina.read())

#neste caso não usa-se BeautifulSoup, por que não há marcação html


#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 35 - Lendo documentos - leitura de arquivo CSV

from urllib.request import urlopen
from io import String IO
import csv

url = input ("informe o caminho do arquivo CSV:")
dados = urlopen(url).read().decode(encoding="utf-8", errors='ignore')
arqDados = StringIO(dados)#carrega o arquivo de dados em memória
csvReader = csv.reader(arqDados)
#pode se utilizar o DictReader para retornar ao invés de linhas um dicionário
    #csvReader = csv.DictReader(arqDados)

for linha in csvReader:
      print(linha)


#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 36 - Lendo documentos - leitura de arquivo PDF

#biblioteca PDFMiner3k

#1º passo instalar a biblioteca
#cmd $ pip install pdfminer3k

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

#abrir arquivo PDF local
from io import open
#abrir arquivo PDF online
from urllib.request import urlopen


#LAParams
      #define os parãmetros que serão passados para a função TextConverter.
      #line_overlap=0.5 (sobreposição de linha)
      #char_margin=2.0 (margem do caracter)
      #line_margin=0.5 (margem da linha)
      #word_margin=0.1 (margem da palavra)
      #paragraph_indent=None (identificação de parágrafo)

#TextCoverter
      #converte o conteúdo do PDF em texto
#HTMLConverter
      #converte o conteúdo do PDF em HTML
#XMLConverter
      #converte o conteúdo do PDF em XML

      
#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 37 - Lendo documentos - leitura de arquivo DOCX

#instalar biblioteca python-docx
pip install python-docx

import docx
doc = docx.Documento('arquivo.docx')
for a in doc.paragraphs:#percorre os parágrafos do documento
     print(a.text)#imprime o conteúdo 


#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 37 - Lendo documentos - leitura de arquivo xlsx

#instalar biblioteca openpyxl
$ pip install openpyxl

from openpyxl import load_workbook

#contar strings
lista = ['m','a',2]
for x in lista:
    print(x)
    if x == str():
        print(len(x))#resultado 1


#fatiando
texto = 'texto pronto -'
texto.split()
#saída ['texto', 'pronto', '-']

texto = 'texto'
texto.split()#saida ['texto']


#remover caracteres especiais
#pandas, aqui já foi passado o arquivo xlsx para train[]
train['new_justifi'] = train['justificativa'].str.replace('[^\w\s]','')


#função head() do pandas - exibe as 5 primeiras linhas


    
#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 39 - Lendo json

import json #biblioteca build in

#criando o json----------------------------------------------------------------------------

dados = {'chave': 'valor',
         'chave2': 'valor2'}

#método dumps converte o dicionário em json

dados_json = json.dumps(dados)

print(dados_json)

#salvando em formato json

with open('nomearquivo.json', 'w') as arq:
      arq.white(json_dumps(dados))

#lendo json----------------------------------------------------------------------------
import json

with open('nomearquivo.json', 'r') as arq:
      conteudo = arq.read()
      dados_json = json.loads(conteudo)#deserializa o json
      print(dados_json['chave2'])#imprimindo o conteúdo da chave 2
      

#lendo novo arquivo ----------------------------------------------------------------------------

import json

with open('arqjson.json', 'r', encoding='utf-8') as arq:#utf-8 para leitura correta com caracteres especiais
      conteudo = arq.read()
      print('*' * 50)
      print('conteudo do arquivo: \n', conteudo)
      dados_json = json.loads(conteudo)
      print('json completo: \n', dados_json)
      print('*' * 50)
      print('primeiro objeto (dados_json[0]) \n', dados_json[0])
      print('*' * 50)
      print('loop em todso os objetos:')
      for dados in dados_json:
      print('curso: ', dados['indice'], )

#lendo json direto da internet ----------------------------------------------------------------------------

import json

from urllib.request import urlopen

dados = urlopen('http://endereço_do_arquivo_na_internet.json').read().decode('utf8')
dados = json_loads(dados)

print(dados)


#imprimir por índice arquivos com objeto dentro do json----------------------------------------------------------------------------

print(dados-json['nomeobjt'][0])#imprindo índice 0 do objeto nomeobjt
print(dados-json['nomeobjt'][0]['chave'])#índice 0, imprimir o valor da chave x


#copiando o conteúdo txt para arquivo json

import os
arq_fonte = 'caminho/dados.json'
arq_destino = 'caminho/json_dados.txt'

with(arq_destino, 'w').write(open(arq_fonte, 'r').read())

#******CURSO UDEMY - PYTHON WEB SCRAPING************************
#AULA 40 - limpando dados



#verificar a versão do pandas instalado, via jupyter
In [76]: import pandas as pd

In [77]: pd.__version__
Out[77]: '0.12.0-933-g281dc4e'

 pd.show_versions(as_json=False)


#REMOVER CARACTERES ESPECIAIS
import re
texto = 'novo texto para - testar o que é carcter # especial;/_ saúde'
string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', texto)
print(string_nova)

#strings são imutáveis

====================================================================================================================
#******CURSO UDEMY - Mineração de Emoção em textos com Python e NLTK************************
#AULA 01 -

#stemming - radical das palavras
#frequência das palavras n-

#******CURSO UDEMY - Mineração de Emoção em textos com Python e NLTK************************
#AULA 06 - mineração de emoções

#mineração de emoções fazem parte dos algorítmos de CLASSIFICAÇÃO

#pode ser classificar por POLARIDADE: POSITIVO - NEUTRO - NEGATIVO

#2ª tÉCNICA CLASSIFICAÇÃO POR EMOÇÃO: surpresa, alegria, tristeza, medo, nojo e raiva (poul ekman)



#******CURSO UDEMY - Mineração de Emoção em textos com Python e NLTK************************
#AULA 07 - Classificação

#Atributos previsores (histórico): utilizados para fazer a previsão

#exemplo - ATRIBUTOS PREVISORES
Historia do credito: Ruim, desconhecida, boa
Dívida: Alta, média, baixa
Garantias: nenhuma, adequada
Renda mensal:< 10000, >=10000, etc

#Saída: ATRIBUTO CLASSIFICADOR ou classe/meta
Risco: alto, moderado, baixo


#divide-se os dados para treinamento(90%) e teste(10%)

#atualizar pacotes
import nltk

nltk.download()

#stemmer para palvras em inglês-------------------------------------------------
from nltk.stem import PorterStemmer
st = PorterStemmer()
palavra = 'booking'
palavra_com_stemming = st.stem(palavra)
print(palavra_com_stemming)#'book'

      

#dividir uma frase, usando split"."-------------------------------------------------

texto = 'Este texto é para teste. Vamos separar a frase em duas.'
texto.split('.')
#['Este texto é para teste', ' Vamos separar a frase em duas', '']


#dividir uma frase, usando nltk"."-------------------------------------------------
import nlkt
texto = nltk.tokenize.sent_tokenize(texto)

#dividir uma frase, usando nltk toke-------------------------------------------------
import nlkt
texto = nltk.word_tokenize(texto)

#dividir uma frase, classificando-------------------------------------------------
import nltk
texto = nltk.pos_tag(texto) #são verbos, adjetivos etc

#PYTHON PROGRAMMING WITH PORTUGUESE
      #www.nltk.org/howto/portuguese_en.html

#instalando biblioteca stopword em português
import nltk
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')


#removendo stopwords manualmete-----------------------------------------------------
base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

#stopwords

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

#função para remover stopwords

def removerstopwords(texto):
    frases=[]
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwords]#ou usando stopwordsnltk abaixo nltk
        frases.append((semstop, emocao))
    return frases

print(removerstopwords(base))
#-----------------------------------------------------

#removendo stopwords com nltk

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
print(stopwordsnltk)


#******CURSO UDEMY - Mineração de Emoção em textos com Python e NLTK************************
#AULA 15 - stemming - extraindo o radical das palavras

stemmer = nltk.stem.RSLPStemmer() #específica para a língua portuguesa

#função para aplicar stemming e retirar stopwords

def aplicastemmer(texto):
      stemmer = nltk.stem.RSLPStemmer()
      frasesstemming = []
      for (palavras, emocao) in texto:
          comstemming = [str(stemmer.stem(p)) for p in palavras.split() if not in stopwordsnltk]
          #stem() função para efetivamente retirar o radical
          frasesstemming.append((comstemming, emocao))
      return frasesstemming

frasescomstemming = aplicastemmer(base)
print(frasescomstemming)


#AULA 16 - listagem das palavras

def buscapalavras(frases):
      todaspalavras =[]
      for (palavras, emocao) in frases:
          todaspalavras.extend(palavras)#extend - adicona uma lista de itens ao final de outra lista
      return todaspalavras

palavras = buscapalavras(frasescomstemming)   
print(palavras)

#AULA 16 - extração das palavras - frequência
#frequência
      
def buscafrequencia(palavras):
      palavras = nltk.FreqDist(palavras)#FreqDist() - é a função do nltk que faz a busca da distribuição das palavras
      return palavras

frequencia = buscafrequencia(palavras)
print(frequencia.most_common(50))#resultado será as 50 primeiras palavras

#extraíndo as palavras únicas
def buscapalavrasunicas(frequencia):
      freq = frequencia.keys()
      return freq

palavrasunicas = buscapalavrasunicas(frequencia)

#aula 18 - extração das palavras de cada frase

def extratorpalavras(documento):
      doc= set(documento)
      caracteristicas = {}
      for palavras in palavrasunicas:
          caracteristicas['%s' % palavras] = {palavras in doc}  
      return caracteristicas

carcteristicasfrase = extratorpalavras(['am', 'nov', 'dia'])
print(carcteristicasfrase)      

#aula 19 - extração das palavras de TODAS as frases
#usando o apply.features

basecompleta = nltk.classify.apply_features(extratorpalavras, frasescomstremming)
print(basecompleta)


#salvando o arquivo excel
#baseContratos.to_excel('C:/Users/f7098849/Documents/Faculdade_Pos_IA/IA_2019/Intro_IA/base_contratos1.xlsx', sheet_name='Planilha1')

#******CURSO UDEMY - Mineração de Emoção em textos com Python e NLTK************************
#AULA 21 - naive_bayes I

#algorítimo de probabilidade
#aplicações: filtros de spam; mineração de emoções; separação de documentos; 

#******CURSO UDEMY - Mineração de Emoção em textos com Python e NLTK************************
#AULA 26 - classificando textos com naive_bayes

#controi a tabela de probabilidade
classificardor = nltk.NaiveBayesClassifier.train(basecompleta)   
print(classificardor.labels())#saída: alegria, medo 
print(classificardor.show_informative_features(5))


      

#REMOVENDO STOPWORDS stopwords ===============================================================
    for x in range(0,tamBase):
    lista = []
    for y in list(baseContratos['objeto'][x].split()):
        if y not in list(stop['stop']):
            lista.append(y)
    baseContratos['objeto'][x] = lista


#******CURSO UDEMY - Mineração de Emoção em textos com Python e NLTK************************
#AULA 30 - matriz de confusão conceito

#comparação de precisão
      por cenário/contexto
      por numero de classes
      por zero regras(maximum posteriori)



#REMOVENDO acentos com normalize ===============================================================
from unicodedata import normalize
texto = 'esse, é um texto #$ com caracteres / espéciais. cão?'
texto = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')



#Para a listagem dos pacotes instalado, utilizamos o comando pip freeze:



#percorrer duas listas com um for ==================================================================

nomes = ['joao','jose', 'maria']
idade = [25, 50, 75]

for x in (nomes, idade):
	print(x)

['joao', 'jose', 'maria']
[25, 50, 75]



#CLASSIFICAÇÃO VETORIAL DE SUPORTE LINEAR==================================================================
      ##CLASSIFICANDO TIMES POR IMAGE
      ##fonte vídeo youtube

import cv2
import numpy as np
import sklearn.svm import SVC
import sklearn.svm import SVR
      
#abrir a img
time = cv2.inread('time.png')
print(time.shape)

#Reduzir o tam da img pra facilitar o processamento
time_reduzido = cv2.resize(time, (10,10))
print(time_reduzido.shape)

#unificar as imgs em uma única matriz

x = np.concatenate(time, time_n, axis=0)
print(x.shape)

#eixo y

y = [1,2,3,4]
y = np.array(y)
y = y.reshape(-1)

#dividir a matriz em 4 partes iguais
x = x.reshape(len(y), -1)
print(x.shape)


#criar o modelo
clf_lin = SVC(kernel='linear')
svr_lin = SVR(kernel='linear')

#treinando
clf_lin.fit(x, y)

#predição
predicao = clf_lin.predict(time.reshape(1,-1))

#verificando score
score = clf_lin.score(x,y)

print(predicao)
print(score)      

#imprimir a img
cv2.imshow(img)#
cv2.waitKey(0)
      
#nltk separar palavras=======================================

#biblioteca capaz de separar palavras de um texto - fonte: livro machine learning - introdução á classificação
import nltk
nltk.download('punkt')
nltk.tokenize.word_tokenize('esta frase será separada !! veja como, fica')
#

import nltk
frase = 'Python eh uma linguagem fenomenal'
frase
palavras = nltk.word_tokenize(frase)
palavras


#wxpython=======================================
      #interface GUI desktop

#instalar
pip install wxpython

#importar a bibli
import wx

app = wx.App(False) #criar aplicação / False não exibe erros na janela

frame = wx.Frame(None, wx.ID_ANY, "window title")#criar a janela - None (se pertence a alguma outra janela) - segundo parâmentro é o ID da janela

frame.Show(True)#mostra a janela

app.MainLoop()#para que a aplicação não abra e feche imediatamente


##criando um editor de texto disponível em youtube: WxPython - 1 - Introdução

import wx

class Myframe(wx.Frame):
      def __init__(self, parent, title):
          wx.Frame.__init__(self, parente, title=title, size=(200,100))
          self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
          self.Show(True)


app = wx.App(False)
frame = MyFrame(None, "Small editor")
app.MainLoop()
           

    
#PANDAS=============
      #resumir os dados de uma coluna
      #resumo da coluna
dados['clusters'].value_counts()

#resumo da coluna, visão % percentual
dados['clusters'].value_counts(normalize=True)




#PANDAS=============
      #excluir/deletar uma coluna
del df['label-da-coluna']

#atribuis de um grupo de colunas para uma variável
name_chave = dados.iloc[:,1:3]#serão atribuídos todos os valores da 2a e 3a coluna
#ou
name_chave = dados.iloc[:,1:3].values

#loc e iloc
#são métodos para resgate de dados
#loc:
#Este método é primariamente baseado nas labels da colunas, porém podemos utilizar com um array booleano também.
df.loc[<linhas>, <colunas>]
df.loc[[5]]#retorna todas as colunas da linha 5
df.loc[[5:8]]#retorna todas as colunas da linha 5 a 8

# Colunas:
df.iloc[:,0] # Todos os dados da primeira coluna do dataset
df.iloc[0:5,-1] # Do primeiro ao quinto dado da última coluna

#Series
from pandas import Series
#são arrays unidimensionais
serie = pd.Series([10,10,10], index=['a', 'b', 'c'])#index é opcional
serie
'''
a    10
b    10
c    10
'''
#mostrar valores de uma série
serie.values

#mostrar os indices de uma série
serie.index

serie[serie<10]

#pandas com dicionário
dict = {'futebol': 'Romário', 'Basktball':'Magic', 'Tenis': 'Guga'}
dicio = pd.Series(dict)
dicio
'''
futebol      Romário
Basktball      Magic
Tenis           Guga
dtype: object
'''
#verificar se há um valor nulo
serie.isnull()
serie.notnull()

#dataFrames
from pandas import DataFrame

data = {}
obt = DataFrame(data)

data = {'Estados': ['SP', 'DF','ES'],
       'População': [10000, 5000, 5500]}

local = pd.DataFrame(data)
local['Estados']
#ou
local.Estados

#unir dois dataframes com pandas

x = pd.DataFrame(dados1)
y = pd.DataFrame(dados2)
xy = pd.merge(x,y, on='nomedacolunabase')

#criando uma série temporal (datas) com pandas
tempo = pd.date_range('01/07/2019', periods=10, freq='D')

#K-MEANS========================
labels = kmeans.labels_ #retorna os labels para cada instância - CLASSES

#NUMPY=======================
#GERAR UM ARRAY
y = np.arange(0,41)# DO 0 ATÉ 40
#ou com a função range(start, stop, step)
y = range(0, 11,1)#saída: range(0,11)

#para fazer uma cópia de um array
a = b.copy()
#caso simplesmente se faça uma atribuição (=) as eventuais alterações servirão para os dois
#outra maneira de fazer uma cóia
c = b.flatten()

c dataFrame, ao longo do  EIXO 1
df = pd.concat([df1, df2], axis=1)

import numpy as np#ou
from numpy import * #importa tudo, não recomendado
np.__version__#consultar a versão

#criando um array
#array conjunto de elementos DO MESMO ITIPO
#array temo muito mais métodos que uma lista
vetor = np.array([x for x in range(0,10,1)])
vetor #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#ou
vetor = np.arange(0,10,1)

#calculo da soma acumulada
vetor.cumsum()#array([ 0,  1,  3,  6, 10, 15, 21, 28, 36, 45], dtype=int32)

vetor[0]=100

#shape verificando as dimensões
vetor.shape #(10,)

#criando um range
vetor2 = np.arange(0,10,2)#start, stop, step
vetor2#[0 2 4 6 8]

x= np.zeros(10)#criar matriz preenchidas com zeros
x= np.eye

#matriz
matriz = np.array([0,1,2],[9,8,7])#matriz de duas dimensões
matriz.shape#(2,3)
matriz.size#(6)
matriz.ndim#2 = total de dimensões

#randomico
rand = np.random.rand(10)#10 elementos float randomicos

#média
v = [0,1,2,3,4]
print(np.mean(v))#2.0

#raiz quadra
v = [0,1,2,3,4]
print(np.sqrt(v))

#desvio padrão
v = [0,1,2,3,4]
print(np.std(v))#1.4142135623730951
#desv pad baixo indica que os dados tendem a estar próximos da média
#desv pad alto indica qiue os dados estão espalhados por uma gama de valores

#soma
v = [0,1,2,3,4]
print(np.sum(v))#10

#produto
v = [0,1,2,3,4]
print(np.prod(v))#0

#slice de array
array = np.arange(0,10,1)
array[2:8:2]#[2,4,6]

#verificar se dois arrays são iguais
np.array_equal(a,b)#return true or false

#arredondar os valores dos elemntos de um array
x = np.array([1.2, 5,9])
np.around(x)

#PYTHON=======================
#FUNÇÃO ZIP() - PERCORRER DUAS SEQUÊNCIAS DE ELEMENTOS EM PARALELO
#agrega valores de duas sequências e retorna uma tupla
#será retornado o total de elementos da lista menor
zip(seq, seq)
alpha = ['a', 'b', 'c']
numer = [0,1,3,2]
r_zip = list(zip(alpha, numer))
r_zip#(['a',0])

for carro, motorista in zip(carros, motoristas):
      (...)

#nuvem de palavras=========================
#instalar a biblioteca wordcloud
pip install wordcloud
conda install -c conda-forge wordcloud


#colleções ===========
#contagem
from collections import Counter
Counter(df['Local'])
'''
Counter({'Coders': 11,
         'Comunidades': 7,
         'Workshop Creators': 1,
         'Feel The Future': 3,
         'Workshop IoT': 4,
         'Entrepreneurship': 3,
         'Workshop Startups': 1,
         'Creativity': 2})
'''

#union Union : Union of two list means it will contain all the elements of both list.
#For example, if one list contains (1,2,3,4) and another list contains (2,3,4,5)
#then the union of both list will be (1,2,3,4,5)

lista=[0,1,2,3]
lista2 = [0,4,5,6]
c = set(lista+lista2)
print(c)

#pontuação
import string
for c in string.punctuation:
...     print("[" + c + "]")


#escrever em arquivo texto

#linha a linha
arquivo_texto.write('linha 1--')
arquivo_texto.write('\n')
arquivo_texto.write('linha --2')
arquivo_texto.close()

arquivo_texto.writelines(df['Registro'][x])

#verificar os pacotes instalados no jupyter
!pip freeze

#verificar os pacotes instalados no conda prompt
conda list

>>> from statistics import *
>>> a = [1,3.5,4,6,10,7.3]
>>> mean(a)
5.3
>>> median(a)
5.0
>>> median_grouped(a)
5.5
>>> median_high(a)
6
>>> median_low(a)
4
>>> min(a)
1


#divisão com duas //
4 // 2 #2
4/2 #2.0

#arredondar
round(3.2222,2)#arredondar duas casas decimais

#potencia
x = x**2


#remover espaços em branco strip()
texto = '  texto com   multiplos espaços  !  '
texto.strip()#'texto com   multiplos espaços  !'
#remove os espaços do INÍCIO e FIM da string

texto = '  texto com   multiplos espaços  !  '
texto.strip()#'  texto com   multiplos espaços  !'
#remove os espaços do FIM da string

#TABULAÇÕES \t ou \n quebra de linha podem ser removidos com strip()
texto = '\t  texto com  multiplos espaços  ! \n '
texto.strip()#'texto com   multiplos espaços  !'

#para remover espaços no MEIO da string

texto = 'texto com      multiplos espaços!'
texto.replace('  ','')#'texto commultiplos espaços!'


#max e min
lista = [0,1,2,3]
max(lista)#3
min(lista)#0
l_letras = ['a','A']
max(l_letras)#'a'
min(l_letras)#'A'
      
#lambda #########################
#permite criar funções anônimas inline
#é uma única expressão
#são bastante úteis quando usada em conjunto com funções map, filter e reduce
#o retorno é o resultado em tempo de execução
lambda x: x+2 #o primeiro x é o parâmetro de entrada, x*2 é o retorno da função
soma = lambda x: x+5
soma(2)#7

reverso = lambda x: x[::-1]#escrever a palavra de trás pra frente
reverso('palavra')

subtracao = lambda x,y: x-y
subtracao(5,2)#3

nomes_geral['cod_sexo'] = nomes_geral['sexo'].apply(lambda x: 1 if x=='masculino' else 0)

##arquivos

#manipular arquivos com funções built-in
open()#abrir
read()#leitura
write()#gravação
seek()#retorna para o início do arquivo
readlines()#retorna a lista de linhas do arquivos
close()#fechar

#open()
arquivo = open('arquivo.txt', 'r')
arquivo.tell()#contar o número de caracteres do arquivo
arquivo.seek(0,0)#início do arquivo


arquivo = open('arquivo.txt', 'w')#escrita, se o arquivo não existir será criado em branco

arquivo = open('arquivo.txt', 'a')#append, acrescentar informações


#módulo power point
pip install python.pptx


#função map(f, seq)
#objetivo é aplicar uma função A TODOS OS ELEMENTOS da sequência
#o retorno é um iteretor/list
#pode ser passada uma função lambda ao map
map(funcao, seq)

#função reduce(f, seq)
#recebe uma função e retorna um ÚNICO elemento
#embora seja uma função build-in a função reduce deve ser importada
from functools import reduce
lista = [0,1,2,4]
def somar(a,b):
    s = a+b
    return s

retorno = reduce(somar, lista)
retorno#7
#também pode aplicar função lambda
#verificando o maior número de uma lista com lambda

maior = lambda a,b: a if (a>b) else b
maior#function lambda
num_maior = reduce(maior, lista)
num_maior#4


#função filter(f, seq)
#filtrar todos os elementos true, verdadeiro
#retorno boolean
#é atribuir uma regra a uma lista
def eh_par(x):
    if (x % 2) == 0:
        return True
    else:
        return False

retorn_filter = list(filter(eh_par, lista))
retorn_filter#[0, 2, 4]
#também pode ser aplicada uma lambda ao filter
f_lambda = lambda x: True if (x%2)==0 else False
r_filter = list(filter(f_lambda, lista))
r_filter#[0, 2, 4]

#list comprehension
#permite desenvolver listas em expressão
lst = [x for x in 'Python']
lst#['P', 'y', 't', 'h', 'o', 'n']
#outro exemplo
l =[x**2 for x in range(0,11)]#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nova_lista = [x for x in range(11) if x%2 ==0]
nova_lista#[0, 2, 4, 6, 8, 10]


#função enumerate(seq)
#retorna uma tupla
#enumerete(indice, valor)
alpha = ['a', 'b', 'c']
t_enumerate = enumerate(alpha)
print(list(t_enumerate))#[(0, 'a'), (1, 'b'), (2, 'c')]


#tratamenmto de erros e exceções
try:
    #comandos
except:
    #comandos
else:
    #comandos
finally:
    #sempre será executado, independente do erro ocorrer ou não


try:
    8+'s'
except:
    print('operação não permitida')

ou try:
    8+'s'
except TypeError:#especifica o erro
    print('operação não permitida')
else:
    print('erro não identificado')

#validando o que o usuário digitou
def valor_num():
    while True:
        try:
            val = int(input('Digite um número qualquer: '))
        except:
            print('Vc não digitou um número. tente novamente!')
            continue
        else:
            print('vc digitou um número')
            break
        finally:
            print('Obrigado pela participação!')

#POO

#programação estruturada
#resumi-se;
#. decisão
#. iteração
#. sequencia

#métodos são funções dentro de classes
#atributos são as características

#CLASSES abstrações computacionais
#objeto é instância de uma classe, possui métodos e atributos
#mensagem é uma chamada do objeto
#herança possibilita que as classes compartilhem métodos, atributos
#polimorfismo os mesmo atributos e métodos com características distintas
#encapsulamento - visibilidade

#CLASSES
#por convenção, começa com letra maiúscula

#criando uma classe
class Livro():
    
    #Este método vai inicializar cada objeto criado a partir desta classe
    #(self) é uma referência a cada atributo de um objeto criado a partir desta classe
    def __init__(self):
        
        #atributos de cada objeto criado a partir desta classe
        #o self indica que estes são atributos dos objetos
        self.titulo = 'O Monge e o executivo'
        self.isbn = 98989898
        print('Construtor chamado para criar um objeto desta classe')
    
    #métodos são funções que recebem como parâmetro atributos do objeto criado
    def imprime(self):
        print('Foi criado o livro %s e ISBN %d' %(self.titulo, self.isbn))

#instanciando a classe Livro
livro1 = Livro()#Construtor chamado para criar um objeto desta classe

type(livro1)#__main__.Livro
livro1.titulo#'O Monge e o executivo'
livro1.isbn#98989898
livro1.imprime()#Foi criado o livro O Monge e o executivo e ISBN 98989898

#outro exemplo
class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo#vindo por parâmetro
        self.isbn = isbn#vindo por parâmetro
        print('construtor foi chamado')
    def imprime(self, titulo, isbn):
        print('O título do livro é %s e o ISBN %d' %(titulo, isbn))

livro2 = Livro('Python fundamentls', 10203)#construtor foi chamado
livro2.titulo#Python fundamentls
livro2.isbn#10203
livro2.imprime('Python fundamentls', 10203)#O título do livro é Python fundamentls: e o ISBN 10203

#outro exemplo
class Cachorro():
    def __init__(self, raca):
        self.raca = raca
        print('construtor init chamado')
    
    def qual_raca(self, raca):
        print('A raça é %s' % raca)

toto = Cachorro('Vira latas')
toto.raca#Vira latas

Romeu = Cachorro('Pug')
Romeu.raca#Pug

#outro exemplo
class Cachorro():
    def __init__(self, raca):
        self.raca = raca
        print('construtor init chamado')
    
    def qual_raca(self, raca):
        print('A raça é %s' % raca)

toto = Cachorro('Vira latas')
toto.raca#Vira latas

s_raca = toto.raca
toto.qual_raca(s_raca)
#construtor init chamado
#A raça é Vira latas


#funções especiais que permitem manipular os atributos de um objeto

func = Funcionario()

#tem o atributo nome?
hasattr(func, 'nome')#retun True or False
#tem o atributo salario?
hasattr(func, 'salario')

#seta o atributo salario com o valor 1200
setattr(func, 'salario', 1200)
#pega o valor
getattr(func, 'salario')#1200
#deleta o ATRIBUTO, não seu valor
delattr(func, 'salario')


#outro exemplo
class Circulo():
    pi = 3.14
    def __init__(self, raio=5):
        self.raio = raio
    def area(self):
        return (self.raio * self.raio)*Circulo.pi
    
    #gerar novo raio
    def setraio(self, novo_raio):
        self.raio = novo_raio
    def getraio(self):
        return self.raio

circ = Circulo()
circ.getraio()#5

circ.area()#78.5

circ.setraio(7)
circ.area()#153.86

#HERANÇA
#super classe
class Animal():
    def __init__(self):
        print('Animal criado')
    def identificacao(self):
        print('Animal')
    def comer(self):
        print('comendo...')

#sub-classe
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cachorro criado')
    def identificacao(self):
        print('Este é um Cachorro')
    def latir(self):
        print('au au')
    
rex = Cachorro()
#Animal criado
#Cachorro criado

#em caso de métodos com o mesmo nome, assume o método dentro da classe mais específica
rex.identificacao()#Este é um Cachorro

rex.comer()#comendo...

#MÉTODOS ESPECIAIS __nomedometodo__
__str__(self) #retorna um texto
def __str__(self):
    return 'este é o texto retornado do método __str__'
    #sempre que for chamado o print() o str será executado


# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

#super classe
class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface
        print('init do Smartphone')
#sub classe
class MP3Player(Smartphone):
    def __init__(self, capacidade, tamanho='Pequeno', interface='colorida'):
        Smartphone.__init__(self, tamanho, interface)
        self.capacidade = capacidade
        print('init do MP3')

celular = MP3Player('12 GB')
celular
celular.tamanho


#programação para crianças
#scratch.mit.edu


#MANIPULANDO BANDO DE DADOS EM PYTHON

#SQLite É UMA VERSÃO SIMPLIFICADA DE DB
#usado na internet, IoT e smartphones
#leve
#análise de dados
#sites com até 100k de visitas diárias fucionam bem com SQLite
#anaconda já tem o sqlite

import sqlite3

#cria a conexão com o db, caso não exista será criado
con = sqlite3.connect('escola.db')#o banco será criado no local do script
type(con)#sqlite3.Connection

#criando um cursor
#cursor permite percorrer todos os registros em um db
cursor = con.cursor()

#criando uma tabela
#instruções em SQL
sql_create = 'create table cursos (id integer primary key, titulo varchar(100), categoria varchar(140))'

#executando a instrução sql
cursor.execute(sql_create)# return <sqlite3.Cursor at 0x14df197eb20>

#sql de inserção
sql_insert = 'insert into cursos values(?,?,?)'

#dados
#lista, com tuplas
recset = [(1, 'Ciência de Dados', 'Data Science'),(2,'Big Data', 'Data Science'),(3,'Python Fundamentos','Analise de dados')]

#inserindo os registros
for rec in recset:
    cursor.execute(sql_insert, rec)

#gravando a transação
#para insert, update e delete de dados o commit deve ser executado
con.commit()

sql_select = 'select * from cursos'

cursor.execute(sql_select)#seleciona os dados
dados = cursor.fetchall()#recupera os registros

#mostra os registros recuperados
for x in dados:
    print(x)

cursor.close()#fecha o cursor
con.close()#fecha a conexão

#sqlite browser
#visualizar os dados 
#www.sqlitebrowser.org
#baixar e instalar


#MONGODB
#communit server - baixar e executar
#após a instalação, é necessário configurar as variáveis de ambiente para o SO identificar onde está o arquivo mongod
#criar o diretório c:/data/db
#executar via cmd mongod
#msg wating for connection port xxxxx

#INSTALAR O PACOTE PYMONGO
#pip install pymongo
#dica: no jupyter:
!pip install pymongo#isso executa no SO pelo jupyter

#CLIENT DO MONGO
from pymongo import MongoClient

#estabelecendo conexão
conn = MongoClient('localhost', 27017)
#uma única instancia do mongo pode suportar diversos bancos

#criando um banco de dados
db = conn.cadastrodb

#coleção é um grupo de documentos, relativamente similar a uma tabela
colecao = db.codastrodb



#com pymongo usamos dicionários para representar documentos

dados = {
    'nome': 'max Pinheiro',
    'cpf': 12345161156
}

inserir = colecao.insert_one(dados)
inserir.inserted_id#mostra o id da inserção. id criado automaticamente

#verificar o nome da coleção
db.name

#verificar as coleções disponíveis
db.collections_names()

#verificando as bases de dados existentes
db.database_names()


#criando coleção
db.create_collection('cadastro')

#retornando dados
db.nomedacolcao.find()#traz tudo


#countvetorizer
>>> from sklearn.feature_extraction.text import CountVectorizer
>>> corpus = [
...     'This is the first document.',
...     'This document is the second document.',
...     'And this is the third one.',
...     'Is this the first document?',
... ]
>>> vectorizer = CountVectorizer()
>>> X = vectorizer.fit_transform(corpus)
>>> print(vectorizer.get_feature_names())
['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
>>> print(X.toarray())  
[[0 1 1 1 0 0 1 0 1]
 [0 2 0 1 0 1 1 0 1]
 [1 0 0 1 1 0 1 1 1]
 [0 1 1 1 0 0 1 0 1]]

#calcular número primo
def primo(numero):
    mult = 0
    for x in range(2,numero):
        if (numero%x)==0:
            mult+=1
    return mult

sair = 'n'
while (sair == 'n'):
    consulta = int(input('Digite um número para saber se é primo: '))
    resultado = primo(consulta)
    if resultado > 0:
        print("%d NÃO É primo!" % consulta)
    else:
        print('%d É um número primo!' % consulta)
    sair = input('Deseja sair? "s" ou "n"')


#Scikit-learn=======================================
'''
biblioteca para machine learnin
biblioteca para criação de modelos

Regressão - quanto custa? quantos são?
'''
